import opc, math, random
from time import monotonic_ns,sleep

xmas_tree_address = 'christmastree.home:7890'

scene_list = [
    "old_skool_string",
    "flickering_candles",
    "ever_fade",
    "twinkling_stars"
    ]

"""
The LED strings are split out per string for more flexibility.
In particualr, the star has two sections:
    Edge: The LEDs which make the outline and center of the star
    Fold: The LEDs which line the center of the star points, where a paper star would be folded when cutting the shape.
The tree has 4 strings of 50 LEDs, which would be placed on the tree like regular Christmas lights.
"""

# Star has two sets of LEDs: the edges (45px) and the folds(20px) for aesthetic reasons.
_star_edge_count = 45
_star_edge_scene = scene_list[3]
_star_fold_count = 20
_star_fold_scene = scene_list[3]

# Tree has 4 strings of 50 LEDs for technical reasons.
_tree_1_count = 50
_tree_1_scene = scene_list[0]
_tree_2_count = 50
_tree_2_scene = scene_list[0]
_tree_3_count = 50
_tree_3_scene = scene_list[0]
_tree_4_count = 50
_tree_4_scene = scene_list[0]

# LED string layout: 50, 50, 50, 50, 45, 20
led_string = [ [0,0,0] ] * ( _star_edge_count + _star_fold_count + ( _tree_1_count * 4 ) )

# Default to 30 FPS, in nanoseconds
_step_period = 1/30*1000000000
_step_last_update = monotonic_ns()


# Begin
xmas_tree = opc.Client(xmas_tree_address)

star_scene = __import__(_xmas_star_scene)
star = star_scene.Scene(_step_period, _star_pixel_count, _star_pixel_segments)
star.startup_msg('star')

tree_scene = __import__(_xmas_tree_scene)
tree = tree_scene.Scene( _step_period, _tree_pixel_count, _tree_pixel_segments)
tree.startup_msg('tree')

while True:
    led_string = tree.led_values() + star.led_values()

    if monotonic_ns() < ( _step_last_update + _step_period ):
        # Sleep for however long we have left until next LED string update.
        sleep( ( _step_last_update + _step_period ) - monotonic_ns() )
    else:
        overshoot = monotonic_ns() - ( _step_last_update + _step_period )
        print('Took too long to process LED string values.')
        print('Increase _step_period by ' + overshoot + ' nanoseconds.')

    _step_last_update = monotonic_ns()
    xmas_tree.put_pixels(led_string,0)
