from room_labirints_assets import assets
from random import choice


def room_creation(difficulty: int):
    variants_list = assets[difficulty - 1]
    return choice(variants_list)
