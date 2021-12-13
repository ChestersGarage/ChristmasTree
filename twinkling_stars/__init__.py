import random

class Scene(object):
    """
    Twinkling warm, neutral and cool white pixels.
    Sends fresh new values at each step_period.
    """
    def __init__(self, string_label, frame_rate, pixel_count, palette, options):
        # ~4700K, "White" and ~9800K
        self._palette = palette
        self._pixel_count = pixel_count
        self._led_string = [ [0,0,0] ] * pixel_count

    def led_values(self):
        pixel = 0
        while pixel < self._pixel_count:
            brightness = random.randrange(50,100) / 100.0
            color = self._palette[random.randrange(len(self._palette))]
            self._led_string[pixel] = [ color[0] * brightness, color[1] * brightness, color[2] * brightness ]
            pixel += 1

        return self._led_string
