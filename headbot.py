import discord
from discord.ext import commands

import os           #for importing all the feature names
import subprocess   #for hosting the user's bot
import json         #for variable information


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="p!", intents=intents)


#user bot_variables

feature_list = []
for filename in os.listdir('./cogs'):
    if filename[-3:] == '.py' :
        feature_list += [ filename[:-3] ]

user_bottoken = [""]
user_prefix = ["b!",""]
features_bool = {}

for i in feature_list :

    features_bool [ i ] = '0'


# runs if a bot is active

@bot.event
async def on_ready():
    print( f' We have logged in as { bot.user } ')


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
    
    await ctx.send ( "Add your bot's bottoken using the command p!bottoken <your_bottoken> " )

    await ctx.send ( 'To add any feature from the feature list just write the command p!add <feature_name>' )
    await ctx.send ( 'feature list' )

    for i in feature_list :
        await ctx.send(i)
    
    await ctx.send ( 'You can also set the prefix to be used in your new bot using p!setprefix <prefix>' )

#bot-token
        
@bot.command()
@commands.dm_only()
async def bottoken ( ctx , message ) :
    
    user_bottoken[0] = str ( message )

    if user_bottoken[0] != '' :
        await ctx.send ( "bottoken recieved" )

    else :
        await ctx.send ( "Kindly write your bottoken after p!bottoken" )



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
        await ctx.send ( 'You can use p!selectedfeatures to see all the selected features' )
        await ctx.send ( 'You can use p!deploybot to deploy your bot' )


#add-prefix
    
@bot.command()
@commands.dm_only()
async def setprefix ( ctx , prefix ) :

    user_prefix[0] = str ( prefix )
    await ctx.send(f'Yay, new bot prefix set to {user_prefix[0]}')
 

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
        if features_bool.get(s) == '1' :
            final_features_bool [ i ] = '1'

    final_features_bool = "".join( final_features_bool )

    user_prefix[1] = ""
    for i in user_prefix[0] :

        a = str ( ord ( i ) )
        a = '0'* ( 3 - len ( a ) ) + a
        user_prefix[1] += a
    
    subprocess.Popen('python mainbot.py ' + final_features_bool + ' ' + user_bottoken[0] + ' ' + user_prefix[1] , shell = True )
    
    await ctx.send("Your bot is hosted..Use your bot yayayay!!")


# loading bot token

f = open ( 'data.json' )
data = json.load(f)
bot.run(data['token'])

