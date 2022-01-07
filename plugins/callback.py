import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import time
import wget
import requests ,lxml, json 
from bs4 import BeautifulSoup 
 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_callback_query()
async def cb_handler(client,query):
    data = query.data
    if data == "ipe":
        await query.message.edit_text(
            text = f"select one",

            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("class11", callback_data = "ipe1"),InlineKeyboardButton("class12", callback_data = "ipe2")
                    ],
                    [
                        InlineKeyboardButton("Back", callback_data = "ipeback1")
                    ]
                ]
            )
        )
    elif data == "ipeback1":
        await query.message.edit_text(
            text=f"**No Data As of Now Ill improve it Soon**",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('Jee', callback_data='jee')],
            [InlineKeyboardButton('APEMCEAT', callback_data='emceat')],
            [InlineKeyboardButton('IPE', callback_data='ipe')],
            [InlineKeyboardButton('Delete', callback_data='del')]],
        )
    )
    elif data == "ipe1back2":
        await query.message.edit_text(
            text = f"select one",

            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("class11", callback_data = "ipe1"),InlineKeyboardButton("class12", callback_data = "ipe2")
                    ],
                    [
                        InlineKeyboardButton("Back", callback_data = "ipeback1")
                    ]
                ]
            )
        )
    elif data == "ipe1":
        await query.message.edit_text(
            text=f"**select subject**",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('Maths', callback_data='ipe1mat')],
            [InlineKeyboardButton('Physics', callback_data='ipe1phy')],
            [InlineKeyboardButton('Chemestry', callback_data='ipe1che')],
            [InlineKeyboardButton('Back', callback_data='ipe1back2')]],
        )
    )
    elif data == "ipe1mat":
        await query.message.edit_text(
            text=f"**select one**",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('Back', callback_data='ipe1')]],
        )
    )
    elif data == "ipe1phy":
        await query.message.edit_text(
            text=f"**select one**",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('Back', callback_data='ipe1')]],
        )
    )
    elif data == "ipe1che":
        await query.message.edit_text(
            text=f"**select one**",
            reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('Atomic Structure', callback_data='cipeas')],
                #[InlineKeyboardButton('Chemichal bonding', callback_data='cipechb')],
                #[InlineKeyboardButton('Periodic Classification', callback_data='cipepc')],
                #[InlineKeyboardButton('Hydrogen and its compounds', callback_data='cipehac')],
                #[InlineKeyboardButton('1A 2A elements', callback_data='cipeiaiia')],
                #[InlineKeyboardButton('13grp', callback_data='cipe13grp')],
                #[InlineKeyboardButton('14grp', callback_data='cipe24grp')],
                [InlineKeyboardButton('Chemichal Equilibrium', callback_data='cipece')],
                [InlineKeyboardButton('chemichal Kinetics', callback_data='cipeck')],
                [InlineKeyboardButton('states of matter', callback_data='cipesom')],
                [InlineKeyboardButton('staichometry', callback_data='cipestcm')],
                [InlineKeyboardButton('thermo chemistry', callback_data='cipetc')],
                [InlineKeyboardButton('thermodynamics', callback_data='cipetd')],
                #[InlineKeyboardButton('Organic', callback_data='cipeoc')],
                [InlineKeyboardButton('Back', callback_data='ipe1')]
                ],
        )
    )
    elif data == "cipeas":
        await query.message.edit_text(
            text = f"Notes",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('Atomic Structure Hand written download', url='t.me/cla12bot?start=cipeas1')],
            [InlineKeyboardButton('Atomic Structure download', url='t.me/cla12bot?start=cipeas2')],
            [InlineKeyboardButton('Back', callback_data='ipe1che')],]
        ))
    elif data == "cipece":
        await query.message.edit_text(
            text = f"Notes",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('Chemichal Equilibrium download', url='t.me/cla12bot?start=cipece')],
            [InlineKeyboardButton('Back', callback_data='ipe1che')],]
        ))
    elif data == "cipeck":
        await query.message.edit_text(
            text = f"Notes",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('chemichal Kinetics1', url='t.me/cla12bot?start=cipeck1')],
            [InlineKeyboardButton('chemichal Kinetics2', url='t.me/cla12bot?start=cipeck2')],
            [InlineKeyboardButton('Back', callback_data='ipe1che')],]
        ))
    elif data == "cipesom":
        await query.message.edit_text(
            text = f"Notes",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('Real gases download', url='t.me/cla12bot?start=cipesom1')],
            [InlineKeyboardButton('Som', url='t.me/cla12bot?start=cipesom2')],
            [InlineKeyboardButton('Back', callback_data='ipe1che')],]
        ))
    elif data == "cipestcm":
        await query.message.edit_text(
            text = f"Notes",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('staichometry download', url='t.me/cla12bot?start=cipestcm')],
            [InlineKeyboardButton('Back', callback_data='ipe1che')],]
        ))
    elif data == "cipetc":
        await query.message.edit_text(
            text = f"Notes",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('thermo chemistry download', url='t.me/cla12bot?start=cipetc')],
            [InlineKeyboardButton('Back', callback_data='ipe1che')],]
        ))
    elif data == "cipetd":
        await query.message.edit_text(
            text = f"Notes",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('thermodynamics download', url='t.me/cla12bot?start=cipetd')],
            [InlineKeyboardButton('Back', callback_data='ipe1che')],]
        ))
    
    elif data == "ipeback":
        await query.message.edit_text(
            text=f"**No Data As of Now Ill improve it Soon**",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('Jee', callback_data='jee')],
            [InlineKeyboardButton('APEMCEAT', callback_data='emceat')],
            [InlineKeyboardButton('IPE', callback_data='ipe')],
            [InlineKeyboardButton('Delete', callback_data='del')]],
        )
    )
    elif data == "ipe2back2":
        await query.message.edit_text(
            text = f"select one",

            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("class11", callback_data = "ipe1"),InlineKeyboardButton("class12", callback_data = "ipe2")
                    ],
                    [
                        InlineKeyboardButton("Back", callback_data = "ipeback1")
                    ]
                ]
            )
        )
    elif data == "ipe2":
        await query.message.edit_text(
            text=f"**select subject**",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('Maths', callback_data='ipe2mat')],
            [InlineKeyboardButton('Physics', callback_data='ipe2phy')],
            [InlineKeyboardButton('Chemestry', callback_data='ipe2che')],
            [InlineKeyboardButton('Back', callback_data='ipe2back2')]],
        )
    )
    elif data == "ipe2mat":
        await query.message.edit_text(
            text=f"**select one**",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('Back', callback_data='ipe2')]],
        )
    )
    elif data == "ipe2phy":
        await query.message.edit_text(
            text=f"**select one**",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('Back', callback_data='ipe2')]],
        )
    )
    elif data == "ipe2che":
        await query.message.edit_text(
            text=f"**select one**",
            reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('1', callback_data='1')],
            [InlineKeyboardButton('Back', callback_data='ipe2')]],
        )
    )





    elif data == "jee":
        text = ("Check ipe")
        await query.answer(text, show_alert=True)
    elif data == "1":
        text = ("Error: Under devlopment or server busy")
        await query.answer(text, show_alert=True)
    elif data == "emceat":
        text = ("check ipe")
        await query.answer(text, show_alert=True)
    elif data == "del":
        firstname = query.from_user.first_name
        id = query.from_user.id
        k = ("deleted by {} {}").format(firstname,id)
        await query.message.edit_text(k)
        time.sleep(3)
        await query.message.delete()