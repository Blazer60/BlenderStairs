"""
    Blender Scripting
"""

import bpy
import math

scale = [0.3, 4, 0.1]
stretch = [4, 1]
offSet = [0, 0]


def getDotProduct(ax, ay, bx, by):
    return ax * bx + ay * by


def getDeterminant(aa, ab, ba, bb):
    return aa * bb - ab * ba


def add_stair(t: float, i: int):
    plane = [0, 1, 0]
    x = stretch[0] * math.cos(t)
    y = stretch[1] * math.sin(t)
    """
    Get the dot product from a horizontal line
    Get the Determinant based on horizontal
    angle = atan2(det, dot)
    angle = atan(det / dot)
    """
    dot = getDotProduct(x, y, plane[0], plane[1])
    det = getDeterminant(plane[0], plane[1], x, y)
    angle = math.atan2(det, dot)
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.selected_objects[0]
    cube.name = "jeff"
    cube.location = [x - offSet[0], y - offSet[1], scale[2] * i * 2]
    cube.scale = scale
    cube.rotation_euler = [0, 0, angle]


if __name__ == "__main__":
    t = -math.pi
    i = 0
    while -4 * math.pi <= t <= 4 * math.pi:
        add_stair(t, i)
        i += 1
        t += scale[0]
    """
        for i in range(100):
        add_stair(i * 0.25)
        # add_cube([math.cos(i), math.sin(i), i/4], [0, 0, math.sin(i)], [1, 0.4, 0.1])
    """
