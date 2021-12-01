import random
from time import monotonic_ns

class Scene(object):
    """
    A small number of pixels spins around in the folds. Stolen from fireflies.
    This scene is specific to the star_fold and has hardcoded numbers for it.
    """
    def __init__(self, string_label, frame_rate, pixel_count, palette, options ):
        self._palette = palette
        self._pixel_count = pixel_count
        self._color_count = len(self._palette)
        self._string_colors = [[0,0,0]] * self._pixel_count

        self._frame_period =  (1/frame_rate)*1000000000 # Frame period in ns
        self._swarm_size =    1       # Number of spinners is random 1-3
        init_position = random.randrange(0,self._pixel_count)
        self._spin_positions = [[init_position,init_position,init_position]] * self._swarm_size # Current and prior location within the string, of each spinner
        self._spin_speed =     [random.randint(50000,200000)] * self._swarm_size # The rate at which each spinner moves
        self._spin_direction = [bool(random.getrandbits(1))] * self._swarm_size # Whether the spinner is coming or going on the string
        self._spin_time =      [monotonic_ns()] * self._swarm_size # The clock time when each spinner moves next
        self._spin_colors =    [self._palette[random.randrange(0,len(self._palette))]] * self._swarm_size # The color of each spinner
        self._spin_rotations = random.randint(2,5) # the number of spins
        self._rotation = 0

    def get_spins(self):
        spin = 0
        while spin < self._swarm_size:
            self._swarm_size =    1       # Number of spinners is random 1-3
            init_position = random.randrange(0,self._pixel_count)
            self._spin_positions[spin] = [init_position,init_position,init_position]
            self._spin_speed[spin] =     random.randint(50000,200000)
            self._spin_direction[spin] = bool(random.getrandbits(1))
            self._spin_time[spin] =      monotonic_ns()+self._spin_speed[spin]
            self._spin_colors[spin] =    self._palette[random.randrange(0,len(self._palette))]
            self._spin_rotations =       random.randint(2,5)
            self._string_colors[self._spin_positions[spin][0]] = self._spin_colors[spin]
            spin += 1

    def led_values(self):
        spin = 0
        while spin < len(self._spin_positions):
            # See if the frame is past the time the spin should move
            if monotonic_ns() >= self._spin_time[spin]:
                # Set the new next time the spin moves by adding the next interval
                self._spin_time[spin] = self._spin_time[spin] + self._spin_speed[spin]
                # Copy the current to the prior pixel position
                self._spin_positions[spin][1] = self._spin_positions[spin][0]

                # Ascending?
                if self._spin_direction[spin]:
                    self._spin_positions[spin][0] += 1
                    # When we reach the end, turn around
                    if self._spin_positions[spin][0] > 23:
                        self._spin_positions[spin][0] = 0
                    if self._spin_positions[spin][0] == self._spin_positions[spin][2]:
                        self._rotation += 1
                else: # Or descending
                    self._spin_positions[spin][0] -= 1
                    # When we reach the end, turn around
                    if self._spin_positions[spin][0] < 0:
                        self._spin_positions[spin][0] = 23
                    if self._spin_positions[spin][0] == self._spin_positions[spin][2]:
                        self._rotation += 1

                # Blank out the old spin pixel
                self._string_colors[self._spin_positions[spin][1]] = [0,0,0]
                # Set the new spin pixel to its color
                self._string_colors[self._spin_positions[spin][0]] = self._spin_colors[spin]

                spin += 1


        if self._rotation >= self._spin_rotations:
            self._rotation = 0
            self._string_colors = [[0,0,0]] * self._pixel_count
            self.get_spins()


        return self._string_colors
