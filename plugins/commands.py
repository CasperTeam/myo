
import requests ,lxml, json 
from bs4 import BeautifulSoup 
from datetime import datetime, timedelta 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from time import sleep
DATA = InlineKeyboardMarkup(
        [[InlineKeyboardButton('Jee', callback_data='jee')],
        [InlineKeyboardButton('APEMCEAT', callback_data='emceat')],
        [InlineKeyboardButton('IPE', callback_data='ipe')],
        [InlineKeyboardButton('Delete', callback_data='del')]],
    )
NEW = InlineKeyboardMarkup(
    [InlineKeyboardButton("Happy new year!", callback_data="h")]
)
@Client.on_message(filters.command(["data", "data@cla12bot"]))
async def data(bot, message):
    await bot.send_message(
        message.chat.id,
        "**No Data As of Now Ill improve it Soon**",
        reply_markup=DATA
    )
    

@Client.on_message(filters.command(["we", "weather", "we@cla12bot", "weather@cla12bot"]))
async def we(bot, message):
#!eval 

    presentday = datetime.now() # presentday = datetime.today() 
#Tomorrow 
    tomorrow = presentday + timedelta(1) 
    today = (presentday.strftime('%d-%m-%Y')) 
    tplus1 = (tomorrow.strftime('%d-%m-%Y')) 
 
#print("Tomorrow = ", tplus1) 
    source = requests.get("https://weather.com/en-IN/weather/today/l/b3ec8bf1b225c8b1032b944faa45df972b38024857e9205ef5a338d1a18701cc").text 
    soup = BeautifulSoup(source, "lxml") 
    a = soup.find("h1") 
    village = a.get_text() 
 
    temp = soup.find('span', {'class': 'CurrentConditions--tempValue--3a50n'}).text#soup.find_all("span") 
    tim = soup.find('div', {'class': 'CurrentConditions--timestamp--23dfw'}).text 
    stat = soup.find('div', {'class': 'CurrentConditions--phraseValue--2Z18W'}).text 
    stat1 = soup.find_all('span')[30] 
    st2 = stat1.get_text()
    mmtemp = soup.find('div', {'class': 'CurrentConditions--tempHiLoValue--3SUHy'}).text
    fl = soup.find('span', {'class': 'TodayDetailsCard--feelsLikeTempValue--Cf9Sl'}).text
    lel = """
**Date** = ``{}``
**Time** = ``{}``
**Area** =  ``{}``
**Min/Max Temp** = ``{}``
**Current temparature** = ``{}``
**Feels Lke** = ``{}``
**Status** =  ``{}`` **and** ``{}``
"""
    s = lel.format(today,tim,village,mmtemp,temp,fl,st2,stat)
    await bot.send_message(message.chat.id, s,parse_mode="md")
