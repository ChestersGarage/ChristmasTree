import time, math, random

class Scene(object):
    """
    Gradients between random colors that span several seconds.
    Each pixel on its own schedule that is randomized at each segment.
    """
    def __init__(self, frame_rate, pixel_count, string_label):
        # ~4700K, "White" and ~9800K
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate
        # Red, Green, Blue, Yellow, Purple, Orange, Aqua
        self._colors = (
            ( 255,   0,   0 ),
            (   0, 255,   0 ),
            (   0,   0, 255 ),
            ( 255, 255,   0 ),
            ( 160,   0, 255 ),
            ( 255, 127,   0 ),
            (   0, 255, 192 )
        )
        self._sequence_counter = [0] * pixel_count
        self._string_sequence = []
        self._last_color = []
        self._next_color = []
        pixel=0
        while pixel < pixel_count:
            self._last_color.append( self._colors[random.randrange(len(self._colors))] )
            self._next_color.append( self._colors[random.randrange(len(self._colors))] )
            pixel += 1
        # Have to loop a second time, or we get index errors on next/last pixel
        pixel=0
        while pixel < pixel_count:
            self._string_sequence.append( self.ever_shift(pixel) )
            pixel += 1
        print('Running scene "ever_change" on string "' + string_label + '".')

    def ever_shift(self, pixel):
        """
        Gradient between two colors over a varying length of time per sequence.
        """
        # Duration in seconds
        cycle = random.randint(40,300)/10
        # Convert to number of frames
        frame_count = int(cycle * self._frame_rate)
        pixel_sequence = []

        # Shift new to last
        self._last_color[pixel] = self._next_color[pixel]

        # Pick a new color
        self._next_color[pixel] = self._colors[random.randrange(len(self._colors))]
        # Make sure it's not the same color as the prior or next pixel
        if (pixel > 0) and (pixel < self._pixel_count - 1):
            while (self._next_color[pixel] == self._next_color[pixel - 1]) or (self._next_color[pixel] == self._next_color[pixel + 1]):
                self._next_color[pixel] = self._colors[random.randrange(len(self._colors))]
        if (pixel == 0) :
            while self._next_color[pixel] == self._next_color[pixel + 1]:
                self._next_color[pixel] = self._colors[random.randrange(len(self._colors))]
        if (pixel == self._pixel_count - 1):
            while self._next_color[pixel] == self._next_color[pixel - 1]:
                self._next_color[pixel] = self._colors[random.randrange(len(self._colors))]

        return [ self._next_color[pixel] ] * frame_count

    def led_values(self):
        """
        Apply the next pixel value to each pixel in the string.
        Upon reaching the end of any pixel sequence, request a new sequence for that pixel.
        """
        next_frame = []
        # Loop through all the pixels in the string
        pixel = 0
        while pixel < self._pixel_count:
            next_frame.append(self._string_sequence[pixel][self._sequence_counter[pixel]])
            # This counter is the sliding window over self._string_sequence
            self._sequence_counter[pixel] += 1
            # Check for the end of the pixel_sequence, and get a new one and reset the counter.
            if self._sequence_counter[pixel] == len(self._string_sequence[pixel]):
                self._string_sequence[pixel] = self.ever_shift(pixel)
                self._sequence_counter[pixel] = 0
            pixel += 1
        return next_frame
