import requests
import discord
from discord.ext import commands
from hiddenFiles.tFile import token


def main():
  print('--Chrysomallos discord bot is awake!--')

  bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

  intents = discord.Intents.default()
  intents.message_content = True  # Enable the message content intent

  @bot.event
  async def on_ready():
    print(f"'We have logged in as {bot.user})")
    print("Bot ready!")
  
  @bot.command()
  async def hello(ctx):
    await ctx.send(f"Hello there! {ctx.author.mention}!")

  @bot.command(aliases=['gm','morning'])
  async def goodmorning(ctx):
    # Convert the user's input to lowercase
    await ctx.send(f"Good Morning! {ctx.author.mention}!")
  

  bot.run(token())


if __name__=="__main__":
  main()