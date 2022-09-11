import os
from discord_webhook import DiscordWebhook
from telethon import TelegramClient, events
try:
    import private_config as config
except ModuleNotFoundError:
    import config

if config.use_proxy:
    client = TelegramClient('session', config.api_id, config.api_hash,connection=config.proxy_type,proxy=config.proxy_settings)
else:
    client = TelegramClient('session', config.api_id, config.api_hash)

@client.on(events.NewMessage)
async def my_event_handler(message):
    chat = await message.get_chat()
    if chat.title == config.channel_name or message.chat_id == config.channel_id:
        webhook = DiscordWebhook(url=config.discord_webhook)
        webhook.avatar_url = config.avatar_url
        webhook.username = config.username
        webhook.content = message.raw_text
        if message.photo:
            path = await client.download_media(message.media)
            with open(path, "rb") as f:
                webhook.add_file(file=f.read(), filename=str(message.photo.date)+".jpg")
        webhook.execute()
        os.remove(path)

client.start()
client.run_until_disconnected()
