import time, math, random

class Scene(object):
    """
    Gradients between random colors that span several seconds.
    Each pixel on its own schedule that is randomized at each segment.
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
        self._last_color =      [ [0,0,0] ] * pixel_count
        self._next_color =      [ [0,0,0] ] * pixel_count
        self._init = True

    def startup_msg(self, segment):
        print('Running scene "ever_fade" on segment "' + segment + '".')

    def ever_fade(self, pixel):
        """
        Gradient between two colors over a varying length of time per sequence.
        """
        cycle = random.randint(4,10)
        frame_count = cycle * self._frame_rate
        pixel_sequence = []

        # Shift new to last
        self._last_color[pixel] = self._next_color[pixel]
        # Pick a new color
        self._next_color[pixel] = self._colors[random.randrange(len(self._colors))]
        # Make sure it's not the same color as the prior pixel
        while self._last_color[pixel] == self._next_color[pixel-1]:
            self._next_color[pixel] = self._colors[random.randrange(len(self._colors))]

        # When the pixel color doesn't change,
        # we just pass back all the same values for the sequence
        if self._last_color[pixel] == self._next_color[pixel]:
            pixel_sequence = [ self._next_color[pixel] ] * frame_count
            return pixel_sequence

        # Otherwise, we have to map each color component value,
        # based on what frame of the sequence we are in,
        # and loop for each pixel component
        frame = 0
        while frame < frame_count:
            component = 0
            while component < 3:
                # Next and prior color components are the same
                if self._last_color[pixel][component] == self._next_color[pixel][component]:
                    pixel_sequence[frame][component] = self._next_color[pixel][component]

                # Next color component is lower value than prior
                if self._last_color[pixel][component] > self._next_color[pixel][component]:
                    # Prior component value - (frame position as a percentage * difference between last and next)
                    pixel_sequence[frame][component] = self._last_color[pixel][component] - ((float(frame) / float(frame_count)) * (self._last_color[pixel][component] - self._next_color[pixel][component]))

                # Next color component is higher value than prior
                if self._last_color[pixel][component] < self._next_color[pixel][component]:
                    # Prior component value + (frame position as a percentage * difference between next and last)
                    pixel_sequence[frame][component] = self._last_color[pixel][component] + ((float(frame) / float(frame_count)) * (self._next_color[pixel][component] - self._last_color[pixel][component]))

                component += 1
            frame += 1

        return pixel_sequence

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
                self._string_sequence[pixel] = self.ever_fade(pixel)
                self._sequence_counter[pixel] = 0
            pixel += 1
        return next_frame

    def init_string_sequence(self):
        """
        Build the initial string sequence at startup.
        """
        pixel_channel = 0
        while pixel_channel < self._pixel_count:
            pixel_sequence = self.ever_fade(pixel_channel)
            self._string_sequence[pixel_channel] = pixel_sequence
            pixel_channel += 1

    def led_values(self):
        if self._init:
            self.init_string_sequence()
            self._init = False

        next_frame = self.get_next_frame()
        return next_frame
