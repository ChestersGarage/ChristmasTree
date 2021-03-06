import time, math, random

class Scene(object):
    """
    Gradients between random colors that span several seconds.
    Each pixel on its own schedule that is randomized at each segment.
    """
    def __init__(self, string_label, frame_rate, pixel_count, palette, options):
        # ~4700K, "White" and ~9800K
        self._pixel_count = pixel_count
        self._frame_rate = frame_rate
        self._palette = palette
        self._sequence_counter = [0] * pixel_count
        self._string_sequence = []
        self._last_color = []
        self._next_color = []
        pixel=0
        while pixel < pixel_count:
            self._last_color.append( [ 0,0,0 ] )
            self._next_color.append( self._palette[random.randrange(len(self._palette))] )
            pixel += 1
        # Have to loop a second time, or ever_fade throws index errors on non-existent next pixel
        pixel=0
        while pixel < pixel_count:
            self._string_sequence.append(self.ever_fade(pixel))
            pixel += 1

    def ever_fade(self, pixel):
        """
        Gradient between two colors over a varying length of time per sequence.
        """
        # Duration in seconds
        cycle = random.randint(100,300)/10
        # Convert to number of frames
        frame_count = int(cycle * self._frame_rate)
        pixel_sequence = []

        # Shift new to last
        self._last_color[pixel] = self._next_color[pixel]

        # Pick a new color
        self._next_color[pixel] = self._palette[random.randrange(len(self._palette))]
        # Make sure it's not the same color as the prior or next pixel
        if (pixel > 0) and (pixel < self._pixel_count - 1):
            while (self._next_color[pixel] == self._next_color[pixel - 1]) or (self._next_color[pixel] == self._next_color[pixel + 1]):
                self._next_color[pixel] = self._palette[random.randrange(len(self._palette))]
        if (pixel == 0) :
            while self._next_color[pixel] == self._next_color[pixel + 1]:
                self._next_color[pixel] = self._palette[random.randrange(len(self._palette))]
        if (pixel == self._pixel_count - 1):
            while self._next_color[pixel] == self._next_color[pixel - 1]:
                self._next_color[pixel] = self._palette[random.randrange(len(self._palette))]

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
