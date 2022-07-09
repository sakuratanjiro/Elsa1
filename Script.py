class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 ❣️

𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 𝙰𝚂𝚆𝙸𝙽"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.

𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 𝙰𝚂𝚆𝙸𝙽"""
    ABOUT_TXT = """╭•━━━━━━━━━━━━━━━➣ 
║┣⪼❈ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
║┣⪼❈ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/moviesclubowne>kristyan</a>
║┣⪼❈ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
║┣⪼❈ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
║┣⪼❈ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
║┣⪼❈ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙾𝙺𝚃𝙴𝚃𝙾
║┣⪼❈ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v2.0.1[𝙱𝙴𝚃𝙰]
╰•━━━━━━━━━━━━━━━➣
 
 𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 kristyan"""
    SOURCE_TXT = """<b>NOTE:</b>
✯ 𝙲𝙸𝙽𝙴𝙼𝙰𝙻𝙰.𝙲𝙾𝙼 𝚋𝚘𝚝 𝚒𝚜 𝚊 𝚘𝚙𝚎𝚗 𝚜𝚘𝚞𝚛𝚌𝚎 𝚙𝚛𝚘𝚓𝚎𝚌𝚝. 𝚁𝚎𝚙𝚘 𝙲𝚛𝚎𝚍𝚒𝚝 𝙴𝚟𝚊 𝚖𝚊𝚛𝚒𝚊.

✯ 𝚂𝚘𝚞𝚛𝚌𝚎 - <a href=https://github.com/EvamariaTG/EvaMaria>𝚁𝙴𝙿𝙾</a>

<b>★𝐃𝐄𝐕𝐒★</b>

✯ <a href=https://t.me/moviesclubowne>kristyan</a>

 𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 Kristyan"""
 
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚆𝙴𝚁𝙴 𝚄𝚂𝙴𝚁𝚂 𝙲𝙰𝙽 𝚂𝙴𝚃 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙴𝙳 𝚁𝙴𝙿𝙻𝙸𝙴𝚂 𝙵𝙾𝚁 𝙰 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻𝙰𝚁 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙰𝙽𝙳 𝙲𝙸𝙽𝙴𝙼𝙰𝙻𝙰.𝙲𝙾𝙼 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝚂𝙿𝙾𝙽𝙳 𝚆𝙷𝙴𝙽𝙴𝚅𝙴𝚁 𝙰 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙸𝚂 𝙵𝙾𝚄𝙽𝙳 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴
<b>NOTE:</b>
1. 𝙲𝙸𝙽𝙴𝙼𝙰𝙻𝙰 .𝙲𝙾𝙼 𝙱𝙾𝚃 𝚂𝙷𝙾𝚄𝙻𝙳 𝙷𝙰𝚅𝙴 𝙰𝙳𝙼𝙸𝙽 𝙿𝚁𝙸𝚅𝙸𝙻𝙻𝙰𝙶𝙴. 
2. 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃.
3. 𝙰𝙻𝙴𝚁𝚃 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝙷𝙰𝚅𝙴 𝙰 𝙻𝙸𝙼𝙸𝚃 𝙾𝙵 64 𝙲𝙷𝙰𝚁𝙰𝙲𝚃𝙴𝚁𝚂.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>
 
 𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 𝙰𝚂𝚆𝙸𝙽"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-  𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙱𝙾𝚃𝙷 𝚄𝚁𝙻 𝙰𝙽𝙳 𝙰𝙻𝙴𝚁𝚃 𝙸𝙽𝙻𝙸𝙽𝙴 𝙱𝚄𝚃𝚃𝙾𝙽𝚂.

<b>NOTE:</b>
1. 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙰𝙻𝙻𝙾𝚆𝚂 𝚈𝙾𝚄 𝚃𝙾 𝚂𝙴𝙽𝙳 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙰𝙽𝚈 𝙲𝙾𝙽𝚃𝙴𝙽𝚃, 𝚂𝙾 𝙲𝙾𝙽𝚃𝙴𝙽𝚃 𝙸𝚂 𝙼𝙰𝙽𝙳𝙰𝚃𝙾𝚁𝚈. 
2. 𝙲𝙸𝙽𝙴𝙼𝙰𝙻𝙰 .𝙲𝙾𝙼 𝙱𝙾𝚃 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷 𝙰𝙽𝚈 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙼𝙴𝙳𝙸𝙰 𝚃𝚈𝙿𝙴. 
3. 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚂𝙷𝙾𝚄𝙻𝙳 𝙱𝙴 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈 𝙿𝙰𝚁𝚂𝙴𝙳 𝙰𝚂 𝙼𝙰𝚁𝙺𝙳𝙾𝚆𝙽 𝙵𝙾𝚁𝙼𝙰𝚃

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/ccomautofilter_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>

 𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 𝙰𝚂𝚆𝙸𝙽"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. 𝙼𝙰𝙺𝙴 𝙼𝙴 𝚃𝙷𝙴 𝙰𝙳𝙼𝙸𝙽 𝙾𝙵 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙸𝙵 𝙸𝚃'𝚂 𝙿𝚁𝙸𝚅𝙰𝚃𝙴. 
2. 𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙳𝙾𝙴𝚂 𝙽𝙾𝚃 𝙲𝙾𝙽𝚃𝙰𝙸𝙽𝚂 𝙲𝙰𝙼𝚁𝙸𝙿𝚂, 𝙿𝙾𝚁𝙽 𝙰𝙽𝙳 𝙵𝙰𝙺𝙴 𝙵𝙸𝙻𝙴𝚂. 
3. 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝚃𝙷𝙴 𝙻𝙰𝚂𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙼𝙴 𝚆𝙸𝚃𝙷 𝚀𝚄𝙾𝚃𝙴𝚂. 𝙸'𝙻𝙻 𝙰𝙳𝙳 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙼𝚈 𝙳𝙱.

 𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 𝙰𝚂𝚆𝙸𝙽"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- 𝚄𝚂𝙴𝙳 𝚃𝙾 𝙲𝙾𝙽𝙽𝙴𝙲𝚃 𝙱𝙾𝚃 𝚃𝙾 𝙿𝙼 𝙵𝙾𝚁 𝙼𝙰𝙽𝙰𝙶𝙸𝙽𝙶 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 
- 𝙸𝚃 𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝙰𝚅𝙾𝙸𝙳 𝚂𝙿𝙰𝙼𝙼𝙸𝙽𝙶 𝙸𝙽 𝙶𝚁𝙾𝚄𝙿𝚂.

<b>NOTE:</b>
1. 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙰 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽. 
2. 𝚂𝙴𝙽𝙳 <𝙲𝙾𝙳𝙴>/𝙲𝙾𝙽𝙽𝙴𝙲𝚃</𝙲𝙾𝙳𝙴> 𝙵𝙾𝚁 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙽𝙶 𝙼𝙴 𝚃𝙾 𝚄𝚁 𝙿𝙼
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>

 𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 𝙰𝚂𝚆𝙸𝙽"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
𝚃𝙷𝙴𝚂𝙴 𝙰𝚁𝙴 𝚃𝙷𝙴 𝙴𝚇𝚃𝚁𝙰 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 𝙾𝙵 𝙲𝙸𝙽𝙴𝙼𝙰𝙻𝙰.𝙲𝙾𝙼 𝙱𝙾𝚃

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>

 𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 𝙰𝚂𝚆𝙸𝙽"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝙾𝙽𝙻𝚈 𝚆𝙾𝚁𝙺𝚂 𝙵𝙾𝚁 𝙼𝚈 𝙰𝙳𝙼𝙸𝙽𝚂

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>

 𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 𝙰𝚂𝚆𝙸𝙽"""
    STATUS_TXT = """❀ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
❀ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
❀ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
❀ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
❀ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱

 𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 𝙰𝚂𝚆𝙸𝙽"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 🙏 Wᴇʟᴄᴏᴍᴇ ᴛᴏ  {}

-Oʙᴇʏ Tʜᴇ Rᴜʟᴇs-

★ᴛʏᴘᴇ ᴄᴏʀʀᴇᴄᴛ sᴘᴇʟʟɪɴɢ
   (Sᴇᴀʀᴄʜ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ɪɴ ɢᴏᴏɢʟᴇ)
★Mᴏᴠɪᴇ ɴᴀᴍᴇ & ʏᴇᴀʀ ᴏɴʟʏ
    - Nᴏ ᴇxᴛʀᴀ ғɪᴛᴛɪɴɢs😅 

Exᴀᴍᴘʟᴇ : ᴋɢғ ᴄʜᴀᴘᴛᴇʀ 2 2022

കൂടുതൽ അറിയാൻ ഗ്രൂപ്പ്‌ റൂൾസ്‌ വായിക്കുക..

⚠️ 𝙳𝚄𝙴 𝚃𝙾 𝙲𝙾𝙿𝚈𝚁𝙸𝙶𝙷𝚃 𝙸𝚂𝚂𝚄𝙴 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙲𝙷𝙰𝚃𝚂 & 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝚆𝙸𝙻𝙻 𝙱𝙴 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙸𝙽 10 𝙼𝙸𝙽⏱️.

© ᴄɪɴᴇᴍᴀʟᴀ.ᴄᴏᴍ </b>"""
