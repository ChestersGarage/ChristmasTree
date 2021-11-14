"""
The LED strings are split out per string for more flexibility.
In particualr, the star has two sections:
    Edge: The LEDs which make the outline and center of the star
    Fold: The LEDs which line the center of the star points, where a paper star would be folded when cutting the shape.
The tree has 4 strings of 50 LEDs, which should be placed on the tree like regular Christmas lights.
"""

import opc, math, random
from time import monotonic_ns,sleep

## These config vars need to be provided as a config file.
_xmas_tree_address = 'christmastree.home:7890'
# The list of available scenes
_scene_list = [
    "old_skool_string",
    "flickering_candles",
    "water_ripples",
    "ever_fade",
    "ever_change",
    "twinkling_stars",
    "all_white",
    "all_gold",
    "all_off",
    "warm_white",
    "cool_white"
    ]
# Star has two strings of LEDs: the edges (41px) and the folds (24px) for aesthetic reasons.
# Tree has 4 strings of 50 LEDs for technical reasons.
# UI is the indicator LED on the project box, and has one scene.
# BTW, this config matches how the LEDs are connected to the Fadecandy board.
# These counts must match the configuration in server.json
_led_layout = {
    "strings": [ "tree_1", "tree_2", "tree_3", "tree_4", "star_edge", "star_fold" ],
    "tree_1_count":     50,
    "tree_2_count":     50,
    "tree_3_count":     50,
    "tree_4_count":     50,
    "star_edge_count" : 41,
    "star_fold_count":  24,
    "tree_1_scene":    "old_skool_string",
    "tree_2_scene":    "old_skool_string",
    "tree_3_scene":    "old_skool_string",
    "tree_4_scene":    "old_skool_string",
    "star_edge_scene": "twinkling_stars",
    "star_fold_scene": "water_ripples",
    "tree_1_options":    { "bright": [ 1.0,  1.0,  1.0], "scene": {} },
    "tree_2_options":    { "bright": [ 1.0,  1.0,  1.0], "scene": {} },
    "tree_3_options":    { "bright": [ 1.0,  1.0,  1.0], "scene": {} },
    "tree_4_options":    { "bright": [ 1.0,  1.0,  1.0], "scene": {} },
    "star_edge_options": { "bright": [0.50, 0.50, 0.50], "scene": {} },
    "star_fold_options": { "bright": [0.50, 0.50, 0.50], "scene": {} }
    }

# Frames per second
_frame_rate = 20
## End of config vars

# Determine length of each frame
_frame_period = 1/_frame_rate*1000000000

# Instantiate the hardware interface
xmas_tree = opc.Client(_xmas_tree_address)

# Set up an instance of the selected scene for each LED string
for string_label in _led_layout['strings']:
    string_scene = __import__( _led_layout[string_label + '_scene'] )
    globals()[string_label] = string_scene.Scene( _frame_rate, _led_layout[string_label + '_count'], string_label )

# Mark the beginning of operation from the highest resolution*, non-varying** time source
last_frame = monotonic_ns()

while True:
    # Build up the set of LED color values
    led_colors = []
    for string_label in _led_layout['strings']:
        raw_led_values = globals()[string_label].led_values()
        temp_led_values = []
        for led_value in raw_led_values:
            temp_led_values.append([
                int(led_value[0]*_led_layout[string_label + '_options']['bright'][0]),
                int(led_value[1]*_led_layout[string_label + '_options']['bright'][1]),
                int(led_value[2]*_led_layout[string_label + '_options']['bright'][2])
            ])

        led_colors.extend(temp_led_values)

    # Wait until it's time to update the LEDs
    if monotonic_ns() < ( last_frame + _frame_period ):
        # Sleep for however long we have left until next LED string update.
        sleep_time = (last_frame + _frame_period - monotonic_ns()) / 1000000000
        if sleep_time <= 0:
            sleep_time = 0

        sleep(sleep_time)
    #else:
        # If we've already passed the period, it affects the visual appeal.
        #overshoot = monotonic_ns() - ( last_frame + _frame_period )
        #print('Took too long to process LED string values.')
        #print('Increase _frame_period by ' + str(overshoot) + ' nanoseconds.')

    # Note the time and update the LEDs.
    last_frame = monotonic_ns()
    xmas_tree.put_pixels(led_colors,0)
