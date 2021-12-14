class Scene(object):
    """
    Static pattern or solid color.
    """
    def __init__(self, string_label, frame_rate, pixel_count, palette, options):
        # Palette size will be exactly 65 colors if it should be mapped directly to the string
        #print(len(palette))
        if len(palette) == 65:
            if string_label == 'star_edge':
                # Edge has 41 LEDs, including the very center LED
                self._palette = palette[0:41]
            elif string_label == 'star_fold':
                # Fold has 24 LEDs
                self._palette = palette[41:]
        else:
            self._palette = palette

        #print(self._palette)

        self._pixel_count = pixel_count
        self._color_count = len(self._palette)
        self._string_colors = []

        color = 0
        pixel = 0
        while pixel < self._pixel_count:
            self._string_colors.append(self._palette[color])
            color += 1
            if color == self._color_count:
                color = 0
            pixel += 1

    def led_values(self):
        return self._string_colors
