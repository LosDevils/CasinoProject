from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from src.services.user import UserService
from sqlalchemy.exc import NoResultFound
from src.api.keyboards_or_buttons.keyboards import keyboards
from src.api.keyboards_or_buttons.buttons import buttons

router = Router()


@router.message(Command("test"))
async def start(message: Message):
    await message.answer("TESTING", reply_markup=keyboards.menu.default)


@router.message(Command("start"))
async def start(message: Message):
    try:
        await UserService().get_user(user_id=message.from_user.id)
        await message.answer("C возвращением!", reply_markup=keyboards.menu.default)
    except NoResultFound:
        await message.answer("ПРАВИЛА", reply_markup=keyboards.register.inline)


@router.callback_query(F.data == buttons.register.accept)
async def accept_register(callback: CallbackQuery):
    await UserService().add_user_by_id(user_id=callback.from_user.id)
    await callback.message.answer("Добро пожаловать и тд и тп", reply_markup=keyboards.menu.default)
    await callback.message.delete_reply_markup()
