import discord
from discord.ext import commands

import os #for importing all the features
import subprocess

import json #for variable information


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="r!", intents=intents)


# runs if a bot is active

@bot.event
async def on_ready():
    print( f' We have logged in as { bot.user } ')


# basic ping

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!") #can also use .reply()


@bot.command()
@commands.dm_only()
async def start ( ctx ) :
    await ctx.send("Poseidon is a discord bot that helps setup discord bots. Choose from a list of features and just provide a bot token to get your ready made discord bot.")



@bot.command()
@commands.dm_only()
async def makebot ( ctx ) :
    await ctx.send("Kindly make a bot user and provide a token using command /bottoken")

@bot.command()
@commands.dm_only()
async def deploybot ( ctx ) :
    subprocess.Popen('python3 test.py 1 0 MTA1MDQxMjUwNDIzNDMzNjI2Ng.GTb5fk._BJFuM1xB2bbm53lx5pmfgaANbXYLz2mfzWjGs', shell=True)
    await ctx.send("Your bot is hosted..Use your bot yayayay!!")



features = [ 0 , 0]

featurelist = [ "music" , "confession" ]





@bot.command()
@commands.dm_only()
async def bottoken ( ctx , message ) :
    
    bottoken = message

    for i in featurelist :

        await ctx.send(f'Would you like to add the feature {i} reply by giving command /add{i} . You can also add 0 after it to remove it')



@bot.command()
@commands.dm_only()
async def addmusic ( ctx , message="1" ) :
    
    if message == "0" :
        features[0] = 0

    elif message == "1" :
        features[0] = 1



@bot.command()
@commands.dm_only()
async def addconfession ( ctx , message="1" ) :
    
    if message == "0" :
        features[1] = 0

    elif message == "1" :
        features[1] = 1
    

# loading bot token

f = open ( 'data.json' )
data = json.load(f)
bot.run('MTA0OTU4NTcwOTMyMjg3NDkwMA.GAVQH-.gV3a7FK6XRcR7G-bCJICK1Cf_8gvhHMo1D_6r4')
