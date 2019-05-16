import discord
from discord.ext import commands
import discord.utils
import asyncio
import json
import datetime
from pathlib import Path


try:

    bot = commands.Bot(command_prefix = 'ssd! ')
    bot.remove_command('help')

    @bot.event
    async def on_ready():
        print("Connected to Discord!")
        activity = discord.Activity(name = "your feedback!", type = discord.ActivityType.listening)
        await bot.change_presence(activity = activity)

    @bot.event
    async def on_message(message):
        if message.content.startswith('poll:') or  message.content.startswith('Poll:'):
            await message.add_reaction("?")
            await message.add_reaction("?")
            await message.add_reaction("?")
        await bot.process_commands(message)

    @bot.event
    async def on_member_join(member):
        introduceyourself = bot.get_channel(543513685809823745)
        welcomechannel = bot.get_channel(413103266017181696)
        getroles = bot.get_channel(552568746732945440)
        embed=discord.Embed(title="💞 Welcome To SSD!", color=0xff69b4, timestamp = datetime.datetime.now())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/542344236901597211/570070857427320892/SERVER_ICON4.png")
        embed.add_field(name="Please take a look at the rules:", value="You can do so in " + welcomechannel.mention + ".", inline=True)
        embed.add_field(name="Tell us about yourself!", value="Be sure to " + introduceyourself.mention + " yourself so we can get to know you better!", inline=False)
        embed.add_field(name="See how you can stand out:", value="Take a look at " + getroles.mention + ".", inline=True)
        embed.add_field(name="Finally, invite 5 friends to get the :star: Star role!", value="This also gets you into unique giveaways. Have fun x", inline=True)
        embed.set_footer(text="School Students Discord")
        await member.send(embed=embed)

    bot.run("tokengoesherewithquotes")
except KeyboardInterrupt:
    sys.exit()
