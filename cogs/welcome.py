import nextcord
from nextcord.ext import commands
from PIL import Image
from io import BytesIO

class Welcome(commands.Cog):

    def __inint__ ( self , bot ) :
        self.bot = bot



    #Events

    @commands.Cog.listener()
    async def on_ready (self) :
        print('Bot is online and welcome feature is active')


    #Commands

    @commands.command()
    async def welcome(self,ctx,user: nextcord.Member = None):
        if user == None:
            user= ctx.author
        kitty = Image.open("catQ.jpg")
        asset = user.avatar.replace(size=128)
        data = BytesIO(await asset.read())
        pfp= Image.open(data)

        pfp = pfp.resize((40,40))
        kitty.paste(pfp, (131,87))
        kitty.save("profile.jpg")
        await ctx.send(file= nextcord.File("profile.jpg"))


def setup( bot ):
    bot.add_cog(Welcome(bot))
    