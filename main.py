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


@bot.tree.command(name="challenge", description="Challenge a user to a duel. Has to be on the same level as you or above")
async def challenge(ctx, user: discord.User):
    await ctx.send('You have challenged: ' + user.mention)


bot.run(
    token
)
