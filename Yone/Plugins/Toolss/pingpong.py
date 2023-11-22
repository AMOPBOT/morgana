
import requests
from pyrogram import filters
import Yone
from pyrogram.enums import ChatAction, ParseMode
from Yone import OWNER_ID, DEEP_API, pbot as app


__help__ = """ᴩɪɴɢ ᴄᴏᴍᴍᴀɴᴅ : :

/ping : sʜᴏᴡ ᴛʜᴇ ᴩɪɴɢ ᴀɴᴅ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
/stats : ɢᴇᴛ ᴛᴏᴩ 10 ᴛʀᴀᴄᴋ ɢʟᴏʙᴀʟ sᴛᴀᴛs, ᴛᴏᴩ 10 ᴜsᴇʀs ᴏғ ᴛʜᴇ ʙᴏᴛ, ᴛᴏᴩ 10 ᴄʜᴀᴛs ᴏɴ ᴛʜᴇ ʙᴏᴛ, ᴛᴏᴩ 10 ᴩʟᴀʏᴇᴅ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ ᴀɴᴅ ᴍᴀɴʏ ᴍᴏʀᴇ..."""

__mod_name__ = "ᴘɪɴɢᴘᴏɴɢ"
