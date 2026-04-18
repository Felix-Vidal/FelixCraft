import discord
from discord import app_commands
from mcrcon import MCRcon
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CARGO_PERMITIDO = os.getenv("CARGO_PERMITIDO")

RCON_IP = os.getenv("RCON_IP")
RCON_PASSWORD = os.getenv("RCON_PASSWORD")
RCON_PORT = int(os.getenv("RCON_PORT"))

class FelixCraft(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(  
            intents = intents
        )
        self.tree = app_commands.CommandTree(self)
    
    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"O Bot {self.user} foi ligado com sucesso")

        for guild in self.guilds:
            cargo = discord.utils.get(guild.roles, name=CARGO_PERMITIDO)
            
            if not cargo:
                try:
                   
                    await guild.create_role(
                        name=CARGO_PERMITIDO, 
                        color=discord.Color.green(), 
                        hoist=True,
                        reason="Criado automaticamente pelo bot de Whitelist"
                    )
                    print(f'Cargo "{CARGO_PERMITIDO}" foi criado automaticamente no servidor {guild.name}!')
                except discord.Forbidden:
                    print(f'Erro: O bot não tem permissão de "Gerenciar Cargos" no servidor {guild.name}.')

bot = FelixCraft()

@bot.tree.command(name="listar_whitelist", description="Mostra todos os jogadores que estão na whitelist")
async def listar_whitelist(interaction: discord.Interaction):
    cargo = discord.utils.get(interaction.guild.roles, name=CARGO_PERMITIDO)
    
    if cargo not in interaction.user.roles:
        await interaction.response.send_message(f"Você precisa do cargo **{CARGO_PERMITIDO}** para usar este comando.", ephemeral=True)
        return

    await interaction.response.defer()
    ip_servidor = RCON_IP
    senha_rcon = RCON_PASSWORD
    porta_rcon = RCON_PORT
    
    try:
        with MCRcon(ip_servidor, senha_rcon, porta_rcon) as mcr:
            resposta = mcr.command("whitelist list")
            
        await interaction.followup.send(f"**Status da Whitelist:**\n```\n{resposta}\n```", ephemeral=True)
        
    except ConnectionRefusedError:
        await interaction.followup.send("Erro: O RCON recusou a conexão. Verifique se o `enable-rcon=true` está no server.properties e se você reiniciou o server.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Ocorreu um erro de conexão: `{e}`", ephemeral=True)

@bot.tree.command(name="whitelist", description="Adiciona um jogador à whitelist do servidor")
async def whitelist(interaction: discord.Interaction, nick: str):
    
    cargo = discord.utils.get(interaction.guild.roles, name=CARGO_PERMITIDO)

    if cargo not in interaction.user.roles:
        await interaction.response.send_message(f"Você precisa do cargo **{CARGO_PERMITIDO}** para usar este comando.", ephemeral=True)
        return
    
    await interaction.response.defer()

    try:
        with MCRcon(RCON_IP, RCON_PASSWORD, port=int(RCON_PORT)) as mcr:
            resposta_servidor = mcr.command(f"whitelist add {nick}")
            
        await interaction.followup.send(f"O jogador **{nick}** foi processado!\nResposta do Console: `{resposta_servidor}`")

    except ConnectionRefusedError:
        await interaction.followup.send("Erro: Conexão recusada. O servidor de Minecraft está ligado e o RCON está ativado?", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Erro ao tentar comunicar com o RCON.\nDetalhe: `{e}`", ephemeral=True)

@bot.tree.command(name="unwhitelist", description="Remove um jogador da whitelist do servidor")
async def unwhitelist(interaction: discord.Interaction, nick: str):
    
    cargo = discord.utils.get(interaction.guild.roles, name=CARGO_PERMITIDO)

    if cargo not in interaction.user.roles:
        await interaction.response.send_message(f"Você precisa do cargo **{CARGO_PERMITIDO}** para usar este comando.", ephemeral=True)
        return
    
    await interaction.response.defer()

    try:
        with MCRcon(RCON_IP, RCON_PASSWORD, port=int(RCON_PORT)) as mcr:
            resposta_servidor = mcr.command(f"whitelist remove {nick}")
            
        await interaction.followup.send(f"O jogador **{nick}** foi removido!\nResposta do Console: `{resposta_servidor}`")

    except ConnectionRefusedError:
        await interaction.followup.send("Erro: Conexão recusada. O servidor de Minecraft está ligado e o RCON está ativado?", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Erro ao tentar comunicar com o RCON.\nDetalhe: `{e}`", ephemeral=True)

@bot.tree.command(name="help", description="Mostra como usar o bot ou quem pode te ajudar.")
async def help_cmd(interaction: discord.Interaction):
    cargo = discord.utils.get(interaction.guild.roles, name=CARGO_PERMITIDO)

    # Prevenção de erro caso o cargo não seja encontrado no Discord
    if not cargo:
        await interaction.response.send_message(f"O cargo **{CARGO_PERMITIDO}** não foi encontrado neste servidor. Avise o Félix!", ephemeral=True)
        return
    
    if cargo in interaction.user.roles:
        mensagem_ajuda = (
            "🛠️ **Painel de Controle - Félix Craft** 🛠️\n\n"
            "Como você tem permissão, aqui estão os comandos disponíveis:\n\n"
            "🔹 `/whitelist [nick]` - Adiciona um jogador para poder entrar no servidor.\n"
            "🔹 `/unwhitelist [nick]` - Remove o acesso de um jogador ao servidor.\n"
            "🔹 `/listar_whitelist` - Listar os jogadores que podem entrar no servidor.\n"
            "🔹 `/help` - Mostra esta mensagem de ajuda."
        )
        await interaction.response.send_message(mensagem_ajuda, ephemeral=True)

    else:
        lista_moderadores = [membro.mention for membro in cargo.members if not membro.bot]
        
        if lista_moderadores:
            mods_formatados = ", ".join(lista_moderadores)
            mensagem_negada = (
                f"Você não possui o cargo necessário para liberar pessoas no servidor.\n"
                f"Por favor, peça para um dos moderadores abaixo executar o comando para você:\n\n"
                f"👉 {mods_formatados}"
            )
        else:
            mensagem_negada = (
                "**Acesso Negado!**\n\n"
                "Você não tem permissão para usar este comando e, no momento, não encontrei nenhum moderador com o cargo para te ajudar. Tente novamente mais tarde!"
            )

        await interaction.response.send_message(mensagem_negada)

bot.run(DISCORD_TOKEN)