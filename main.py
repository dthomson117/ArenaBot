import discord
from discord.ext import commands

f = open('token.txt', 'r')
token = f.read()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(
    command_prefix='!',
    intents=intents
)


@client.command()
async def hello(ctx):
    await ctx.send('Hello!')


client.run(
    token
)
