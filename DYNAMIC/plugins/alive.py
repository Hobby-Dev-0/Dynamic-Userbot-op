import asyncio
import random
from telethon import events
from DYNAMIC.utils import admin_cmd
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/7486dce0f715ccc0576b6.jpg"
file2 = "https://telegra.ph/file/cc44dbb6c06fae646da13.jpg"
file3 = "https://telegra.ph/file/4189164cadd30a8a2d6da.jpg"
file4 = "https://telegra.ph/file/1b6d7ec6c2382fb80a094.jpg"
file5 = "https://telegra.ph/file/d57626f8b84037d156d88.jpg"
file6 = "https://telegra.ph/file/5c0bd9eacf8789ab4f4c3.jpg"
file7 = "https://telegra.ph/file/33727f0de96eb4affc714.jpg"
pm_caption = "🔥🔥 **DYNAMIC IS WORKING FINE LIKE MY OWNER..!! **🔥🔥\n\n"
pm_caption += "⚔️⚔️ ** REAL OWNER AND BOT CODER TEAM DYNAMIC**⚔️⚔️\n\n"
pm_caption += "◆◆S𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂◆◆◆\n\n"
pm_caption += "●●𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ●● : 1.19.5\n"
pm_caption += "f●●  DYNAMIC VERSION ●●>> : 0.1\n"
pm_caption += "●●DYNAMIC OP ●● : OP\n"
pm_caption += "●●【S】【U】【P】【P】【O】【R】【T】∆【G】【R】【O】【U】【P】●● : [GROUP](https://t.me/DYNAMIC_USERBOT\n)"
pm_caption += "●●【F】【O】【R】 【U】【P】【D】【A】【T】【E】【S】●● : [CHANNEL](https://t.me/DYNAMICXOP\n)"
@borg.on(admin_cmd(pattern=r"alive"))

async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file5)
    
    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file6)
    
    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file7)

    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
