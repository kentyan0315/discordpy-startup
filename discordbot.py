from discord.ext import commands
import os
import traceback
from datetime import datetime, date, timedelta
import locale
import calendar
import discord



bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

channnel_ID = 803873798487146516 #チャンネルID


@client.event

        

date = datetime.now()

month = date.strftime('%m')
day = date.strftime('%d')
weekdays = date.strftime('%A')

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
while num < 7:
 #print(date.strftime('%m%d,%A'))
# day += 1

 if weekday == 7:
  weekday = 0
 #print(daylist[num] , weeklist[weekday])
   async def on_message(message):
   if message.content == '/boss':
    await message.channel.send(daylist[num] , weeklist[weekday])
 weekday += 1 
 num += 1
    



bot.run(token)
