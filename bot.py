import discord
from discord.ext import commands
import string
import random

client = commands.Bot(command_prefix='$')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('$help - watching you'))
    print('Bot is ready')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msgContainsMii6 = False
    msgContainsDiss = False
    dissResponseList = ["h o w  d a r e  y o u  i n s u l t  m e e 6",
                        "thou shalt respect the bot", "a p o l o g i z e  n o w", "say sorry NOW", "be nicer", "reconsider your language"]
    # split the message up
    wordList = str(message.content).split(sep=' ')
    # check for disses/mee6 references
    for word in wordList:
        if (word == "mee6" or word == "mii6" or word == "mee" or word == "mii" or word == "sadnuts" or word == "m" or word == "nuts"):
            msgContainsMii6 = True
        elif (word == "smell" or word == "kill" or word == "suck" or word == "poo" or word == "poop" or word == "bad" or word == "screw" or word == "stupid" or word == "dumb" or word == "dum" or word == "stoopid" or word == "crappy" or word == "useless" or word == "crap" or word == "idiot" or word == "meany" or word == "annoying" or word == "anoying" or word == "rude"):
            msgContainsDiss = True

    # if a diss and mee6 reference are in the same sentence then trigger
    if(msgContainsMii6 == True and msgContainsDiss == True):
        channel = message.channel
        await channel.send(random.choice(dissResponseList))

    # nice little reference
    if(message.content.startswith('hello there')):
        channel = message.channel
        await channel.send('general kenobi!')

    await client.process_commands(message)


@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)} ms')


@client.command()
async def clear(ctx, amount=5):
    if(amount == 0):
        await ctx.send(f'you can\'t purge zero messages')
    else:
        amount += 1
        await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} was kicked for ' + reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} was banned for ' + reason)


@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    recipient = await author.create_dm()
    embed = discord.Embed(
        color=discord.Colour.orange()
    )
    modembed = discord.Embed(
        color=discord.Colour.red()
    )
    embed.set_author(name='Help')
    embed.add_field(name='ping', value='returns latency in ms', inline=False)
    modembed.set_author(name='Mod Commands')
    modembed.add_field(
        name='clear [number]', value='clears the number of messages given, command doesn\'t count towards the number', inline=False)
    modembed.add_field(name='kick [@mention] [reason]',
                       value='kicks the given user from the server- does not ban. reason not required.', inline=False)
    modembed.add_field(name='ban [@mention] [reason]',
                       value='bans the given user from the server. reason not required', inline=False)
    modembed.add_field(name='unban [username#discriminator]',
                       value='unbans the given user from the server.', inline=False)
    await recipient.send(embed=embed)
    await recipient.send(embed=modembed)


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return


client.run("NzEwNTY4Mzg4MzAwMjQzMDU3.Xr2Wcg.KhCe_hGTHkcpTA-ltwO0qNPLO-4")
