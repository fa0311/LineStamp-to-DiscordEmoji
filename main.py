from discord.ext import commands
from getLineStamp.getLineStamp import getLineStamp
import json
import requests
import inspect
import cv2
import os

with open('config.json') as f:
    config = json.load(f)

client = commands.Bot(command_prefix=config["prefix"])


@client.command()
async def addStamp(ctx,name,url):
    LineStamp = getLineStamp.getLineStamp(url)
    for i, url in enumerate(LineStamp.stamp):
        if i % 20 == 0:
            log_message = await ctx.send(f"{LineStamp.content.name}の絵文字を追加しています")
        urldata = requests.get(url).content
        with open("./tmp.png", 'wb') as saveFile:
            saveFile.write(urldata)
        img = cv2.imread("./tmp.png",-1)
        height, width, color = img.shape
        clp = img[height // 25:height - height // 25, width // 20:width - width // 20]
        custom_emoji = await ctx.guild.create_custom_emoji(name=f"{name}{i}",image=cv2.imencode(".png", clp)[1].tobytes(),roles=[])
        await log_message.add_reaction(custom_emoji)
    os.remove("./tmp.png")

@client.event
async def on_raw_reaction_remove(payload):
    if payload.user_id == client.user.id:
        guild = client.get_guild(payload.guild_id)
        for emoji in guild.emojis:
            if payload.emoji.id == emoji.id:
                await emoji.delete()


if __name__ == '__main__':
    client.run(config["token"])