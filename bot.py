import discord
from discord.ext import commands
import asyncio
import requests
import os

description = '''EchoBot by EchoNoahGaming'''
bot = commands.Bot(command_prefix='-', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
	
@bot.command()
async def announcement(ctx, *, args):
	"""Announcement command!"""
	embed=discord.Embed(title="Announcement", description=args, color=0x7700aa)
	embed.set_footer(text="By EchoNoahGaming")
	await ctx.send("", embed=embed)

async def embed(*):
	"""Input anything, and the bot will say it back in a embed thing."""
	embed=discord.Embed(title="Embed Message", description=args, color=0x7700aa)
	embed.set_footer(text="By EchoNoahGaming")
	await ctx.send("", embed=embed)

client.run(str(os.environ.get('BOT_TOKEN')))
