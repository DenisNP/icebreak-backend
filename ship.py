ships = [
    {
        'id': 1,
        'speed': 10
    },
    {
        'id': 2,
        'speed': 15
    }
]

normal_speed = 40

class Ship:
    def __init__(self, data):
        self.id = data['id']
        self.speed = data['speed']
        self.active = False
        self.vertical = 1
        self.horizontal = 1
        self.current_hex = [49, 14]
        self.current_speed = normal_speed
        self.left_ticks = self.current_speed
        self.set_next_hex()

    def update(self, state):
        if self.left_ticks > 0:
            self.left_ticks -= 10
        else:
            self.set_next_hex()

    def set_next_hex(self):
        self.choose_next_hex()
        #self.current_speed = 
        self.left_ticks = self.current_speed

    def choose_next_hex(self):
        return None

def get_all():
    all = []
    for shp in ships:
        all.append(Ship(shp))
    return all