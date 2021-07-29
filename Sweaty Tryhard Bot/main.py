import discord
from discord.ext import commands
import os
import keep_alive
import random

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print(f"{bot.user.name} bot is in!".format(bot))
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="Sweaty Minecraft"))


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)


@bot.command(brief="Kills anyone you want!!")
async def kill(ctx, person: discord.Member):
    choices = [
        f"{person.display_name}'s bed was ripped apart by {ctx.author.display_name}!", f"{person.display_name} was comboed by {ctx.author.display_name}!"
    ]
    await ctx.send(random.choice(choices))


@bot.command(brief="Answers a question!")
async def ask(ctx):
    choices = ["Yes!", "No!"]
    await ctx.send(random.choice(choices))


@bot.command(brief="Sends someone an anonymous private message!")
async def dm(ctx, person: discord.Member, args):
    await person.send(args)


keep_alive.keep_alive()

bot.run(os.environ['TOKEN'])
