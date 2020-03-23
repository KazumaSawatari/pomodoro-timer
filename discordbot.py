import asyncio
from time import sleep

from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='#')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.command()
async def join(ctx):
    # voicechannelを取得
    vc = ctx.author.voice.channel
    # voicechannelに接続
    await vc.connect()


@bot.command()
async def bye(ctx):
    # 切断
    await ctx.voice_client.disconnect()


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def start(ctx):
    asyncio.ensure_future(count_time(ctx))


async def count_time(ctx):
    await ctx.send('!sh s')
    await ctx.send('作業を開始。23分後終了')
    await ctx.send('!sh read_limit 0')
    #    sleep(1380000)
    await asyncio.sleep(600)
    await ctx.send('!sh read_limit 20')
    await ctx.send('10分経過。')
    await ctx.send('!sh read_limit 0')

    await asyncio.sleep(780)
    await ctx.send('!sh read_limit 20')
    await ctx.send('作業を終了。7分間休憩')
    await ctx.send('!sh read_limit 0')
    #    sleep(1380000)
    await asyncio.sleep(420)
    await ctx.send('休憩終了。')
    await ctx.send('!sh read_limit 20')

bot.run(token)
