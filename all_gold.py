class Scene(object):
    """
    Twinkling warm, neutral and cool white pixels.
    Sends fresh new values at each step_period.
    """
    def __init__(self, frame_rate, pixel_count):
        # ~4700K, "White" and ~9800K
        self._colors = [
            ( 255, 192, 0 )
            ]
        self._string_colors = [ self._colors[0] ] * pixel_count

    def led_values(self):
        return self._string_colors

    def startup_msg(self,segment):
        print('Running scene "all_gold" on segment "' + segment + '".')
