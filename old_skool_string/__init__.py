import opc, random

class Scene(object):
    """
    Random basic colors without any changes, for now.
    """
    def __init__(self, frame_rate, pixel_count, string_label):
        # Red, blu, yel, cyn, mag, wht, grn
        self._colors = [
            (   0, 255,   0 ),
            (   0,   0, 255 ),
            ( 255, 220,   0 ),
            ( 255,   0,   0 ),
            (   0, 255, 255 ),
            ( 220,   0, 220 ),
            ( 200, 200, 200 )
        ]
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate
        self._string_sequence = []
        pixel = 0
        while pixel < pixel_count:
            color = 0
            while color < len(self._colors):
                self._string_sequence.append(self._colors[color])
                color += 1
                pixel += 1
                if pixel >= pixel_count:
                    break
        print('Running scene "old_skool_string" on string "' + string_label + '".')

    def blinkers(self):
        num_blinkers = random.randrange(int(self._pixel_count/10))
        blinker_list = []
        blinker = 0
        while blinker < num_blinkers:
            blinker_list.append(random.randrange(self._pixel_count))

        for blinker in blinker_list:


        return pixel_sequence

    def led_values(self):
        return self._string_sequence
