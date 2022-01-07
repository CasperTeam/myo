import asyncio
import logging
import math
import os
import shlex
import time
from math import ceil
from traceback import format_exc
from typing import Tuple

from pyrogram import Client
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)


import mimetypes
def get_readable_time(seconds: int) -> int:
    """Get Time So That Human Can ReadIt"""
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
    

def humanbytes(size):
    """Convert Bytes To Bytes So That Human Can Read It"""
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"

def run_in_exc(f):
    @functools.wraps(f)
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(exc_, lambda: f(*args, **kwargs))
    return wrapper


def time_formatter(milliseconds: int) -> str:
    """Time Formatter"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]



async def progress(current, total, message, start, type_of_ps, file_name=None):
    """Progress Bar For Showing Progress While Uploading / Downloading File - Normal"""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join(["●" for i in range(math.floor(percentage / 10))]), 
            "".join(["○" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(
                    "{}\n**File Name:** `{}`\n{}".format(type_of_ps, file_name, tmp)
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit("{}\n{}".format(type_of_ps, tmp))
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

import os
import time
import logging
from pyrogram import Client, filters
@Client.on_message(filters.command(["dl"]))
async def download(bot, message):
    s_time = time.time()
    await message.reply_text("Downloading to Server..")
    if not message.reply_to_message:
        await message.edit("`Reply to a message to download!")
        return
    if not message.reply_to_message.media:
        await message.edit("`Reply to a message to download!`")
        return
    c_time = time.time()
    Escobar = await message.reply_to_message.download(
        progress=progress, progress_args=(c_time, f"`Downloading This File!`")
    )
    e_time = time.time()
    dl_time = round(s_time - e_time)
    file_txt = "__Downloaded This File To__ `{}` __in__ `{}`."

    await message.edit(file_txt.format(Escobar, dl_time))