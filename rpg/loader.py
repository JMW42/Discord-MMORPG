from enum import IntEnum
from typing import List
from rpg import world, stage
import csv

class STAGEFILE(IntEnum):
    ID:int = 0
    NAME:int = 1
    TEXT:int = 2



def load_word(stagefile:str):
    print("loading world:")
    w = world.World("world", "description")

    with open(stagefile, "r") as file:
        print(f' - loading stages:')
        data = csv.reader(file); next(data)

        for row in data:
            s = stage.Stage(id=row[STAGEFILE.ID], name=row[STAGEFILE.NAME], text=row[STAGEFILE.TEXT])
            w.stages.append(s)

            print(f'\t {s.id} : {s.name}, - {s.text}')

    return w