import discord
from discord.ext import commands
import configparser
class voll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('poll:') or message.content.startswith('Poll:'):
            rconf = configparser.ConfigParser()
            rconf.read('config.ini')
            for i in range(len(dict(rconf.items('Poll')))):
                await message.add_reaction(rconf.get('Poll', 'emote' + str(i)))

def setup(bot):
    bot.add_cog(voll(bot))
