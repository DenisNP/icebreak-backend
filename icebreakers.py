import research

breakers = [
    {
        'id' : 1,
        'name' : 'Ленин (пр. 92М)',
        'image': 'http://www.rosatomflot.ru/img/images/1-1024x1024-5-0_23893d98f565.jpg',
        'description': '"Ленин" связал запад и восток страны: даже тяжелые арктические льды не могли помешать судну проследовать кратчайшим морским путем от европейской части к Дальнему Востоку.',
        'requirements': [1],
        'maximum_progress': 600,
        'cost': 30,
        'parameters': [
            ['Длина','134 м'],
            ['Ширина','27,6 м'],
            ['Высота борта','16,1 м'],
            ['Водоизмещение', '19 240 т'],
            ['Мощность главной установки', '44 000 л.с.'],
            ['Скорость хода на чистой воде', '19,6 уз']
        ],

    },
    {
        'id' : 2,
        'name' : 'Таймыр (пр. 10580)',
        'image': 'http://www.rosatomflot.ru/img/images/1-1024x1024-5-0_a95f5c941a24.jpg',
        'description': 'Атомный ледокол, предназначенный для проводки судов в устья сибирских рек. Отличается уменьшенной осадкой. Назван в честь ледокольного парохода начала XX века «Таймыр».',
        'requirements': [3,4],
        'maximum_progress': 1200,
        'cost': 60,
        'parameters': [
            ['Длина','151,8 м'],
            ['Ширина','29,2 м'],
            ['Высота борта','15,2 м'],
            ['Водоизмещение', '21 000 т'],
            ['Мощность главной установки', '50 000 л.с.'],
            ['Скорость хода на чистой воде', '18,5 уз']
        ]
    },
    {
        'id' : 3,
        'name' : 'Арктика (пр. 10520)',
        'image': 'http://www.rosatomflot.ru/img/images/1-1024x1024-5-0_afe64c1d9cf9.jpg',
        'description': 'Первое в истории судно, достигшее Северного полюса в надводном плавании; Второй в мире атомный ледокол.',
        'requirements': [5,6],
        'maximum_progress': 1800,
        'cost': 90,
        'parameters': [
            ['Длина','147,9 м'],
            ['Ширина','29,9 м'],
            ['Высота борта','17,2 м'],
            ['Водоизмещение', '23 000 т'],
            ['Мощность главной установки', '75 000 л.с.'],
            ['Скорость хода на чистой воде', '20,8 уз']
        ]
    },
     {
        'id' : 4,
        'name' : 'Арктика ЛК-60Я (пр. 22220)',
        'image': 'https://media.tvzvezda.ru/news/opk/content/201807021201-jcjy.htm/1.jpg',
        'description': 'Новый тип российских атомных ледоколов. Благодаря использованию переменной осадки ледоколы данного проекта способны равно эффективно работать как на глубокой воде, так и на мелководье в руслах сибирских рек. Данная особенность позволяет заменить этими ледоколами как ледоколы типа «Арктика», так и типа «Таймыр» и следовательно, уменьшить общую стоимость эксплуатации атомного ледокольного флота, полностью сохранив все его возможности.',
        'requirements': [7,8],
        'maximum_progress': 2400,
        'cost': 110,
        'parameters': [
            ['Длина','173,3 м'],
            ['Ширина','34,0 м'],
            ['Высота борта','15,2 м'],
            ['Водоизмещение', '33 530 т'],
            ['Мощность главной установки', '82 000 л.с.'],
            ['Скорость хода на чистой воде', '22 уз']
        ]
    },
     {
        'id' : 5,
        'name' : 'Лидер ЛК-120Я (пр. 10520)',
        'image': 'https://severpost.ru/docs/upload/2018/06/1529060302.jpg',
        'description': 'Единственный ледоколом в мире для круглогодичной проводки судов по Северному морскому пути при толщине льда свыше 4 м. За счет обширной автоматизации может работать без вмешательства операторов.',
        'requirements': [9,10],
        'maximum_progress': 3000,
        'cost': 200,
        'parameters': [
            ['Длина','209,0 м'],
            ['Ширина','47,7 м'],
            ['Высота борта','20,3 м'],
            ['Водоизмещение', '71 380 т'],
            ['Мощность главной установки', '163 000 л.с.'],
            ['Скорость хода на чистой воде', '24 уз']
        ]
    },
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
        self.parameters = data['parameters']
        self.requirements = []
        for req in data['requirements']:
            new_req = {}
            req_data = research.data_by_id(req)
            new_req['completed'] = False
            new_req['id'] = req
            new_req['name'] = req_data['name']
            new_req['image'] = req_data['image']
            self.requirements.append(new_req)

    def update(self, gamestate):
        #iterating progress bar
        if self.progress > 0 and self.progress < self.maximum_progress:
            self.progress = self.progress + 1
            if self.progress == self.maximum_progress:
                gamestate.activate_ship(self.id)

        #checking if technologies are created and set them completed
        for research in self.requirements:
            res = gamestate.get_research_by_id(research['id'])
            if not research['completed'] and res.progress == res.maximum_progress:
                research['completed'] = True
 
    def start_building(self, gamestate):
        if gamestate.money >= self.cost and self.progress == 0 and all(res.completed == True for res in self.requirements):
            gamestate.money = gamestate.money - self.cost
            self.progress = 1

def get_all():
    all = []
    for br_data in breakers:
        all.append(IceBreaker(br_data))
    return all