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

class Ship:
    def __init__(self, data):
        self.id = data['id']
        self.speed = data['speed']
        self.active = False

    def update(self, state):
        return None

def get_all():
    all = []
    for shp in ships:
        all.append(Ship(shp))
    return all