from time import sleep

from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='#')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def s(ctx):
    await ctx.send('作業を開始。23分後終了')
#    sleep(1380000)
    sleep(10000)
    ctx.send('作業を終了。7分間休憩')
#    sleep(1380000)
    sleep(10000)


bot.run(token)
