import discord
from discord.ext import commands
import asyncio
import config

bot = commands.Bot(command_prefix='?')

async def annoy():
	chan = bot.get_channel(config.channel_to_send)
	await chan.send('<@!{}>'.format(config.user_to_ping))
	await asyncio.sleep(5)

@bot.event
async def on_ready():
	count = 0
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	while 1 == 1:
		count = count + 1
		if count%10 == 0:
			print(count)
		task = await asyncio.create_task(annoy())

bot.run(config.bot_token)