import customtkinter
from .read_json import read_json
import json
# імпортуємо всі необхідні модулі
mainframe = customtkinter.CTk(fg_color="#008000")
# створюємо графічне вікно та задаємо колір тексту
main_config = read_json(name_file= "config.json")
# print(json.dumps(main_config, indent= 4))
# загружаємо файл конфігурації в змінну
WIDTH = main_config["main_frame"]["width"]
HEIGHT = main_config["main_frame"]["height"]
# задаємо ширину і довжину вікна
mainframe.geometry(f"{WIDTH}x{HEIGHT}")
# встановлюємо геометрію вікна у форматі ширина x довготa