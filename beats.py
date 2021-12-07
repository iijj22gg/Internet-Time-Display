import time, discord
from discord.ext import tasks
from math import floor

bot = discord.Client()

@tasks.loop(seconds=2)
async def status():
    global bot
    bTime = str(floor(((int(time.strftime("%M", time.gmtime())) * 60) + ((int(time.strftime("%H", time.gmtime())) + 1) * 3600)) / 86.4))
    try:
        if bTime > oldTime: await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="@" + str(bTime)))
    except: await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="@" + str(bTime)))
    oldTime = bTime

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    await status.start()

bot.run('token')
