import blenderproc as bproc
import numpy as np
import bpy

bproc.init()

# Create a simple object:
#obj = bproc.object.create_primitive("MONKEY")
obj2 = bpy.ops.import_mesh.stl(filepath="/Users/shenchi/Documents/code/python/exercise/chamber_project/data/chamber.stl")


# Create a point light next to it
#light = bproc.types.Light()
#light.set_location([2, -2, 0])
#light.set_energy(300)

# Set the camera to be in front of the object
cam_pose = bproc.math.build_transformation_mat([0, 1355, -20], [np.pi / 2, 0, -np.pi])
bproc.camera.add_camera_pose(cam_pose)

bpy.context.scene.camera.data.clip_end = 10000
bpy.context.scene.camera.data.sensor_width = 100

# Render the scene
data = bproc.renderer.render()

# Write the rendering into an hdf5 file
bproc.writer.write_hdf5("output/", data)

