import opc, time, math, random, tree_star

scene_list = [
    "old_skool_string",
    "flickering_candles",
    "ever_fade",
    "shimmering_stars"
    ]

_xmas_star_scene = star_scene_list[3]
_xmas_tree_scene = tree_scene_list[0]

_step_period = 1/30
_star_pixel_count = 65
_tree_pixel_count = 200

class SetScene(object):
    """
    Select which scene to run on the tree, or the default.
    """
    def __init__(self,scene):
        self.scene = __import__(scene)

        return self.scene

xmas_tree = opc.Client('christmastree.home:7890')

star_scene = SetScene(_xmas_star_scene)
star = star_scene.Scene(_star_pixel_count,_step_period)

tree_scene = SetScene(_xmas_tree_scene)
tree = tree_scene.Scene(_tree_pixel_count,_step_period)
#        star.start_msg() = 'Servicing ' + str(self.total_pixels) + ' LED pixels.'
            #print('Starting LED Christmas tree scene: Tree Star.')

