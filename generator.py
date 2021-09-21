class LevelInfo:
    boundaries: list  # лист поинтов(x, y). Первый равен (0, 0)


class LevelGraphics:
    _lvl_info: LevelInfo

    def __init__(self, lvl_info):
        self._lvl_info = lvl_info

    def print_graphics(self):
        print("TODO")


class GenerationSettings:
    chunk_size: float
    level_scale: float


# defs here

# enddefs

def generate_boundaries(lvl: LevelInfo, gen_settings: GenerationSettings) -> list[tuple]:
    size_mod = gen_settings.level_scale
    size = gen_settings.chunk_size * size_mod
    boundaries = [
        (0, 0),
        (size, 0),
        (size, size),
        (size, size),
    ]
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
