import discord
from discord.ext import commands
from decouple import config
import os #for importing all the features
import subprocess
import json #for variable information


BOT_TOKEN = config('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="p!", intents=intents)



# features = [ "0" , "1" ]
# featurelist = [ "music" , "confession" ]
#botoken = 'MTA1MDQxMjUwNDIzNDMzNjI2Ng.GVsCZr.c4inb8WjLjHFE5g_RLUDGRiWgdNT1UwWfqBJqc'

#user bot_variables
features_bool = {}
feature_list = [ "tictactoe" , "snakes", "confession" , "music" ]
user_bottoken = [""]

# runs if a bot is active

@bot.event
async def on_ready():
    print( f' We have logged in as { bot.user } ')
    print(BOT_TOKEN)


# basic ping

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!") #can also use .reply()


#info
@bot.command()
@commands.dm_only()
async def start ( ctx ) :
    await ctx.send("Poseidon is a discord bot that helps create customisable discord bots without any coding necessary.")
    await ctx.send("Head over to https://discord.com/developers/applications and create your botapplication then come here and simply choose from a list of features and just provide a bot token to get your ready made discord bot in seconds..!! use p!makebot for more info")


#make-bot
@bot.command()
@commands.dm_only()
async def makebot ( ctx ) :
    await ctx.send("Kindly make a bot user and provide a token using command p!bottoken <bottokenhere>")

    for i in feature_list :
        await ctx.send(i)


#bot-token
@bot.command()
@commands.dm_only()
async def bottoken ( ctx , message ) :
    
    user_bottoken[0] = str ( message )

    await ctx.send ( 'To add any feature from the feature list just write the command p!addfeaturename' )
    await ctx.send ( 'feature list' )


#add-features 
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
 

#selected-features
@bot.command()
@commands.dm_only()
async def selectedfeatures( ctx ) :
    
    await ctx.send ( 'Selected features are  : ' )

    for i in features_bool :
        if features_bool [ i ] == '1':
            await ctx.send(i)


#final-deploy
@bot.command()
@commands.dm_only()
async def deploybot ( ctx ) :

    if user_bottoken[0] == "":
        await ctx.send("Please provide a bot token first.!!")
        return

    final_features_bool = ['0'] * len ( feature_list )

    for i , s in enumerate ( feature_list ) :

        if features_bool.get(s) == None or features_bool.get(s) == '0' :

            continue

        if features_bool.get(s) == '1' :

            final_features_bool [ i ] = '1'

    final_features_bool = "".join( final_features_bool )

    print(final_features_bool)
    print(user_bottoken[0])
    subprocess.Popen('python3 test.py ' + final_features_bool + ' ' + user_bottoken[0] , shell=True)
    await ctx.send("Your bot is hosted..Use your bot yayayay!!")


# loading bot token

f = open ( 'data.json' )
data = json.load(f)
bot.run(str(BOT_TOKEN))


