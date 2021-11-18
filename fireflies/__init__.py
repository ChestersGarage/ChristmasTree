import random
from time import monotonic_ns

class Scene(object):
    """
    A small number of pixels moves around on the string.
    This scene is specific to the star_edge and has hardcoded numbers for it.
    """
    def __init__(self, string_label, frame_rate, pixel_count, palette ):
        self._palette = palette
        self._pixel_count = pixel_count
        self._color_count = len(self._palette)
        self._string_colors = [[0,0,0]] * self._pixel_count

        self._frame_period =  (1/frame_rate)*1000000000 # Frame period in ns
        self._swarm_size =    self._color_count         # Number of fireflies equals the palette size
        self._fly_positions = [] # Current and prior location within the string, of each firefly
        self._fly_speed =     [] # The rate at which each firefly moves
        self._fly_direction = [] # Whether the firefly is coming or going on the string
        self._fly_time =      [] # The clock time when each firefly moves next
        self._fly_colors =    [] # The color of each firefly

        fly = 0
        while fly < self._swarm_size:
            self._fly_positions.append([random.randrange(0,self._pixel_count),1])
            self._fly_speed.append(random.randint(50000000,200000000))
            self._fly_direction.append(bool(random.getrandbits(1)))
            self._fly_time.append(monotonic_ns()+self._fly_speed[fly])
            self._fly_colors.append(self._palette[fly])
            self._string_colors[self._fly_positions[fly][0]] = self._fly_colors[fly]
            fly += 1
        self._string_colors[0] = [255,255,255]

    def led_values(self):
        fly = 0
        while fly < len(self._fly_positions):
            # See if the frame is past the time the fly should move
            if monotonic_ns() >= self._fly_time[fly]:
                # Set the new next time the fly moves by adding the next interval
                self._fly_time[fly] = self._fly_time[fly] + self._fly_speed[fly]
                # Copy the current to the prior pixel position
                self._fly_positions[fly][1] = self._fly_positions[fly][0]

                # Ascending?
                if self._fly_direction[fly]:
                    self._fly_positions[fly][0] += 1
                    # When we reach the end, turn around
                    if self._fly_positions[fly][0] > 40:
                        self._fly_positions[fly][0] = 1
                else: # Or descending
                    self._fly_positions[fly][0] -= 1
                    # When we reach the end, turn around
                    if self._fly_positions[fly][0] < 1:
                        self._fly_positions[fly][0] = 40

                # Blank out the old fly pixel
                if self._fly_positions[fly][1] >= 20:
                    # Need to reverse pixel positions above 20 to make the effect contiguous
                    new_pos = 40-self._fly_positions[fly][1]+20
                    self._string_colors[new_pos] = [0,0,0]
                else:
                    self._string_colors[self._fly_positions[fly][1]] = [0,0,0]

            # Set the new fly pixel to its color
            if self._fly_positions[fly][0] >= 20:
                # Need to reverse pixel positions above 20 to make the effect contiguous
                new_pos = 40-self._fly_positions[fly][0]+20
                try:
                    self._string_colors[new_pos] = self._fly_colors[fly]
                except:
                    print(new_pos)
            else:
                self._string_colors[self._fly_positions[fly][0]] = self._fly_colors[fly]

            fly += 1

        return self._string_colors
