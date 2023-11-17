from aiogram import Router, F
from aiogram.types import Message
from src.api.keyboards_or_buttons.buttons import buttons

router = Router()


@router.message(F.text == buttons.menu.profile)
async def profile(message: Message):
    pass
