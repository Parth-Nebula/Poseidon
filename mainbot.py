import discord
from discord.ext import commands

import sys      #for getting input arguments
import os       #for loading features


feature_list = []
for filename in os.listdir('./cogs'):
    if filename[-3:] == '.py' :
        feature_list += [ filename[:-3] ]


features_bool = sys.argv[1]
final_features_bool = {}

for i , s in enumerate ( feature_list ) :
    if features_bool [ i ] == '1' :
        final_features_bool [ s ] = '1'

bottoken = sys.argv[2]

user_prefix = ""
for i in range ( 0 , len (sys.argv[3]) , 3 ) :
    user_prefix += chr ( int ( sys.argv[3][i:i+3] ) )

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot=commands.Bot(command_prefix=user_prefix, case_insensitive=True , intents = intents )

@bot.event
async def on_ready():
    print(f'User bot is ready and running as {bot.user}')

@bot.command()
async def ping(ctx):
  await ctx.send('Pong!')


for filename in os.listdir('./cogs'):
    if filename[-3:] == '.py' :
        if final_features_bool.get(filename[:-3]) == '1' :
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(bottoken)
