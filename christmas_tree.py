"""
The LED strings are split out per string for more flexibility.
In particualr, the star has two sections:
    Edge: The LEDs which make the outline and center of the star
    Fold: The LEDs which line the center of the star points, where a paper star would be folded when cutting the shape.
The tree has 4 strings of 50 LEDs, which would be placed on the tree like regular Christmas lights.
"""

import opc, math, random
from time import monotonic_ns,sleep

# These config vars need to be provided as a JSON config file.
_xmas_tree_address = 'christmastree.home:7890'
# The list of available scenes and what the
_scene_list = [
    "old_skool_string",
    "flickering_candles",
    "ever_fade",
    "twinkling_stars",
    "all_white",
    "all_gold"
    ]
# Star has two sets of LEDs: the edges (45px) and the folds(20px) for aesthetic reasons.
# Tree has 4 strings of 50 LEDs for technical reasons.
# BTW, this config matches how the LEDs are connected to the Fadecandy board.
_led_layout = {
    "segments": [ "tree_1", "tree_2", "tree_3", "tree_4", "star_edge", "star_fold" ],
    "tree_1_count":     50,
    "tree_2_count":     50,
    "tree_3_count":     50,
    "tree_4_count":     50,
    "star_edge_count" : 45,
    "star_fold_count":  20,
    "tree_1_scene":    "flickering_candles",
    "tree_2_scene":    "flickering_candles",
    "tree_3_scene":    "flickering_candles",
    "tree_4_scene":    "flickering_candles",
    "star_edge_scene": "twinkling_stars",
    "star_fold_scene": "twinkling_stars"
    }
# 30 FPS, in nanoseconds (1e+09 ns per second)
_frame_rate = 15
## End of config vars


_frame_period = 1/_frame_rate*1000000000

# Begin
xmas_tree = opc.Client(_xmas_tree_address)

# Set up an instance of each scene for each LED string
for segment_label in _led_layout['segments']:
    segment_scene = __import__( _led_layout[segment_label + '_scene'] )
    globals()[segment_label] = segment_scene.Scene( _frame_rate, _led_layout[segment_label + '_count'] )
    globals()[segment_label].startup_msg(segment_label)

step_last_update = monotonic_ns()

while True:
    # Build up the set of LED color values
    led_colors = []
    for segment_label in _led_layout['segments']:
        led_colors.extend(globals()[segment_label].led_values())

    # Wait until it's time to update the LEDs
    if monotonic_ns() < ( step_last_update + _frame_period ):
        # Sleep for however long we have left until next LED string update.
        sleep_time = (step_last_update + _frame_period - monotonic_ns()) / 1000000000
        sleep( sleep_time )
    #else:
        # If we've already passed the period, it affects the visual appeal.
        #overshoot = monotonic_ns() - ( step_last_update + _frame_period )
        #print('Took too long to process LED string values.')
        #print('Increase _frame_period by ' + str(overshoot) + ' nanoseconds.')

    # Note the time and update the LEDs.
    step_last_update = monotonic_ns()
    xmas_tree.put_pixels(led_colors,0)
