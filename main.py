import requests
import discord
from discord.ext import commands
from hiddenFiles.tFile import token


def main():
  print('--Chrysomallos discord bot is awake!--')

  bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

  @bot.event
  async def on_ready():
    print("Bot ready!")
  
  @bot.command()
  async def hello(ctx):
    await ctx.send("Hello there!")


  bot.run(token())


if __name__=="__main__":
  main()