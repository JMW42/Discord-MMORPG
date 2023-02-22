from ast import alias
from modules.cogs import TemplateCog as TemplateCog
from discord.ext import commands
import discord, sys

##############################################################################################################
##############################################################################################################

class BotControll(TemplateCog):
    def __init__(self, bot) -> None:
        """ Bot Controll Extension """
        TemplateCog.__init__(self, bot)
        self.bot = bot
        self.color_embed = 0x000066
        

    # --------------------------------------------------------------------------------------------------------
    # COMMANDS:

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def extension(self, ctx, subcommand:str, extension:str=""):
        """ Managing all extensions, aviable subcommands: load, unload, reload, list"""

        embed = discord.Embed(title="Extensions", url=self.embed_author_url, description="\t", color=self.color_embed)
        embed.set_author(name=type(self).__name__ , url=self.embed_title_url, icon_url=self.author_icon_url)
        embed.set_thumbnail(url=self.thumbnail_icon_url)
        embed.set_footer(text=f"Command requested by {ctx.author.display_name}")

        if(subcommand=="list"):
            embed.title="Extensions"
            for p in  self.bot.extensions:
                embed.add_field(name=f"{p}", value=self.bot.cogs[p].__doc__, inline=False)
            
        elif(subcommand == "load"):
            self.bot.load_extension(f"{extension}")
        
        elif(subcommand == "unload"):
            self.bot.unload_extension(f"{extension}")

        elif(subcommand == "reload"):
            self.bot.reload_extension(f"{extension}")
            

        if(subcommand!="list"):
            print(f"{subcommand}ing {extension}")
            embed.description = f'{extension} successfully {subcommand}ed'

        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def cog(self, ctx, subcommand:str, cog:str=""):
        """ Managing all command modules"""
        #await self.list(ctx)
        embed = discord.Embed(title="Cogs", url=self.embed_author_url, description="\t", color=self.color_embed)
        embed.set_author(name=type(self).__name__ , url=self.embed_title_url, icon_url=self.author_icon_url)
        embed.set_thumbnail(url=self.thumbnail_icon_url)
        embed.set_footer(text=f"Command requested by {ctx.author.display_name}")

        if (subcommand == "list"):
            for p in  self.bot.cogs:
                embed.add_field(name=f"{p}", value=self.bot.cogs[p].__doc__, inline=False)

        elif(subcommand == "load"):
            self.bot.load_extension(f"cogs.{cog}")

        elif(subcommand == "reload"):
            self.bot.reload_extension(f"cogs.{cog}")

        elif(subcommand == "unload"):
            self.bot.unload_extension(f"cogs.{cog}")


        if (subcommand != "list"):
            print(f"{subcommand}ing cog: {cog}")
            embed.description=f'{cog} successfully {subcommand}ed'

        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.is_owner()
    async def prefix(self, ctx, prefix:str):
        """ setting the prefix globally"""
        print("setting prefix:", prefix)
        self.bot.command_prefix = prefix

        embed = discord.Embed(title="Prefix", url=self.embed_author_url, description=f"prefix has been succesfully set to: **{prefix}**", color=self.color_embed)
        embed.set_author(name=type(self).__name__ , url=self.embed_title_url, icon_url=self.author_icon_url)
        embed.set_thumbnail(url=self.thumbnail_icon_url)
        embed.set_footer(text=f"Command requested by {ctx.author.display_name}")

        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        """ shutdown bot"""
        await ctx.send("shuting down")
        await self.bot.close()
        sys.exit(0)


    # --------------------------------------------------------------------------------------------------------


##############################################################################################################
##############################################################################################################

def setup(bot):
    BotControll(bot)
    