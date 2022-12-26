import time, discord
from discord.ext import tasks
from math import floor

client = discord.Client(intents=discord.Intents.none())
oldTime = 0

@tasks.loop(seconds=2)
async def status():
    global client
    global oldTime
    hour = int(time.strftime("%H", time.gmtime()))
    minute = int(time.strftime("%M", time.gmtime()))
    second = int(time.strftime("%S", time.gmtime()))
    bTime = floor(((second + minute * 60) + (hour + 1) * 3600) / 86.4)
    if bTime > 1000: bTime = bTime - 1000
    if bTime < 100:
        if bTime < 10: bTime = "00" + str(bTime)
        else: bTime = "0" + str(bTime)
    if int(bTime) == 1000:
        bTime = "000"
        oldTime = -1
    if int(bTime) > int(oldTime): await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="@" + str(bTime)))
    oldTime = bTime

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    try: await status.start()
    except: pass

client.run('TOKEN')
