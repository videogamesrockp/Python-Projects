import discord
from discord.ext import commands
import random
import os
import keep_alive
import time

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print(f"{bot.user.name} bot is in!".format(bot))


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)


@bot.command(brief="Kills anyone!")
async def kill(ctx, person: discord.Member):
    choices = [
        f"{person.name} committed suicide after their car ran out of steam... :sob: ",
        f":fire: {person.name}'s car got too hot... What a terrible way to go..."
    ]
    await ctx.send(random.choice(choices))


@bot.command(brief="Answers a question!")
async def ask(ctx):
    choices = ["Of course!", "No, are you kidding me?"]
    await ctx.send(random.choice(choices))


@bot.command(brief="VROOM VROOM VROOM!")
async def race(ctx):
    embedVar = discord.Embed(
        title="INFERNO RACER'S RACE!",
        description="This is the live Inferno Racer race!",
        color=0xFF0000)
    file = discord.File("Fire Logo.png", filename="image.png")
    embedVar.set_image(url="attachment://image.png")
    msg = await ctx.send(file=file, embed=embedVar)
    embedVar = discord.Embed(
        title="INFERNO RACER'S RACE!",
        description="This is the live Inferno Racer race!",
        color=0xFFFF00)
    file = discord.File("Fire Logo.png", filename="image.png")
    embedVar.set_image(url="attachment://image.png")
    embedVar.add_field(
        name="1st Minute Progress!",
        value=
        "Dull Ash Racer is completely out of steam and have stopped at the road! Inferno Racer, however, is ABSOLUTELY on fire!! FLAMES ARE ERUPTING OUT OF THE SPEEDING CAR AS IT IS APPROACHING SPEEDS OF 1,000 WPM!! ASTOUNDING!!"
    )
    time.sleep(2.5)
    await msg.delete()
    msg = await ctx.send(file=file, embed=embedVar)
    embedVar = discord.Embed(
        title="INFERNO RACER'S RACE!",
        description="This is the live Inferno Racer race!",
        color=0x800080)
    file = discord.File("Fire Logo.png", filename="image.png")
    embedVar.set_image(url="attachment://image.png")
    embedVar.add_field(
        name="2nd Minute Progress",
        value=
        "Uh oh, another car is coming right behind, but Inferno Bot is too speedy! THE SPEED!! THIS IS INSANITY!! BOTH OF THEM GOING WHEEL TO WHEEL! PURPLE FIRE AGAINST BRIGHT YELLOW FIRE!!"
    )
    time.sleep(7.5)
    await msg.delete()
    msg = await ctx.send(file=file, embed=embedVar)
    embedVar = discord.Embed(
        title="INFERNO RACER'S RACE!",
        description="This is the live Inferno Racer race!",
        color=0x00FFFF)
    file = discord.File("Fire Logo.png", filename="image.png")
    embedVar.set_image(url="attachment://image.png")
    embedVar.add_field(
        name="Finish!",
        value=
        "As they are nearing the finish, Inferno is pulling ahead!! It looks like the other car has no chance at this point!! OH! THE SPEED!! In a last ditch effort, the other car tried to pull ahead, and their car overheated!! That's what happens when you compete with the ONE AND ONLY INFERNO RACER!!!"
    )
    time.sleep(7.5)
    await msg.delete()
    await ctx.send(file=file, embed=embedVar)


@bot.command(brief = "You can submit your ideas for the bot straight to the developers!")
async def submit(ctx, *, message):
    embedVar = discord.Embed(title=f"Submission by {ctx.author}",
                             description=message,
                             colour=discord.Color.purple())
    await ctx.send("Your idea has been submitted!")
    channel = bot.get_channel(842552081004757063)
    msg = await channel.send(embed=embedVar)
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")


keep_alive.keep_alive()

bot.run(os.environ['TOKEN'])
