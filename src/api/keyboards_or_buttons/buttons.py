from dataclasses import dataclass
from src.api.keyboards_or_buttons.models import (Menu, Register
                                                 )
from typing import Type


@dataclass
class Buttons:
    menu: Type[Menu] = Menu()
    register: Type[Register] = Register()


buttons = Buttons()
