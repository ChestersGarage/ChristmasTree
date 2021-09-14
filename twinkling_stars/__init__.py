import random

class Scene(object):
    """
    Twinkling warm, neutral and cool white pixels.
    Sends fresh new values at each step_period.
    """
    def __init__(self, frame_rate, pixel_count, string_label):
        # ~4700K, "White" and ~9800K
        self._colors = [
            ( 255, 223, 194 ),
            ( 225, 225, 225 ),
            ( 206, 220, 255 )
            ]
        self._pixel_count = pixel_count
        self._led_string = [ [0,0,0] ] * pixel_count
        print('Running scene "twinkling_stars" on string "' + string_label + '".')

    def led_values(self):
        pixel = 0
        while pixel < self._pixel_count:
            brightness = random.randrange(60,65) / 100.0
            hue = self._colors[random.randrange(len(self._colors))]
            self._led_string[random.randrange(self._pixel_count)] = [ hue[0] * brightness, hue[1] * brightness, hue[2] * brightness ]
            pixel += 1

        return self._led_string
