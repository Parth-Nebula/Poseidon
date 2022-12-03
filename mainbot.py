import nextcord
from nextcord.ext import commands

import os #for importing all the features

import json #for variable information


intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


# runs if a bot is active

@bot.event
async def on_ready():
    print( f' We have logged in as { bot.user } ')


# basic ping

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!") #can also use .reply()


# to load and unload files

@bot.command()
async def load ( ctx , extension ) :
    bot.load_extension(f'cogs.{extension}' )

@bot.command()
async def unload ( ctx , extension ) :
    bot.unload_extension(f'cogs.{extension}' )


# loading all the features on startup

for filename in os.listdir('./cogs'):
    if filename[-3:] == '.py' :
        bot.load_extension(f'cogs.{filename[:-3]}')


# loading bot token

f = open ( 'data.json' )
data = json.load(f)
bot.run(data['token'])
