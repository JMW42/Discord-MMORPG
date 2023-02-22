from ast import alias
from modules.cogs import TemplateCog as TemplateCog
from discord.ext import commands
import discord, sys

from config import WORLD as WORLD
##############################################################################################################
##############################################################################################################

class RPG(TemplateCog):
    def __init__(self, bot) -> None:
        global WORLD
        """ Bot Controll Extension """
        TemplateCog.__init__(self, bot)
        self.bot = bot
        self.color_embed = 0x006600

        self.world = WORLD
        

    # --------------------------------------------------------------------------------------------------------
    # COMMANDS:

    @commands.command()
    @commands.is_owner()
    async def rpg(self, ctx):
        """ rpg"""
        await ctx.send("RPG")
        await ctx.send(WORLD.name)

    # --------------------------------------------------------------------------------------------------------


##############################################################################################################
##############################################################################################################

def setup(bot):
    RPG(bot)
    