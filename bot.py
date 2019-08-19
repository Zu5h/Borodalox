import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')

doublemix = []
pickArr = []
doublemix_last_str = ""
reqAmount = 2

@bot.event
async def on_ready():
        print('bot is online')

@bot.command()
async def test(ctx):
    await ctx.send(f'ping is {round(bot.latency * 1000)} ms')

@bot.command()
async def clear(ctx, msg_amount=5):
    await ctx.channel.purge(limit=msg_amount)
    await ctx.send(f'Cleared {msg_amount} messages')

@bot.command(aliases=['8ball','random','rand'])
async def _8ball(ctx, *, question):
    responses = ['yes', 'no', 'probably', 'not sure']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@bot.command()
async def info(ctx, member : discord.Member):
    await ctx.send(f'Id is {member.id}\nIs it a bot? {member.bot}\n')

@bot.command(aliases=['++'])
async def add(ctx):
    author = ctx.message.author.name

    doublemix_last_str = "none"

    if not doublemix:
        print("List is empty")
    else:
        doublemix_last_str = doublemix[-1]
    if author == doublemix_last_str:
        await ctx.send(f'{author}, youre already in the list!')
        doublemix.remove(author)

    doublemix.append(author)
    Uamount = len(doublemix)

    if Uamount == reqAmount:
        await ctx.send(f'{Uamount} out of {reqAmount} members are in a mix\nList of players:')
        for x in doublemix:
            await ctx.send(f'{x}')
        pickArr = doublemix.copy()
        doublemix.clear()

        pick()
    else:
        await ctx.send(f'{Uamount} players in a mix:')
        for x in doublemix:
            await ctx.send(f'{x}')

@bot.command(aliases=['--'])
async def remove(ctx):
    author = ctx.message.author.name
    doublemix.remove(author)
    Uamount = len(doublemix)
    await ctx.send(f'{author} left the mix')

@bot.command()
async def pick():
    await ctx.send(f'Pick')

@bot.command()
async def who(ctx):
    if not doublemix:
        await ctx.send(f'There are no people in a mix')
    else:
        Uamount = len(doublemix)
        await ctx.send(f'{Uamount} players in a mix:')
        for x in doublemix:
            await ctx.send(f'{x}')

bot.run('NjEyNzk4ODk1ODIyNzMzMzM4.XVnpIw.V7H6taOSBLbjH9qjX5Afa_9YUrg')
