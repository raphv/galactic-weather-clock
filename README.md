# galactic-weather-clock
 A clock showing the weather on a Pimoroni Galactic Unicorn

### What is it?

A Micropython script for Pimoroni's Galactic Unicorn [currently out of stock on the Pimoroni shop](https://shop.pimoroni.com/products/galactic-unicorn) that shows a clock as well as the weather forecast for the next 12 hours.

It uses the [Open Meteo API](https://open-meteo.com/en/docs) to retrieve the weather forecast as well as to adjust the time zone.

This clock plays the song of a blackbird every hour.

### Dependencies

 * This is based on version 1.19.1 of the Micropython firmware for the Raspberry Pi Pico W. Check <https://github.com/pimoroni/pimoroni-pico/releases> for Firmware updates
 * Please download `chunk.py` and `wave.py` from <https://github.com/joeky888/awesome-micropython-lib/tree/master/Audio> to read WAV files

### Description of files

 * <blackbird-song.wav>: A Common Blackbird *(Turdus merula)* singing in a forest in Southern Finland by Oona Räisänen <https://en.wikipedia.org/wiki/File:Turdus_merula_2.ogg>
 * <connect.py>: creates a WIFI network connection. You need to populate a file named `WIFI_CONFIG.py`.
 * <location_config.py>: This is where you put your latitude, longitude and timezone to get your local forecast.
 * <wave_player.py>: Uses the aforementioned `wave.py` module and the Galactic Unicorn's `play_sample` function to play WAV file. Due to the Galactic Unicorn's feature, the WAV file must be **mono**, **16-bit** and with a **22050Hz** sampling rate.
 * <weatherclock_assets.py>: The custom fonts used for the digits, and the icons used to display weather states.
 * <weatherclock.py>: The main source code for the weather clock.
