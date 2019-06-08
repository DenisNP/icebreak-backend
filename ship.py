import hexes

ships = [
    {
        'id': 1,
        'speed': 0.8
    },
    {
        'id': 2,
        'speed': 0.9
    }
]

normal_duration = 40
rotation_downspeed = 0.8
clockwise = [[1, 1], [1, 0], [1, -1], [-1, -1], [-1, 0], [-1, 1]]
movements_length = 3

class Movement:
    time_to_me = normal_duration
    rotation = -60
    hex = [49, 14]
    direction = [1, 1]

class Ship:
    def __init__(self, data):
        self.id = data['id']
        self.speed = data['speed']
        self.active = False
        
        m = Movement()
        m.rotation = -60
        m.hex = [49, 14]
        m.time_to_me = self.get_duration_to_hex(self, m.hex)
        m.direction = [1, 1]

        self.movements = [m]
        for _ in range(movements_length - 1):
            self.set_next_hex()

    def get_duration_to_hex(self, hex):
        return int(round(normal_duration / self.speed))

    def update(self, state):
        if self.active:
            if self.left_ticks > 0:
                self.left_ticks -= 1
            else:
                self.set_next_hex()

    def set_next_hex(self):
        while len(self.movements) > movements_length - 1:
            self.movements.pop(0)
        self.movements.append(self.next_movement_from(self.movements[-1]))
        self.left_ticks = self.movements[1].time_to_me

    def next_movement_from(self, movement):
        next = hexes.neighbour_hex(movement.hex[0], movement.hex[1], movement.direction[0], movement.direction[1])
        if next:
            next_movement = Movement()
            next_movement.hex = next
            next_movement.time_to_me = self.get_duration_to_hex(next)
            next_movement.rotation = movement.rotation
            next_movement.direction = movement.direction
        else:
            next_cw = self.find_dist(movement, clockwise)
            next_ccw = self.find_dist(movement, clockwise[::-1])
            next_movement = Movement()
            if next_cw[0] <= next_ccw[0]:
                next_movement.direction = next_cw[1]
                next_movement.hex = next_cw[2]
                next_duration = self.get_duration_to_hex(next_movement.hex)
                next_movement.time_to_me = int(round(next_duration * (rotation_downspeed ** next_cw[0]))) # TODO
                # rotate clockwise
                next_movement.rotation = movement.rotation + next_cw[0] * 60
            else:
                next_movement.direction = next_ccw[1]
                next_movement.hex = next_ccw[2]
                next_duration = self.get_duration_to_hex(next_movement.hex)
                next_movement.time_to_me = int(round(next_duration * (rotation_downspeed ** next_ccw[0]))) # TODO
                # rotate counter clockwise
                next_movement.rotation = movement.rotation - next_ccw[0] * 60
        
        return next_movement
            
    def find_index(self, direction, array):
        for i in range(6):
            if array[i][0] == direction[0] and array[i][1] == direction[1]:
                return i
        return -1

    def find_dist(self, movement, array):
        index = self.find_index(movement.direction, array)
        dist = 0
        while dist < 6:
            dist += 1
            new_idx = index + dist
            if new_idx >= len(clockwise):
                new_idx -= len(clockwise)
            new_direction = clockwise[new_idx]
            potential_next = hexes.neighbour_hex(movement.hex[0], movement.hex[1], new_direction[0], new_direction[1])
            if potential_next:
                break
        return [dist, new_direction, potential_next]

def get_all():
    all = []
    for shp in ships:
        all.append(Ship(shp))
    return all