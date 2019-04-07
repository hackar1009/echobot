import discord
from discord.ext import commands
import random
import asyncio

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
	await ctx.send("@everyone", embed=embed)
	
bot.run('NTY0Mjg0NTU2NTM5MTk5NDg4.XKlpCw.YE-TkbMjAPdt-I0XCLxJ0kPvLvM')
