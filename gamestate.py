import uuid, json
import hexes

class GameState:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.colors = hexes.initial_state(self)

    def to_json(self):
        return json.dumps(self.__dict__)