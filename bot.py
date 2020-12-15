import discord
from discord.ext import commands
import json
import random
import os

intents = discord.Intents.all()

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
bot = commands.Bot(command_prefix= 'syscall ', intents = intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('[EXECUTIØN...]'))
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member: discord.Member):
    if member.dm_channel == None:
        await member.create_dm()
    embed=discord.Embed(title=None, color=0x60D1F6)
    embed.set_author(name="由系統發出", icon_url="https://i.imgur.com/DYUdPXX.png")
    embed.set_thumbnail(url="https://i.imgur.com/haluZrL.png")
    embed.add_field(name="**歡迎**", value="*[Loading...]*\n您好，很高興見到您:)\n本機為伺服器的核心系統\n本機將會為你快速了解本伺服器:D\n🔹 <#687676397707067439> 務必閱讀\n🔹 目害就是進步，玻璃，BAD :/\n🔹 想邀請朋友加入，請詢問管理員\n🔹 群主是菜雞，不用懷疑:D\n*[End of File]*", inline=False)
    embed.set_footer(icon_url = 'https://i.imgur.com/zzGOcth.png', text="您不須回覆這則訊息")
    await member.dm_channel.send(embed=embed)

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')

@bot.command()
@commands.is_owner()
async def iswork(ctx):
    await ctx.send("Yes.")

@bot.command()
@commands.is_owner()
async def dm(ctx, member: discord.Member, *, msg):
    await ctx.message.delete()
    if member.dm_channel == None:
        await member.create_dm()
    
    embed=discord.Embed(title=None, color=0x60D1F6)
    embed.set_author(name="由系統發出", icon_url="https://i.imgur.com/DYUdPXX.png")
    embed.set_thumbnail(url="https://i.imgur.com/haluZrL.png")
    embed.add_field(name="**一則私人訊息**", value=f'*[Loading...]*\n{msg}\n*[End of File]*', inline=False)
    embed.set_footer(icon_url = 'https://i.imgur.com/zzGOcth.png', text="請不要直接在此頻道回覆")
    await member.dm_channel.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    embed=discord.Embed(title="ERROR", color=0xff0000)

    if isinstance(error, commands.errors.CommandNotFound):
        return
    elif isinstance(error, commands.errors.NotOwner):
        embed.set_thumbnail(url="https://i.imgur.com/GPIo93l.png")
    else:
        embed.set_thumbnail(url="https://i.imgur.com/g1THUl5.png")

    embed.set_author(name="系統訊息", icon_url="https://i.imgur.com/DYUdPXX.png")    
    embed.add_field(name="*[Error message]*", value=error, inline=False)
    embed.set_footer(icon_url = 'https://i.imgur.com/zzGOcth.png', text="請重試或通知管理員")
    await ctx.send(embed=embed)
         

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])