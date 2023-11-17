from dataclasses import dataclass, asdict
from aiogram.utils.keyboard import (ReplyKeyboardBuilder, InlineKeyboardBuilder, KeyboardButton, InlineKeyboardButton,
                                    ReplyKeyboardMarkup, InlineKeyboardMarkup)


@dataclass
class Markup:
    def __init__(self, keyboard, adjust: int = 2, resize_keyboard: bool = True):
        keyboard_dict = asdict(keyboard)
        print(keyboard_dict)
        self.__keyboard_dict = keyboard_dict
        self.__adjust = adjust
        self.__resize_keyboard = resize_keyboard
        self.__make_default_keyboard()
        self.__make_inline_keyboard()

    inline: InlineKeyboardMarkup = NotImplemented
    default: ReplyKeyboardMarkup = NotImplemented
    __keyboard_dict: dict = NotImplemented
    __adjust: int = NotImplemented
    __resize_keyboard: bool = NotImplemented

    def __make_default_keyboard(self):
        builder = ReplyKeyboardBuilder()
        for key, value in self.__keyboard_dict.items():
            builder.add(KeyboardButton(text=value))
        builder.adjust(self.__adjust)
        self.default = builder.as_markup(resize_keyboard=self.__resize_keyboard)

    def __make_inline_keyboard(self):
        builder = InlineKeyboardBuilder()
        for key, value in self.__keyboard_dict.items():
            builder.add(InlineKeyboardButton(text=value, callback_data=value))
        builder.adjust(self.__adjust)
        self.inline = builder.as_markup(resize_keyboard=self.__resize_keyboard)

