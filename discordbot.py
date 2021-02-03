from discord.ext import commands
import os
import traceback
from datetime import datetime, date, timedelta
import locale
import calendar
import discord

class schedule:
    def __init__(self,date, today, weekday, weeklist, daylist):
        self.date = date
        self.today = today
        self.weekday = weekday
        self.weeklist = weeklist
        self.daylist = daylist
        
date = datetime.now()
# 2018-01-01 00:00:00
'''
month = date.strftime('%m')
day = date.strftime('%d')
weekdays = date.strftime('%A')
'''
today = datetime.today()

weekday = date.today().weekday()

weeklist = ['月', '火', '水', '木', '金', '土', '日']
daylist = [0] * 10
n = 0
for n in range(7):
    daylist[n] = today.date() + timedelta(days=n)
    
'''    
daylist[0] = today.date()
daylist[1] = today.date() + timedelta(days=1)
daylist[2] = today.date() + timedelta(days=2)
daylist[3] = today.date() + timedelta(days=3)
daylist[4] = today.date() + timedelta(days=4)
daylist[5] = today.date() + timedelta(days=5)
daylist[6] = today.date() + timedelta(days=6)
'''
num = 0
for num in range(7):
 #print(date.strftime('%m%d,%A'))
# day += 1


 if weekday == 7:
  weekday = 0
 print(daylist[num] , weeklist[weekday])
 weekday += 1 
 num += 1


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    


@bot.command()
async def ping(boss):
    await ctx.send('daylist[0] = today.date() + timedelta(days=0)')
bot.run(token)
