from noise import pnoise2
import numpy as np
import hexes, copy, random

hor_count = max(hexes.hor_count_even, hexes.hor_count_odd)
shape = (hor_count, hexes.ver_count)
scale = 10.0
octaves = 1
persistence = 0
lacunarity = 0.5

seed = np.random.randint(0, 100)
seed = 50
resolution = 4

max_val = 0.75
min_val = -0.75

ticks_between_states = 300
basic_speed = 2

class Ice:
    def __init__(self):
        self.hor_shift = 0
        self.ver_shift = 0
        self.hor_speed = random.randint(-1, 1) * basic_speed
        self.ver_speed = random.randint(-1, 1) * basic_speed

        self.generate_next_field()
        self.current_field = copy.deepcopy(self.next_field)
        self.move_field()
        self.generate_next_field()

        self.current_phase = 0
        self.trails = {}

    def move_field(self):
        self.hor_shift += self.hor_speed
        self.ver_shift += self.ver_speed
        self.hor_speed += random.randint(-1, 1) * basic_speed
        self.ver_speed += random.randint(-1, 1) * basic_speed

    def generate_next_field(self):
        try:
            self.start_field = copy.deepcopy(self.current_field)
        except:
            pass

        world = np.zeros(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                world[i][j] = round(pnoise2((i + self.hor_shift)/scale, (j + self.ver_shift)/scale, octaves=octaves, lacunarity=lacunarity, base=seed)*resolution)/resolution

        ice = []
        for c in range(len(world)):
            ice.append([])
            for r in range(len(world[c])):
                if hexes.is_hex_exists(r, c):
                    val = (world[c][r] - min_val) / (max_val - min_val)
                    if val > 1:
                        val = 1
                    if val < 0:
                        val = 0
                    ice[-1].append(int(round(val * 100)))
                else:
                    ice[-1].append(0)
        
        self.next_field = ice

    def update(self):
        if self.current_phase >= ticks_between_states:
            self.move_field()
            self.generate_next_field()
            self.current_phase = 0
        
        for i in range(len(self.current_field)):
            for k in range(len(self.current_field[i])):
                next_val = self.next_field[i][k]
                start_val = self.start_field[i][k]
                self.current_field[i][k] = int(round(start_val + (next_val - start_val) * (self.current_phase / ticks_between_states)))
                trail = str(i * 1000 + k)
                if self.trails[trail]:
                    self.current_field[i][k] = max(0, self.current_field[i][k] - self.trails[trail]/10)

        for trail in self.trails:
            self.trails[trail] -= 1
            if self.trails[trail] <= 0:
                self.trails.pop(trail, None)

        self.current_phase += 1

    def place_ship(self, hex):
        i = hex[0]
        k = hex[1]
        trail = str(i * 1000 + k)
        if self.trails[trail]:
            self.trails[trail] += 300
        else:
            self.trails[trail] = 300

if __name__ == '__main__':
    world = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = round(pnoise2((i)/scale, (j)/scale, octaves=octaves, lacunarity=lacunarity, base=seed)*resolution)/resolution

    flatten = np.array(world).flatten()
    print(max(flatten), min(flatten))