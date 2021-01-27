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
async def ping(ctx):
    await ctx.send('pong')
    

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%A')
    if now == '2':
        channel = client.get_channel(channnel_ID)
        await channel.send('/boss')  

#ループ処理実行
loop.start()


bot.run(token)
