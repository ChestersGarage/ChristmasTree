import time, math, random

class Scene(object):
    """
    Twinkling warm, neutral and cool white pixels.
    Send new values at each frame_rate.
    """
    def __init__(self, frame_rate, pixel_count):
        # ~4700K, "White" and ~9800K
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate
        self._candle_map = [[9, 1, 0], [11, 1, 0], [12, 1, 0], [13, 2, 0], [14, 2, 0], [15, 2, 0], [16, 3, 0], [18, 3, 0], [19, 3, 0], [20, 4, 0], [21, 4, 0], [23, 5, 0], [24, 5, 0], [25, 5, 0], [27, 6, 0], [28, 6, 0], [29, 7, 0], [31, 7, 0], [32, 8, 0], [34, 8, 0], [35, 9, 0], [37, 9, 0], [38, 10, 0], [40, 11, 0], [41, 11, 0], [43, 12, 0], [45, 12, 0], [46, 13, 0], [48, 14, 0], [49, 14, 0], [51, 15, 0], [53, 15, 0], [55, 16, 0], [56, 17, 0], [58, 18, 0], [60, 19, 0], [62, 20, 0], [63, 20, 0], [65, 21, 0], [67, 22, 0], [69, 23, 0], [71, 24, 0], [73, 25, 0], [75, 25, 0], [77, 27, 0], [79, 28, 0], [81, 29, 0], [83, 30, 0], [85, 30, 0], [87, 31, 0], [89, 33, 0], [91, 34, 0], [93, 35, 0], [95, 35, 0], [97, 37, 0], [100, 37, 0], [102, 38, 0], [104, 39, 0], [106, 40, 0], [109, 41, 0], [111, 42, 0], [113, 43, 0], [115, 44, 0], [118, 45, 0], [120, 46, 0], [123, 48, 0], [125, 48, 0], [127, 50, 0], [130, 51, 0], [132, 52, 0], [135, 53, 0], [137, 54, 0], [140, 55, 0], [142, 56, 0], [145, 57, 0], [147, 58, 0], [150, 60, 0], [153, 61, 0], [155, 63, 0], [158, 64, 0], [161, 66, 0], [163, 68, 0], [166, 69, 0], [169, 71, 0], [172, 73, 0], [174, 74, 0], [177, 75, 0], [180, 76, 0], [183, 78, 0], [186, 79, 0], [189, 81, 0], [190, 81, 0], [191, 82, 0], [192, 82, 0], [193, 83, 0], [194, 83, 0], [195, 84, 0], [196, 84, 0], [197, 85, 0], [198, 85, 0], [199, 86, 0], [200, 87, 0], [201, 88, 0], [202, 89, 0], [203, 90, 0], [204, 91, 0], [205, 92, 0], [206, 93, 0], [207, 93, 0], [208, 94, 0], [209, 94, 0], [210, 95, 0], [211, 95, 0], [212, 96, 0], [213, 97, 0], [214, 98, 0], [215, 99, 0], [216, 99, 0], [217, 100, 0], [218, 100, 0], [219, 101, 1], [220, 101, 1], [221, 102, 1], [222, 102, 1], [223, 103, 1], [224, 104, 1], [225, 105, 1], [226, 106, 1], [227, 107, 1], [228, 108, 1], [229, 109, 1], [230, 109, 1], [231, 110, 1], [232, 110, 1], [233, 111, 1], [234, 112, 1], [235, 112, 1], [236, 113, 1], [237, 114, 1], [238, 114, 1], [239, 115, 1], [240, 116, 1], [241, 116, 1], [242, 117, 1], [243, 118, 1], [244, 119, 1], [245, 119, 1], [246, 120, 1], [247, 121, 1], [248, 121, 1], [249, 122, 1], [250, 123, 1], [251, 123, 1], [252, 124, 1], [253, 125, 1], [254, 125, 1], [255, 126, 1]]
        # Pre-calc the map size to save a few clocks on the CPU.
        self._map_size = len(self._candle_map)
        self._sequence_counter = [0] * pixel_count
        self._string_sequence = [ [0,0,0] ] * pixel_count
        self._init = True

    def startup_msg(self, segment):
        print('Running scene "flickering_candles" on segment "' + segment + '".')

    def make_sine_sequence(self, frames, flicker, brightness):
        """
        Create one full sine wave within the number of steps provided,
        and return a pattern of brightness values for one pixel.

        Flicker - (sine amplitude) how bright and dim the candle gets. Range: 0 thru int(len(self_candle_map)/2).
        Brightness - (sine offset) median brightness of the candle. Range: flicker thru (len(self_candle_map)-flicker).
        """
        i = 0
        sine_sequence = []
        while i < frames:
            # Pre-calculate the sine wave values
            sine_sequence.append(int((flicker*math.sin(i*(math.pi*2)/frames))+brightness))
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
                    self._candle_map[v][0],
                    self._candle_map[v][1],
                    self._candle_map[v][2]
                ]
            except:
                pass
                print(sine_sequence)
        return pixel_sequence

    def bouncing_flame(self):
        """
        Bounce the candle flame the way candles seem to do randomly.
        Ramp up from a small bounce to higher.
        Sustain the high bounce for a few seconds.
        Ramp down again over 1-2 seconds.
        To-do: Create "windy" condition where the flame bounces but very fast and rough for about 1-2 seconds.
        """
        sine_sequence = []
        # Centered on 50 flicker, minus one extra to cover rounding/typing error
        brightness = 106

        # Ramp up the flicker intensity
        # More frames per flick makes a slower, longer sine
        # Start with a fast, small flicker, and increase frames per flick

        flick_duration = random.randint(15,25)/100
        frames_per_flick = flick_duration * self._frame_rate
        frames_multiplier = random.randint(110,125)/100
        # Start with small bounce and increase to 50
        flicker = random.randint(5,10)
        flicker_multiplier = random.randint(150,200)/100
        target_flicker = 50

        try:
            while flicker <= target_flicker:
                sine_sequence.extend(self.make_sine_sequence(frames_per_flick, flicker, brightness))
                #frames_per_flick = int(frames_per_flick * frames_multiplier + 0.5)
                flicker = int(flicker * flicker_multiplier + 0.5)

            flicker = 50
            # Sustain the intense flick for 4-8 seconds
            sustain_flicks = random.randint(int( 4 * self._frame_rate / frames_per_flick ),int( 8 * self._frame_rate / frames_per_flick ))
            flick =1
            while flick <= sustain_flicks:
                sine_sequence.extend(self.make_sine_sequence(frames_per_flick, flicker, brightness))
                flick += 1

            # ramp down the flicker intensity
            frames_multiplier = random.randint(75,90)/100
            flicker_multiplier = random.randint(75,90)/100
            target_flicker = random.randint(1,5)

            while flicker >= target_flicker:
                sine_sequence.extend(self.make_sine_sequence(frames_per_flick, flicker, brightness))
                #frames_per_flick = int(frames_per_flick * frames_multiplier - 0.5)
                flicker = int(flicker * flicker_multiplier - 0.5)
            pixel_sequence = self.make_pixel_sequence(sine_sequence)
        except:
            print(pixel_sequence)
            exit(0)
        return pixel_sequence

    def standard_glow(self):
        """
        Regular candle flame that gently changes brightness and color temperature.
        """
        # Each flame cycle is between 2 and 20 seconds
        cycle = random.randint(5,10)
        frames = cycle * self._frame_rate
        flicker = random.randint(30,50)
        # Centered on 50 flicker, minus one extra to cover rounding/typing error
        brightness = 106
        sequence_iterations = random.randint(1,4)
        sine_sequence = self.make_sine_sequence(frames, flicker, brightness) * sequence_iterations
        pixel_sequence = self.make_pixel_sequence(sine_sequence)
        return pixel_sequence

    def near_blow_out(self):
        sine_sequence = [ 0 ] * self._pixel_count
        pixel_sequence = self.make_pixel_sequence(sine_sequence)
        return pixel_sequence

    def choose_pixel_scene(self):
        """
        Determines whether a new pixel sequence will be normal or "bounce" or ??
        """

        dice = random.randint(1,100)
        if dice >= 30 and dice < 40:
            #print('bouncing_flame')
            return self.bouncing_flame()
            #elif dice >= 70 and dice < 80:
            #return self.near_blow_out()"""
        else:
            #print('standard_glow')
            return self.standard_glow()

    def get_next_frame(self):
        """
        Apply the next pixel value to each pixel in the string.
        Upon reaching the end of any pixel sequence, request a new sequence for that pixel.
        """
        next_frame = [[0,0,0]] * self._pixel_count
        # Loop through all the pixels in the string
        pixel = 0
        while pixel < self._pixel_count:
            next_frame[pixel] = self._string_sequence[pixel][self._sequence_counter[pixel]]
            # This counter is the sliding window over self._string_sequence
            self._sequence_counter[pixel] += 1
            # Check for the end of the pixel_sequence, and get a new one and reset the counter.
            if self._sequence_counter[pixel] == len(self._string_sequence[pixel]):
                self._string_sequence[pixel] = self.choose_pixel_scene()
                self._sequence_counter[pixel] = 0
            pixel += 1
        return next_frame

    def init_string_sequence(self):
        """
        Build the initial string sequence at startup.
        """
        pixel_channel = 0
        while pixel_channel < self._pixel_count:
            pixel_sequence = self.standard_glow()
            self._string_sequence[pixel_channel] = pixel_sequence
            pixel_channel += 1

    def led_values(self):
        if self._init:
            self.init_string_sequence()
            self._init = False
            #print(self._string_sequence)
            #exit(0)

        next_frame = self.get_next_frame()
        return next_frame
