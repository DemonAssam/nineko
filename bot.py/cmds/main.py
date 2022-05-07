import discord
from discord.ext import commands
from core.classes import Cog_Extention
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class main(Cog_Extention):

    @commands.command()
    async def DD(self, ctx):
        random_DD = random.choice(jdata['pic'])
        pic = discord.File(random_DD)
        await ctx.send(file= pic)

    @commands.command()
    async def ts1(self, ctx):
        embed=discord.Embed(title="Vtuber生態箱", url="https://www.youtube.com/channel/UCLDgwPRyFiZVtU__ERL7yCA", description="烤肉manYT", color=0xffffff)
        embed.set_thumbnail(url="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/84246343_108688477396159_6363726654480580608_n.png?_nc_cat=108&_nc_sid=09cbfe&_nc_ohc=OMlqjUpd3U8AX-ICOYA&_nc_ht=scontent-tpe1-1.xx&oh=efc1f78f610a6c1b53c0f47c1451b800&oe=5EE79B18")
        embed.add_field(name="YT", value="https://www.youtube.com/channel/UCLDgwPRyFiZVtU__ERL7yCA", inline=False)
        embed.add_field(name="FB粉專", value="https://www.facebook.com/VtuberEcologyBox/?modal=admin_todo_tour", inline=False)
        embed.add_field(name="推特", value="https://twitter.com/YangHoward0616", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def ts2(self, ctx):
        embed=discord.Embed(title="凍立方", url="https://www.youtube.com/channel/UCpavoZlurKAvIO8xWrL0TEg", description="烤肉manYT", color=0x00ffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/709398691198402581/711614014559617084/image0.jpg")
        embed.add_field(name="YT", value="https://www.youtube.com/channel/UCpavoZlurKAvIO8xWrL0TEg", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(main(bot))