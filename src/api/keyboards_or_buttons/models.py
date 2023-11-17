from dataclasses import dataclass


@dataclass
class Menu:
    profile: str = "Профиль"
    games: str = "Игры"
    setting: str = "Настройки"
    support: str = "Поддержка"
    about_service: str = "О сервисе"


@dataclass
class Register:
    accept: str = "Принимаю"
