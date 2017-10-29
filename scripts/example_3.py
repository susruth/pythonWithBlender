# Author: Nadimpalli Susruth
# Email: u6106064@anu.edu.au 
# Date: 25/10/2017

import bpy
import numpy as np
from math import sin


# Creating a new mesh with name 'sin' which is a sin wave.

m = bpy.data.meshes.new('sin')


n = 100

# Adding 100 vertices.

m.vertices.add(n)

# As edges connect our vertices we need 1 less.

m.edges.add(n-1)

# Creating 100 equally spaced points between 0 to 10.

yvals = np.linspace(0,10,100)


# looping through and adding vertices and edges to our mesh.

for i,y in zip(range(n),yvals):
	m.vertices[i].co = (0,y,sin(y))

	if i < n-1:
		m.edges[i].vertices = (i,i+1)

# Assigning the newly created mesh and linking it to the scene.

op = bpy.data.objects.new('sin',m)

bpy.context.scene.objects.link(op)