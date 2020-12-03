import discord
import os
import platform
import sys
import re

# Import our config file
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found :(")

import config
import commands


#######################
### GETTING STARTED ###
#######################
# - Create your own `config.py` by entering the required varibles
# - Install `discord.py` from PIP
# - Run `bot.py` using the respective commands for your operating system

# !DOCUMENTATION! : https://discordpy.readthedocs.io/en/latest

print("Bot starting...\n")

client = discord.Client()


@client.event
async def on_ready():
    # Print some debugging information which
    # is almost always a good idea!
    print(f'Logged in as `{client.user.name}`')
    print(f'Discord.py version: {discord.__version__}')
    print(f'Python version: {platform.python_version()}')
    print(f'Running on: {platform.system()} {platform.release()} ({os.name})')
    print('-----')
    # Set status of bot
    # client.

# Dictionary of the available commands
commandsList = {
    'ping': commands.ping,  # Pong!
    'uptime': commands.uptime,  # tells you the bot's uptime
    'dm': commands.dm,  # sends you a DM
    'embed': commands.embed,  # sends you an "embed"
    'react': commands.react,  # reacts to your message
    'roles': commands.roles,  # list roles, add role, remove role
}


@client.event
async def on_message(msg: discord.Message):
    global commandsList  # use the `global` keyword to use global variables
    #######################
    ### FILTER MESSAGES ###
    #######################
    # Ignore message if the sender is a bot
    if msg.author.bot:
        return
    # Filter all messages that start with
    if msg.content.startswith(config.prefix):
        #####################
        ### PARSE MESSAGE ###
        #####################

        # *Basic* way: `args = msg.content[1:].split()`
        # *Big Brain* way (regex):
        args = re.compile(' +').split(msg.content[1:])
        if len(args) == 0:  # do not except commands that are empty
            return
        # the pop function returns the value of the removed item
        cmd = args.pop(0)
        # print(cmd) # uncomment this to see what is being seen by your bot
        # print(args)

        #############################
        ### PROCESS COMMANDS HERE ###
        #############################
        # !NOTE: there are multiple ways to approach this!!! Lemme explain -Nathan

        # Recall that a dictionary is a "unordered collection of key-value pairs"
        response = await commandsList.get(cmd)(msg, args)
        # ^^ the "response" is a boolean value telling you
        #  if the command ran without errors/problems


client.run(config.token)
