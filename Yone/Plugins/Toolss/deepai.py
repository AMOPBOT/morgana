import requests
from pyrogram import filters
import Yone
from pyrogram.enums import ChatAction, ParseMode
from Yone import OWNER_ID, DEEP_API, pbot as app
api_key = DEEP_API



@app.on_message(filters.command(["deep" , ],  prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def deepchat(app: app, message):
    name = message.from_user.first_name
    try:
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(f"Hello {name}\nPlease provide text after the /deep command")
        else:
            a = message.text.split(' ', 1)[1]

            data = {
                'text': a,  
            }

            headers = {
                'api-key': api_key,
            }

            r = requests.post("https://api.deepai.org/api/text-generator", data=data, headers=headers)
            response = r.json()
            answer_text = response['output']
            await message.reply_text(f"{answer_text}")
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e}")


__help__ = """ask any this 
*Commands*:
‣ `/deep`*:* Your Text
  """

__mod_name__ = "DeepAIOp"
