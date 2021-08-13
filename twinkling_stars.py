import random

class Scene(object):
    """
    Twinkling warm, neutral and cool white pixels.
    """
    def __init__(self,pixel_count,step_period,star_pixel_edge_count=0,star_pixel_fold_count=0):
        # ~4700K, "White" and ~9800K
        self._colors = [
            ( 255, 223, 194 ),
            ( 240, 240, 240 ),
            ( 206, 220, 255 )
            ]
        self._pixel_count = pixel_count
        self._star_pixel_edge_count = star_pixel_edge_count
        self._star_pixel_fold_count = star_pixel_fold_count
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
