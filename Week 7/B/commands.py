async def help(msg, args):
    # Return an embed
    return True


async def ping(msg, args):
    await msg.channel.send('Pong!')
    return True


async def uptime(msg, args):
    return True


async def dm(msg, args):
    return True


async def embed(msg, args):
    return True


async def react(msg, args):
    return True


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
