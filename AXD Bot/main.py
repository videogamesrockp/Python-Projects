import discord
from discord.ext import commands
import os
import json
import keep_alive
import random

help_command = commands.DefaultHelpCommand(no_category='Commands')

bot = commands.Bot(command_prefix="$", help_command=help_command)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is in!")
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=f"{bot.command_prefix}help"),
                              status=discord.Status.idle)


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"{error}")


@bot.command(brief="Creates a new coin account!")
async def create_balance(ctx):
    with open("money.json", "r+") as file:
        data = json.load(file)
        if str(ctx.author.id) not in data:
            data[str(ctx.author.id)] = 100
            await ctx.send(f"Created new bank account for {ctx.author}")
        file.seek(0)
        file.truncate(0)
        json.dump(data, file)


@bot.command(brief="Rob someone else!")
async def rob(ctx, person: discord.Member):
    if person.id == ctx.author.id:
        await ctx.send("You can't rob yourself!")
        return
    with open("money.json", "r+") as file:
        data = json.load(file)
        if data.get(str(person.id)) > 0:
            amount = random.randint(-data.get(str(ctx.author.id)),
                                    data.get(str(person.id)))
            data[str(ctx.author.id)] += amount
            data[str(person.id)] -= amount
            file.seek(0)
            file.truncate(0)
            json.dump(data, file)
            if amount >= 0:
                await ctx.send(
                    f"You successfully robbed {person.display_name} for {amount} coins!"
                )
            else:
                await ctx.send(
                    f"{person.display_name} found out and you lost {abs(amount)} coins!"
                )
        else:
            await ctx.send("This user has no more coins to rob!")


@bot.command(brief="Give someone money!")
async def give(ctx, person: discord.Member, amount):
    with open("money.json", "r+") as file:
        if person.id == ctx.author.id:
            await ctx.send("You can't give yourself money!")
            return
        data = json.load(file)
        amount = int(amount)
        if data.get(str(ctx.author.id)) >= amount:
            data[str(ctx.author.id)] -= amount
            data[str(person.id)] += amount
            file.seek(0)
            file.truncate(0)
            json.dump(data, file)
            await ctx.send(
                f"You successfully gave {person.display_name} {amount} coins!")
        else:
            await ctx.send("You don't have that many coins!")


@bot.command(brief="Check your balance!")
async def balance(ctx, person: discord.Member = None):
    with open("money.json", "r+") as file:
        data = json.load(file)
        if person:
            await ctx.send(f"This player has {data.get(str(person.id))} coins!"
                           )
        else:
            await ctx.send(
                f"Your balance is {data.get(str(ctx.author.id))} coins!")


@bot.command(brief="Kills someone!")
async def kill(ctx, person: discord.Member):
    choices = [
        f"{person.display_name} was diced into pieces by {ctx.author.display_name}!"
    ]
    await ctx.send(random.choice(choices))


keep_alive.keep_alive()

bot.run(os.getenv("TOKEN"))
