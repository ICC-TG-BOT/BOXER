from pyrogram import Client, filters

import requests

import random

import os

import re

import asyncio

import time

from AnonX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(

    filters.command("owner")

    & filters.group

    & ~filters.edited & filters.group & ~filters.edited)

async def help(client: Client, message: Message):

    await message.reply_photo(

        photo=f"https://te.legra.ph/file/9c348b01c603f3591ad3d.jpg",

        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "🌹 𝐎𝐖𝐍𝐄𝐑 🌹", url=f"https://t.me/ToXiC_BoY_OFFICIAL")

                ]

            ]

        ),

    )

@app.on_message(

    filters.command("owner")

    & filters.private

    & ~filters.edited & filters.private & ~filters.edited)

async def help(client: Client, message: Message):

    await message.reply_photo(

        photo=f"https://te.legra.ph/file/9c348b01c603f3591ad3d.jpg",

        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "🌹 𝄟⃝🥀⃟🇹‌𝐎𝐗𝐈𝐂⍣⃝🇧𝐎𝐘⃝🍁 🌹", url=f"https://t.me/ToXiC_BoY_OFFICIAL")

                ]

            ]

        ),

    )

@app.on_message(

    filters.command("pari")

    & filters.group

    & ~filters.edited & filters.group & ~filters.edited)

async def help(client: Client, message: Message):

    await message.reply_photo(

        photo=f"https://te.legra.ph/file/cf6d2f4537d44d4e8b13c.jpg",

        caption=f"""🦋•────────────────•🦋 \n          🇸𝗧𝗨𝗗𝗬  𝙉𝘿 𝘾𝙍𝙔😭

🦋•────────────────•🦋

┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

𝐌𝗢𝐇𝗔𝐁𝗕𝐀𝗧 𝐇𝗢 𝐆𝗔𝐘𝗜 𝐓𝗛𝐈 𝐃𝗢𝐍𝗢 𝐊𝗢[ Sᴛᴜᴅʏ ɴᴅ ᴍᴇ ] 𝐄𝗞 𝐀𝗥S𝗔 𝐇𝗢 𝐆𝗬𝐀

👉👈 𝐌𝗘𝐑𝗔 𝐘𝗘 𝐈𝗦𝐇𝗤 𝐓𝗛𝐀 𝐃𝗢 𝐓𝗔𝐑𝗙𝐀 𝐄𝗞 𝐓𝗔𝐑𝗙𝐀 𝐇𝗢 𝐆𝗔𝐘𝗔❤️😭🦋😂

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "pari", url=f"https://t.me/ofy_cutie")

                ]

            ]

        ),

    )

@app.on_message(

    filters.command("govind")

    & filters.group

    & ~filters.edited & filters.group & ~filters.edited)

async def help(client: Client, message: Message):

    await message.reply_photo(

        photo=f"https://te.legra.ph/file/ca4bfdbaae44764c05792.jpg",

        caption=f"""🦋•────────────────•🦋 \n          🇸𝗧𝗨𝗗𝗬  𝙉𝘿 𝘾𝙍𝙔😭

🦋•────────────────•🦋

┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

𝐌𝗢𝐇𝗔𝐁𝗕𝐀𝗧 𝐇𝗢 𝐆𝗔𝐘𝗜 𝐓𝗛𝐈 𝐃𝗢𝐍𝗢 𝐊𝗢[ Sᴛᴜᴅʏ ɴᴅ ᴍᴇ ] 𝐄𝗞 𝐀𝗥S𝗔 𝐇𝗢 𝐆𝗬𝐀

👉👈 𝐌𝗘𝐑𝗔 𝐘𝗘 𝐈𝗦𝐇𝗤 𝐓𝗛𝐀 𝐃𝗢 𝐓𝗔𝐑𝗙𝐀 𝐄𝗞 𝐓𝗔𝐑𝗙𝐀 𝐇𝗢 𝐆𝗔𝐘𝗔❤️😭🦋😂

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "sumit", url=f"https://t.me/GOVIND_OFFICIAL_MP42")

                ]

            ]

        ),

    )

@app.on_message(

    filters.command("repo")

    & filters.group

    & ~filters.edited & filters.group & ~filters.edited)

async def help(client: Client, message: Message):

    await message.reply_photo(

        photo=f"https://te.legra.ph/file/df3246d81ef013346d280.jpg",

        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/GOVIND-BOTS/haramibot")

                ]

            ]

        ),

    )

@app.on_message(

    filters.command("repo")

    & filters.group

    & ~filters.edited & filters.group & ~filters.edited)

async def help(client: Client, message: Message):

    await message.reply_photo(

        photo=f"https://https://te.legra.ph/file/df3246d81ef013346d280.jpg",

        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "🌱ƨσʋяcɛ🌱", url=f"https://telegra.ph//file/2af6eb42ca2a28828e37a.mp4")

                ]

            ]

        ),

    )

@app.on_message(

    filters.command("toxicgirl")

    & filters.private

    & ~filters.edited & filters.private & ~filters.edited)

async def help(client: Client, message: Message):

    await message.reply_photo(

        photo=f"https://te.legra.ph/file/6d905f9e58b3ab15216f1.jpg",

        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎💖𝐎𝐖𝐍𝐄𝐑🥰𝐒𝐈𝐒𝐓𝐄𝐑🍁""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "💖 𝄟⃝🥀⃟🇹‌𝐎𝐗𝐈𝐂⍣⃝🇬‌𝐈𝐑𝐋⃝🍁 💖", url=f"https://t.me/ToXiC_GiRl_OFFICIAL")

                ]

            ]

        ),

    )
