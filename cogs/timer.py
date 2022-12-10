import nextcord
from nextcord.ext import commands
import asyncio

class Timer(commands.Cog):

    def __inint__ ( self , bot ) :
        self.bot = bot



    #Events

    @commands.Cog.listener()
    async def on_ready (self) :
        print('Bot is online and sample feature is active')


    #Commands

    @commands.command()
    async def timer(self,ctx,minutes,seconds):
        try:
            minuteint=int(minutes)
            secondint=int(seconds)
        
            if secondint <=0:
                await ctx.send("Choose a valid time")
                raise BaseException

            while True:
                while True:
                    secondint -= 1
                    if secondint==0:
                        minuteint -=1
                        secondint +=59
                        break
                    await asyncio.sleep(1)
                if minuteint<0:
                    
                    break
    
                
            await ctx.send(f"{ctx.author.mention} Time over")
        except ValueError:
            await ctx.send("You must enter an integer")


def setup( bot ):
    bot.add_cog(Timer(bot))