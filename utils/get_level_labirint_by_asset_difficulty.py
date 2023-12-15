from room_labirints_assets import assets


def get_level_labirint_by_asset_difficulty(level_asset, difficulty):
    level_labirint = assets[difficulty - 1][level_asset]
    return level_labirint
