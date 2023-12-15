from room_labirints_assets import assets
from random import randint


def room_creation(difficulty: int):
    variants_list = assets[difficulty - 1]
    asset_id = randint(0, len(variants_list))
    return variants_list[asset_id], asset_id
