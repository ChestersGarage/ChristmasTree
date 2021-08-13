import opc, math, random
from time import monotonic_ns

xmas_tree_address = 'christmastree.home:7890'

scene_list = [
    "old_skool_string",
    "flickering_candles",
    "ever_fade",
    "twinkling_stars"
    ]

# Default scenes
_xmas_star_scene = star_scene_list[3]
_xmas_tree_scene = tree_scene_list[0]

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

def set_scene(scene):
    """    Select which scene to run on the tree.    """
    return __import__(scene)


# Begin
xmas_tree = opc.Client(xmas_tree_address)

star_scene = set_scene(_xmas_star_scene)
star = star_scene.Scene(_star_pixel_count, _step_period, _star_pixel_segments)
star.startup_msg()

tree_scene = set_scene(_xmas_tree_scene)
tree = tree_scene.Scene(_tree_pixel_count, _step_period, _tree_pixel_segments)
tree.startup_msg()

while True:
    led_string = tree.led_values() + star.led_values()
    while monotonic_ns() < ( _step_last_update + _step_period ):
        continue

    _step_last_update = monotonic_ns()
    xmas_tree.put_pixels(led_string,0)
