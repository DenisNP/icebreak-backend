import research

breakers = [
    {
        'id' : 1,
        'name' : 'Ленин',
        'image': 'http://seaman-sea.ru/images/stories/main8/atamahod_lenin.jpg',
        'description': '"Ленин" связал запад и восток страны: даже тяжелые арктические льды не могли помешать судну проследовать кратчайшим морским путем от европейской части к Дальнему Востоку.',
        'requirements': [1],
        'maximum_progress' : 1000,
        'cost': 1000
    },
    {
        'id' : 2,
        'name' : 'Арктика',
        'image': 'http://seaman-sea.ru/images/stories/main8/atamahod_lenin.jpg',
        'description': '"Арктика" связал запад и восток страны: даже тяжелые арктические льды не могли помешать судну проследовать кратчайшим морским путем от европейской части к Дальнему Востоку.',
        'requirements': [1],
        'maximum_progress': 10000,
        'cost': 10000
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
        self.maximum_progress = data['maximum_progress']
        self.requirements = []
        for req in data['requirements']:
            new_req = {}
            req_data = research.data_by_id(req)
            new_req['completed'] = False
            new_req['id'] = req
            new_req['name'] = req_data['name']
            self.requirements.append(new_req)

    def update(self, gamestate):
        #iterating progress bar
        if self.progress > 0 and self.progress < self.maximum_progress:
            self.progress = self.progress + 1

        #checking if technologies are created and set them completed
        for research in self.requirements:
            res = gamestate.get_research_by_id(research.id)
            if not research.completed and res.progress == res.maximum_progress:
                research.completed = True
 
    def start_building(self, gamestate):
        if gamestate.money >= self.cost and self.progress == 0 and all(res.completed == True for res in self.requirements):
            gamestate.money = gamestate.money - self.cost
            self.progress = 1

def get_all():
    all = []
    for br_data in breakers:
        all.append(IceBreaker(br_data))
    return all