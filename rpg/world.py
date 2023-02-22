from typing import List
import rpg.stage as stage

class World:

    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.stages: List[stage.Stage] = []