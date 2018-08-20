import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    global keep_walking
    if message.content.startswith('!gezdir') and "Admin" in (x.name for x in message.author.roles):
        keep_walking = True
        asyncio.ensure_future(take_a_walk(message))

    if message.content.startswith('!gezdirbitir'):
        keep_walking = False


async def take_a_walk(message):
    global keep_walking
    contents = message.content.split()
    print(contents)
    while keep_walking:
        for channel in message.server.channels:
            if channel.type is discord.enums.ChannelType(2):
                try:
                    await client.move_member(message.server.get_member_named(contents[1]), channel)
                except discord.errors.DiscordException as err:
                    print(err)


with open('bot_token', 'r') as f:
    TOKEN = f.readline().strip()

client.run(TOKEN)