researches = [
    {
        'id' : 1,
        'name' : 'Атомный Реактор',
        'image': 'http://seaman-sea.ru/images/stories/main8/atamahod_lenin.jpg',
        'description': 'Без атомного реактора далеко не уплывешь',
        'required_level': 1,
        'maximum_progress' : 200
    }
]

class Research:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.image = data['image']
        self.description = data['description']
        self.required_level = data['required_level']
        self.maximum_progress = data['maximum_progress']
        self.progress = 0

    def update(self):
        if self.progress > 0 and self.progress < self.maximum_progress:
            self.progress = self.progress + 1
        
    def start_research(self, gamestate):
        if not gamestate.check_if_any_research_in_progress():
            self.progress = 1
           
def data_by_id(id):
    for res in researches:
        if res['id'] == id:
            return res

def get_all():
    all = []
    for res_data in researches:
        all.append(Research(res_data))
    return all