import discord
import re

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot başarıyla giriş yaptı: {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Mesajın özel bir kanalda olup olmadığını kontrol edin
    if isinstance(message.channel, discord.channel.DMChannel):
        return

    content = message.content
    if 'x.com' in content or 'twitter.com' in content:
        new_content = re.sub(r'(https?:\/\/)(www\.)?(x\.com|twitter\.com)', r'\1fxtwitter.com', content)
        await message.channel.send(new_content)



client.run('NTEwMTE0MjQxMzA3NjA3MDUx.GMhvts.Atlgbhe4pqQKLvULtYY-EysUzqnk5QhOqL0-Bs')
