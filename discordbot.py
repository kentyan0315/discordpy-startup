from discord.ext import commands
import os
import traceback
import datetime
import locale
import calendar


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

channnel_ID = 803873798487146516 #チャンネルID

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def test(ctx):
    await ctx.send('動作中')
    
@bot.command()    
async def boss(ctx):
    dt_now = datetime.datetime.now()
    locale.setlocale(locale.LC_time,'ja_JP.UTF-8')
    for num in range(7):
        await ctx.sent(dt_now.day':'de_now.strftime('%A'))

bot.run(token)
