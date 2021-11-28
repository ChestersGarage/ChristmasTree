import time, math, random

class Scene(object):
    """
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

    def make_pixel_sequence(self, sine_sequence):
        """
        Ingest a sine_sequence and map it to a pixel_sequence.
        """
        pixel_sequence = [ [0,0,0,] ] * len(sine_sequence)
        for i,v in enumerate(sine_sequence):
            try:
                pixel_sequence[i] = [
                    self._palette[v][0],
                    self._palette[v][1],
                    self._palette[v][2]
                ]
            except:
                pass
                print(sine_sequence)
        return pixel_sequence

    def chase(self):
        """
        """
        cycle = random.randint(50,100)/100
        frames = int(cycle * self._frame_rate)
        flicker = random.randint(60,79)
        brightness = int(self._map_size/2)
        sequence_iterations = random.randint(10,60)
        sine_sequence = self.make_sine_sequence(frames, flicker, brightness) * sequence_iterations
        pixel_sequence = self.make_pixel_sequence(sine_sequence)
        return pixel_sequence

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
