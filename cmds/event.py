import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel.id == 511376568451334157:
            if len(str(msg.content)) == 6 and msg.content.isdigit():
                await msg.channel.send(f'https://nhentai.net/g/{msg.content}')
            elif len(str(msg.content)) == 5 and msg.content.isdigit():
                await msg.channel.send(f'https://www.wancg.com/photos-index-aid-{msg.content}.html')
            else:
                pass


def setup(bot):
    bot.add_cog(Event(bot))