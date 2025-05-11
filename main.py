import discord
from discord.ext import commands
from commands.agenda_commands import setup_agenda_commands
from commands.general_commands import setup_general_commands
import json

# Cargar configuración
with open("config.json") as f:
    config = json.load(f)

TOKEN = config["token"]

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# Configurar comandos
setup_agenda_commands(bot)
setup_general_commands(bot)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

bot.run(TOKEN)
