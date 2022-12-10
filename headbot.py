import discord
from discord.ext import commands

import os #for importing all the features
import subprocess #for hosting made bots

import json #for variable information


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="r!", intents=intents)


features_bool = {}
feature_list = [ "tictactoe" , "snakes" ]
user_bottoken = [""]

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
    await ctx.send("Kindly make a bot user and provide a token using command /bottoken your_bottoken")

@bot.command()
@commands.dm_only()
async def deploybot ( ctx ) :

    final_features_bool = ['0'] * len ( feature_list )

    for i , s in enumerate ( feature_list ) :

        if features_bool.get(s) == None or features_bool.get(s) == '0' :

            continue

        if features_bool.get(s) == '1' :

            final_features_bool [ i ] = '1'

    final_features_bool = "".join( final_features_bool )

    subprocess.Popen('python3 test.py ' + final_features_bool + ' ' + user_bottoken[0] , shell=True)
    await ctx.send("Your bot is hosted..Use your bot yayayay!!")



@bot.command()
@commands.dm_only()
async def bottoken ( ctx , message ) :
    
    user_bottoken[0] = str ( message )

    await ctx.send ( 'To add any feature from the feature list just write the command /addfeaturename' )
    await ctx.send ( 'feature list' )

    for i in feature_list :
        await ctx.send(i)



@bot.command()
@commands.dm_only()
async def add ( ctx , feature ,message="1" ) :

    if feature not in feature_list :

        await ctx.reply ( f'Sorry, feature {feature} does not exit. Kindly check if there is a typo' )
    
    elif message == '0' :
        
        features_bool[feature] = '0'

        await ctx.reply ( f'Feature {feature} has been removed. ' )

    elif message == '1' :
        
        features_bool[feature] = '1'

        await ctx.reply ( f'Yeah, feature {feature} has been added.' )

# loading bot token

f = open ( 'data.json' )
data = json.load(f)
bot.run( data['token'] )
