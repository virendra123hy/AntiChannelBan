from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command(["start", "start@ChannelBanRobot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ðï¸!</b>
 `Heya I'm A Anti Channel Tegram bot to delete and ban message sent by channel`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¢ CÊá´É´É´á´Ê", url="https://t.me/DeeCodeBots"
                    ),
                    InlineKeyboardButton(
                        "Sá´á´á´á´Êá´ ð¥", url="https://t.me/DeCodeSupport"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð§âð» Dá´á´  ð§âð»", url="https://t.me/DeeCodeDevs"
                    )
                ]
            ]
        )
    )
