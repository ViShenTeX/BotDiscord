import discord
from discord.ext import commands
from datetime import datetime
import json
import os

AGENDA_FILE = "agenda.json"

def cargar_agenda():
    if os.path.exists(AGENDA_FILE):
        with open(AGENDA_FILE, "r") as f:
            return json.load(f)
    return []

def guardar_agenda(agenda):
    with open(AGENDA_FILE, "w") as f:
        json.dump(agenda, f, indent=2)

def setup_agenda_commands(bot):
    @bot.tree.command(name="agendar", description="Agendar una descripción con una fecha")
    async def agendar(interaction: discord.Interaction, descripcion: str, fecha: str):
        try:
            datetime.strptime(fecha, "%d-%m-%Y")  # validar fecha
        except ValueError:
            await interaction.response.send_message("Fecha inválida. Usa formato DD-MM-YYYY.", ephemeral=True)
            return

        agenda = cargar_agenda()
        agenda.append({"descripcion": descripcion, "fecha": fecha})
        guardar_agenda(agenda)

        await interaction.response.send_message(f"✅ Agendado: `{descripcion}` para el `{fecha}`")
