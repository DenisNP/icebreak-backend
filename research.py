researches = [
    {
        'id' : 1,
        'name' : 'Корабельная ядерная установка',
        'image': 'http://www.seaships.ru/img/6_27.jpg',
        'description': 'Ядерными энергетическими установками оснащаются мощные ледоколы, используемые в северных широтах земного шара.',
        'required_level': 1,
        'maximum_progress' : 100
    },
    {
        'id' : 2,
        'name' : 'Спутниковая навигация и связь',
        'image': 'http://epizodsspace.airbase.ru/bibl/ziv/2006/1-17.jpg',
        'description': 'Возросшие масштабы и интенсивность грузопотоков, связанный с этим рост аварий судов и самолетов обусловили необходимость создания глобальной оперативной системы поиска и спасения на базе спутниковых навигационных систем.',
        'required_level': 1,
        'maximum_progress' : 600
    },
        {
        'id' : 3,
        'name' : 'Турбины повышенной мощности',
        'image': 'http://www.morvesti.ru.images.1c-bitrix-cdn.ru/upload/iblock/7c1/7787.jpg?1529918255125646',
        'description': 'Использованы новые конструкторские решения в установке лопаток на роторе и корпусе турбины. Применен новый материал ротора для работы турбоустановки при повышенных нагрузках',
        'required_level': 1,
        'maximum_progress' : 600
    },
        {
        'id' : 4,
        'name' : 'Планкированая сталь для ледового пояса',
        'image': 'http://www.proatom.ru/img14/coj_ris7.jpg',
        'description': 'Для борьбы с интенсивным коррозионным износом металла, с образованием глубоких язв, достигавших глубины 2-5 мм за один сезон.',
        'required_level': 2,
        'maximum_progress' : 1200
    },
        {
        'id' : 5,
        'name' : 'Усовершенствованные гребные винты',
        'image': 'https://cdn.iz.ru/sites/default/files/styles/900x506/public/article-2017-05/0fbbfa8ea4eb373e113ff0a9f4cf006a.jpg?itok=Qh1w1UO4',
        'description': 'Перспективные винты неуязвимы для льда и могут в зависимости от скорости ледокола принимать оптимальную форму. Благодаря этому вырастут маневренность и мощность ледокола. ',
        'required_level': 2,
        'maximum_progress' : 1200
    },
        {
        'id' : 6,
        'name' : 'Энергоснабжение береговых объектов',
        'image': 'https://img-fotki.yandex.ru/get/9815/20701029.85/0_11375f_45b187dd_XXL.jpg',
        'description': 'В марте 2002 года во время стоянки у причала в Мурманске впервые в истории атомного ледокольного флота энергетическая установка атомохода была использована для энергоснабжения береговых объектов.',
        'required_level': 2,
        'maximum_progress' : 2400
    },
        {
        'id' : 7,
        'name' : 'Система электрического движения',
        'image': 'http://information-technology.ru/images/03-15/icebracker6.jpg',
        'description': 'Судовой ледокольный двигатель вращает электрогенератор. Генератор питает двигатель, а тот крутит гребной винт. Это позволяет наилучшим образом управлять скоростью судна.',
        'required_level': 3,
        'maximum_progress' : 2400
    },
        {
        'id' : 8,
        'name' : 'Двухосадочная конструкция',
        'image': 'http://information-technology.ru/images/03-15/icebracker1.jpg',
        'description': 'при глубокой осадке способен проламывать толстые океанские льды, при мелкой — работать в руслах рек, тем самым замещая собой сразу два ледокола: классов «Арктика» и «Таймыр» соответственно.',
        'required_level': 3,
        'maximum_progress' : 3000
    },
        {
        'id' : 9,
        'name' : 'Роботизация узлов и агрегатов',
        'image': 'https://s0.rbk.ru/v6_top_pics/resized/1180xH/media/img/2/83/755404513540832.jpeg',
        'description': 'Максимальная автономность всех систем корабля',
        'required_level': 3,
        'maximum_progress' : 3000
    },
        {
        'id' : 10,
        'name' : 'Автономное управление',
        'image': 'https://myremdom.ru/upload/vk/img/7865_Mf9b8nJbUPY.jpg',
        'description': 'Морские переходы без вмешательства человека',
        'required_level': 4,
        'maximum_progress' : 3600
    },

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