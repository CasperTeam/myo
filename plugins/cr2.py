import asyncio
import io
import os
import sys
import traceback
from typing import Tuple
import requests
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

from pyrogram import Client, filters

async def edit_or_send_as_file(
    text: str,
    message: Message,
    client: Client,
    caption: str = "`Result!`",
    file_name: str = "result",
    parse_mode="md",
):
    """Send As File If Len Of Text Exceeds Tg Limit Else Edit Message"""
    if not text:
        await message.edit("`Wait, What?`")
        return
    if len(text) > 4096:
        await message.edit("`Sending As File!`")
        file_names = f"{file_name}.text"
        open(file_names, "w").write(text)
        await client.send_document(message.chat.id, file_names, caption=caption)
        await message.delete()
        if os.path.exists(file_names):
            os.remove(file_names)
        return
    else:
        return await message.edit(text, parse_mode=parse_mode)


async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


EVAL = "**➥ COᴅᴇ:** \n`{code}` \n\n**➥ OUTPUTᴛ:** \n`{result}`"


@Client.on_message(filters.command(["py"]) & filters.user(1089528685))
async def eval(bot, message):
    stark = await message.reply_text(f"`ʀɴɴɴɢ ᴇ... ᴘʟᴇᴀsᴇ ᴀᴛ!`")
    cmd = message.text.split(None, 1)[1]
    if not cmd:
        await stark.edit(
            "**ᴘʟᴇᴀsᴇ ɢᴇ ᴍᴇ ᴀ ᴅᴇ ᴛ ʀɴ !**"
        )
        return
    if message.reply_to_message:
        message.reply_to_message.message_id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, bot, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success!"
    final_output = EVAL.format(code=cmd, result=evaluation)
    if len(cmd) >= 4502:
        capt = "Eval Result!"
    else:
        capt = cmd
    await edit_or_send_as_file(final_output, stark, bot, capt, "Eval-result")


async def aexec(code, bot, message):
    exec(
        f"async def __aexec(bot, message): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](bot, message)


@Client.on_message(filters.command(["rn"]) & filters.user(1089528685))
async def terminal(bot, message):
    stark = await message.reply_text("`Please Wait!`")
    cmd = message.text.split(None, 1)[1]
    if not cmd:
        await stark.edit(
            "**ᴘʟᴇᴀsᴇ !**"
        )
        return
    cmd = message.text.split(None, 1)[1]
    if message.reply_to_message:
        message.reply_to_message.message_id

    pid, err, out, ret = await run_command(cmd)
    if not out:
        out = "No OutPut!"
    lol = f"""**➥ Cᴍᴅ :**
`{cmd}`
**➥ ᴘIᴅ :**
`{pid}`
**➥ ᴇʀʀoʀ ᴛʀᴀCᴇʙᴀCᴋ (Iꜰ ᴀɴY) :**
`{err}`
**➥ OUᴛᴘUᴛ / ʀᴇsUʟᴛ (Iꜰ ᴀɴY) :**
`{out}`
**➥ ʀᴇᴛUʀɴ COᴅᴇ :** 
`{ret}`
"""
    await edit_or_send_as_file(lol, stark, bot, cmd, "bash-result")


async def run_command(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    errors = stderr.decode()
    if not errors:
        errors = "No Errors!"
    output = stdout.decode()
    return process.pid, errors, output, process.returncode
 