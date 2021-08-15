class Scene(object):
    """
    Twinkling warm, neutral and cool white pixels.
    Sends fresh new values at each step_period.
    """
    def __init__(self, step_period, pixel_count):
        # ~4700K, "White" and ~9800K
        self._colors = [
            ( 255, 192, 0 )
            ]
        self._pixel_count = pixel_count
        self._step_period = step_period
        self._led_colors = [ self._colors[0] ] * pixel_count
        self._init = True

    def led_values(self):
        if self._init:
            self._led_colors = [ self._colors[0] ] * self._pixel_count
            self._init = False

        return self._led_colors

    def startup_msg(self,segment):
        print('Running scene "all_gold" on segment "' + segment + '".')
