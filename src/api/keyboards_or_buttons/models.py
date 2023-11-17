from dataclasses import dataclass


@dataclass
class Menu:
    profile: str = "Профиль"
    games: str = "Игры"
    setting: str = "Настройки"
    support: str = "Поддержка"
    about_service: str = "О сервисе"


@dataclass
class Games:
    slot: str = "Слот"
    dice: str = "Кубик"
    soccer: str = "Футбол"
    bowling: str = "Боулинг"
    basketball: str = "Баскетболл"
    darts: str = "Дартс"


@dataclass
class Register:
    accept: str = "Принимаю"
