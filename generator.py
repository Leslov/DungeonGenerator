from polygon_generator import to_convex_contour
from GenerationSettings import GenerationSettings
from LevelInfo import LevelInfo


def generate_boundaries(lvl: LevelInfo, gen_settings: GenerationSettings) -> list[tuple]:
    size_mod = gen_settings.level_scale
    size = gen_settings.chunk_size * size_mod
    contour = to_convex_contour(gen_settings.edges_count) # Нужно упростить генерацию
    boundaries = [(x * size, y * size) for x, y in contour]
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
