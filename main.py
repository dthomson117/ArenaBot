import discord
from discord.ext import commands
from discord import app_commands

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

"""
@bot.tree.command(name="challenge",
                  description="Challenge a user to a duel. Has to be on the same level as you or above")
async def challenge(ctx, interaction: discord.Interaction):
    await ctx.send('You have challenged: ' + interaction.user.mention)

"""


@bot.tree.command()
@app_commands.describe(
    first_value='The first value you want to add something to',
    second_value='The value you want to add to the first value',
)
async def add(interaction: discord.Interaction, first_value: int, second_value: int):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')


bot.run(
    token
)
