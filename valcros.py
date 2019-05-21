import os.path
import configparser
import discord
from discord.ext import commands
import datetime
import distutils
class valcros(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def m(self, ctx, requested_macro):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'macros/' + requested_macro + '.macro')
        if not os.path.isfile(filename):
            await ctx.send("That macro doesn't exist.")
        else:
            await ctx.send(embed=await self.constructmacro(requested_macro, ctx))
    async def constructmacro(self, constructee, ctx):
        mread = configparser.ConfigParser(interpolation=None)
        mread.read('macros/' + constructee + ".macro")
        role_names = [role.name for role in ctx.author.roles]
        if mread.get('Meta', 'permissedrole') not in role_names:
            await ctx.send("You don't have sufficient permissions to use this macro!")
            return
        rconf = configparser.ConfigParser()
        rconf.read('config.ini')
        if len(mread.get('Meta', 'title')) > 256:
            return 
        if len(mread.get('Meta', 'footer')) > 2048:
            return 
        embed = discord.Embed(title=mread.get('Meta', 'title'), color=0xff69b4, timestamp=datetime.datetime.now())
        embed.set_footer(text=mread.get('Meta', 'footer'))
        embed.set_author(name=mread.get('Meta', 'author'), url=mread.get('Meta', 'authorlink'), icon_url=mread.get('Meta', 'authoricon'))
        embed.set_thumbnail(url=str(mread.get('Meta', 'thumbnail')))
        for i in range(26):
            try:
                CurrentWorkingField = mread.get('Field ' + str(i), 'name')
            except:
                pass
            else:
                embed.add_field(name=mread.get('Field ' + str(i), 'name'), value=mread.get('Field ' + str(i), 'value'), inline=mread.get('Field ' + str(i), 'inline').startswith("T"))
        return embed
        
def setup(bot):
    bot.add_cog(valcros(bot))

