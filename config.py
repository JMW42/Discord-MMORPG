from rpg import world
from enum import IntEnum, Enum
from typing import List
from rpg import world, stage
import csv, yaml


class STAGESFILE(IntEnum):
    ID:int = 0
    NAME:int = 1
    TEXT:int = 2


class WORLDFILE(Enum):
    NAME:str = "NAME"
    DESCRIPTION:str = "DESCRIPTION"


WORLD = world.World("emptyworld", "emptytext")


def load_word(worldfile:str, stagesfile:str):
    global WORLD
    print("loading world:")
    w = world.World("world", "description")

    # load world config
    print(f"loading world configuration file: {worldfile}")
    with open(worldfile, "r") as stream:
        try:
            data = yaml.safe_load(stream)
            for key in data:
                print(f"\t - {key}: {data[key]}")
                w.name = data[WORLDFILE.NAME.value]
                w.name = "HELLO"
                w.description = data[WORLDFILE.DESCRIPTION.value]
        except yaml.YAMLError as exc:
            print(exc)


    # load stages
    print(f"loading stagesfile: {stagesfile}")
    try: 
        with open(stagesfile, "r") as file:
            print(f' - loading stages:')
            data = csv.reader(file); next(data)

            for row in data:
                s = stage.Stage(id=row[STAGESFILE.ID], name=row[STAGESFILE.NAME], text=row[STAGESFILE.TEXT])
                w.stages.append(s)

                print(f'\t {s.id} : {s.name}, - {s.text}')
    except Exception as E:
        print(E)
    
    WORLD = w
    return w