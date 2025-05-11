import discord
from discord.ext import commands
from datetime import datetime
import json
import os

intents = discord.Intents.default()
intents.message_content = True  # Habilitar el intent de contenido de mensajes
bot = commands.Bot(command_prefix="!", intents=intents)

# Obtener variables desde secrets
TOKEN = os.environ['token']
CANAL_ID = int(os.environ['canal_id'])

AGENDA_FILE = "agenda.json"

def cargar_agenda():
    if os.path.exists(AGENDA_FILE):
        with open(AGENDA_FILE, "r") as f:
            return json.load(f)
    return []

def guardar_agenda(agenda):
    with open(AGENDA_FILE, "w") as f:
        json.dump(agenda, f, indent=2)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.event
async def setup_hook():
    print("🔄 Comandos sincronizados.")

# Comando para agendar
@bot.command(name="agendar")
async def agendar(ctx, descripcion: str, fecha: str):
    try:
        datetime.strptime(fecha, "%d-%m-%Y")  # validar fecha
    except ValueError:
        await ctx.send("❌ Fecha inválida. Usa formato DD-MM-YYYY.")
        return

    agenda = cargar_agenda()
    agenda.append({"descripcion": descripcion, "fecha": fecha})
    guardar_agenda(agenda)

    await ctx.send(f"✅ Agendado: `{descripcion}` para el `{fecha}`")

# Comando general
@bot.command(name="sitesusabesa")
async def sitesusabesa(ctx):
    await ctx.send("Amasa la masa!")

bot.run(TOKEN)