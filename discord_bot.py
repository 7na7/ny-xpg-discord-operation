#!/usr/bin/env python
import discord
import config
import subprocess
import re
import requests
import json
import manage_kvm

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Bot起動時に呼び出される関数
@client.event
async def on_ready():
    channel = client.get_channel(int(config.CHANNEL_ID))
    await channel.send('Bot is ready!')

# メッセージの検知
@client.event
async def on_message(message):
    # 自身が送信したメッセージには反応しない
    if message.author == client.user:
        return

    if client.user in message.mentions and '/virsh list' in message.content:
        await message.channel.send(embed=manage_kvm.get_status(client))

    if client.user in message.mentions and '/neko' in message.content:
        await message.channel.send('にゃーん')

    if client.user in message.mentions and '/inu' in message.content:
        await message.channel.send('わんわん')

# Bot起動
client.run(config.DISCORD_TOKEN)
