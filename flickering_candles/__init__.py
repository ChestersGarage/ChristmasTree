import time, math, random

class Scene(object):
    """
    Twinkling warm, neutral and cool white pixels.
    Send new values at each frame_rate.
    """
    def __init__(self, frame_rate, pixel_count, string_label):
        # ~4700K, "White" and ~9800K
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate
        self._candle_map = [[1, 0, 0], [3, 0, 0], [4, 0, 0], [5, 0, 0], [6, 1, 0], [7, 1, 0], [8, 1, 0], [9, 1, 0], [10, 2, 0], [11, 2, 0], [13, 2, 0], [14, 3, 0], [15, 3, 0], [16, 3, 0], [18, 4, 0], [19, 4, 0], [20, 5, 0], [22, 5, 0], [23, 5, 0], [24, 6, 0], [26, 6, 0], [27, 7, 0], [29, 7, 0], [30, 8, 0], [31, 8, 0], [33, 9, 0], [35, 10, 0], [36, 10, 0], [38, 11, 0], [39, 11, 0], [41, 12, 0], [42, 12, 0], [44, 13, 0], [46, 14, 0], [47, 15, 0], [49, 15, 0], [51, 16, 0], [53, 17, 0], [54, 18, 0], [56, 18, 0], [58, 19, 0], [60, 20, 0], [62, 21, 0], [63, 22, 0], [65, 23, 0], [67, 23, 0], [69, 24, 0], [71, 25, 0], [73, 26, 0], [75, 27, 0], [77, 28, 0], [79, 29, 0], [81, 30, 0], [83, 31, 0], [85, 32, 0], [87, 33, 0], [89, 34, 0], [92, 34, 0], [94, 36, 0], [96, 36, 0], [98, 37, 0], [100, 38, 0], [103, 39, 0], [105, 40, 0], [107, 41, 0], [109, 42, 0], [112, 43, 0], [114, 44, 0], [116, 46, 0], [119, 46, 0], [121, 48, 0], [124, 48, 0], [126, 50, 0], [129, 51, 0], [131, 52, 0], [133, 53, 0], [136, 54, 0], [139, 56, 0], [141, 57, 0], [144, 59, 0], [146, 60, 0], [149, 62, 0], [152, 63, 0], [154, 65, 0], [157, 67, 0], [160, 67, 0], [162, 69, 0], [165, 70, 0], [168, 72, 0], [171, 72, 0], [173, 74, 0], [176, 75, 0], [179, 77, 0], [182, 77, 0], [185, 79, 0], [188, 80, 0], [191, 82, 0], [194, 83, 0], [197, 85, 0], [198, 85, 0], [199, 86, 0], [200, 87, 0], [201, 88, 0], [202, 89, 0], [203, 90, 0], [204, 91, 0], [205, 92, 0], [206, 93, 0], [207, 93, 0], [208, 94, 0], [209, 94, 0], [210, 95, 0], [211, 95, 0], [212, 96, 0], [213, 97, 0], [214, 98, 0], [215, 99, 0], [216, 99, 0], [217, 100, 0], [218, 100, 0], [219, 101, 1], [220, 101, 1], [221, 102, 1], [222, 102, 1], [223, 103, 1], [224, 104, 1], [225, 105, 1], [226, 106, 1], [227, 107, 1], [228, 108, 1], [229, 109, 1], [230, 109, 1], [231, 110, 1], [232, 110, 1], [233, 111, 1], [234, 112, 1], [235, 112, 1], [236, 113, 1], [237, 114, 1], [238, 114, 1], [239, 115, 1], [240, 116, 1], [241, 116, 1], [242, 117, 1], [243, 118, 1], [244, 119, 1], [245, 119, 1], [246, 120, 1], [247, 121, 1], [248, 121, 1], [249, 122, 1], [250, 123, 1], [251, 123, 1], [252, 124, 1], [253, 125, 1], [254, 125, 1], [255, 126, 1]]
        # Pre-calc the map size to save a few clocks on the CPU.
        self._map_size = len(self._candle_map)
        self._sequence_counter = [0] * pixel_count
        self._string_sequence = [ [0,0,0] ] * pixel_count
        pixel = 0
        while pixel < pixel_count:
            pixel_sequence = self.standard_glow()
            self._string_sequence[pixel] = pixel_sequence
            pixel += 1
        print('Running scene "flickering_candles" on string "' + string_label + '".')

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

        flick_duration = random.randint(10,20)/100
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
            frames_multiplier = random.randint(85,95)/100
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
        if dice >= 30 and dice < 33:
            #print('bouncing_flame')
            return self.bouncing_flame()
            #elif dice >= 70 and dice < 80:
            #return self.near_blow_out()"""
        else:
            #print('standard_glow')
            return self.standard_glow()

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
            # This counter is the sliding window over self._string_sequence
            self._sequence_counter[pixel] += 1
            # Check for the end of the pixel_sequence, and get a new one and reset the counter.
            if self._sequence_counter[pixel] == len(self._string_sequence[pixel]):
                self._string_sequence[pixel] = self.choose_pixel_scene()
                self._sequence_counter[pixel] = 0
            pixel += 1
        return next_frame
