import bpy
import numpy as np
import math


# This the radius of our virtual sphere.

radius = 10

# Using linspace to get 15 equally spaced angles between -180 to +180 
# degrees so that all our cubes are orderly distributed around the sphere.

avals = np.linspace(-math.pi,math.pi,15)
bvals = np.linspace(-math.pi,math.pi,15)

for a in avals:
	for b in bvals:

		# This should create 225 cubes (15*15) on our virtual sphere.
		
		x,y,z = radius*math.sin(a)*math.cos(b),radius*math.sin(a)*math.sin(b),radius*math.cos(a)
		bpy.ops.mesh.primitive_cube_add(
			location = [x,y,z]
		)