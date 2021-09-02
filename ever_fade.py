import time, math, random

class Scene(object):
    """
    Gradient between random colors that spans several seconds
    """
    def __init__(self, frame_rate, pixel_count):
        # ~4700K, "White" and ~9800K
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate
        self._colors = [
            ( 255,   0,   0 ),
            (   0, 255,   0 ),
            (   0,   0, 255 ),
            ( 192, 128,   0 ),
            ( 192,   0, 192 ),
            ( 192,   0, 192 ),
            ( 192, 192, 192 )
        ]
        self._sequence_counter = [0] * pixel_count
        self._string_sequence = [ [0,0,0] ] * pixel_count
        self._init = True

    def startup_msg(self, segment):
        print('Running scene "ever_fade" on segment "' + segment + '".')

    def ever_fade(self):
        fadeTime = 5
        ledString = [ [0,0,0] ] * self._pixel_count

        while True:
            p = 0
            while p < self._pixel_count:
                ledString[p] = colors[random.randrange(len(colors))]
                while ledString[p] == ledString[p-1]:
                    ledString[p] = colors[random.randrange(len(colors))]
                p += 1

            client.put_pixels(ledString,0)
            time.sleep(fadeTime)
        return pixel_sequence

    def choose_pixel_scene(self):
        """
        With multiple scene options, chooses one to use.
        """
        return self.ever_fade()

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
            pixel_sequence = self.ever_fade()
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
