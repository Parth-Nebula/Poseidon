import nextcord
from nextcord.ext import commands
from googleapiclient.discovery import build
import random
api_key = "AIzaSyB6aEDabul04D8KAHVz6NCBDpfsRtuZBmk"

class ImageSearch(commands.Cog):

    def __inint__ ( self , bot ) :
        self.bot = bot



    #Events

    @commands.Cog.listener()
    async def on_ready (self) :
        print('Bot is online and sample feature is active')


    #Commands
    @commands.command(aliases=["show"])
    async def showpic(self,ctx,*,search):
        ran = random.randint(0,9)
        resource = build("customsearch", "v1", developerKey =  api_key).cse()
        result = resource.list(q=f"{search}", cx="30e2e8425ff1740d0",searchType ="image").execute()
        url =  result["items"][ran]["link"]
        embed1 = nextcord.Embed(title= f"Here's your image ({search.title()})")
        embed1.set_image(url=url)
        await ctx.send(embed=embed1)

def setup( bot ):
    bot.add_cog(ImageSearch(bot))
    
