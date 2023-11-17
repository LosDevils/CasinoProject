from dataclasses import dataclass

from src.api.keyboards_or_buttons.markup import Markup
from src.api.keyboards_or_buttons.models import (Menu, Register
                                                 )


@dataclass
class Keyboards:
    menu: Markup = Markup(Menu())
    register: Markup = Markup(Register())


keyboards = Keyboards()
