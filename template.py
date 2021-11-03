import opc, random

class Scene(object):
    def __init__(self, frame_rate, pixel_count, string_label):
        self._colors = [
            (   0, 255,   0 ),
            (   0,   0, 255 ),
            ( 255, 220,   0 ),
            ( 255,   0,   0 ),
            (   0, 255, 192 ),
            ( 160,   0, 255 ),
            ( 192, 192, 192 )
        ]
        self._sequence_counter = [0] * pixel_count
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate
        self._string_sequence = []

        # Initialize the string_sequence with pixel_sequences
        self._string_sequence = []
        color = 0
        num_colors = len(self._colors)
        string_pixel = 0
        while string_pixel < pixel_count:
            self._pixel_colors.append(self._colors[color])
            color += 1
            if color >= num_colors:
                color = 0

            try:
                # Using a random length per pixel so that the entire string is not recalculated all at once.
                self._string_sequence.append([ self._pixel_colors[pixel] ] * (frame_rate * random.randrange(10,20)))
            except:
                print(self._string_sequence)
                exit(0)

            pixel += 1

        print('Running scene "old_skool_string" on string "' + string_label + '".')


    def make_pixel_sequence(self, pixel):

    def choose_pixel_scene():

    def led_values(self):
