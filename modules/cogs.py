from discord.ext import commands

##############################################################################################################
##############################################################################################################

class TemplateCog(commands.Cog):
    def __init__(self, bot, color_embed = 0xffffff) -> None:
        """ template cog """
        self.bot = bot
        self.color_embed = color_embed
        
        self.embed_author_url = "https://www.google.com/"
        self.embed_title_url = "https://www.google.com/"
        self.author_icon_url = "https://cdn-icons-png.flaticon.com/512/5968/5968759.png"
        self.thumbnail_icon_url = "https://cdn-icons-png.flaticon.com/512/5968/5968759.png"

        self.on_ready()
        self.cog_setup(bot)

    def cog_setup(self, bot):
        print(f"loading cog-module: {type(self).__name__}")
        bot.add_cog(self)

    def on_ready(self):
        try: 
            self.author_icon_url = self.bot.user.avatar_url
            self.thumbnail_icon_url = self.bot.user.avatar_url
        except Exception as E:
            self.author_icon_url = "https://cdn-icons-png.flaticon.com/512/5968/5968759.png"
            self.thumbnail_icon_url = "https://cdn-icons-png.flaticon.com/512/5968/5968759.png"
        

    # --------------------------------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------------------------------

##############################################################################################################
##############################################################################################################

#def setup(bot):
#    print("cog_setup: Owner")
#    bot.add_cog(TemplateCog(bot))
