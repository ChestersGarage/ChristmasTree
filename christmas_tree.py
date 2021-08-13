import opc, time, math, random

scene_list = [
    "old_skool_string",
    "flickering_candles",
    "ever_fade",
    "twinkling_stars"
    ]

_xmas_star_scene = star_scene_list[3]
_xmas_tree_scene = tree_scene_list[0]

_step_period = 1/30
_star_pixel_count = 65
"""Star is broken into two sets of LEDs: the edges (45px) and the folds(20px)."""
_star_pixel_segments = [ 45, 20 ]
_tree_pixel_count = 200
"""Tree is broken into 4 strings of 50 LEDs."""
_tree_pixel_segments = [ 50, 50, 50, 50 ]

def set_scene(scene):
    """
    Select which scene to run on the tree, or the default.
    """
    scene_module = __import__(scene)

    return scene_module

xmas_tree = opc.Client('christmastree.home:7890')

star_scene = set_scene(_xmas_star_scene)
star = star_scene.Scene(_star_pixel_count, _step_period, _star_pixel_segments)

tree_scene = set_scene(_xmas_tree_scene)
tree = tree_scene.Scene(_tree_pixel_count, _step_period, _tree_pixel_segments)
#        star.start_msg() = 'Servicing ' + str(self.total_pixels) + ' LED pixels.'
            #print('Starting LED Christmas tree scene: Tree Star.')
star.startup_msg()
tree.startup_msg()

while True:
    led_string = tree.led_values() + star.led_values()
    xmas_tree.put_pixels(led_string,0)
