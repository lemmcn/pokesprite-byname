import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=";")
prefix = '^'

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    args = str(message.content).split(" ")
    if args[0] == prefix + "sprite":
        await message.channel.send("Click the link below!\n"
                                   "https://img.pokemondb.net/sprites/silver/normal/args" + args[1] + '.png')
bot.run('')
