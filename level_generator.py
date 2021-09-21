import generator
from generator import LevelInfo, LevelGraphics, GenerationSettings


def get_default_settings():
    player_width = 10.0
    settings = GenerationSettings()
    settings.chunk_size = player_width * 1.5
    settings.level_scale = 100
    return settings


def generate_level_info(gen_settings, pref_gen_set: GenerationSettings = None):
    lvl = LevelInfo()
    generator.generate_boundaries(lvl, gen_settings)  # 1) Границы уровня
    generator.generate_exits(lvl, gen_settings)  # 2) Координаты выходов
    generator.generate_roads(lvl, gen_settings)  # 3) Дороги
    generator.generate_rooms(lvl, gen_settings)  # 4) Комнаты
    generator.generate_doors(lvl, gen_settings)  # 5) Двери
    generator.generate_traps(lvl, gen_settings)  # 6) Ловушки
    generator.generate_enemies(lvl, gen_settings)  # 7) Враги
    generator.generate_lights(lvl, gen_settings)  # 8) Свет
    generator.generate_loot(lvl, gen_settings)  # 9) Лут
    generator.generate_static_environment(lvl, gen_settings)  # 10) Статик окружение
    generator.generate_new_gen_settings(lvl, gen_settings, pref_gen_set)  # 11) Настройки соединенных уровней
    return lvl


level_info = generate_level_info(get_default_settings())
level = LevelGraphics(level_info)
level.print_graphics()
# boundaries = generator.generate_area_boundaries()