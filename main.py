from distutils import extension
from discord.ext import commands
import discord, yaml
from rpg import world, loader

TOKEN:str = "none"
VERSION:str = "xx.xx"
COLOR_EMBED:hex = 0x000000
PREFIX = "-"


bot = commands.Bot(command_prefix="-")
WORLD = world.World("emptyworld", "emptytext")

def load_config(file:str):
    global TOKEN, VERSION, COLOR_EMBED, PREFIX
    print(f"loading bot configuration file: {file}")
    with open(file, "r") as stream:
        try:
            data = yaml.safe_load(stream)
            for key in data:
                print(f"\t - {key}: {data[key]}")
            TOKEN = data["TOKEN"]
            VERSION = data["VERSION"]
            COLOR_EMBED = int(data["COLOR_EMBED"], 16)
            PREFIX = data["PREFIX"]
            bot.command_prefix = PREFIX
        except yaml.YAMLError as exc:
            print(exc)

##############################################################################################################
##############################################################################################################
# BOT EVENTS

@bot.event
async def on_ready():
    print("Bot is ready")
    for cog in bot.cogs:
        bot.cogs[cog].on_ready()


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You don`t have the permission for this command')
    else:
        print(str(error))
        await ctx.send(str(error))


##############################################################################################################
##############################################################################################################
# BASIC COMMANDS

@bot.command()
#@commands.is_owner()
async def info(ctx):
    embed = discord.Embed(title="Information", url="https://www.google.com/", description="\t", color=COLOR_EMBED)

    embed.set_author(name=bot.user.name , url="https://www.google.com/", icon_url=bot.user.avatar_url)
    embed.set_thumbnail(url=bot.user.avatar_url)

    embed.add_field(name="Current Version", value=str(VERSION))
    embed.add_field(name="Connected Server", value=str(len(bot.guilds)), inline=True)
    embed.add_field(name="Active Private Chats", value=str(len(bot.private_channels)), inline=True)
    embed.add_field(name="Extendsions", value=str(len(bot.extensions)), inline=True)
    embed.add_field(name="Cogs", value=str(len(bot.cogs)), inline=True)
    embed.add_field(name="Users", value=str(len(bot.users)), inline=True)
    embed.add_field(name="Emojis", value=str(len(bot.emojis)), inline=True)
    
    #embed.add_field(name="Stickers", value=str(len(bot.stickers)), inline=True) # causes error
    # "Command raised an exception: AttributeError: 'Bot' object has no attribute 'stickers'"

    embed.add_field(name="Latency:", value=str(bot.latency)+" sec.", inline=False)

    embed.set_footer(text=f"Information requested by {ctx.author.display_name}")

    await ctx.send(embed=embed)


##############################################################################################################
##############################################################################################################

if __name__ == '__main__':

    load_config("C:/data/Discord MMORPG/botconfig.yaml")
    loader.load_word("data/stages.csv")

    bot.load_extension("cogs.controll")
    bot.run(TOKEN)
    
    print("shutting down ....")
