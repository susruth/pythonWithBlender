import bpy
from random import randint


for i in range(randint(50,100)):
	bpy.ops.mesh.primitive_monkey_add(
		location = [randint(-10,10) for axis in 'xyz']
	)