import discord
from discord.ext import commands

f = open('token.txt', 'r')
token = f.read()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix='/',
    intents=intents
)


@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')


@bot.command()
async def challenge(ctx, user: discord.User):
    await ctx.send('You have challenged: ' + user.mention)


bot.run(
    token
)
