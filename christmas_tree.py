import opc, math, random
from time import monotonic_ns,sleep

xmas_tree_address = 'christmastree.home:7890'

scene_list = [
    "old_skool_string",
    "flickering_candles",
    "ever_fade",
    "twinkling_stars"
    ]

# Default scenes
_xmas_star_scene = scene_list[3]
_xmas_tree_scene = scene_list[0]

# Star has two sets of LEDs: the edges (45px) and the folds(20px) for aesthetic reasons.
_star_pixel_count = 65
_star_pixel_segments = [ 45, 20 ]

# Tree has 4 strings of 50 LEDs for technical reasons.
_tree_pixel_count = 200
_tree_pixel_segments = [ 50, 50, 50, 50 ]

# LED string layout: 50, 50, 50, 50, 45, 20
led_string = [ [0,0,0] ] * (_tree_pixel_count + _star_pixel_count )

# Default to 30 FPS, in nanoseconds
_step_period = 1/30*1000000000
_step_last_update = monotonic_ns()


# Begin
xmas_tree = opc.Client(xmas_tree_address)

star_scene = __import__(_xmas_star_scene)
star = star_scene.Scene(_star_pixel_count, _star_pixel_segments, _step_period)
star.startup_msg('star')

tree_scene = __import__(_xmas_tree_scene)
tree = tree_scene.Scene(_tree_pixel_count, _tree_pixel_segments, _step_period)
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
