from pyrogram import Client, filters
@Client.on_message(filters.command("h"))
async def h(bot, message):
    await bot.send_message(
        message.chat.id,
        "/start /data /we /rn /py /go /image /dl"
    )