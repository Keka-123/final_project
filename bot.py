import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Здравствуй, я {bot.user}!')

@bot.command()
async def globalno(ctx):
    globalno = ["Что такое глобальное потепление?", "Что вы знаете о глобальном потеплении?","Изза чего может появится ГП?","Что нового вы узнали?"]
    await ctx.send(random.choice(globalno))



bot.run("MTIyODczMTU4NTgxODUyNTcxNw.GIwYpG.i3PofkLtMpPY69gtccPuf4pUX6cy1MAIZhjLtE")