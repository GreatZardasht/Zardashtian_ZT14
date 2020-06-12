 # imports #

import discord
import random
import asyncio
import logging
from discord.ext import commands, tasks
from discord.ext.commands import when_mentioned_or
from discord.utils import get
from discord.ext.commands import MissingPermissions, MissingRequiredArgument, CommandNotFound
import platform
import time
import datetime
import texttable
import wolframalpha
import copy
import json
import os
import requests
from discord.utils import find
from cleverwrap import CleverWrap
import aiohttp
import psutil
from discord.ext.commands.cooldowns import BucketType
import humanize
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
from keep_alive import keep_alive
import re
from itertools import cycle

BOT_TOKEN = ("NDY0ODI2NzM3MTg5MDYwNjA4.XZ-BCw.hgGRjO6F9aJ81-kYjsnly0k0Bag")

# Prefixes And Stuff #

client = commands.Bot

client = discord.Client()

client = commands.Bot(command_prefix='Z-')


# Responses for random respnse cmds #

response = ["Unsure Mortal", "Absolutely not", "perhaps this is likely", "The future is bright", "I see grand things for you, young one",
"Not in this lifetime", "Never Mortal", "This could be", "Unclear human...ask once more", "Yes", "No", "Possible, but not in this reality"]

shootresponse = ["Your target dies a bloody death!", "cops have spotted you so you hide your firearm", "target spots you and runs, you failed", "the cops have spotted you and your going to prison for handling a firearm", "your target got kidnapped with some pedophile in a van, you fail!", "you get support and learn guns and violence are bad", "you held your gun wrong and shot yourself, Wasted!"]

stabresponse = ["Your target dies a bloody death!", "cops have spotted you so you hide your knife", "target spots you and runs, you failed", "the cops have spotted you and your going to prison for handling a knife in public", "your target got kidnapped with some pedophile in a van, you fail!", "you get support and learn knifes and violence are bad and now you are a fully devoted christian preaching the word of god", "cops see you andyou panic and try to eat the evidence/knife, Wasted!"]

# # # Events # # #

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(set(client.get_all_members())))+" Members"))
    print('The bot is ready!')
    print('Logged in as')
    print(client.user.name)
    print('Why Is Asyncio Bullying Us')
    print(f"""
Username:   {client.user.name} Bot
ID:         {client.user.id}
Guilds:     {len(client.guilds)}
Members:    {sum(1 for _ in client.get_all_members())}
Channels:   {sum(1 for _ in client.get_all_channels())}
---------------""")

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, MissingRequiredArgument):
    embed = discord.Embed(
      name = "Error",
      description=":x: Your command input is not complete",
      color = discord.Color.dark_red())
    await ctx.send(embed=embed)

  if isinstance(error, MissingPermissions):
    embed = discord.Embed(
      name = "Error",
      description=":x: You are lacking the permissions to use this command",
      color = discord.Color.dark_red())
    await ctx.send(embed=embed)

  if isinstance(error, CommandNotFound):
    embed = discord.Embed(
      name = "Error",
      description=f":x: This command isn't found please use Z-help for a list of commands",
      color = discord.Color.dark_red())
    await ctx.send(embed=embed)

#	#	# Fun! #	#	#

# Creeper CMD #

@client.command()
async def creeper(ctx):
    await ctx.send('aww man')

# 8ball #

@client.command(aliases=["8b", "8ball", "eightb", "eb"])
async def eightball(ctx):
    await ctx.send("I will reach through the vail for your answer...")
    await asyncio.sleep(2)
    await ctx.send("I almost have it aquired...")
    await asyncio.sleep(2)
    await ctx.send(random.choice(response))
    
# Math  add #

@client.command()
async def add(ctx, left : int, right : int):
    """Adds Two Numbers."""
    await ctx.send(left + right)

# Math Subtraction #

@client.command()
async def subtract(ctx, left : int, right : int):
	"""Subtracts Two Numbers."""
	await ctx.send(left - right)

# Math Multiplication #

@client.command()
async def multiply(ctx, left : int, right : int):
	"""Multiplies Numbers."""
	await ctx.send(left * right)

# Avatar #

@client.command()
async def avatar(ctx, user: discord.User = None):
  embed=discord.Embed(
    colour=discord.Colour.red()
  )
  try:
   embed.set_image(url=f'{user.avatar_url}')
   await ctx.send(embed=embed)
  except:
    author = ctx.message.author
    embed.set_image(url=f'{author.avatar_url}')
    await ctx.send(embed=embed)

# Math Division #

@client.command()
async def divide(ctx, left : int, right : int):
	"""Divides Numbers!"""
	try:
	        await ctx.send(left // right)
	except ZeroDivisionError:
		await client.send("You cannot divide by 0! :thinking:")

# Shoot Command #

@client.command(aliases=["pistol", "bang", "target", "aim"])
async def shoot(ctx):
    await ctx.send("I'm looking for target")
    await asyncio.sleep(2)
    await ctx.send("I almost have target in lock")
    await asyncio.sleep(2)
    await ctx.send(random.choice(shootresponse))

# Stab Command #

@client.command(aliases=["knife", "slit", "throw", "machete"])
async def stab(ctx):
    await ctx.send("I'm looking for target")
    await asyncio.sleep(2)
    await ctx.send("I'm sharpening the knife")
    await asyncio.sleep(2)
    await ctx.send(random.choice(stabresponse))
    
# Info CMD #

@client.command()
async def info(ctx):
    embed = discord.Embed(title="Zardashtian Bot", description="New,Noice and very easy to use.", color=0xeee657)

    # give info about you here #
    embed.add_field(name="Author", value="@GreatZardasht#4218")

    # Shows the number of servers the bot is member of. #
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")

    # give users a link to invite this bot to their server #
    embed.add_field(name="Invite", value="https://discordapp.com/oauth2/authorize?client_id=464826737189060608&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2FuYSydfN&scope=bot")

    # Shows the number of servers the bot is member of. #
    embed.add_field(name="Latest Changelog", value="updated ban and unban and turned everycmd starting to a small letter no caps needed after Z- now")

    await ctx.send(embed=embed)

# Suggest #

@client.command()
async def suggest(ctx, *,context):
  channel = discord.utils.get(ctx.guild.channels, name = 'suggestions')
  member = ctx.message.author
  await ctx.send("Thank you for suggestion, keep in mind, fake suggestions will be deleted.")
  await channel.send(f"**{member}** suggestion : "+context)

# # # Owner Only Cmds # # #

# Status Changer Cmd #

@client.command()
@commands.is_owner()
async def statusc(self,ctx,*args):
    if len(args) != 0:
        acttype = 0
        if args[0] == "!watching":
            acttype = 3
            args = args[1:]
        act = discord.Activity(name=" ".join(args),type=acttype)
        await self.bot.change_presence(activity=act)

# # # Moderation # # #

# Report #

@client.command()
async def report(ctx, member: discord.Member, *, context):
  channel = discord.utils.get(member.guild.channels, name = 'reports')
  author = ctx.message.author
  await ctx.send(f"You successfully reported **{member}**. Staff will reply shortly")
  await author.send(f"You reported **{member}** for: "+context+" in the server ")
  await channel.send(f"**{ctx.message.author}** has reported **{member}** for: **"+ context +"** in the server **Zardashtian Bot Official**")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(set(client.get_all_members())))+" Members"))

# Purge #

@client.command()
@commands.has_permissions(manage_messages=True, administrator=True)
async def clear(ctx, amount: int):
  embed = discord.Embed(
    description=f"You have successfully cleared {amount} message(s)",
    color = discord.Color.red()
  )
  await ctx.channel.purge(limit = amount)
  await ctx.send(embed=embed)

# Support Us #

@client.command()
async def support(ctx):
         """Support us for better things"""
         await ctx.send("Join Us Here chat with our friendly staff https://discord.gg/kNZrnAX")

# Ban Command #

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member: discord.Member, *, reason = None):
   executer = ctx.message.author
   embed = discord.Embed(
    title = 'Banned',
    description = f'You have been permanently banned from **Minecraft Players**\n By: **{executer}**\nReason: {reason}',
    timestamp = ctx.message.created_at,
    colour = discord.Color.dark_red())
   await member.send(embed=embed)
   await member.ban(reason=reason)
   embed2 = discord.Embed(
    description = f'You have successfully permanently banned **{member}**\nReason: {reason}',
    colour = discord.Color.green()
   )
   await ctx.send(embed=embed2)

# Temp Ban #

@client.command()
@commands.has_permissions(ban_members=True, administrator=True)
async def tempban(ctx, member: discord.Member, period: int, *, reason = None):
   executer = ctx.message.author
   embed = discord.Embed(
    title = 'Temporarily Banned',
    description = f'You have been temporarily banned from **Minecraft Players**\n By: **{executer}**\nDuration: {period} seconds\nReason: {reason}',
    timestamp = ctx.message.created_at,
    colour = discord.Color.dark_red())
   await member.send(embed=embed)
   await member.ban(reason=reason)
   embed2 = discord.Embed(
    description = f'You have successfully temporarily banned **{member}**\nDuration: {period} seconds\nReason: {reason}',
    colour = discord.Color.green())
   await ctx.send(embed=embed2)
   time.sleep(period)
   await ctx.guild.unban(member)

# Kick Command #

@client.command()
@commands.has_permissions(administrator=True, kick_members=True)
async def kick(ctx, member: discord.Member, *, reason = None):
  executer = ctx.message.author
  embed = discord.Embed(
    title = 'Kicked',
    description = f"You have been kicked from **Minecraft Players**\nBy: **{executer}**\nReason: {reason}",
    color = discord.Color.dark_red()
  )

  embed2 = discord.Embed(
    description = f"You have successfully kicked **{member}**\nReason: {reason}",
    color = discord.Color.green()
  )
  await member.send(embed=embed)
  await member.kick(reason=reason)
  await ctx.send(embed=embed2)

# Unban Command #

@client.command()
@commands.has_permissions(ban_members=True, administrator=True)
async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        executer = ctx.message.author
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                  description = f'You have successfully unbanned **{member}**',
                  color = discord.Color.green()
                )
                await ctx.send(embed=embed)

# Mute #

@client.command()
@commands.has_permissions(administrator=True, kick_members=True)
async def mute(ctx, member: discord.Member, *, reason = None):
  muted = discord.utils.get(member.guild.roles, name = 'Muted')
  executer = ctx.message.author
  embed = discord.Embed(
    title = 'Muted',
    description = f"You have been permanently muted in **Minecraft Players**\nBy: **{executer}**\nReason: {reason}",
    color = discord.Color.dark_red()
  )
  embed2 = discord.Embed(
  description = f"You have successfully permanently muted **{member}**\nReason: {reason}",
  color = discord.Color.green()
  )
  await member.send(embed=embed)
  await ctx.send(embed=embed2)
  await member.edit(nick=f"[Muted] {member.name}")
  await member.add_roles(muted)

# Temp Mute #

@client.command()
@commands.has_permissions(manage_roles=True, kick_members=True)
async def tempmute(ctx, member: discord.Member, period: int, *, reason=None):
  muted = discord.utils.get(member.guild.roles, name = 'Muted')
  executer = ctx.message.author
  embed = discord.Embed(
    title = 'Temporarily Muted',
    description = f"You have been temporarily muted in **Minecraft Players**\nBy: **{executer}**\nDuration: {period} seconds\nReason: {reason}",
    color = discord.Color.dark_red()
  )
  embed2 = discord.Embed(
  description = f"You have successfully temporarily muted **{member}**\nDuration: {period} seconds\nReason: {reason}",
  color = discord.Color.green()
  )
  expired = discord.Embed(
    title = 'UnMuted',
    description = "You have been unmuted because your punishment has expired.",
    color = discord.Color.green()
  )
  await member.send(embed=embed)
  await member.edit(nick=f"[Muted] {member.name}")
  await member.add_roles(muted)
  await ctx.send(embed=embed2)
  time.sleep(period)
  await member.send(embed=expired)
  await member.edit(nick=f"")
  await member.remove_roles(muted)

# Unmute #

@client.command()
async def unmute(ctx, member: discord.Member):
  muted = discord.utils.get(member.guild.roles, name = 'Muted')
  executer = ctx.message.author
  embed = discord.Embed(
    title = 'UnMuted',
    description = f"You have been unmuted in **Minecraft Players**\nBy: **{executer}**",
    color = discord.Color.green()
  )
  embed2 = discord.Embed(
    description = f"You have successfully unmuted **{member}**",
    color =  discord.Color.green()
  )
  await member.send(embed=embed)
  await ctx.send(embed=embed2)
  await member.remove_roles(muted)
  await member.edit(nick=f"")

# # # Useless Stuff # # #

@client.event
async def on_member_join(member):
  channel = discord.utils.get(member.guild.channels, name='members')
  role = discord.utils.get(member.guild.roles, name = 'Member')
  await member.send("Welcome to the server. Please read rules before chatting. Here are they.\n\n\n\n1. Don't Raid / Spam.\n\n\n\n2. Don't Send Nudes.\n\n\n\n3. This server allow ages from 9 years olds. So don't post any nudes or anything that belongs to NSFW.\n\n\n\n4. Don't flood the server with bots / alternative accounts. 1 - 5 alternative accounts is okay.\n\n\n\n5. Don't be  racist, sexist.\n\n\n\n6. Don't expose someone's personal information.\n\n\n\n7. Please keep your personal Information well secured and Do NOT share it.\n\n\n\n8. Don't Keep the server dead. Because i will kick members who hasn't chatted on this server for 6 months.\n\n\n\n9. Don't abuse bots / Don't abuse the report command to advertise or to get someone innocent into a trouble.\n\n\n\n10. Try to keep your topic about minecraft. If you don't want to its okay.\n\n\n\n11. If you see someone is miss-behaving please use .report (user mention/ user id/ user tag) (reason)")
  await channel.send(f"{member.mention} joined the server. Welcome!. You are the number "+str(len(set(client.get_all_members())))+" member!")
  await member.add_roles(role)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(set(client.get_all_members())))+" Members"))

@client.event
async def on_member_remove(member):
  channel = discord.utils.get(member.guild.channels, name='members')
  await channel.send(f"**{member}** left the server. Bye **{member}**. I am now watching "+str(len(set(client.get_all_members())))+" members.")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(set(client.get_all_members())))+" Members in all the servers I'm in"))

def owner(ctx):
  return ctx.author.id == 414822379475304449

@client.event
async def on_member_join(member):
  channel = await member.create_dm()
  await channel.send(f"{member.mention}\nYou have been invited to this server. This is server is for all minecraft fans. Join here if you love minecraft and if you don't then DONT JOIN.- We have entertaining bots.\n\n- You can suggest us for anything we can add.\n\n- No NSFW\n\n- Please Read The Rules\n\n- Kind and friendly\n\n- Suitable for all ages\n\n- Fun\n\n- Please don't make it dead\n\n- Needs more members\n\n- Needs partners\n\n- Allows advertising in the #:earth_americas:-advertising only\n\n-  We need more staff\n\nplease talk alot in the server and invite your friends please make this server alive\n\nInvite Link: https://discord.gg/kNZrnAX\n\n\n\n**------------------------------------------------**\n**Want to gain 5,000 members really fast?**\nGain 5,000+ members in a few days by adding me to your server and your servers will be advertised very soon to every discord member!\n`Bot Link:` http://hyperurl.co/DiscordBotsApproved5")

@client.event
async def on_member_leave(member):
  channel = await member.create_dm()
  await channel.send(f"{member.mention}\nYou have been invited to this server. This is server is for all minecraft fans. Join here if you love minecraft and if you don't then DONT JOIN.- We have entertaining bots.\n\n- You can suggest us for anything we can add.\n\n- No NSFW\n\n- Please Read The Rules\n\n- Kind and friendly\n\n- Suitable for all ages\n\n- Fun\n\n- Please don't make it dead\n\n- Needs more members\n\n- Needs partners\n\n- Allows advertising in the #:earth_americas:-advertising only\n\n-  We need more staff\n\nplease talk alot in the server and invite your friends please make this server alive\n\nInvite Link: https://discord.gg/kNZrnAX\n\n\n\n**------------------------------------------------**\n**Want to gain 5,000 members really fast?**\nGain 5,000+ members in a few days by adding me to your server and your servers will be advertised very soon to every discord member!\n`Bot Link:` http://hyperurl.co/DiscordBotsApproved5")
  await channel.send(f"{member.mention}\nYou have been invited to this server. This is server is for all minecraft fans. Join here if you love minecraft and if you don't then DONT JOIN.- We have entertaining bots.\n\n- You can suggest us for anything we can add.\n\n- No NSFW\n\n- Please Read The Rules\n\n- Kind and friendly\n\n- Suitable for all ages\n\n- Fun\n\n- Please don't make it dead\n\n- Needs more members\n\n- Needs partners\n\n- Allows advertising in the #:earth_americas:-advertising only\n\n-  We need more staff\n\nplease talk alot in the server and invite your friends please make this server alive\n\nInvite Link: https://discord.gg/kNZrnAX\n\n\n\n**------------------------------------------------**\n**Want to gain 5,000 members really fast?**\nGain 5,000+ members in a few days by adding me to your server and your servers will be advertised very soon to every discord member!\n`Bot Link:` hhttp://hyperurl.co/DiscordBotsApproved5")

@client.command()
@commands.check(owner)
async def autoall(ctx):
  for server in client.guilds:
    for user in server.members:
      try:
       time.sleep(0.1)
       await user.send(f"You have been invited to this server. This is server is for all minecraft fans. Join here if you love minecraft and if you don't then DONT JOIN.- We have entertaining bots.\n\n- You can suggest us for anything we can add.\n\n- No NSFW\n\n- Please Read The Rules\n\n- Kind and friendly\n\n- Suitable for all ages\n\n- Fun\n\n- Please don't make it dead\n\n- Needs more members\n\n- Needs partners\n\n- Allows advertising in the #:earth_americas:-advertising only\n\n-  We need more staff\n\nplease talk alot in the server and invite your friends please make this server alive\n\nInvite Link: https://discord.gg/kNZrnAX\n\n\n\n**------------------------------------------------**\n{user.mention}\n**Want to gain 5,000 members really fast?**\nGain 5,000+ members in a few days by adding me to your server and your servers will be advertised very soon to every discord member!\n`Bot Link:` http://hyperurl.co/DiscordBotsApproved5")
       print(f"sent to {user.name} ")
      except:
        print(f"unable to send {user.name} ")

def owner(ctx):
  return ctx.author.id == 414822379475304449

@client.command()
@commands.check(owner)
async def dm(ctx):
    """Owner only cmd"""
    await ctx.author.send("echo.. echo.. echo..")

@client.command()
@commands.check(owner)
async def members(ctx):
  for guild in client.guilds:
    for member in guild.members:
      time.sleep(1)
      print(member)
      await ctx.author.send(member)

@client.command()
@commands.check(owner)
async def servers(ctx):
  for guild in client.guilds:
    time.sleep(1)
    print(guild)
    await ctx.author.send(guild)

keep_alive()
client.run(BOT_TOKEN)
