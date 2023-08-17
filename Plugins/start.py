from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardRemove, InlineKeyboardMarkup, CallbackQuery


# /start command
@Client.on_message(filters.command("start"))
def start(client: Client, message: Message):
    message.reply_text("welcome to s music bot, you should join to my channel to continue;)",
                       reply_markup=InlineKeyboardMarkup(
                           [
                               [InlineKeyboardButton(text='me doing drugs', callback_data="button1")],
                               [InlineKeyboardButton(text="در کانال عضو شو",url="https://t.me/+NsTmMQFXzFFiNmQ8")]
                           ]
                       ))


@Client.on_callback_query()
def on_callblck(c: Client, callback: CallbackQuery):
    if callback.data == "button1":
        callback.message.reply_photo("https://t.me/Specialmusic58/649")

