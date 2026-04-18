# 🛡️ Félix Craft - Gestor de Whitelist

O **Félix Craft** é um bot de Discord exclusivo para gerenciar a whitelist do meu servidor de Minecraft hospedado em VPS. 

O objetivo principal deste bot é dar **autonomia** aos membros do servidor. Com ele, meus amigos podem convidar e autorizar novas pessoas para jogar sem que eu precise estar online para editar arquivos ou rodar comandos manualmente no console da VPS.

## 🚀 Motivação
- **Automação:** Chega de esperar o dono do server acordar para adicionar alguém na whitelist!
- **Segurança:** O servidor permanece fechado para desconhecidos. Apenas pessoas autorizadas via Discord conseguem entrar.
- **Praticidade:** Tudo é feito através de comandos simples dentro do Discord.

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
   git clone https://github.com/Felix-Vidal/Felix-Craft.git
```

2. Instale as dependências

```bash
pip install discord.py
pip install mcrcon
pip install requests
pip install python-dotenv
```

3. Configure as variáveis de ambiente

```env
DISCORD_TOKEN="seu_token_do_discord_aqui"
CARGO_PERMITIDO="Nome_Do_Cargo_Ou_ID"
RCON_IP="127.0.0.1" # Ou o IP público da sua VPS
RCON_PASSWORD="sua_senha_rcon_aqui"
RCON_PORT=25575
```
## 🐳 Deploy em Produção (Recomendado via Docker)
A forma ideal de rodar o bot na sua VPS (ex: Oracle Cloud / Ubuntu) é através do Docker Compose, garantindo que ele rode 24/7 e reinicie automaticamente em caso de falhas.

Pré-requisitos
Docker e Docker Compose instalados no servidor.

## Execução
```bash
python main.py
```


## Comandos Disponíveis
```bash
/whitelist {nick}
```
```bash
/unwhitelist {nick}
```
```bash
/listar_whitelist
```


## 🔒 Segurança

- O bot foi desenhado para ser privado. Certifique-se de configurar as permissões de cargo no Discord para que apenas seus amigos tenham permissão de usar os comandos de whitelist.

- Nota: Nunca submeta seu arquivo main.py com o Token exposto ao GitHub. Use arquivos .env ou segredos do repositório.

Desenvolvido por Felix-Vidal 👨‍💻
