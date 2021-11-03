import time, math, random

class Scene(object):
    """
    Gently shimmering blue to aqua.
    Copied from flickering_candles.
    """
    def __init__(self, frame_rate, pixel_count, string_label):
        # ~4700K, "White" and ~9800K
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate
        self._water_map = [
            (0,0,255),
            (0,1,255),
            (0,2,255),
            (0,3,255),
            (0,4,255),
            (0,5,255),
            (0,6,255),
            (0,7,255),
            (0,8,255),
            (0,9,255),
            (0,10,255),
            (0,11,255),
            (0,12,255),
            (0,13,255),
            (0,14,255),
            (0,15,255),
            (0,16,255),
            (0,17,255),
            (0,18,255),
            (0,19,255),
            (0,20,255),
            (0,21,255),
            (0,22,255),
            (0,23,255),
            (0,24,255),
            (0,25,255),
            (0,26,255),
            (0,27,255),
            (0,28,255),
            (0,29,255),
            (0,30,255),
            (0,31,255),
            (0,32,255),
            (0,33,255),
            (0,34,255),
            (0,35,255),
            (0,36,255),
            (0,37,255),
            (0,38,255),
            (0,39,255),
            (0,40,255),
            (0,41,255),
            (0,42,255),
            (0,43,255),
            (0,44,255),
            (0,45,255),
            (0,46,255),
            (0,47,255),
            (0,48,255),
            (0,49,255),
            (0,50,255),
            (0,51,255),
            (0,52,255),
            (0,53,255),
            (0,54,255),
            (0,55,255),
            (0,56,255),
            (0,57,255),
            (0,58,255),
            (0,59,255),
            (0,60,255),
            (0,61,255),
            (0,62,255),
            (0,63,255),
            (0,64,255),
            (0,65,255),
            (0,66,255),
            (0,67,255),
            (0,68,255),
            (0,69,255),
            (0,70,255),
            (0,71,255),
            (0,72,255),
            (0,73,255),
            (0,74,255),
            (0,75,255),
            (0,76,255),
            (0,77,255),
            (0,78,255),
            (0,79,255),
            (0,80,255),
            (0,81,255),
            (0,82,255),
            (0,83,255),
            (0,84,255),
            (0,85,255),
            (0,86,255),
            (0,87,255),
            (0,88,255),
            (0,89,255),
            (0,90,255),
            (0,91,255),
            (0,92,255),
            (0,93,255),
            (0,94,255),
            (0,95,255),
            (0,96,255),
            (0,97,255),
            (0,98,255),
            (0,99,255),
            (0,100,255),
            (0,101,255),
            (0,102,255),
            (0,103,255),
            (0,104,255),
            (0,105,255),
            (0,106,255),
            (0,107,255),
            (0,108,255),
            (0,109,255),
            (0,110,255),
            (0,111,255),
            (0,112,255),
            (0,113,255),
            (0,114,255),
            (0,115,255),
            (0,116,255),
            (0,117,255),
            (0,118,255),
            (0,119,255),
            (0,120,255),
            (0,121,255),
            (0,122,255),
            (0,123,255),
            (0,124,255),
            (0,125,255),
            (0,126,255),
            (0,127,255),
            (0,128,255),
            (0,129,255),
            (0,130,255),
            (0,131,255),
            (0,132,255),
            (0,133,255),
            (0,134,255),
            (0,135,255),
            (0,136,255),
            (0,137,255),
            (0,138,255),
            (0,139,255),
            (0,140,255),
            (0,141,255),
            (0,142,255),
            (0,143,255),
            (0,144,255),
            (0,145,255),
            (0,146,255),
            (0,147,255),
            (0,148,255),
            (0,149,255),
            (0,150,255),
            (0,151,255),
            (0,152,255),
            (0,153,255),
            (0,154,255),
            (0,155,255),
            (0,156,255),
            (0,157,255),
            (0,158,255),
            (0,159,255),
            (0,160,255),
            (0,161,254),
            (0,162,253),
            (0,163,252),
            (0,164,251),
            (0,165,250),
            (0,166,249),
            (0,167,248),
            (0,168,247),
            (0,169,246),
            (0,170,245),
            (0,171,244),
            (0,172,243),
            (0,173,242),
            (0,174,241),
            (0,175,240),
            (0,176,239),
            (0,177,238),
            (0,178,237),
            (0,179,236),
            (0,180,235),
            (0,181,234),
            (0,182,233),
            (0,183,232),
            (0,184,231),
            (0,185,230),
            (0,186,229),
            (0,187,228),
            (0,188,227),
            (0,189,226),
            (0,190,225),
            (0,191,224),
            (0,192,223),
            (0,193,222),
            (0,194,221),
            (0,195,220),
            (0,196,219),
            (0,197,218),
            (0,198,217),
            (0,199,216),
            (0,200,215),
            (0,201,214),
            (0,202,213),
            (0,203,212),
            (0,204,211),
            (0,205,210),
            (0,206,209),
            (0,207,208),
            (0,208,207),
            (0,209,206),
            (0,210,205),
            (0,211,204),
            (0,212,203),
            (0,213,202),
            (0,214,201),
            (0,215,200),
            (0,216,199),
            (0,217,198),
            (0,218,197),
            (0,219,196),
            (0,220,195),
            (0,221,194),
            (0,222,193),
            (0,223,192),
            (0,224,191),
            (0,225,190),
            (0,226,189),
            (0,227,188),
            (0,228,187),
            (0,229,186),
            (0,230,185),
            (0,231,184),
            (0,232,183),
            (0,233,182),
            (0,234,181),
            (0,235,180),
            (0,236,179),
            (0,237,178),
            (0,238,177),
            (0,239,176),
            (0,240,175),
            (0,241,174),
            (0,242,173),
            (0,243,172),
            (0,244,171),
            (0,245,170),
            (0,246,169),
            (0,247,168),
            (0,248,167),
            (0,249,166),
            (0,250,165),
            (0,251,164),
            (0,252,163),
            (0,253,162),
            (0,254,161),
            (0,255,160)
        ]
        # Pre-calc the map size to save a few clocks on the CPU.
        self._map_size = len(self._water_map)
        self._sequence_counter = [0] * pixel_count
        self._string_sequence = [ [0,0,0] ] * pixel_count
        pixel = 0
        while pixel < pixel_count:
            pixel_sequence = self.standard_glow()
            self._string_sequence[pixel] = pixel_sequence
            pixel += 1
        print('Running scene "flickering_candles" on string "' + string_label + '".')

    def make_sine_sequences(self, frames, flicker, brightness):
        """
        Create one full sine wave within the number of steps provided,
        and return a pattern of brightness values for one pixel.

        Flicker - (sine amplitude) how bright and dim the candle gets. Range: 0 thru int(len(self_water_map)/2).
        Brightness - (sine offset) median brightness of the candle. Range: flicker thru (len(self_water_map)-flicker).
        """
        i = 0
        sine_sequence = []
        while i < frames:
            # Pre-calculate the sine wave values
            sine_sequence.append([ int((flicker*math.sin(i*(math.pi*2)/frames))+brightness) ])
            sine_sequence.append([ int((flicker*math.sin(i*(math.pi*2)/frames)+(2*math.pi/3))+brightness) ])
            sine_sequence.append([ int((flicker*math.sin(i*(math.pi*2)/frames)+2*(2*math.pi/3))+brightness) ])
            i += 1
        #print(sine_sequence)
        #exit(0)
        return sine_sequence

    def make_pixel_sequence(self, sine_sequence):
        """
        Ingest a sine_sequence and map it to a pixel_sequence.
        """
        pixel_sequence = [ [0,0,0,] ] * len(sine_sequence)
        for i,v in enumerate(sine_sequence):
            try:
                pixel_sequence[i] = [
                    self._water_map[v][0],
                    self._water_map[v][1],
                    self._water_map[v][2]
                ]
            except:
                pass
                print(sine_sequence)
        return pixel_sequence

    def chase(self):
        """
        Regular candle flame that gently changes brightness and color temperature.
        """
        # Each flame cycle is between 0.75 and 3 seconds
        cycle = random.randint(50,100)/100
        frames = int(cycle * self._frame_rate)
        flicker = random.randint(60,79)
        # Stick to the middle because we never really want pure blue nor cyan (maybe?)
        brightness = int(self._map_size/2)
        sequence_iterations = random.randint(10,60)
        sine_sequence = self.make_sine_sequence(frames, flicker, brightness) * sequence_iterations
        pixel_sequence = self.make_pixel_sequence(sine_sequence)
        return pixel_sequence

    def choose_pixel_scene(self):
        """
        Unused but kept for consistency.
        """
        return self.chase()

    def led_values(self):
        """
        Apply the next pixel value to each pixel in the string.
        Upon reaching the end of any pixel sequence, request a new sequence for that pixel.
        """
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
                self._string_sequence[pixel] = self.choose_pixel_scene()
                self._sequence_counter[pixel] = 0
            pixel += 1
        return next_frame
