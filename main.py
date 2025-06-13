import discord
from discord.ext import commands
from model import get_model


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def cargar(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./files/{file_name}")
            await ctx.send(get_model(model_path = "./keras_model.h5", labels_path = "./labels.txt", image_path = f"./files/{file_name}"))

    else:
        await ctx.send("No hay un archivo adjunto")

bot.run("TOKEN AQUÍ")