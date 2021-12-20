import blenderproc as bproc
import numpy as np
import bpy

bproc.init()

# Create a simple object:
# obj = bproc.object.create_primitive("MONKEY")
obj2 = bpy.ops.import_mesh.stl(filepath="/Users/shenchi/Documents/code/python/exercise/chamber_project/data/chamber.stl")


# Create a point light next to it
# light = bproc.types.Light()
# light.set_location([0, 1400, 0])
# light.set_energy(300)

# Set the camera to be in front of the object
cam_pose = bproc.math.build_transformation_mat([0, 1355, -20], [np.pi / 2, 0, -np.pi])
bproc.camera.add_camera_pose(cam_pose)

bpy.context.scene.camera.data.clip_end = 10000
bpy.context.scene.camera.data.sensor_width = 100

cam = bpy.data.objects["Camera"].data
scene = bpy.context.scene

intrinsic = [[1.28532115e+03, 0.00000000e+00, 7.99553411e+02],
			 [0.00000000e+00, 1.29038353e+03, 4.74003146e+02],
			 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]

f_x = intrinsic[0][0]
f_y = intrinsic[1][1]
c_x = intrinsic[0][2]
c_y = intrinsic[1][2]
w = 1536
h = 960
sensor_width_in_mm = cam.sensor_width

cam.shift_x = -(c_x / w - 0.5)
cam.shift_y = (c_y - 0.5 * h) / w

cam.lens = f_x / w * sensor_width_in_mm
pixel_aspect = f_y / f_x
scene.render.pixel_aspect_x = 1.0
scene.render.pixel_aspect_y = pixel_aspect

# Render the scene
data = bproc.renderer.render()

# Write the rendering into an hdf5 file
bproc.writer.write_hdf5("output/", data)

