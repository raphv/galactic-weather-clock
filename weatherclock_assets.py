DIGITS3x5 = (
    0o35556, 0o72232, #0,1
    0o71243, 0o34347, #2,3
    0o44755, 0o34717, #4,5
    0o35716, 0o11247, #6,7
    0o35256, 0o34756, #8,9
    0o00700, 0o66000, # a => -, b => .
    0o57500, 0o00252, # c => hour symbol ("h" in French, "u" in Dutch), d => degree sign
    0, 0, # e => +, f => nothing
)

BASE_COLORS = (
   ( 0x00, 0x00, 0x00 ), # 0 = BLACK
   ( 0xff, 0x60, 0x60 ), # 1 = RED
   ( 0x60, 0xff, 0x60 ), # 2 = GREEN
   ( 0x60, 0x60, 0xff ), # 3 = BLUE
   ( 0xff, 0xff, 0x60 ), # 4 = YELLOW
   ( 0xff, 0x60, 0xff ), # 5 = MAGENTA
   ( 0x60, 0xff, 0xff ), # 6 = CYAN
   ( 0xff, 0xa0, 0xa0 ), # 7 = RED-ISH
   ( 0xa0, 0xff, 0xa0 ), # 8 = GREEN-ISH
   ( 0xa0, 0xa0, 0xff ), # 9 = BLUE-ISH
   ( 0xff, 0xff, 0xa0 ), # a = YELLOW-ISH
   ( 0xff, 0xa0, 0xff ), # b = MAGENTA-ISH
   ( 0xa0, 0xff, 0xff ), # c = CYAN-ISH
   ( 0x80, 0x80, 0x80 ), # d = GRAY
   ( 0xcc, 0xcc, 0xcc ), # e = OFF-WHITE
   ( 0xff, 0xff, 0xff ), # f = WHITE
)

SNOW = (
    (71, 73, 75, 77, 85, 86),
    # 71, 73, 75 Snow fall: Slight, moderate, and heavy intensity
    # 77: Snow grains
    # 85, 86: Snow showers slight and heavy
    (   
        0x000eeeeee000000, 
        0x0eeeeeeeeeeee00, 
        0xeeeeeeeeeeeeeee, 
        0x0eeeeeeeeeeeee0, 
        0x000000000000000, 
        0x000f00000000000, 
        0x0f0f0f0000f0f00, 
        0x00fff000000f000, 
        0x0f0f0f000fffff0, 
        0x000f0000000f000, 
        0x0000000000f0f00, 
    ),
    (   
        0x000eeeeee000000, 
        0x0eeeeeeeeeeee00, 
        0xeeeeeeeeeeeeeee, 
        0x0eeeeeeeeeeeee0, 
        0x000000000000000, 
        0x00f0f0000000000,
        0x000f0000000f000, 
        0x0fffff000f0f0f0, 
        0x000f000000fff00, 
        0x00f0f0000f0f0f0,
        0x00000000000f000,
    ),
)

CLOUDS = (
    (2, 3),
    (   
        0x000eee000000000, 
        0x0eeeeeee0000000, 
        0xeeeeeeeeee00000,
        0x0eeeeeeee000000, 
        0x000000000000000,
        0x000000cc00cc000, 
        0x000cccccccccc00,
        0x00ccccccccccccc,
        0x00ccccccccccccc,
        0x000ccccccccccc0,
        0x000000000000000,
    ),
    (   
        0x0000eee00000000,
        0x00eeeeeee000000,
        0x0eeeeeeeeee0000,
        0x00eeeeeeee00000,
        0x000000000000000,
        0x00000cc00cc0000,
        0x00cccccccccc000,
        0x0ccccccccccccc0,
        0x0ccccccccccccc0,
        0x00ccccccccccc00,
        0x000000000000000,
    ),
)

CLOUDS_LIGHT = (
    (1, ),
    (   
        0x000000000044400,
        0x000000000444440,
        0x000000004444444,
        0x000000004444444,
        0x000000004444444,
        0x000000000444440,
        0x000000cc00cc400,
        0x00cccccccccc000,
        0x0ccccccccccccc0,
        0x00ccccccccccc00,
        0x000000000000000,
    ),
    (   
        0x000000000044400,
        0x000000000444440,
        0x000000004444444,
        0x000000004444444,
        0x000000004444444,
        0x000000000444440,
        0x00000cc00cc4400,
        0x0cccccccccc0000,
        0xccccccccccccc00,
        0x0ccccccccccc000,
        0x000000000000000,
    ),
)

FOG = (
    ( 45, 48 ),
    (   
        0x000000000000000,
        0xeeeeee00eeeeee0,
        0x000000000000000,
        0x0eeeeee00eeeeee,
        0x000000000000000,
        0xeeeeee00eeeeee0,
        0x000000000000000,
        0x0eeeeee00eeeeee,
        0x000000000000000,
        0xeeeeee00eeeeee0,
        0x000000000000000,
    ),
    (   
        0x000000000000000,
        0x0eeeeee00eeeeee,
        0x000000000000000,
        0xeeeeee00eeeeee0,
        0x000000000000000,
        0x0eeeeee00eeeeee,
        0x000000000000000,
        0xeeeeee00eeeeee0,
        0x000000000000000,
        0x0eeeeee00eeeeee,
        0x000000000000000,
    ),
)

RAIN = (
    ( 53, 55, 57, 63, 65, 67, 81, 82 ),
    (   
        0x000eeeeee000000, 
        0x0eeeeeeeeeeee00, 
        0xeeeeeeeeeeeeeee, 
        0x0eeeeeeeeeeeee0, 
        0x000000000000000, 
        0x030003000300030,
        0x000300030003000,
        0x030003000300030,
        0x000300030003000,
        0x030003000300030,
        0x000300030003000,
    ),
    (   
        0x000eeeeee000000, 
        0x0eeeeeeeeeeee00, 
        0xeeeeeeeeeeeeeee, 
        0x0eeeeeeeeeeeee0, 
        0x000000000000000,
        0x000300030003000,
        0x030003000300030,
        0x000300030003000,
        0x030003000300030,
        0x000300030003000,
        0x030003000300030,
    ),
)

RAIN_LIGHT = (
    ( 51, 56, 61, 66, 80 ),
    (   
        0x000eeeeee000000, 
        0x0eeeeeeeeeeee00, 
        0xeeeeeeeeeeeeeee, 
        0x0eeeeeeeeeeeee0, 
        0x000000000000000, 
        0x030000000300000,
        0x000003000000030,
        0x000000000000000,
        0x000000000000000,
        0x030000000300000,
        0x000003000000030,
    ),
    (   
        0x000eeeeee000000, 
        0x0eeeeeeeeeeee00, 
        0xeeeeeeeeeeeeeee, 
        0x0eeeeeeeeeeeee0, 
        0x000000000000000,
        0x000003000000030,
        0x030000000300000,
        0x000000000000000,
        0x000000000000000,
        0x000003000000030,
        0x030000000300000,
    ),
)

SUN = (
    [0],
    (
        0x000000000000000,
        0x000000000000000,
        0x000000444000000,
        0x000004444400000,
        0x000044444440000,
        0x000044444440000,
        0x000044444440000,
        0x000004444400000,
        0x000000444000000,
        0x000000000000000,
        0x000000000000000,
    ),
    (
        0x000000040000000,
        0x000400000004000,
        0x000040444040000,
        0x000004444400000,
        0x000044444440000,
        0x044044444440440,
        0x000044444440000,
        0x000004444400000,
        0x000040444040000,
        0x000400000004000,
        0x000000040000000,
    ),
)

STORM = (
    [95, 96, 99],
    (   
        0x000eeeeee000000, 
        0x0eeeeeeeeeeee00, 
        0xeeeeeeeeeeeeeee, 
        0x0eeeeeeeeeeeee0, 
        0x000000000000000,
        0x000000aaa000000,
        0x000000aaa000000,
        0x00000aaa0000000,
        0x00000aaa0000000,
        0x0000000aa000000,
        0x00000000a000000,
    ),
    (   
        0x000eeeeee000000, 
        0x0eeeeeeeeeeee00, 
        0xeeeeeeeeeeeeeee, 
        0x0eeeeeeeeeeeee0, 
        0x000000000000000,
        0x000000000000000,
        0x000000000000000,
        0x000000000000000,
        0x000000000000000,
        0x000000000000000,
        0x000000000000000,
    ),
)

WEATHER_TYPES = (
    SNOW, CLOUDS, CLOUDS_LIGHT, FOG, RAIN, RAIN_LIGHT, SUN, STORM,
)

HEART = (
    0b11011,
    0b11111,
    0b01110,
    0b00100,
)

BIRD = (
    0b0001110000000,
    0b0011011000000,
    0b1111111100000,
    0b0011111100000,
    0b1111111100000,
    0b0011111000000,
    0b0001110001001,
    0b0011111011011,
    0b0111111111111,
    0b0011111111110,
    0b0001111111100,
)
