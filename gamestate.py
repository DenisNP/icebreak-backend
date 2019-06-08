import uuid, jsonpickle
import hexes, icebreakers, research

class GameState:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.colors = hexes.initial_state(self)
        self.icebreakers = icebreakers.get_all()
        self.research = research.get_all()

    def update(self):
        for brkr in self.icebreakers:
            brkr.update(self)
    
    def get_research_by_id(self, research_id):
        return list(filter(lambda x: x.id == research_id, self.research))[0]
            
    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)


state = GameState()
print (state.get_research_by_id(1).name)