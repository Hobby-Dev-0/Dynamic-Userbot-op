# MADE BY SIDDHARTH  
# NEW VERSION UPDATED BY SRIDHAR
# COPYRIGHT TO TEAM TANDAV X 2021-2022 SHOULD NOT FOUND ANYWHERE ELSE YOU WILL GET GBAN AND WE WILL COPYRIGHT YOUR REPO
import asyncio
import random
from telethon import events
from . import admin_cmd
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/08ab534ee3ed230c45f78.jpg"
file2 = "https://telegra.ph/file/08ab534ee3ed230c45f78.jpg"
file3 = "https://telegra.ph/file/08ab534ee3ed230c45f78.jpg"
file4 = "https://telegra.ph/file/08ab534ee3ed230c45f78.jpg"
file5 = "https://telegra.ph/file/08ab534ee3ed230c45f78.jpg"
file6 = "https://telegra.ph/file/08ab534ee3ed230c45f78.jpg"
file7 = "https://telegra.ph/file/08ab534ee3ed230c45f78.jpg"
pm_caption = "🔥🔥 **TANDAV X IS WORKING FINE LIKE MY OWNER..!! **🔥🔥\n\n"
pm_caption += "⚔️⚔️ ** REAL OWNER AND BOT CODER TEAM TANDAV**⚔️⚔️\n\n"
pm_caption += "◆◆S𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂◆◆◆\n\n"
pm_caption += "●●𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ●● : 1.21.1\n\n"
pm_caption += "●●  TANDAV VERSION ●●>> :1.0 Stable \n\n"
pm_caption += " PYTHON VERSION : 3.9.2 \n\n"
pm_caption += " DISK USAGE : 500 GB/1.5 TB \n\n"
pm_caption += " TANDAV SOFTWARE : STABLE VERSION \n\n"
pm_caption += "EVERTHING IS FINE \n\n"
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
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
