print(" $ Run python file")

import discord
from discord.ext import commands
from config import *
import os
import requests

print(" $ Import lib")


client = commands.Bot(command_prefix = prefix)
client.remove_command('help')


@client.event
async def on_ready():
	print(' $ Bot in system')
	await client.change_presence(status = discord.Status.online, activity = discord.Game('$get_help'))


@client.event
async def on_member_join(member):
	print(f'{member} join to server')


@client.event
async def on_member_remove(member):
	print(f'{member} has left a server')

@client.event
async def on_command_error(ctx, error):
	pass


@client.command(pass_context = True)
async def get_help(ctx):
	help_user_bar = discord.Embed(title = "User Commands")
	help_user_bar.add_field(name = f'{prefix}get_help', value = 'Список команд користувача')
	help_user_bar.add_field(name = f'{prefix}get_info', value = 'Інформація про бота')
	help_user_bar.add_field(name = f'{prefix}get_ping', value = 'Пінг користувача')

	await ctx.send(embed = help_user_bar)


@client.command(pass_context = True)
async def get_info(ctx):
	await ctx.send(f"Bot Name: {bot_name}\nVersion: {version}")


@client.command(pass_context = True)
async def get_ping(ctx):
	await ctx.send(f"You has ping: {round(client.latency * 1000)}")


@client.command( pass_context = True )
@commands.has_permissions(administrator = True)
async def get_admin_help(ctx):
	help_admin_bar = discord.Embed(title = "Admin Commands")
	help_admin_bar.add_field(name = f'{prefix}clear', value = 'Очищення чату')
	await ctx.author.send( embed = help_admin_bar)


@client.command( pass_context = True )
@commands.has_permissions(administrator = True)
async def clear(ctx, amount = 100):
	await ctx.channel.purge( limit = amount)

@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.name}, для коректної роботи цієї команди потрібно вводити аргумент')
	if isinstance(error, commands.MissingPermissions):
		pass
	if isinstance(error, commands.CommandNotFound):
		pass
# Run bot
client.run(os.environ['DISCORD_KEY'])
