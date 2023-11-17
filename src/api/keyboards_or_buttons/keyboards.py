from dataclasses import dataclass

from src.api.keyboards_or_buttons.markup import Markup
from src.api.keyboards_or_buttons.models import (Menu, Register, Games
                                                 )


@dataclass
class Keyboards:
    menu: Markup = Markup(Menu())
    register: Markup = Markup(Register())
    games: Markup = Markup(Games())


keyboards = Keyboards()
