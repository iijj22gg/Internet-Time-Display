import time, discord
from discord.ext import tasks
from math import floor

bot = discord.Client()
oldTime = 0

@tasks.loop(seconds=2)
async def status():
    global bot
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
    if int(bTime) > int(oldTime): await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="@" + str(bTime)))
    oldTime = bTime

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    try: await status.start()
    except: pass

bot.run('token')
