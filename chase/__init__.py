from time import monotonic_ns

class Scene(object):
    """
    Cycle each LED through the palette.
    """
    def __init__(self, string_label, frame_rate, pixel_count, palette, options):
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate
        self._palette = palette
        # Pre-calc the map size to save a few clocks on the CPU.
        self._color_count = len(self._palette)
        self._string_sequence = []
        self._chase_period = int(float(options[string_label]['chase_period'])*1000000000)

        self._color_dir = options[string_label]['color_dir']
        if self._color_dir == 'r':
            self._palette.reverse()

        self._chase_dir = options[string_label]['chase_dir']
        if self._chase_dir == 'f':
            self._next_color = self._color_count-1
        else:
            self._next_color = 1

        pixel = 0
        color = 0
        while pixel < self._pixel_count:
            self._string_sequence.append(self._palette[color])
            color += 1
            if color == self._color_count:
                color = 0
            pixel += 1

        self._chase_time = monotonic_ns()+self._chase_period

    def led_values(self):
        """
        Apply the next pixel value to each pixel in the string.
        """

        if monotonic_ns() >= self._chase_time:
            self._chase_time = self._chase_time + self._chase_period
            if self._chase_dir == 'f':
                pixel = self._pixel_count-1
                while pixel > 0:
                    self._string_sequence[pixel] = self._string_sequence[pixel-1]
                    pixel -= 1

                self._string_sequence[0] = self._palette[self._next_color]
                self._next_color -= 1
                if self._next_color < 0:
                    self._next_color = self._color_count-1
            else:
                pixel = 0
                while pixel < self._pixel_count-1:
                    self._string_sequence[pixel] = self._string_sequence[pixel+1]
                    pixel += 1

                self._string_sequence[self._pixel_count-1] = self._palette[self._next_color]
                self._next_color += 1
                if self._next_color == self._color_count:
                    self._next_color = 0

        return self._string_sequence
