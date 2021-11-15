"""
The LED strings are split out per string for more flexibility.
In particualr, the star has two sections:
    Edge: The LEDs which make the outline and center of the star
    Fold: The LEDs which line the center of the star points, where a paper star would be folded when cutting the shape.
The tree has 4 strings of 50 LEDs, which should be placed on the tree like regular Christmas lights.
"""

import opc, math, random, json
from time import monotonic_ns,sleep

# Load configs from file
with open('config.json') as f:
    _config = json.loads(f.read())
    #print(_config)
    #exit()

# Determine length of each frame
_frame_period = 1/_config['frame_rate']*1000000000

# Instantiate the hardware interface
xmas_tree = opc.Client(_config['xmas_tree_address'])

# Set up an instance of the selected scene for each LED string
for string_label in _config['led_layout']['strings']:
    string_scene = __import__( _config['scenes'][string_label][0] )
    globals()[string_label] = string_scene.Scene( _config['frame_rate'], _config['led_layout'][string_label], string_label, _config["color_palettes"][_config['scenes'][string_label][1]] )

# Mark the beginning of operation from the highest resolution*, non-varying** time source
last_frame = monotonic_ns()

while True:
    # Build up the set of LED color values
    led_colors = []
    for string_label in _config['led_layout']['strings']:
        raw_led_values = globals()[string_label].led_values()
        temp_led_values = []
        for led_value in raw_led_values:
            #print (led_value[0])
            #exit(0)
            temp_led_values.append([
                int(led_value[0] * _config['tuning'][string_label]['color_balance'][0]),
                int(led_value[1] * _config['tuning'][string_label]['color_balance'][1]),
                int(led_value[2] * _config['tuning'][string_label]['color_balance'][2])
            ])

        led_colors.extend(temp_led_values)

    # Wait until it's time to update the LEDs
    if monotonic_ns() < ( last_frame + _frame_period ):
        # Sleep for however long we have left until next LED string update.
        sleep_time = (last_frame + _frame_period - monotonic_ns()) / 1000000000
        if sleep_time > 0:
            sleep(sleep_time)
    #else:
        # If we've already passed the period, it affects the visual appeal.
        #overshoot = monotonic_ns() - ( last_frame + _frame_period )
        #print('Took too long to process LED string values.')
        #print('Increase _frame_period by ' + str(overshoot) + ' nanoseconds.')

    # Note the time and update the LEDs.
    last_frame = monotonic_ns()
    xmas_tree.put_pixels(led_colors,0)
