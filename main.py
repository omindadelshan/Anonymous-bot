from telethon.sync import TelegramClient, events, Button
from telethon import errors
from telethon.tl.types import InputPeerChat
from telethon.errors import FloodWaitError
from telethon.tl.types import ChatEmpty
import os
import uuid
import shutil
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

from creds import Credentials

client = TelegramClient('Telethon Anonymous Bot',
                    api_id = Credentials.API_ID,
                    api_hash=Credentials.API_HASH).start(bot_token=Credentials.BOT_TOKEN)

DEFAULT_START = ("🤗Hey! 👨‍💻𝐼 𝐴𝑚 𝑆𝐷 𝑃𝑟𝑜𝑗𝑒𝑐𝑡 𝐴𝑛𝑦𝑚𝑜𝑢𝑠𝑒 𝑠𝑒𝑛𝑑𝑒𝑟 𝑏𝑜𝑡.⚡⚡ 🌀 𝑀𝑎𝑑𝑒 𝐵𝑦 @omindas 🌀🌀🔥🔥.\n\n"
                 "💥🌟**Just Forward me some messages or media and I will anonymize the sender**💥🌟.\n\n"
                 "🤖🤖You Can Give a This Bot Source codes and more help in our channal.⚡⚡ Our Channal is a @sdprojectupdates ⚡⚡             A Bot By Ominda And Powerd By SD Projectupdates👨‍💻👨‍💻")


if Credentials.START_MESSAGE is not None:
  START_TEXT = Credentials.START_MESSAGE
else:
  START_TEXT = DEFAULT_START
  
@client.on(events.NewMessage)
async def startmessage(event):
  try:
    if '/start' in event.raw_text:
      ok = event.chat_id
      await client.send_message(event.chat_id,
                                message=START_TEXT,
                                buttons=[[Button.url("🔥 Developer 🔥","https://t.me/omindas"),
                                         Button.url("🤖Support Channel🤖","https://t.me/sdprojectupdates"),
                                         Button.url("👨‍💻 Help 👨‍💻","https://t.me/omindas")]])                                                                
    if event.message.media:
      await client.send_message(event.chat_id,file=event.message.media)
    else:
      await client.send_message(event.chat_id,event.message)
  except FloodWaitError as e:
    pass
    

with client:
  client.run_until_disconnected() 
