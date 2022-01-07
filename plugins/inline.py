import asyncio
from pyrogram.handlers import InlineQueryHandler
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, errors
from .commands import DATA
buttons = DATA

@Client.on_inline_query()
async def search(client, query):
    answers = []
    if query.query == "":
        answers.append(
            InlineQueryResultArticle(
                title="list",
                input_message_content=InputTextMessageContent("list"),
                reply_markup=InlineKeyboardMarkup(buttons)
                )
            )
        await query.answer(results=answers, cache_time=0)