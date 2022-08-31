import os
from discord_webhook import DiscordWebhook
from telethon import TelegramClient, events
try:
    import private_config
except ModuleNotFoundError:
    import config as private_config

client = TelegramClient('session', private_config.api_id, private_config.api_hash,connection=private_config.proxy_type,proxy=private_config.proxy_settings)

@client.on(events.NewMessage)
async def my_event_handler(message):
    chat = await message.get_chat()
    if chat.title == private_config.channel_name or message.chat_id == private_config.channel_id:
        webhook = DiscordWebhook(url=private_config.discord_webhook)
        webhook.avatar_url = private_config.avatar_url
        webhook.username = private_config.username
        webhook.content = message.raw_text
        if message.photo:
            path = await client.download_media(message.media)
            with open(path, "rb") as f:
                webhook.add_file(file=f.read(), filename=str(message.photo.date)+".jpg")
        webhook.execute()
        os.remove(path)

client.start()
client.run_until_disconnected()
