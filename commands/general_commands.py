from discord.ext import commands

def setup_general_commands(bot):
    @bot.tree.command(name="sitesusabesa", description="Responde con un mensaje divertido")
    async def sitesusabesa(interaction: discord.Interaction):
        await interaction.response.send_message("Amasa la masa!")
