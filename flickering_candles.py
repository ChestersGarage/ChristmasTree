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
        self._candle_map = [
            (  99, 14, 0 ),
            ( 100, 15, 0 ),
            ( 101, 16, 0 ),
            ( 102, 16, 0 ),
            ( 103, 17, 0 ),
            ( 104, 18, 0 ),
            ( 105, 19, 0 ),
            ( 106, 20, 0 ),
            ( 107, 21, 0 ),
            ( 108, 22, 0 ),
            ( 109, 23, 0 ),
            ( 110, 24, 0 ),
            ( 111, 24, 0 ),
            ( 112, 25, 0 ),
            ( 113, 26, 0 ),
            ( 114, 27, 0 ),
            ( 115, 28, 0 ),
            ( 116, 29, 0 ),
            ( 117, 29, 0 ),
            ( 118, 30, 0 ),
            ( 119, 31, 0 ),
            ( 120, 32, 0 ),
            ( 121, 33, 0 ),
            ( 122, 34, 0 ),
            ( 123, 34, 0 ),
            ( 124, 35, 0 ),
            ( 125, 36, 0 ),
            ( 126, 37, 0 ),
            ( 127, 38, 0 ),
            ( 128, 38, 0 ),
            ( 129, 39, 0 ),
            ( 130, 39, 0 ),
            ( 131, 40, 0 ),
            ( 132, 41, 0 ),
            ( 133, 42, 0 ),
            ( 134, 43, 0 ),
            ( 135, 44, 0 ),
            ( 136, 44, 0 ),
            ( 137, 45, 0 ),
            ( 138, 46, 0 ),
            ( 139, 47, 0 ),
            ( 140, 48, 0 ),
            ( 141, 49, 0 ),
            ( 142, 49, 0 ),
            ( 143, 50, 0 ),
            ( 144, 51, 0 ),
            ( 145, 52, 0 ),
            ( 146, 53, 0 ),
            ( 147, 53, 0 ),
            ( 148, 54, 0 ),
            ( 149, 55, 0 ),
            ( 150, 56, 0 ),
            ( 151, 57, 0 ),
            ( 152, 57, 0 ),
            ( 153, 58, 0 ),
            ( 154, 58, 0 ),
            ( 155, 59, 0 ),
            ( 156, 59, 0 ),
            ( 157, 60, 0 ),
            ( 158, 60, 0 ),
            ( 159, 61, 0 ),
            ( 160, 61, 0 ),
            ( 161, 62, 0 ),
            ( 162, 63, 0 ),
            ( 163, 63, 0 ),
            ( 164, 64, 0 ),
            ( 165, 64, 0 ),
            ( 166, 65, 0 ),
            ( 167, 66, 0 ),
            ( 168, 66, 0 ),
            ( 169, 67, 0 ),
            ( 170, 67, 0 ),
            ( 171, 68, 0 ),
            ( 172, 68, 0 ),
            ( 173, 69, 0 ),
            ( 174, 69, 0 ),
            ( 175, 70, 0 ),
            ( 176, 71, 0 ),
            ( 177, 72, 0 ),
            ( 178, 73, 0 ),
            ( 179, 74, 0 ),
            ( 180, 75, 0 ),
            ( 181, 76, 0 ),
            ( 182, 77, 0 ),
            ( 183, 78, 0 ),
            ( 184, 78, 0 ),
            ( 185, 79, 0 ),
            ( 186, 79, 0 ),
            ( 187, 80, 0 ),
            ( 188, 80, 0 ),
            ( 189, 81, 0 ),
            ( 190, 81, 0 ),
            ( 191, 82, 0 ),
            ( 192, 82, 0 ),
            ( 193, 83, 0 ),
            ( 194, 83, 0 ),
            ( 195, 84, 0 ),
            ( 196, 84, 0 ),
            ( 197, 85, 0 ),
            ( 198, 85, 0 ),
            ( 199, 86, 0 ),
            ( 200, 87, 0 ),
            ( 201, 88, 0 ),
            ( 202, 89, 0 ),
            ( 203, 90, 0 ),
            ( 204, 91, 0 ),
            ( 205, 92, 0 ),
            ( 206, 93, 0 ),
            ( 207, 93, 0 ),
            ( 208, 94, 0 ),
            ( 209, 94, 0 ),
            ( 210, 95, 0 ),
            ( 211, 95, 0 ),
            ( 212, 96, 0 ),
            ( 213, 97, 0 ),
            ( 214, 98, 0 ),
            ( 215, 99, 0 ),
            ( 216, 99, 0 ),
            ( 217, 100, 0 ),
            ( 218, 100, 0 ),
            ( 219, 101, 1 ),
            ( 220, 101, 1 ),
            ( 221, 102, 1 ),
            ( 222, 102, 1 ),
            ( 223, 103, 1 ),
            ( 224, 104, 1 ),
            ( 225, 105, 1 ),
            ( 226, 106, 1 ),
            ( 227, 107, 1 ),
            ( 228, 108, 1 ),
            ( 229, 109, 1 ),
            ( 230, 109, 1 ),
            ( 231, 110, 1 ),
            ( 232, 110, 1 ),
            ( 233, 111, 1 ),
            ( 234, 112, 1 ),
            ( 235, 112, 1 ),
            ( 236, 113, 1 ),
            ( 237, 114, 1 ),
            ( 238, 114, 1 ),
            ( 239, 115, 1 ),
            ( 240, 116, 1 ),
            ( 241, 116, 1 ),
            ( 242, 117, 1 ),
            ( 243, 118, 1 ),
            ( 244, 119, 1 ),
            ( 245, 119, 1 ),
            ( 246, 120, 1 ),
            ( 247, 121, 1 ),
            ( 248, 121, 1 ),
            ( 249, 122, 1 ),
            ( 250, 123, 1 ),
            ( 251, 123, 1 ),
            ( 252, 124, 1 ),
            ( 253, 125, 1 ),
            ( 254, 125, 1 ),
            ( 255, 126, 1 )
        ]
        # Pre-calc the map size to save a few clocks on the CPU.
        self._map_size = len(self._candle_map)
        self._sequence_counter = [0] * pixel_count
        self._led_colors = [ [0,0,0] ] * pixel_count
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
        return sine_sequence

    def bouncing_flame(self):
        """
        Bounce the candle flame the way candles seem to do randomly.
        Ramp up from a small bounce to higher.
        Sustain the high bounce for a few seconds.
        Ramp down again over 1-2 seconds.
        To-do: Create "windy" condition where the flame bounces but very fast and rough for about 1-2 seconds.
        """
        # Ramp up  over .5-1.5 seconds
        ramp_up_duration = random.randint(50,150)/100
        ramp_up_frames = int(self._frame_rate*ramp_up_duration)

        # Start with small bounce
        flicker = 10
        brightness = 106 # Centered on 50 flicker
        # Number of sine sequences in the ramp-up
        flicks = random.randint(2,5)
        frames_per_flick = int(ramp_up_frames / flicks)

        # Ramp up the flicker intensity
        pixel_sequence = []
        frame = 1
        while frame <= flicks:
            pixel_sequence.extend(self.make_sine_sequence(frames_per_flick, flicker, brightness))
            flicker = flicker * 1.2
            if flicker > 50:
                flicker = 50

        # Sustain the intense flick for a moment
        iters = 0
        maxIters = random.randint(30)
        while iters < maxIters:
            pixel_sequence.extend(self.make_sine_sequence(steps, flicker, brightness))
            iters += 1

        # ramp down the flicker intensity
        while flicker > 8:
            pixel_sequence.extend(self.make_sine_sequence(steps, flicker, brightness))
            flicker = flicker * .95

        return pixel_sequence

    def standard_glow(self):
        # Regular candle flame that gently changes brightness and color temperature.
        steps = random.randint(60, 600)
        flicker = random.randint(30,50)
        brightness = 106 # Centered on 50 flicker
        sequenceIterations = random.randint(1,4)
        pixel_sequence = self.make_sine_sequence(steps, flicker, brightness) * sequenceIterations
        return pixel_sequence

    def choose_pixel_sequence_type(self):
        """
        Determines whether a new pixel sequence will be normal or "bounce" or ??
        """
        jump = random.randint(10)
        if jump == 3:
            next_sequence = self.bouncing_flame()
        else:
            next_sequence = self.standard_glow()
        return next_sequence

    def make_string_sequence(self):
        """
        Build the initial string sequence at startup.
        Only regualr pixel sequences - no bounce
        """
        stringSequence = []
        for pixel in self._led_colors:
            pixel_sequence = self.standard_glow()
            stringSequence.append(pixel_sequence)
        return stringSequence

    def map_pixel_sequences_to_string(self, stringSequence):
        """
        Apply the next pixel value to each pixel in the string.
        Upon reaching the end of any pixel sequence, request a new sequence for that pixel.
        """
        # Loop through all the pixels in the string
        for index,pixel in enumerate(self._led_colors):
            # Pull one pixel color value from the candle map
            self._led_colors[index] = [
                                      self._candle_map[ stringSequence[index][ self._sequence_counter[index]] ][0],
                                      self._candle_map[ stringSequence[index][ self._sequence_counter[index]] ][1],
                                      self._candle_map[ stringSequence[index][ self._sequence_counter[index]] ][2]
                                    ]
            self._sequence_counter[index] += 1
            if self._sequence_counter[index] == len(stringSequence[index]):
                stringSequence[index] = self.choose_pixel_sequence_type()
                self._sequence_counter[index] = 0

        return self._led_colors

    def led_values(self):
        if self._init:
            stringSequence = self.make_string_sequence()
            self._init = False

        return self.map_pixel_sequences_to_string(stringSequence)
