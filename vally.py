import discord
from discord.ext import commands
import discord.utils
import asyncio
import json
import datetime
import configparser
from pathlib import Path
import sys
import valcros
import velcomer
import volls
# Read filesystem for token, close and warn if file can't be found/read
try:
    with open('discord.token', 'r') as tokeninput:
            token=tokeninput.read().replace('\n', '')
except:
    print("Failed to read token! Make sure you put your token into 'discord.token' in the bot's directory!")
    sys.exit(2)

#Read configuration file, save variables.
rconf = configparser.ConfigParser()
rconf.read('config.ini')
#Set variables
prefix = rconf.get('Main', 'prefix')
embedcolour = rconf.get('Main', 'embedcolour')

#Initialize the bot
bot = commands.Bot(command_prefix = prefix)
bot.load_extension('valcros')
bot.load_extension('velcomer')
bot.load_extension('volls')
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Connected to Discord!")
    activity = discord.Activity(name = "your feedback!", type = discord.ActivityType.listening)
    await bot.change_presence(activity = activity)

bot.run(token)
