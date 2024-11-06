import discord
from discord.ext import commands
from hiddenFiles.tFile import token

# Configure intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

# Create an instance of a bot with the configured intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    """This is called when the bot is ready."""
    print(f"We have logged in as {bot.user}")
    print("Bot ready!")

# Command for saying hello
@bot.command()
async def hello(ctx):
    """Command that sends a hello message."""
    await ctx.send(f"Hello there! {ctx.author.mention}!")

# Command for saying good morning, with aliases 'gm' and 'morning'
@bot.command(aliases=['gm', 'morning'])
async def goodmorning(ctx):
    """Command for saying good morning."""
    await ctx.send(f"Good Morning! {ctx.author.mention}!")

# Command that replies to !sheep
@bot.command()
async def sheep(ctx):
    """Command that replies to !sheep with a baa."""
    print(f"Received a sheep command from {ctx.author}")
    await ctx.send("Baa! 🐑")

# Handle errors globally for commands
@bot.event
async def on_command_error(ctx, error):
    """Handle errors in commands."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I don't understand that command!")
    else:
        await ctx.send(f"An error occurred: {error}")
        print(f"Error in {ctx.command}: {error}")

def run_bot():
    """Function to run the bot."""
    bot.run(token())  # Ensure the correct token is provided

if __name__ == "__main__":
    run_bot()
