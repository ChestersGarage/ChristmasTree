import opc, random

class Scene(object):
    """
    Pattern of colors with some that blink like an old blinker bulb.
    """
    def __init__(self, frame_rate, pixel_count, string_label, options):
        # Green, Blue, Yellow, Red, Aqua, Magenta
        self._colors = [
            (   9, 255,   9 ),
            (   9,   9, 255 ),
            ( 255, 210,   9 ),
            (   9, 255, 192 ),
            ( 255,   9,   9 ),
            ( 160,   9, 255 )
        ]
        """
        self._colors = [
            (   0, 255,   0 ),
            (   0,   0, 255 ),
            ( 255, 255,   0 ),
            (   0, 255, 255 ),
            ( 255,   0,   0 ),
            ( 255,   0, 255 )
        ]"""

        self._sequence_counter = [0] * pixel_count
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate

        # Create the list of random blinkers
        num_blinkers = int(pixel_count/10)
        self._blinker_map = {}
        blinker = 0
        while blinker < num_blinkers:
            # Choose a pixel randomly, and set the on and off frame counts
            # self._blinker_map = { 12: [ 45, 60 ], 35: [ 53, 32 ], ... }
            blinker_pixel = random.randrange(pixel_count)
            # Weed out adjacent blinkers
            while blinker_pixel+1 in self._blinker_map.keys() or blinker_pixel-1 in self._blinker_map.keys():
                blinker_pixel = random.randrange(pixel_count)
            self._blinker_map[blinker_pixel] = [ int((random.randrange(500,3000)/1000.0)*frame_rate), int((random.randrange(500,3000)/1000.0)*frame_rate) ]
            blinker += 1
        #self._blinker_map[1] = [ int((random.randrange(500,3000)/1000.0)*frame_rate), int((random.randrange(500,3000)/1000.0)*frame_rate) ]
        #print(self._blinker_map)

        # Initialize the string_sequence with a pattern of colors
        self._string_sequence = []
        # Stores the color of each pixel because they do not change in this
        self._pixel_colors = []
        color = 0
        num_colors = len(self._colors)
        pixel = 0
        while pixel < pixel_count:
            self._pixel_colors.append(self._colors[color])
            color += 1
            if color == num_colors:
                color = 0
            # Using a random length per pixel so that the entire string is not recalculated all at once.
            self._string_sequence.append([ self._pixel_colors[pixel] ] * int( self._frame_rate * (random.randrange(100,2000)/100) ) )
            pixel += 1

        print('Running scene "old_skool_string" on string "' + string_label + '".')

    def new_pixel_sequence(self, pixel):
        """
        Generate a pixel sequence.
        """
        #print('new_pixel_sequence')
        cycle = []
        pixel_sequence = []
        if pixel in self._blinker_map.keys():
            # Populate "on" frames
            frame = 0
            while frame < (self._blinker_map[pixel][0]+int(self._frame_rate*random.randrange(500)/1000)):
                cycle.append(list(self._pixel_colors[pixel]))
                frame += 1
            # Populate "off" frames
            frame = 0
            while frame < (self._blinker_map[pixel][1]-int(self._frame_rate * random.randrange(500)/1000)):
                cycle.append([0,0,0])
                frame += 1
            #print(cycle)
            #exit(0)
            iterations = random.randrange(10,20)
            i = 0
            while i < iterations:
                pixel_sequence.extend(cycle)
                i += 1
            #print(pixel_sequence)
            return pixel_sequence

        else:
            pixel_sequence = [ self._pixel_colors[pixel] ] * int(self._frame_rate * (random.randrange(1000,2000)/100))
            return pixel_sequence

    def led_values(self):
        """
        Apply the next pixel value to each pixel in the string.
        Upon reaching the end of any pixel sequence, request a new sequence for that pixel.
        """
        #print('led_values')
        next_frame = [[0,0,0]] * self._pixel_count
        # Loop through all the pixels in the string
        pixel = 0
        while pixel < self._pixel_count:
            next_frame[pixel] = self._string_sequence[pixel][self._sequence_counter[pixel]]
            #print(self._string_sequence)
            #print(self._sequence_counter)
            #exit(0)
            # This counter is the sliding window over self._string_sequence
            self._sequence_counter[pixel] += 1
            # Check for the end of the pixel_sequence, and get a new one and reset the counter.
            if self._sequence_counter[pixel] == len(self._string_sequence[pixel]):
                self._string_sequence[pixel] = self.new_pixel_sequence(pixel)
                self._sequence_counter[pixel] = 0
            pixel += 1
        return next_frame
