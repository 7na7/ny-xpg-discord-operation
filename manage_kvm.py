#!/usr/bin/env python
import discord
import subprocess
import re

def get_status(client):
        embedtext = discord.Embed(
            title="VM List",
            color=0x00ff00,
            description="NY-XPG Virtual Machines info"
        )
        embedtext.set_author(name=client.user)
        embedtext.add_field(name="Hostname",value="NY-XPG-DNSCACHE",inline=False)
        embedtext.set_footer(text="Discord bot by NY-XPG Admin")
        return embedtext

def kvm_control():
    return 0
