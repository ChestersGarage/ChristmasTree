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

    def led_values(self):
        self._led_colors = [ self._colors[0] ] * self._pixel_count

        return self.led_colors

    def startup_msg(self,segment):
        print('Running scene "all_white" on segment "' + segment + '".')
