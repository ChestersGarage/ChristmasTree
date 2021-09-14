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
        self._colors = (
            ( 255,   0,   0 ),
            (   0, 255,   0 ),
            (   0,   0, 255 ),
            ( 255, 255,   0 ),
            ( 240,   0, 255 ),
            (   0, 255, 255 )
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
        pixel = 0
        while pixel < pixel_count:
            self._string_sequence.append(self.ever_fade(pixel))
            pixel += 1
        print('Running scene "ever_fade" on string "' + string_label + '".')

    def ever_fade(self, pixel):
        """
        Gradient between two colors over a varying length of time per sequence.
        """
        # Duration in seconds
        cycle = random.randint(10,30)
        # Convert to number of frames
        frame_count = cycle * self._frame_rate
        pixel_sequence = []

        # Shift new to last
        self._last_color[pixel] = self._next_color[pixel]

        # Pick a new color
        self._next_color[pixel] = self._colors[random.randrange(len(self._colors))]
        # Make sure it's not the same color as the prior pixel
        if pixel > 0:
            while self._next_color[pixel] == self._next_color[pixel-1]:
                self._next_color[pixel] = self._colors[random.randrange(len(self._colors))]

        # When the pixel color doesn't change,
        # we just pass back all the same values for the whole sequence
        if self._last_color[pixel] == self._next_color[pixel]:
            pixel_sequence = [ self._next_color[pixel] ] * frame_count
            return pixel_sequence

        # Otherwise, we have to map each color component value,
        # based on what frame of the sequence we are in,
        # and loop for each color component
        frame = 0
        while frame < frame_count:
            component = 0
            pixel_temp = []
            while component < 3:
                # Next and prior color components are the same
                if self._last_color[pixel][component] == self._next_color[pixel][component]:
                    pixel_temp.append(self._next_color[pixel][component])
                    component += 1
                    continue

                # Next color component is lower value than prior
                if self._last_color[pixel][component] > self._next_color[pixel][component]:
                    # Prior component value - (frame position as a percentage * difference between last and next)
                    pixel_temp.append(int(self._last_color[pixel][component] - ((float(frame) / float(frame_count)) * (self._last_color[pixel][component] - self._next_color[pixel][component]))))
                    component += 1
                    continue

                # Next color component is higher value than prior
                if self._last_color[pixel][component] < self._next_color[pixel][component]:
                    # Prior component value + (frame position as a percentage * difference between next and last)
                    pixel_temp.append(int(self._last_color[pixel][component] + ((float(frame) / float(frame_count)) * (self._next_color[pixel][component] - self._last_color[pixel][component]))))
                    component += 1
                    continue

            pixel_sequence.append(pixel_temp)
            frame += 1

        # Add another frame_count of just self._next_color[pixel]
        # to provide a period of the target color un-changing
        pixel_temp = [ self._next_color[pixel] ] * frame_count

        return pixel_sequence

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
                self._string_sequence[pixel] = self.ever_fade(pixel)
                self._sequence_counter[pixel] = 0
            pixel += 1
        return next_frame
