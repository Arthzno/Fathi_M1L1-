
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def roll (ctx, num_sides: int = 6):
    """Rolls a dice with a specified number of sides (default is 6)."""
    roll_result = random.randint(1, num_sides)
    await ctx.send(f'You rolled a {roll_result} on a {num_sides}-sided dice!')

bot.run("MTI2NjY5ODQ4MzcwOTExNjQ1Nw.GB-NZq.XbhRpilMpmglAUHR7zuSdr2ZsSch4FtEaIL0F8")
