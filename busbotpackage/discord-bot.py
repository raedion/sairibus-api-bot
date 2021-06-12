import discord
import busbotpackage
client = discord.Client()

@client.event
async def on_message(message):
	if message.author.bot:
		return
	if message.content == "/bus":
		await message.channel.send(busbotpackage.loadTime())

client.run("ここにトークンを入力してください")
