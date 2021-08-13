import random

class Star(object):
    def __init__(self,pixel_count,step_period):
        # 4700K, "White" and 9800K
        self._colors = [
            ( 255, 223, 194 ),
            ( 240, 240, 240 ),
            ( 206, 220, 255 )
            ]
        #self.pixel_count = 65
        self._pixel_count = pixel_count
        #self.step_period = 1 / 10
        self._step_period = step_period
        self._led_string = [ [0,0,0] ] * self._pixel_count

    def led_values(self):
        pixels_to_change = int(self._pixel_count / 5)
        if pixels_to_change <= 1:
            pixels_to_change = 1
        else:
            pixels_to_change = random.randrange(pixels_to_change * 2)

        p = 0
        while p < pixels_to_change:
            brightness = random.randrange(60,80) / 100.0
            hue = colors[random.randrange(len(self.colors))]
            self.led_string[random.randrange(self.pixel_count)] = [ hue[0] * brightness, hue[1] * brightness, hue[2] * brightness ]
            p += 1

        return led_string
