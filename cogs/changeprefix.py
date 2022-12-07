import nextcord
from nextcord.ext import commands
import json

class ChangePrefix(commands.Cog):

    def __inint__ ( self , bot ) :
        self.bot = bot

    @commands.command()
    async def changeprefix ( self , ctx , prefix ) :
		
        with open('prefixes.json','r') as f :
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json','w') as f :
            json.dump(prefixes , f , indent = 4)
		
        await ctx.send(f'Prefix changed to {prefix}')


def setup( bot ):
    bot.add_cog(ChangePrefix(bot))
    
