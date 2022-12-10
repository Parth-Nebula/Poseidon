import discord
import sys
from discord.ext import commands 

n = len(sys.argv)

musicbool = 0
confessionbool = 0
bottoken = 0
musicbool = sys.argv[1]
confessionbool = sys.argv[2]
#bottoken = sys.argv[3]
bottoken = 'MTA1MDQxMjUwNDIzNDMzNjI2Ng.GVsCZr.c4inb8WjLjHFE5g_RLUDGRiWgdNT1UwWfqBJqc'

#replace lines 15 to till client.run with your code @pratham @pradnya
ashish = discord.Intents.default()
ashish.members = True
client=commands.Bot(command_prefix='l!', case_insensitive=True , intents = ashish)

@client.event
async def on_ready():
    print('Bot2 is ready and running')
    print(musicbool)
    print(confessionbool)
    print(bottoken)

@client.command()
async def ping(ctx):
  await ctx.send('Pong!')

if confessionbool == '1':
    @client.command()
    @commands.dm_only()
    async def confess(ctx,*,message):
        print(message)
        await ctx.send('Your confesssion will be posted anonymously after verification by the admins. The admins won\'t be able to know your identity.')
        jojo = client.get_channel(1049589905979887639)
        message1 = await jojo.send(f'{message}')
        await jojo.send(f'{message}')

@client.command()
@commands.dm_only()
async def music(ctx,*,message):
    print(message)
    await ctx.send('Your music taste is shit. Who listens to',{message})
    jojo = client.get_channel(1049589905979887639)
    message1 = await jojo.send(f'{message}')
    await jojo.send(f'{message}')

client.run('MTA1MDQxMjUwNDIzNDMzNjI2Ng.GVsCZr.c4inb8WjLjHFE5g_RLUDGRiWgdNT1UwWfqBJqc')
