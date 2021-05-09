import discord
import os
import random
from stay_online import keep_alive



choice=["rock","paper","scissors"]

client=discord.Client()
@client.event
async def on_ready():
	print('we have logged in as {0.user}'.format(client))
	



@client.event
async def on_message(message):
	if message.author==client.user:
		return

	elif message.content.startswith('$help'):
		await message.channel.send('To play rock paper scissors, use "$" before each option')

	elif message.content.startswith('$goo'):
		await message.channel.send('goo khale')

	elif message.content.startswith('$owner'):
		await message.channel.send('I was created by god of gods: Jalapeño#9587')

	elif message.content.startswith('$rock'):
		ai_choice=random.choice(choice)
		if ai_choice=="rock":
			await message.channel.send("The bot chose rock too. This war ends in a tie")
		elif ai_choice=="paper":
			await message.channel.send("The bot chose paper. You have been defeated by the bot GGEZ NOOB")
		else:
			await message.channel.send("The bot chose scissors. You have defeated the bot GGs")


	elif message.content.startswith('$paper'):
		ai_choice=random.choice(choice)
		if ai_choice=="rock":
			await message.channel.send("The bot chose rock. You have defeated the bot GGs")
		elif ai_choice=="paper":
			await message.channel.send("The bot chose paper. This war ends in a tie")
		else:
			await message.channel.send("The bot chose scissors. You have been defeated by the bot GGEZ NOOB")


	elif message.content.startswith('$scissors'):
		ai_choice=random.choice(choice)
		if ai_choice=="rock":
			await message.channel.send("The bot chose rock. You have been defeated by the bot GGEZ NOOB")
		elif ai_choice=="paper":
			await message.channel.send("The bot chose paper. You have defeated the bot GGs")
		else:
			await message.channel.send("The bot chose scissors. This war ends in a tie")

keep_alive()
client.run(os.getenv('TOKEN'))
	
