import random

quests_delivery = [
    {
        'id' : 1,
        'name' : 'Ледовая проводка в Диксон',
        'image': 'quests/ship.png',
        'description': '',
        'coordinates': [62, 54],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 2,
        'name' : 'Проводка каравана на Чукотку',
        'image': 'quests/ship.png',
        'description': '',
        'coordinates': [3, 86],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 3,
        'name' : 'Доставка топлива и провизии в Певек',
        'image': 'quests/ship.png',
        'description': '',
        'coordinates': [15, 91],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 4,
        'name' : 'Проводка груза нефтепродуктов в Архангельск',
        'image': 'quests/ship.png',
        'description': '',
        'coordinates': [21, 68],
        'salary' : 40,
        'ttl' : 1800
    },
        {
        'id' : 5,
        'name' : 'Научная экспедиция на северный полюс',
        'image': 'quests/science.png',
        'description': '',
        'coordinates': [24, 45],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 6,
        'name' : 'Туристический рейс на северный полюс',
        'image': 'quests/tent.png',
        'description': '',
        'coordinates': [24, 45],
        'salary' : 40,
        'ttl' : 1800
    },
        {
        'id' : 7,
        'name' : 'Оборудование для дрейфующей станции',
        'image': 'quests/science.png',
        'description': '',
        'coordinates': [22, 49],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 8,
        'name' : 'Груз на военно-морскую базу',
        'image': 'quests/submarine.png',
        'description': '',
        'coordinates': [57,6],
        'salary' : 40,
        'ttl' : 1800
    },    {
        'id': 9,
        'name' : 'Проводка каравана сухогрузов из Китая',
        'image': 'quests/ship.png',
        'description': '',
        'coordinates': [6, 84],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 10,
        'name' : 'Крупный транспортный караван из Мурманска',
        'image': 'quests/ship.png',
        'description': '',
        'coordinates': [65, 15],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 11,
        'name' : 'Проводка судов на утилизацию из Тикси',
        'image': 'quests/ship.png',
        'description': '',
        'coordinates': [62, 54],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id': 12,
        'name' : 'Экологическая научная экспедиция',
        'image': 'quests/bear.png',
        'description': '',
        'coordinates': [49, 36],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 13,
        'name' : 'Исследования полярной фауны',
        'image': 'quests/bear.png',
        'description': '',
        'coordinates': [3, 86],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 14,
        'name' : 'Доставка припасов на приледнившуюся подводную лодку',
        'image': 'quests/submarine.png',
        'description': '',
        'coordinates': [15, 91],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 15,
        'name' : 'Эвакуация судна замерзшего во льдах',
        'image': 'quests/ship.png',
        'description': '',
        'coordinates': [21, 68],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 16,
        'name' : 'Доставка экологов на дрейфующую станцию',
        'image': 'quests/science.png',
        'description': '',
        'coordinates': [24, 45],
        'salary' : 40,
        'ttl' : 1800
    },
     {
        'id': 17,
        'name' : 'Прокладка кабеля для подводного датацентра',
        'image': 'quests/science.png',
        'description': '',
        'coordinates': [43, 2],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 18,
        'name' : 'Археологическая экспедиция по маршрутам полярных исследователей',
        'image': 'quests/tent.png',
        'description': '',
        'coordinates': [68, 47],
        'salary' : 40,
        'ttl' : 1800
    },
    {
        'id' : 19,
        'name' : 'Помощь Норвежцам в рамках международного сотрудничества',
        'image': 'quests/ship.png',
        'description': '',
        'coordinates': [43, 2],
        'salary' : 80,
        'ttl' : 1800
    },
    {
        'id' : 20,
        'name' : 'Груз морепродуктов из Сабетты',
        'image': 'quests/ship.png',
        'description': '',
        'coordinates': [68, 47],
        'salary' : 60,
        'ttl' : 1800
    },
]

class Quest:
    def __init__(self, data):
        self.completed = False
        self.taken = False
        self.failed = False

        self.id = data['id']
        self.name = data['name']
        self.image = data['image']
        self.description = data['description']
        self.coordinates = data['coordinates']
        self.salary = data['salary']
        self.ttl = data['ttl']
        self.start_ttl = data['ttl']

    def update(self):
        if self.taken and not self.completed and not self.failed:
            self.ttl -= 1
            if self.ttl <= 0:
                self.failed = True

    def complete_quest(self, gamestate):
        if self.taken and not self.completed and not self.failed:
            self.completed = True
            gamestate.money += self.salary
    
    def take_quest(self):
        if not self.taken:
            self.taken = True
            # TODO maybe random coordinates
            # self.coordinates = ...
    
def get_all():
    all = []
    for q_data in quests_delivery:
        all.append(Quest(q_data))
    return all