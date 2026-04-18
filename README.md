# 🛡️ Félix Craft - Gestor de Whitelist

O **Félix Craft** é um bot de Discord exclusivo para gerenciar a whitelist do meu servidor de Minecraft hospedado em VPS. 

O objetivo principal deste bot é dar **autonomia** aos membros do servidor. Com ele, meus amigos podem convidar e autorizar novas pessoas para jogar sem que eu precise estar online para editar arquivos ou rodar comandos manualmente no console da VPS.

## 🚀 Motivação
- **Automação:** Chega de esperar o dono do server acordar para adicionar alguém na whitelist!
- **Segurança:** O servidor permanece fechado para desconhecidos. Apenas pessoas autorizadas via Discord conseguem entrar.
- **Praticidade:** Tudo é feito através de comandos simples (Slash Commands) dentro do Discord.

## 📋 Funcionalidades
- [x] **Comandos de Barra**: Interface moderna e intuitiva.
- [x] **Autonomia**: Amigos adicionam convidados sem depender do administrador.
- [x] **Sincronização em tempo real**: O comando executado no Discord reflete instantaneamente no jogo.
- [ ] **Sistema de Logs**: Registro de quem adicionou qual nickname (Em desenvolvimento).

## ⚙️ Como funciona
1. **Convite:** Um membro confiável do Discord usa o comando de barra do bot.
2. **Processamento:** O bot recebe o nickname do Minecraft.
3. **Execução:** O bot se conecta à instância do Minecraft na VPS e executa o comando `whitelist add nickname`.
4. **Confirmação:** O jogador é avisado no Discord que já pode entrar no servidor.

## 💻 Requisitos de Instalação (Para Desenvolvedor)
Se você for rodar o bot na sua própria máquina ou VPS:

1. Clone o repositório:
   ```bash
   git clone [https://github.com/Felix-Vidal/Felix-Craft.git](https://github.com/Felix-Vidal/Felix-Craft.git)

2. Instale as dependências

    ```bash
    pip install discord.py
    pip install mcrcon
    pip install requests
    pip install python-dotenv

3. Configure as variáveis de ambiente

        DISCORD_TOKEN="TOKEN"

        CRAFTY_URL="https://ip:8443" 

        CARGO_PERMITIDO="nome do cargo"

        RCON_IP="ip" 

        RCON_PASSWORD="SenhaSuperSeguraRcon2026!"
    
        RCON_PORT=25575

## Execução

      python main.py


## Comandos Disponíveis

    /whitelist {nick}

    /unwhitelist {nick}

    /listar_whitelist


## 🔒 Segurança

- O bot foi desenhado para ser privado. Certifique-se de configurar as permissões de cargo no Discord para que apenas seus amigos tenham permissão de usar os comandos de whitelist.

- Nota: Nunca submeta seu arquivo main.py com o Token exposto ao GitHub. Use arquivos .env ou segredos do repositório.

Desenvolvido por Felix-Vidal 👨‍💻
