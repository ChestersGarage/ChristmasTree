class Scene(object):
    """
    All white LEDs
    """
    def __init__(self, frame_rate, pixel_count, string_label):
        # ~4700K, "White" and ~9800K
        self._colors = [ ( 0, 0, 0 ) ]
        self._string_colors = [ self._colors[0] ] * pixel_count
        print('Running scene "all_white" on string "' + string_label + '".')

    def led_values(self):
        return self._string_colors
