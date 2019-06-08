import research

breakers = [
    {
        'id' : 1,
        'name' : 'Ленин',
        'image': 'http://seaman-sea.ru/images/stories/main8/atamahod_lenin.jpg',
        'description': '"Ленин" связал запад и восток страны: даже тяжелые арктические льды не могли помешать судну проследовать кратчайшим морским путем от европейской части к Дальнему Востоку.',
        'requirements': [1],
        'cost': 1000
    }
]

class IceBreaker:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.image = data['image']
        self.description = data['description']
        self.cost = data['cost']
        self.progress = 0
        self.requrements = []
        for req in data['requirements']:
            new_req = {}
            req_data = research.data_by_id(req)
            new_req['completed'] = False
            new_req['id'] = req
            new_req['name'] = req_data['name']

def get_all():
    all = []
    for br_data in breakers:
        all.append(IceBreaker(br_data))
    return all