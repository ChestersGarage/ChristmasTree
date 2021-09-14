import random

class Scene(object):
    """
    Twinkling warm, neutral and cool white pixels.
    Sends fresh new values at each step_period.
    """
    def __init__(self, frame_rate, pixel_count):
        # ~4700K, "White" and ~9800K
        self._colors = [
            ( 255, 223, 194 ),
            ( 225, 225, 225 ),
            ( 206, 220, 255 )
            ]
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate
        self._led_string = [ [0,0,0] ] * pixel_count

    def led_values(self):
        pixels_to_change = int(self._pixel_count)
        """if pixels_to_change <= 1:
            pixels_to_change = 1
        else:
            pixels_to_change = random.randrange(pixels_to_change * 2)
        """
        p = 0
        while p < pixels_to_change:
            brightness = random.randrange(60,80) / 100.0
            hue = self._colors[random.randrange(len(self._colors))]
            self._led_string[random.randrange(self._pixel_count)] = [ hue[0] * brightness, hue[1] * brightness, hue[2] * brightness ]
            p += 1

        return self._led_string

    def startup_msg(self,segment):
        print('Running scene "twinkling_stars" on segment "' + segment + '".')
