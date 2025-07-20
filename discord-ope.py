#!/usr/bin/env python
import discord
import config
import subprocess
import re
import requests
import json
import sys

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Bot起動時に呼び出される関数
@client.event
async def on_ready():
    # print("Ready!")
    # print(config.CHANNEL_ID)
    channel = client.get_channel(int(config.CHANNEL_ID))
    # print(channel)
    await channel.send('Bot is ready!')

# VPNログ監視
# @client.event
# async def logging():
#     cmd = "sudo tail -f /usr/local/vpnserver/server_log/vpn_$(date '+%Y%m%d').log"
#     log = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True).communicate()[0]
#     pattern = '仮想 HUB がオンラインになりました。'
#     while True:
#         line = log.stdout.readline()
#         if line:
#             print(line)
#             online = pattern.search(log).group(0).decode()
#             print(online)
#             await channel.send(online)
#         if not line and log.poll() is not None:
#             break

# メッセージの検知
@client.event
async def on_message(message):
    # 自身が送信したメッセージには反応しない
    if message.author == client.user:
        return
    embed = discord.Embed(
            title="Example Embed",
            color=0x00ff00,
            description="Example Embed for NY-XPG-VPNS Admin"
            # url=""
            )
    embed.set_author(name=client.user)
    embed.add_field(name="フィールド1",value="値1")
    embed.add_field(name="フィールド2",value="値2")
    embed.set_footer(text="Discord bot by NY-XPG Admin")

    if client.user in message.mentions and '/example' in message.content:
        await message.channel.send(embed=embed)
    if client.user in message.mentions and '/neko' in message.content:
        await message.channel.send('にゃーん')
    if client.user in message.mentions and '/inu' in message.content:
        await message.channel.send('わんわん')

# Bot起動
client.run(config.DISCORD_TOKEN)
