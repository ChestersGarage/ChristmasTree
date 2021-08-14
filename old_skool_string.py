import opc, random

class Scene(object):
    """
    Twinkling warm, neutral and cool white pixels.
    Sends fresh new values at each step_period.
    """
    def __init__(self, step_period, pixel_count):
        # Red, blu, yel, cyn, mag, wht, grn
        self.colors = [
            ( 255,   0,   0 ),
            (   0,   0, 255 ),
            ( 255, 220,   0 ),
            (   0, 255, 255 ),
            ( 192,   0, 192 ),
            (   0, 255,   0 ),
            ( 200, 200, 200 )
        ]
        self._pixel_count = pixel_count
        self._step_period = step_period
        self._led_colors = [ [0,0,0] ] * pixel_count

    def led_values(self):
        self._led_colors = [ [255,255,255] ] * self._pixel_count
        i = 0
        while i <= self._pixel_count:
            self._led_colors[i] = self.colors[random.randrange(len(colors))]
            while self._led_colors[i] == self._led_colors[i-1]:
                self._led_colors[i] = self.colors[random.randrange(len(colors))]
            i += 1
        """
        d = 0
        while d <= holdTime:
            client.put_pixels(ledString,1)
            time.sleep(timeIncrement)
            d += timeIncrement
        """
        return self.led_colors

    def startup_msg(self,segment):
        print('Running scene "old_skool_string" on segment "' + segment + '".')

