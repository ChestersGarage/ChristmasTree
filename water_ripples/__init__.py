import time, math, random

class Scene(object):
    """
    Gently shimmering blue to aqua.
    Copied from flickering_candles.
    """
    def __init__(self, string_label, frame_rate, pixel_count, palette):
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate
        self._palette = palette
        # Pre-calc the map size to save a few clocks on the CPU.
        self._map_size = len(self._palette)
        self._sequence_counter = [0] * pixel_count
        self._string_sequence = [ [0,0,0] ] * pixel_count
        pixel = 0
        while pixel < pixel_count:
            pixel_sequence = self.ripples()
            self._string_sequence[pixel] = pixel_sequence
            pixel += 1

    def make_sine_map(self, frames, amplitude, offset):
        """
        Create one full sine wave within the number of steps provided,
        and return a pattern of sine map position values.

        amplitude - how bright and dim the sequence gets. Range: 0 thru int(len(self._palette)/2).
        offset - median brightness of the sequence. Range: amplitude thru (len(self._palette)-flicker).
        assert: amplitude + offset <= len(self._palette)
        """
        i = 0
        sine_map = []
        while i < frames:
            sine_map.append(int((amplitude*math.sin(i*(math.pi*2)/frames))+offset))
            i += 1

        return sine_map

    def map_sine_to_pixel_sequence(self, sine_map):
        """
        Ingest a sine_map and convert it to a pixel_sequence.
        """
        pixel_sequence = []
        for v in sine_map:
            pixel_sequence.append(self._palette[v])

        return pixel_sequence

    def ripples(self):
        """
        Ripply water with sine fades.
        """
        # Each wave cycle is between 1 and 15 seconds
        cycle = random.randint(100,1500)/100
        frames = int(cycle * self._frame_rate)
        offset = int(self._map_size/2)
        amplitude = random.randint(int(self._map_size/4),int(self._map_size/3))
        sequence_iterations = random.randint(10,60)
        sine_map = self.make_sine_map(frames, amplitude, offset) * sequence_iterations
        pixel_sequence = self.map_sine_to_pixel_sequence(sine_map)
        return pixel_sequence

    def choose_pixel_scene(self):
        """
        Unused but kept for consistency.
        """
        return self.ripples()

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
