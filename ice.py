from noise import pnoise2
import numpy as np
import hexes

hor_count = max(hexes.hor_count_even, hexes.hor_count_odd)
shape = (hor_count, hexes.ver_count)
scale = 50.0
octaves = 1
persistence = 0
lacunarity = 10.0

seed = np.random.randint(0, 100)
seed = 50
resolution = 20

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = round(pnoise2((i)/scale,
                                    (j)/scale,
                                    octaves=octaves,
                                    lacunarity=lacunarity, 
                                    base=seed)*resolution)/resolution

flatten = np.array(world).flatten()
max_val = max(flatten)
min_val = min(flatten)

ice = []
for c in range(len(world)):
    ice.append([])
    for r in range(len(world[c])):
        if hexes.is_hex_exists(r, c):
            val = (world[c][r] - min_val) / (max_val - min_val)
            ice[-1].append(int(round(val * 100)))
        else:
            ice[-1].append(0)
# for line in world:
#      print(line)