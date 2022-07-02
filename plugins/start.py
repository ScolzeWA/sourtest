from modules.config import (
    START_PIC, 
    BOT_USERNAME,
    SUPPORT_GROUP,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
)
from modules.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
 await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**━━━━━━━━━━━━
اهـلا يـبـنـي.؟ {message.from_user.mention()} !
مـرحبآ بـك انــا بــوت اقـوم بــتـشـغـيـل الاغــانــي فـي الـمـڪـالـمـه الـصـوتـية .🤔❤؟
يمكنني التشغيل بصوت رائع وبدون اي مشاكل او تقطيع في الاغنيه
 +اضفني الى مجموعتك وارفعني رول بشڪل مع ڪامل الصلاحيات
 البوت يشتغل بالاوامر عربي وانجليزي
 لانضمام الحساب المساعد لتشغيل البوت اكتب انضم


  لمعرفة استخدامي بشڪل صحيح اضغط علي زر الاوامر. 🤔𝑫𝑬𝑽 [𝑾𝑶𝑹𝑳𝑫 𝑴𝑼𝑺𝑰𝑪 💗ˣ](t.me/WORLD_MUSIC_F)
━━━━━━━━━━━━━━━━━━**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎯 ¦ اضـفـني الى مـجمـوعـتك ¦ 🎯",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("🥇 ¦ المـــطور", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("🖥 ¦ الأوامــر", url=f"https://telegra.ph/%D8%A7%D9%87%D9%84%D8%A7-%D8%A8%D9%83-%D8%AC%D9%85%D9%8A%D8%B9-%D8%A7%D9%84%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%B9%D8%B1%D8%A8%D9%8A%D9%87-%D9%8A%D9%85%D9%83%D9%86%D9%83-%D8%AA%D8%B4%D8%BA%D9%8A%D9%84-%D9%81%D9%8A-%D8%A7%D9%84%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%A7%D9%84%D8%A7%D8%AC%D9%86%D8%A8%D9%8A%D9%87-%D8%A7%D9%8A%D8%B6%D8%A2-%D9%88%D8%B4%D9%83%D8%B1%D8%A7-%D9%84%D9%83%D9%85-07-01"),
                ],
                [
                    InlineKeyboardButton(
                        "🥇 ¦ الــجــروب", url=f"{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "⚙️ ¦ الـسـورس", url=f"{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
    )


@Client.on_message(command(["source"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg",
        caption=f"""ᴘʀᴏɢʀᴀᴍᴍᴇʀ [𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 ☤ ](https://t.me/WORLD_MUSIC_F) 𖡼\nᴛᴏ ᴄᴏᴍᴍụɴɪᴄᴀᴛᴇ ᴛᴏɢᴇᴛʜᴇʀ 𖡼\nғᴏʟʟᴏᴡ ᴛʜᴇ ʙụᴛᴛᴏɴѕ ʟᴏᴡᴇʀ 𖡼""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("♡اضف البوت الى مجموعتك♡", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["developer","dev"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg",
        caption=f"""◍ مش محتاجين نكتب كلام كتير خش ع اول زرار وانت هتعرف""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("• 𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 ☤ ", url=f"https://t.me/WORLD_MUSIC_F"),
            ],
            [
                InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )
