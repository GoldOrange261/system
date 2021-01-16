import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)


class Achi(Cog_Extension):
    @commands.command()
    @commands.has_permissions(administrator= True)
    async def achi(self, ctx, name: discord.Member, role: discord.Role):
        await ctx.message.delete()
        accRL = [719582059495948318, 715503723652186184, 722282493675307081, 719582909350150184, 719580193915797624, 719588995700359258, 719589865666117688, 719590751763431525, 719690680875745351, 719692250057015317, 687648945367023669, 687650705309171766, 722039532563857439, 700860403483410473, 701445458467487764, 699919673600508045, 695808765341073448, 699026573948616784, 687687472024649775, 719246325677555783, 769940465491378176, 771339354383450122, 771240084971192351, 773395001303891978, 780370886460178432, 
        780365382510837760, 779732521863872522, 781328450442100766, 781740048185163818, 795323407339618354]
        blRL = [769940465491378176, 771339354383450122, 771240084971192351, 773395001303891978, 779732521863872522, 781328450442100766, 781740048185163818, 795323407339618354]
        isbeyond_limit_role = False
        if not(role.id in accRL):
            embed=discord.Embed(title="ERROR", color=0xff0000)
            embed.add_field(name="NOT Achievement", value=f"{role.mention}", inline=False)
            await ctx.send(embed=embed)
            return

        if role.id in blRL:
            isbeyond_limit_role = True

        await name.add_roles(role)
        n = name.nick
        if n == None:
            n = name

        if isbeyond_limit_role:
            embed=discord.Embed(title="INCREDIBLE!!!", color=role.color)
            embed.add_field(name=str(n) + "已達成超限成就", value=f"{role.mention}", inline=False)
        else:
            embed=discord.Embed(title="Congratulations", color=role.color)
            embed.add_field(name=str(n) + "已達成成就", value=f"{role.mention}", inline=False)
        # embed.set_footer(text="使用.cmd來查詢你想了解的指令")
        await ctx.send(embed=embed)    

    @commands.command()
    @commands.has_permissions(administrator= True)
    async def chal(self, ctx, name: discord.Member, role: discord.Role):
        await ctx.message.delete()
        drole = None
        guild = self.bot.get_guild(509693135539142658)
        if role.id == 726341982477221919:
            drole = None
        elif role.id == 726342384237150249:
            drole = guild.get_role(726341982477221919)
        elif role.id == 726342515862536283:
            drole = guild.get_role(726342384237150249)
        elif role.id == 726342705160126505:
            drole = guild.get_role(726342515862536283)
        elif role.id == 726342886475694101:
            drole = guild.get_role(726342705160126505)
        elif role.id == 726343073054982244:
            drole = guild.get_role(726342886475694101)
        elif role.id == 726343182031519774:
            drole = guild.get_role(726343073054982244)
        elif role.id == 726343273014100008:
            drole = guild.get_role(726343182031519774)
        else:
            embed=discord.Embed(title="ERROR", color=0xff0000)
            embed.add_field(name="NOT Challange", value=f"{role.mention}", inline=False)
            await ctx.send(embed=embed)
            return

        if drole != None:
            await name.remove_roles(drole)
        await name.add_roles(role)
        n = name.nick
        if n == None:
            n = name
        embed=discord.Embed(title="Congratulations", color=role.color)
        embed.add_field(name=str(n) + "已達成挑戰", value=f"{role.mention}", inline=False)
        embed.set_footer(text="往更難的挑戰邁進吧!!")
        await ctx.send(embed=embed) 

    @commands.command()
    @commands.has_permissions(administrator= True)
    async def fini(self, ctx, name: discord.Member, role: discord.Role):
        await ctx.message.delete()
        # guild = commands.get_guild(509693135539142658)
        accRL = [743128723913441371, 743129417127034982, 743131123751714887, 743130224014655671, 743221018792820786, 743221162732945488, 743221308925542451, 743223094218457098]
        if not(role.id in accRL):
            embed=discord.Embed(title="ERROR", color=0xff0000)
            embed.add_field(name="NOT Challange", value=f"{role.mention}", inline=False)
            await ctx.send(embed=embed)
            return

        await name.add_roles(role)
        n = name.nick
        if n == None:
            n = name
        embed=discord.Embed(title="INCREDIBLE!!!", color=role.color)
        embed.add_field(name=str(n) + "已通過試煉", value=f"{role.mention}", inline=False)
        embed.set_footer(text="打敗了桔喵，您是神仙吧？！")
        await ctx.send(embed=embed)  


def setup(bot):
	bot.add_cog(Achi(bot))
