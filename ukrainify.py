import io

import click
import discord
import requests
from discord.ext import commands
from PIL import Image


class UkrainifyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def overlay(self, original_bytes, overlay_path):
        original_f = io.BytesIO(original_bytes)
        original = Image.open(original_f)

        overlay = Image.open(overlay_path).resize(original.size)
        original.paste(overlay, (0, 0), overlay)

        destination = io.BytesIO()
        original.save(destination, format="PNG")
        destination.seek(0)

        return destination

    async def overlay_avatar(self, ctx, overlay_path):
        destination = self.overlay(await ctx.author.avatar.read(), overlay_path)

        file = discord.File(fp=destination, filename="avatar.png")
        await ctx.respond(file=file)

    @commands.slash_command(
        description="Return your profile picture with the ukrainian flag as the outline"
    )
    async def ukrainify(self, ctx):
        await self.overlay_avatar(ctx, "ukrainify_template.png")


@click.command(
    help="A discord bot capable of adding an overlay (originally the outline of the ukrainian flag) to your avatar"
)
@click.option("-t", "--token", type=str, help="Your discord bot token", prompt=True)
def main(token):
    bot = discord.Bot("!")
    bot.add_cog(UkrainifyCog(bot))
    bot.run(token)


if __name__ == "__main__":
    main()
