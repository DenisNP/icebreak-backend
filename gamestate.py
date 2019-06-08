import uuid, jsonpickle, hexes, icebreakers, research, time, ship

ticks_per_second = 10
tick_duration = round(1000 / ticks_per_second)
start_money = 10000

class GameState:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.colors = hexes.initial_state(self)
        
        self.icebreakers = icebreakers.get_all()
        self.research = research.get_all()
        self.ships = ship.get_all()

        self.last_request = self.ct()
        self.money = start_money
        self.research_level = 0

    def ct(self):
        return int(round(time.time() * 1000))

    def update_all(self):
        t = self.ct()
        diff = round(t - self.last_request)
        ticks = round(diff / tick_duration)
        for _ in range(ticks):
            self.update()

    def update(self):
        for brkr in self.icebreakers:
            brkr.update(self)
        for rsrch in self.research:
            if (not rsrch.progress == 0 and not rsrch.progress == rsrch.maximum_progress):
                rsrch.update(self)
    
    def get_research_by_id(self, research_id):
        return list(filter(lambda x: x.id == research_id, self.research))[0]
    
    def check_if_any_research_in_progress(self):
        res = list(filter(lambda x: x.progress > 0 and x.progress < x.maximum_progress, self.research))
        if res:
            return res[0]
        
        return None

            
    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)


state = GameState()

for brkr in state.icebreakers:
    for req in brkr.requirements:
        req.completed = True
    
    brkr.start_building(state)