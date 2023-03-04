import discord
from discord.ext import commands

f = open('token.txt', 'r')
token = f.read()

client = commands.Bot(
    command_prefix='!',
    help_command=None
)


@client.command()
async def hello(ctx):
    await ctx.send('Hello!')


client.run(
    token
)
