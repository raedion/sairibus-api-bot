import discord
import busbotpackage
client = discord.Client()

@client.event
async def on_message(message):
	if message.author.bot:
		return
	if message.content.lower().startswith("/bus"):
		cmdList = message.content.split()
		if len(cmdList) > 1:
			await message.channel.send(busbotpackage.loadTime(cmdList[1]))
		else:
			await message.channel.send(busbotpackage.loadTime())
#	elif message.content.lower().startswith("/sairi"):
#		await message.channel.send("なさけねぇな")

client.run("ここにトークンを入力してください")
