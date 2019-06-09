import uuid, jsonpickle, hexes, icebreakers, research, time, ship
import sys
from datacenter import DataCenter
from ice import Ice

ticks_per_second = 10
tick_duration = round(1000 / ticks_per_second)
start_money = 10000
datacenter_start_cost = 10
datacenter_cost_coeff = 1.2

class GameState:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.build_hexes = hexes.build_hexes.copy()
        
        self.icebreakers = icebreakers.get_all()
        self.research = research.get_all()
        self.ships = ship.get_all()
        self.ships[0].active = True

        self.last_request = self.ct()
        self.money = start_money
        self.research_level = 0
        self.datacenters = []
        self.datacenter_cost = 0
        self.set_next_dc_cost()

        self.ice_field = Ice()

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
        # print(ticks, file=sys.stdout)
        for _ in range(ticks):
            self.update()
        self.last_request = t

    def update(self):
        for brkr in self.icebreakers:
            brkr.update(self)
        
        res = self.check_if_any_research_in_progress()
        if res:
            res.update()

        for shp in self.ships:
            shp.update(self)

        self.ice_field.update()

    def build_datacenter(self, row, col):
        if self.money >= self.datacenter_cost:
            for b_hex in self.build_hexes:
                if b_hex[0] == row and b_hex[1] == col:
                    self.money -= self.datacenter_cost
                    self.set_next_dc_cost()
                    self.datacenters.append(DataCenter(row, col))
                    self.research_level -= 1

                    self.build_hexes.remove(b_hex)
                    break

    def activate_ship(self, id):
        for shp in self.ships:
            if shp.id == id:
                shp.active = True
                # TODO event?
                break
    
    def get_research_by_id(self, research_id):
        return list(filter(lambda x: x.id == research_id, self.research))[0]
    
    def check_if_any_research_in_progress(self):
        res = list(filter(lambda x: x.progress > 0 and x.progress < x.maximum_progress, self.research))
        if res:
            return res[0]
        
        return None

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['ice_field']
        state['ice'] = self.ice_field.current_field
        return state
            
    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)