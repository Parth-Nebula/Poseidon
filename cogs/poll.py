import nextcord
from nextcord.ext import commands

class Confirm(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.green)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Confirmed", ephemeral=True)
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.grey)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Cancelled", ephemeral=True)
        self.value = False
        self.stop()

class UserInfo(commands.Cog):

    def __inint__ ( self , bot ) :
        self.bot = bot



    #Events

    @commands.Cog.listener()
    async def on_ready (self) :
        print('Bot is online and userInfo feature is active')


    #Commands
    
    


    @commands.command()
    async def poll(self,ctx,*,message):
        view = Confirm()
        await ctx.send(f"{message}", view=view)

        await view.wait()
        yes = 0
        no =0
        if not view.value == None:
            print("Timed Out")
        if view.value == True:
            yes+=1
            print("Confirmed")
        if view.value == False:
            no+=1
            print("Cancelled")     
        
        em=nextcord.Embed(title="Poll" , description="The result of poll is", color = nextcord.Colour.dark_purple())
        em.add_field(name="For",value= f"{yes}")
        em.add_field(name="Against",value= f"{no}")

        await ctx.send(embed=em)

def setup( bot ):
    bot.add_cog(UserInfo(bot))
    