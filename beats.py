import time
import discord
from datetime import datetime, timedelta, timezone

client = discord.Client(intents=discord.Intents.none())

async def update_status():
    
    while True:
        now = datetime.now(timezone(timedelta(hours=1)))
        beats = ((now.hour * 3600 + now.minute * 60 + now.second) / 86.4) % 1000
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"@{beats:03.0f}"))
        
        next_beat_seconds = 86.4 - (now.second + now.microsecond / 1_000_000) % 86.4
        await discord.utils.sleep_until(datetime.utcnow() + timedelta(seconds=next_beat_seconds))

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(update_status())

client.run('TOKEN')
