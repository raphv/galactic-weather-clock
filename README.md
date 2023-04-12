# galactic-weather-clock
 A clock showing the weather on a Pimoroni Galactic Unicorn

### What is it?

A Micropython script for Pimoroni's Galactic Unicorn [currently out of stock on the Pimoroni shop](https://shop.pimoroni.com/products/galactic-unicorn) that shows a clock as well as the weather forecast for the next 12 hours.

It uses the [Open Meteo API](https://open-meteo.com/en/docs) to retrieve the weather forecast as well as to adjust the time zone.

This clock plays a random bird song every hour.

### Preview

![A photo of the Galactic Weather Clock](galactic-weather-clock.jpg)

### Dependencies

 * You need version 1.19.18 of the Micropython firmware for the Raspberry Pi Pico W (I am using the new HSV pen function from that release). Check <https://github.com/pimoroni/pimoroni-pico/releases> for Firmware updates
 * You need to download `chunk.py` and `wave.py` from <https://github.com/joeky888/awesome-micropython-lib/tree/master/Audio> into the `lib` folder to read WAV files

### Description of files

 * [connect.py](connect.py): creates a WIFI network connection. You need to populate a file named `WIFI_CONFIG.py`.
 * <location_config.py>: This is where you put your latitude, longitude and timezone to get your local forecast.
 * <wave_player.py>: Uses the aforementioned `wave.py` module and the Galactic Unicorn's `play_sample` function to play WAV file. Pimoroni's playback libraries only seem to work with **mono**, **16-bit**, **22050Hz** audio, so make sure to save your WAV files in that format if you want to use your own.
 * <weatherclock_assets.py>: The custom fonts used for the digits, and the icons used to display weather states.
 * <weatherclock.py>: The main source code for the weather clock.
 * [The birds directory](birds): A Collection of bird songs from Wikimedia Commons
     * Common Blackbird *(Turdus merula)* from Southern Finland by Oona Räisänen <https://en.wikipedia.org/wiki/File:Turdus_merula_2.ogg> License: Public Domain
     * European Herring Gull *(Larus argentatus)* from the Bay of Mont-Saint-Michel in Normandie by ADVL <https://commons.wikimedia.org/wiki/File:XC707075_-_European_Herring_Gull_-_Larus_argentatus.mp3> [License: Creative Commons CC0 Universal Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/deed.en)
     * Carrion Crow  *(Corvus corone)* from The Hague, South Holland by Sander Pieterse <https://commons.wikimedia.org/wiki/File:Corvus_corone_-_Carrion_Crow_XC24828.mp3>  [License: Creative Commons Attribution-Share Alike (CC-BY-SA)](https://creativecommons.org/licenses/by-sa/4.0/deed.en)
     * Common Cuckoo *(Cuculus canorus)* from Kaluga, Russia by Vladimir Yu. Arkhipov <https://en.wikipedia.org/wiki/File:Cuculus_canorus.ogg> [License: Creative Commons Attribution-Share Alike (CC-BY-SA)](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
     * Canada Goose *(Branta canadensis)* from the United States by Jonathon Jongsma <https://commons.wikimedia.org/wiki/File:Branta_canadensis_-_Canada_Goose_-_XC62259.ogg>  [License: Creative Commons Attribution-Share Alike (CC-BY-SA)](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
     * European Robin *(Erithacus rubecula)* from Tver, Russia by Vladimir Yu. Arkhipov <https://en.wikipedia.org/wiki/File:Erithacus_rubecula.ogg> [License: Creative Commons Attribution-Share Alike (CC-BY-SA)](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
     * Blue Tit *(Cyanistes caeruleus)* from Kaluzhskiye Zaseki, Russia by Vladimir Yu. Arkhipov <https://commons.wikimedia.org/wiki/File:Cyanistes_caeruleus.ogg> [License: Creative Commons Attribution-Share Alike (CC-BY-SA)](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

