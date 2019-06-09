import hexes, sys

ships = [
    {
        'id': 1,
        'speed': 0.8
    },
    {
        'id': 2,
        'speed': 0.9
    },
    {
        'id': 3,
        'speed': 1.0
    },
    {
        'id': 4,
        'speed': 1.1
    }
]

normal_duration = 40
rotation_downspeed = 0.8
clockwise = [[1, 1], [1, 0], [1, -1], [-1, -1], [-1, 0], [-1, 1]]
angles = [-60, 0, 60, 120, 180, 240]
movements_length = 3

class Movement:
    time_to_me = normal_duration
    rotation = -60
    hex = [65, 25]
    direction = [1, 1]

class Ship:
    def __init__(self, data):
        self.id = data['id']
        self.speed = data['speed']
        self.active = False
        
        m = Movement()
        m.rotation = -60
        m.hex = [65, 25]
        m.time_to_me = self.get_duration_to_hex(m.hex, None)
        m.direction = [1, 1]

        self.movements = [m]
        for _ in range(movements_length - 1):
            self.set_next_hex(None)

    def get_duration_to_hex(self, hex, gamestate):
        base = int(round(normal_duration / self.speed))
        if gamestate:
            ice_thickness = (100 - gamestate.ice_field.current_field[hex[0]][hex[1]])
            ice_thickness_norm = ice_thickness * 1.0 / 100.0 - 1.0
            return int(round(base * (1.0 + ice_thickness_norm)))
        else:
            return base

    def update(self, gamestate):
        if self.active:
            if self.left_ticks > 0:
                self.left_ticks -= 1
            else:
                self.set_next_hex(gamestate)
            # print(self.left_ticks)

    def set_next_hex(self, gamestate):
        while len(self.movements) > movements_length - 1:
            self.movements.pop(0)
        self.movements.append(self.next_movement_from(self.movements[-1], gamestate))
        self.left_ticks = self.movements[1].time_to_me
        
        if gamestate:
            new_movement = self.movements[-1]
            gamestate.ice_field.place_ship(new_movement.hex)

        # self.target_hexes = self.get_allowed_neighbours()
        neighbours = self.get_allowed_neighbours()
        target_hexes = []
        for h in neighbours:
            is_target = True
            for m in self.movements:
                if m.hex[0] == h[0] and m.hex[1] == h[1]:
                    is_target = False
            if is_target:
                target_hexes.append(h)

        self.target_hexes = target_hexes.copy()

    def next_movement_from(self, movement, gamestate):
        next = hexes.neighbour_hex(movement.hex[0], movement.hex[1], movement.direction[0], movement.direction[1])
        if next:
            next_movement = Movement()
            next_movement.hex = next
            next_movement.time_to_me = self.get_duration_to_hex(next, gamestate)
            next_movement.rotation = movement.rotation
            next_movement.direction = movement.direction
        else:
            next_cw = self.find_dist(movement, clockwise)
            next_ccw = self.find_dist(movement, clockwise[::-1])
            next_movement = Movement()
            cw = next_cw[0] <= next_ccw[0]
            if cw:
                next_movement.direction = next_cw[1]
                next_movement.hex = next_cw[2]
                next_duration = self.get_duration_to_hex(next_movement.hex, gamestate)
                next_movement.time_to_me = int(round(next_duration * (rotation_downspeed ** next_cw[0])))
                # rotate clockwise
                next_movement.rotation = movement.rotation + next_cw[0] * 60
            else:
                next_movement.direction = next_ccw[1]
                next_movement.hex = next_ccw[2]
                next_duration = self.get_duration_to_hex(next_movement.hex, gamestate)
                next_movement.time_to_me = int(round(next_duration * (rotation_downspeed ** next_ccw[0])))
                # rotate counter clockwise
                next_movement.rotation = movement.rotation - next_ccw[0] * 60

        # check rotation
        rot = next_movement.rotation
        while rot > 240:
            rot -= 360
        while rot < -60:
            rot += 360
        if not rot in angles:
            index = self.find_index(next_movement.direction, clockwise)
            next_movement.rotation = angles[index]
        
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

    def get_allowed_neighbours(self):
        neighbours = []
        if len(self.movements):
            m = self.movements[-1]
            for direction in clockwise:
                n = hexes.neighbour_hex(m.hex[0], m.hex[1], direction[0], direction[1])
                if n:
                    neighbours.append(n)

        return neighbours

def get_all():
    all = []
    for shp in ships:
        all.append(Ship(shp))
    return all