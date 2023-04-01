import time
import ntptime
import urequests
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN
from connect import connect, isconnected
import weatherclock_assets
import location_config
from wave_player import WavePlayer

graphics = PicoGraphics(display=DISPLAY_GALACTIC_UNICORN)
gu = GalacticUnicorn()
wp = WavePlayer(gu)

WIDTH = gu.WIDTH
HEIGHT = gu.HEIGHT

current_tz = 0 # UTC by default, can be updated via Open Meteo
REFRESH_NTP = 3600
REFRESH_WEATHER = 1200

FORECASTS_TO_SHOW = list(range(1,13))
FORECAST_DURATION = 6

WEATHER_URL = "http://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&timezone=%s&hourly=weathercode,temperature_2m&forecast_days=2&current_weather=true"%(
    location_config.LATITUDE,
    location_config.LONGITUDE,
    location_config.TZ_DEF.replace('/','%2F')
    )

PENS = [ graphics.create_pen(*color) for color in weatherclock_assets.BASE_COLORS ]
BLACK  = PENS[0]
WHITE  = PENS[15]


def update_time():
    global last_ntp_update
    print('Updating time')
    try:
        if not isconnected():
            print('Reconnecting')
            connect()
        ntptime.settime()
        last_ntp_update = time.time()
    except (RuntimeError, OSError) as e:
        print('Error fetching time', e)

def update_weather():
    global last_weather_update, current_tz, forecasts
    print('Updating weather')
    try:
        print(WEATHER_URL)
        r = urequests.get(
            WEATHER_URL)
        j = r.json()
        now_time = j["current_weather"]["time"]
        index_now = 0
        for i,t in enumerate(j["hourly"]["time"]):
            if t == now_time:
                index_now = i
                break
        forecasts = [
            (int(j["hourly"]["time"][i + index_now][-5:-3]),
             j["hourly"]["temperature_2m"][i + index_now],
             j["hourly"]["weathercode"][i + index_now],
            ) for i in FORECASTS_TO_SHOW
        ]
        print(forecasts)
        current_tz = j["utc_offset_seconds"]
        last_weather_update = time.time()
    except (Exception) as e:
        print('Error getting weather', e)

def get_weather_type(weather_code):
    for weather in weatherclock_assets.WEATHER_TYPES:
        if weather_code in weather[0]:
            return weather
    return None

@micropython.native
def draw_weather(weather_code, frame_parity, offset_x=0, offset_y=0):
    weather_tuple = get_weather_type(weather_code)
    if weather_tuple is None:
        return
    pixels = weather_tuple[1+frame_parity]
    for y in range(11):
        ypos = offset_y + y
        if (ypos >= 0) or (ypos < HEIGHT):
            line = pixels[y]
            for x in range(15):
                xpos = offset_x + x
                if (xpos >= 0 or xpos < WIDTH):
                    pixelvalue = (line >> 4*x) & 0xf
                    if pixelvalue:
                        graphics.set_pen(PENS[pixelvalue])
                        graphics.pixel(xpos, ypos)

@micropython.native
def paint_digit(i, offset_x, offset_y):
    digit = weatherclock_assets.DIGITS3x5[i]
    for y in range(5):
        ypos = offset_y + y
        if (ypos >= 0) or (ypos < HEIGHT):
            line = (digit >> y*3) & 7
            for x in range(3):
                xpos = offset_x + x
                if (xpos >= 0 or xpos < WIDTH) and (line & 2**x):
                    graphics.pixel(xpos, ypos)
                    
def char_to_digit(digit_char):
    if type(digit_char) == int:
        return digit_char & 0xf
    try:
        ch = str(digit_char)[0]
        if ch == '-':
            return 0xa
        elif ch == '.':
            return 0xb
        elif ch == '+':
            return 0xe
        return int(ch,16)
    except (Exception):
        return 0xf
    
def paint_number( num, offset_x, offset_y, from_right=False):
    numstr = str(num)
    x = offset_x
    if from_right:
        x = x + 1 - 4*len(numstr)
    for digit in numstr:
        paint_digit(char_to_digit(digit), x, offset_y)
        x += 4

def draw_forecast(forecast, offset_y):
    graphics.set_pen(PENS[8])
    paint_number('%dc'%forecast[0],36,offset_y,True)
    graphics.set_pen(PENS[11])
    paint_number('%.0fd'%forecast[1],36,6+offset_y,True)
    draw_weather(forecast[2],parity,38,offset_y)

graphics.set_pen(BLACK)
graphics.clear()
graphics.set_pen(WHITE)
graphics.set_font('display8')
graphics.text("Hello!", 0, 0, scale=.5)
gu.set_brightness(.5)
gu.update(graphics)
connect()

forecasts = None
last_ntp_update = 0
last_weather_update = 0
last_hour = 0
last_second = 0
scrolling_pos = 0
displayed_forecast_index = 0
year, month, day, hour, minute, second = (0,0,0,0,0,0)
is_scrolling = False

while True:
    now = time.time()
    msecs = time.ticks_ms()
    parity = (msecs//500)&1
    if (now != last_second):
        if (now - last_ntp_update) > REFRESH_NTP:
            print('Time to update NTP Time')
            update_time()
        if (now - last_weather_update) > REFRESH_WEATHER:
            print('Time to update weather')
            update_weather()
        local_now = now + current_tz
        year, month, day, hour, minute, second, _, _ = time.localtime(local_now)
        gu.set_brightness(max(.15,min(1.,gu.light()/600)))
        if last_hour != hour and minute == 0: #Sing every hour
            last_hour = hour
            if hour >= 8 and hour <= 19: #But not at night
                wp.play('blackbird-song.wav')
    graphics.set_pen(BLACK)
    graphics.clear()
    graphics.set_pen(PENS[9])
    paint_number('{:02}'.format(day),0,0)
    paint_number('{:02}'.format(month),10,0)
    graphics.set_pen(PENS[10])
    paint_number('{:02}'.format(hour),0,6)
    paint_number('{:02}'.format(minute),10,6)
    graphics.set_pen(WHITE)
    if parity:
        graphics.pixel(8,7)
        graphics.pixel(8,9)
      
    if forecasts is not None:
        if (not now % FORECAST_DURATION) and not is_scrolling:
            scrolling_pos = 1
        draw_forecast(forecasts[displayed_forecast_index],-scrolling_pos)
        is_scrolling = bool(scrolling_pos)
        if scrolling_pos:
            draw_forecast(forecasts[(1+displayed_forecast_index)%len(forecasts)],HEIGHT+2-scrolling_pos)
            scrolling_pos = (1+scrolling_pos)%(2+HEIGHT)
            if not scrolling_pos:
                displayed_forecast_index = (1+displayed_forecast_index)%len(forecasts)
    time.sleep(.1)
        
    gu.update(graphics)
