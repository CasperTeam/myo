from .commands import DATA
import requests ,lxml, json 
from bs4 import BeautifulSoup 
from datetime import datetime, timedelta 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from time import sleep




@Client.on_message(filters.command(["start", "start@cla12bot"]))
async def start(bot, message):
        if (" " in message.text):
                msf = await message.reply_text("**Processing.. This may take a while..**")
                file = message.text.split(" ")[1]
                cipeas1 = "https://vid.ourclg.tech/0:/NOTES/CHEMISTRY/PHYSICAL/Atomic%20Structure/Atomic%20structure%20Handwritten%20notes%20.pdf"
                cipeas2 = "https://vid.ourclg.tech/0:/NOTES/CHEMISTRY/PHYSICAL/Atomic%20Structure/Atomic%20Structure.pdf"
                cipece = "https://vid.ourclg.tech/0:/NOTES/CHEMISTRY/PHYSICAL/Chemical%20Equlibrium/Chemical%20Equilibrium.pdf"
                cipeck1 = "https://vid.ourclg.tech/0:/NOTES/CHEMISTRY/PHYSICAL/Chemical%20Kinetics/SASIDHAR%20SERIES/Chemical%20Kinetics.pdf"
                cipeck2 = "https://vid.ourclg.tech/0:/NOTES/CHEMISTRY/PHYSICAL/Chemical%20Kinetics/RAVALI%20MAM/Chemical%20kinetics%20notes.pdf"
                cipesom1 = "https://vid.ourclg.tech/0:/NOTES/CHEMISTRY/PHYSICAL/States%20of%20Matter/Real%20Gases.pdf"
                cipesom2 = "https://vid.ourclg.tech/0:/NOTES/CHEMISTRY/PHYSICAL/States%20of%20Matter/States%20Of%20Matter.pdf"
                cipestcm = "https://vid.ourclg.tech/0:/NOTES/CHEMISTRY/PHYSICAL/Stoichiometry/Stoichiometry.pdf"
                cipetc = "https://vid.ourclg.tech/0:/NOTES/CHEMISTRY/PHYSICAL/Thermochemistry/Thermochemistry.pdf"
                cipetd = "https://vid.ourclg.tech/0:/NOTES/CHEMISTRY/PHYSICAL/Thermodynamics/Thermodynamics.pdf"


                if file == "cipeas1":
                    await message.reply_document(cipeas1)
                elif file == "cipeas2":
                    await message.reply_document(cipeas2)
                elif file == "cipece":
                    await message.reply_document(cipece)
                elif file == "cipeck1":
                    await message.reply_document(cipeck1)
                elif file == "cipeck2":
                    await message.reply_document(cipeck2)
                elif file == "cipesom1":
                    await message.reply_document(cipesom1)
                elif file == "cipesom2":
                    await message.reply_document(cipesom2)
                elif file == "cipestcm":
                    await message.reply_document(cipestcm)
                elif file == "cipetc":
                    await message.reply_document(cipetc)
                elif file == "cipetd":
                    await message.reply_document(cipetd)       
                await message.delete()
                sleep(2)
                await message.reply_text("successfully Sent!")
                sleep(1)
                await msf.delete()
        else:
            c = "plugins/k.jpg"
            await bot.send_photo(
            message.chat.id,
            c,
            reply_markup=DATA
        )

