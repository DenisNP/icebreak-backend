import uuid, jsonpickle, hexes, icebreakers, research, time, ship, quests
import sys, random
from datacenter import DataCenter
from ice import Ice

ticks_per_second = 10
tick_duration = round(1000 / ticks_per_second)
start_money = 11
datacenter_start_cost = 10
datacenter_cost_coeff = 1.2

fail_quests_count = 3
quest_frequency_per_ship = 1200
first_quest_start = 100

class GameState:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.build_hexes = hexes.build_hexes.copy()
        
        self.icebreakers = icebreakers.get_all()
        self.research = research.get_all()
        self.ships = ship.get_all()
        self.ships[0].active = True

        self.icebreakers[0].progress = self.icebreakers[0].maximum_progress
        self.research[0].progress = self.research[0].maximum_progress

        self.last_request = self.ct()
        self.money = start_money
        self.research_level = 1
        self.datacenters = []
        self.datacenter_cost = 0
        self.set_next_dc_cost()

        self.quests = quests.get_all()

        self.ice_field = Ice()
        self.status = 0
        self.last_quest_got = self.ct() - int(round((quest_frequency_per_ship - first_quest_start) * (1000 / ticks_per_second)))
        # print(self.last_quest_got, self.ct(), self.ct() - self.last_quest_got, "last got")

    def ct(self):
        return int(round(time.time() * 1000))

    def ships_count(self):
        cnt = sum(1 for x in self.icebreakers if x.progress >= x.maximum_progress)
        return max(cnt, 1)

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
        self.check_if_get_quest()

    def check_if_get_quest(self):
        diff = self.ct() - self.last_quest_got
        wait = int(round(quest_frequency_per_ship / self.ships_count()) * 1000 / ticks_per_second)
        # print(diff, wait)
        if diff >= wait:
            self.last_quest_got = self.ct() + int(round(random.randint(-100, 100) / self.ships_count()))
            # print("get quest", self.last_quest_got, diff, wait)
            quests = list(filter(lambda q: not q.taken and not q.failed and not q.completed, self.quests))
            if len(quests) > 0:
                idx = random.randint(0, len(quests) - 1)
                quest = quests[idx]
                # print("quest found")
                quest.take_quest()

    def check_if_complete_quest(self, hex):
        for q in self.quests:
            if q.taken and not q.completed and not q.failed:
                coords = q.coordinates
                for i in [-3, -2, -1, 0, 1, 2, 3]:
                    for k in [-3, -2, -1, 0, 1, 2, 3]:
                        if hex[0] + i == coords[0] and hex[1] + k == coords[1]:
                            q.complete_quest(self)
                            return None

    def update(self):
        if self.status == 0:
            for brkr in self.icebreakers:
                brkr.update(self)
            
            res = self.check_if_any_research_in_progress()
            if res:
                res.update()

            for shp in self.ships:
                shp.update(self)

            for q in self.quests:
                q.update()

            self.ice_field.update()
            self.check_status()

    def disable_ice(self):
        self.ice_field.enabled = False

    def check_status(self):
        count_q = sum(1 for x in self.quests if x.failed)
        if count_q >= fail_quests_count:
            self.status = -1

        count_s = self.ships_count()
        if count_s >= len(self.icebreakers):
            self.status = 1

    def build_datacenter(self):
        if self.money >= self.datacenter_cost:
            free_hexes = [x for x in hexes.build_hexes if self.not_busy(x)]
            if len(free_hexes) > 0:
                index = random.randint(0, len(free_hexes) - 1)
                hex = free_hexes[index]
                dc = DataCenter(hex[0], hex[1])
                self.datacenters.append(dc)
                self.money -= self.datacenter_cost
                self.set_next_dc_cost()
                self.research_level += 1

    def not_busy(self, hex):
        for dc in self.datacenters:
            if dc.row == hex[0] and dc.col == hex[1]:
                return True
        return False

    def activate_ship(self, id):
        for shp in self.ships:
            if shp.id == id:
                shp.active = True
                # TODO event?
                break
    
    def get_research_by_id(self, research_id):
        return list(filter(lambda x: x.id == research_id, self.research))[0]
    
    def get_icebreaker_by_id(self, icebreaker_id):
        return list(filter(lambda x: x.id == icebreaker_id, self.icebreakers))[0]
    
    def get_ship_by_id(self, ship_id):
        return list(filter(lambda x: x.id == ship_id, self.ships))[0]
    
    def check_if_any_research_in_progress(self):
        res = list(filter(lambda x: x.progress > 0 and x.progress < x.maximum_progress, self.research))
        if res:
            return res[0]
        
        return None

    def parse_action(self, req_data):
        # print(req_data, "parse_action")
        try:
            action = req_data['action']
        except:
            action = ''
        
        if action == 'Research':
            research_id = req_data['researchId']
            res = self.get_research_by_id(research_id)
            res.start_research(self)
        
        if action == 'Icebreaker':
            icebreaker_id = req_data['icebreakerId']
            brkr = self.get_icebreaker_by_id(icebreaker_id)
            brkr.start_building(self)
        
        if action == 'Datacenter':
            self.build_datacenter()
        
        if action == 'ControlShip':
            ship_id = req_data['shipId']
            direction = list(req_data['direction'])
            shp = self.get_ship_by_id(ship_id)
            shp.force_move(self, direction)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['ice_field']
        if self.ice_field.enabled:
            state['ice'] = self.ice_field.current_field
        else:
            state['ice'] = []
        return state
            
    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)