import time, math, random

class Scene(object):
    """
    Candles, each slowly drifting around and occasionally flicker
    """
    def __init__(self, string_label, frame_rate, pixel_count, palette):
        # ~4700K, "White" and ~9800K
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate
        self._palette = palette
        # Pre-calc the map size to save a few clocks on the CPU.
        self._map_size = len(self._palette)
        self._sequence_counter = [0] * pixel_count
        self._string_sequence = [ [0,0,0] ] * pixel_count
        pixel = 0
        while pixel < pixel_count:
            pixel_sequence = self.standard_glow()
            self._string_sequence[pixel] = pixel_sequence
            pixel += 1

    def make_sine_map(self, frames, flicker, brightness):
        """
        Create one full sine wave within the number of steps provided,
        and return a pattern of brightness values for one pixel.

        Flicker - (sine amplitude) how bright and dim the candle gets. Range: 0 thru int(len(self_palette)/2).
        Brightness - (sine offset) median brightness of the candle. Range: flicker thru (len(self_palette)-flicker).
        """
        i = 0
        sine_map = []
        while i < frames:
            # Pre-calculate the sine wave values
            sine_map.append(int((flicker*math.sin(i*(math.pi*2)/frames))+brightness))
            i += 1
        #print(sine_map)
        #exit(0)
        return sine_map

    def map_sine_to_pixel_sequence(self, sine_map):
        """
        Ingest a sine_map and map it to a pixel_sequence.
        """
        pixel_sequence = [ [0,0,0,] ] * len(sine_map)
        for i,v in enumerate(sine_map):
            pixel_sequence[i] = self._palette[v]

        return pixel_sequence

    def bouncing_flame(self):
        """
        Bounce the candle flame the way candles seem to do randomly.
        Ramp up from a small bounce to higher.
        Sustain the high bounce for a few seconds.
        Ramp down again over 1-2 seconds.
        To-do: Create "windy" condition where the flame bounces but very fast and rough for about 1-2 seconds.
        """
        sine_map = []
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
                sine_map.extend(self.make_sine_map(frames_per_flick, flicker, brightness))
                #frames_per_flick = int(frames_per_flick * frames_multiplier + 0.5)
                flicker = int(flicker * flicker_multiplier + 0.5)

            flicker = 50
            # Sustain the intense flick for 4-8 seconds
            sustain_flicks = random.randint(int( 4 * self._frame_rate / frames_per_flick ),int( 8 * self._frame_rate / frames_per_flick ))
            flick =1
            while flick <= sustain_flicks:
                sine_map.extend(self.make_sine_map(frames_per_flick, flicker, brightness))
                flick += 1

            # ramp down the flicker intensity
            frames_multiplier = random.randint(85,95)/100
            flicker_multiplier = random.randint(75,90)/100
            target_flicker = random.randint(1,5)

            while flicker >= target_flicker:
                sine_map.extend(self.make_sine_map(frames_per_flick, flicker, brightness))
                #frames_per_flick = int(frames_per_flick * frames_multiplier - 0.5)
                flicker = int(flicker * flicker_multiplier - 0.5)
            pixel_sequence = self.map_sine_to_pixel_sequence(sine_map)
        except:
            print(pixel_sequence)
            exit(0)
        return pixel_sequence

    def standard_glow(self):
        """
        Regular candle flame that gently changes brightness and color temperature.
        """
        # Each flame cycle is between 3 and 15 seconds
        cycle = random.randint(300,1500)/100
        frames = int(cycle * self._frame_rate)
        offset = int((self._map_size/3)*2)
        amplitude = random.randint(int(self._map_size/5),int(self._map_size/4))
        sequence_iterations = random.randint(1,4)
        sine_map = self.make_sine_map(frames, amplitude, offset) * sequence_iterations
        pixel_sequence = self.map_sine_to_pixel_sequence(sine_map)
        return pixel_sequence

    def near_blow_out(self):
        sine_map = [ 0 ] * self._pixel_count
        pixel_sequence = self.map_sine_to_pixel_sequence(sine_map)
        return pixel_sequence

    def choose_pixel_scene(self):
        """
        Determines whether a new pixel sequence will be normal or "bounce" or ??
        """

        dice = random.randint(1,100)
        if dice == 30:
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
