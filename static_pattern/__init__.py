class Scene(object):
    """
    Static pattern or solid color.
    """
    def __init__(self, frame_rate, pixel_count, palette):
        self._palette = palette
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
