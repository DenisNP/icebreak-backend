import uuid, json
import hexes, icebreakers, research

class GameState:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.colors = hexes.initial_state(self)
        self.icebreakers = [icebreakers.breaker]
        self.research = [research.reactor]

    def to_json(self):
        return json.dumps(self.__dict__)