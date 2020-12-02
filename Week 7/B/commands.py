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


async def roles(msg, args):
    return True
