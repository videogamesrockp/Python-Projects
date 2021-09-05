import discord
from discord.ext import commands
import os
import keep_alive
import random

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

bot = commands.Bot(command_prefix = "$", help_command = help_command)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is in!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f"{bot.command_prefix}help"), status = discord.Status.idle)


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"{error}")


@bot.command(brief = "Kills someone!")
async def kill(ctx, person: discord.Member):
    choices = [f"{person.display_name} was diced into pieces by {ctx.author.display_name}!"]
    await ctx.send(random.choice(choices))


keep_alive.keep_alive()

bot.run(os.getenv("TOKEN"))
