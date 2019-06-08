import uuid, jsonpickle, hexes, icebreakers, research, time, ship
from datacenter import DataCenter

ticks_per_second = 10
tick_duration = round(1000 / ticks_per_second)
start_money = 10000
datacenter_start_cost = 100
datacenter_cost_coeff = 1.2

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
        self.datacenters = []
        self.datacenter_cost = 0
        self.set_next_dc_cost()

    def ct(self):
        return int(round(time.time() * 1000))

    def set_next_dc_cost(self):
        if self.datacenter_cost == 0:
            self.datacenter_cost = datacenter_start_cost
        else:
            self.datacenter_cost = int(round(self.datacenter_cost * datacenter_cost_coeff))

    def update_all(self):
        t = self.ct()
        diff = round(t - self.last_request)
        ticks = round(diff / tick_duration)
        for _ in range(ticks):
            self.update()

    def update(self):
        for brkr in self.icebreakers:
            brkr.update(self)
        
        res = self.check_if_any_research_in_progress()

        if res:
            res.update()
        for rsrch in self.research:
            if (not rsrch.progress == 0 and not rsrch.progress == rsrch.maximum_progress):
                rsrch.update(self)

    def build_datacenter(self, row, col):
        if self.money >= self.datacenter_cost:
            self.money -= self.datacenter_cost
            self.set_next_dc_cost()
            self.datacenters.append(DataCenter(row, col))
            self.research_level -= 1
    
    def get_research_by_id(self, research_id):
        return list(filter(lambda x: x.id == research_id, self.research))[0]
    
    def check_if_any_research_in_progress(self):
        res = list(filter(lambda x: x.progress > 0 and x.progress < x.maximum_progress, self.research))
        if res:
            return res[0]
        
        return None

            
    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)

