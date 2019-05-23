import discord
from discord.ext import commands
from valcros import valcros
import configparser
class velcomer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        rconf = configparser.ConfigParser()
        rconf.read('config.ini')
        await member.send(embed= await valcros.constructmacro(valcros, rconf.get('Welcomer', 'welcomemacro')))

def setup(bot):
    bot.add_cog(velcomer(bot))
