from machine import Timer
import wave # Downloaded from https://github.com/joeky888/awesome-micropython-lib/tree/master/Audio

class WavePlayer():
    
    def __init__(self, unicorn):
        self._timer = Timer(-1)
        self._unicorn = unicorn
        self._length = 0
        self._framerate = 22050 # Framerate is hard coded in Galactic Unicorn
        self._freq = 4
    
    def _play_samples(self, timer):
        #print('play')
        if self._wavfile.tell() < self._length:
            frames = self._wavfile.readframes(self._framerate//self._freq)
            self._unicorn.play_sample(bytearray(frames))
        else:
            self._loop -= 1
            if self._loop:
                self._wavfile.rewind()
            else:
                timer.deinit()
                self._wavfile.close()
    
    def play(self, filename, loop=1):
        self._timer.init(
            freq=self._freq, mode=Timer.PERIODIC, callback=self._play_samples
        )
        self._wavfile = wave.open(filename)
        self._length = self._wavfile.getnframes()
        self._loop = loop
