from GenerationSettings import GenerationSettings
from LevelInfo import LevelInfo


def generate_boundaries(lvl: LevelInfo, gen_settings: GenerationSettings) -> list[tuple]:
    size_mod = gen_settings.level_scale
    size = gen_settings.chunk_size * size_mod
    boundaries = [
        (size*0.1, size*0.1),
        (size*0.9, size*0.2),
        (size*0.9, size*0.8),
        (size*0.4, size*0.9),
    ]  # Координаты должны иметь только положительные значения
    lvl.boundaries = boundaries


def generate_exits(lvl: LevelInfo, gen_settings: GenerationSettings):
    return None


def generate_roads(lvl: LevelInfo, gen_settings: GenerationSettings):
    return None


def generate_rooms(lvl: LevelInfo, gen_settings: GenerationSettings):
    return None


def generate_doors(lvl: LevelInfo, gen_settings: GenerationSettings):
    return None


def generate_traps(lvl: LevelInfo, gen_settings: GenerationSettings):
    return None


def generate_enemies(lvl: LevelInfo, gen_settings: GenerationSettings):
    return None


def generate_lights(lvl: LevelInfo, gen_settings: GenerationSettings):
    return None


def generate_loot(lvl: LevelInfo, gen_settings: GenerationSettings):
    return None


def generate_static_environment(lvl: LevelInfo, gen_settings: GenerationSettings):
    return None


def generate_new_gen_settings(lvl: LevelInfo, gen_settings: GenerationSettings, prev_gen_settings: GenerationSettings):
    if not prev_gen_settings:
        pass
    return None
