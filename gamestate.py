import uuid, jsonpickle
import hexes, icebreakers, research

class GameState:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.colors = hexes.initial_state(self)
        self.icebreakers = icebreakers.get_all()
        self.research = research.get_all()

    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)