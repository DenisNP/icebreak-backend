from noise import pnoise2
import numpy as np

shape = (10,10)
scale = 10.0
octaves = 6
persistence = 0.5
lacunarity = 10.0

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = round(pnoise2(i/scale,
                                    j/scale,
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    base=0)*20)

for line in world:
    print(line)