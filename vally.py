import discord
from discord.ext import commands
import discord.utils
import asyncio
import json
import datetime
from pathlib import Path
import sys



# Read filesystem for token, close and warn if file can't be found/read
try:
    with open('discord.token', 'r') as tokeninput:
            token=tokeninput.read().replace('\n', '')
except:
    print("Failed to read token! Make sure you put your token into 'discord.token' in the bot's directory!")
    sys.exit(2)

#Initialize the bot
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
        await message.add_reaction("👍")
        await message.add_reaction("👎")
        await message.add_reaction("🤷")
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    embed=discord.Embed(title="💞 Welcome To SSD!", color=0xff69b4, timestamp = datetime.datetime.now())
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/542344236901597211/570070857427320892/SERVER_ICON4.png")
    embed.add_field(name="Please take a look at the rules:", value="You can do so in " + "#welcome-and-rules + ".", inline=True)
    embed.add_field(name="Tell us about yourself!", value="Be sure to " + "#introduce-yourself" + " so we can get to know you better!", inline=False)
    embed.add_field(name="See how you can stand out:", value="Take a look at " + "#get-roles + ".", inline=True)
    embed.add_field(name="Finally, invite 5 friends to get the :star: Star role!", value="This also gets you into unique giveaways. Have fun x", inline=True)
    embed.set_footer(text="School Students Discord")
    await member.send(embed=embed)

bot.run(token)
