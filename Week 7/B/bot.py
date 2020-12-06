import discord
import os
import platform
import sys
import re
import timeit

# Import our config file
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found :(")

import config


#######################
### GETTING STARTED ###
#######################
# - Create your own `config.py` by entering the required varibles
# - Install `discord.py` from PIP
# - Run `bot.py` using the respective commands for your operating system

# !DOCUMENTATION! : https://discordpy.readthedocs.io/en/latest

# print(f"Path: {sys.path}") # for debuging Python's PATH

# for calculating uptime later
startTime = timeit.default_timer()

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
    # TODO: for 2nd Discord.py meeting:
    # - bot activity
    # - bot profile
    # - bot nickname

# Dictionary of the available commands
# !~ go to the bottom to see the actual list of commands!
commandsList = {} # this just initializes the list

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
        print(f"{msg.author.name} ran the command `{cmd}`" + ("." if response else " but failed.")) # the brackets are important btw
                         # .nickname

        if not response:
            await msg.add_reaction('🚫') # DOCS: https://discordpy.readthedocs.io/en/latest/api.html?highlight=message#discord.Message.add_reaction
                # Parameters:  emoji (Union[Emoji, Reaction, PartialEmoji, str]) 
                # Where to find ascii emojis: https://emojipedia.org/

async def help(msg, args):
    # Return an embed
    return True


async def ping(msg, args):
    await msg.channel.send('Pong!')
    return True

async def failed(msg, args):
    return False

async def uptime(msg, args):
    currentTime  = timeit.default_timer()
    uptime = currentTime - startTime
    # TODO: for next meeting, convert time into a more readable measurement
    await msg.channel.send(
        f"The bot has been active for {uptime} seconds")
    return True


async def dm(msg, args):
    return True


async def embed(msg, args):
    return True


async def react(msg, args):
    await msg.add_reaction('👌')
    await msg.add_reaction('👋')
    await msg.add_reaction('🍌')
    await msg.add_reaction('👿')
    await msg.add_reaction('🐧')
    # TODO: show custom emoji querying for next week
    return False # did this for effect :)


# https://discordpy.readthedocs.io/en/latest/api.html#discord.Member.add_roles
async def roles(msg, args):
    return True


#################################
### Save these for the future ###
#################################


async def listeners(msg, args):
    return True


# https://discordpy.readthedocs.io/en/latest/api.html#invite
async def sendInvite(msg, args):
    return True


# https://discordpy.readthedocs.io/en/latest/api.html#attachment
async def sendAttachment(msg, args):
    return True


# https://discordpy.readthedocs.io/en/latest/api.html#voice
async def playMusic(msg, args):
    return True


async def kick(msg, args):
    return True


async def ban(msg, args):
    return True


commandsList = {
    'ping': ping,  # Pong!
    'uptime': uptime,  # tells you the bot's uptime
    'failed': failed, # Used to test the command system
    'dm': dm,  # sends you a DM
    'embed': embed,  # sends you an "embed"
    'react': react,  # reacts to your message
    'roles': roles,  # list roles, add role, remove role
}
client.run(config.token)
