import discord
import sys
import os
from discord.ext import commands 

feature_list = [ "tictactoe" , "snakes" ]
features_bool = sys.argv[1]
final_features_bool = {}

for i , s in enumerate ( feature_list ) :

    if features_bool [ i ] == '1' :

        final_features_bool [ s ] = '1'

bottoken = sys.argv[2]

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot=commands.Bot(command_prefix='l!', case_insensitive=True , intents = intents )

@bot.event
async def on_ready():
    print(f'User bot is ready and running as {bot.user}')
    print(features_bool)

@bot.command()
async def ping(ctx):
  await ctx.send('Pong!')

for filename in os.listdir('./cogs'):
    if filename[-3:] == '.py' :
        if final_features_bool.get(filename[:-3]) == '1' :
            bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(bottoken)
