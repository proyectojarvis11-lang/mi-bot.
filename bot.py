import discord
from discord import app_commands
import os
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# ── Sistema de idiomas ─────────────────────────────────────
idioma_servidor = {}

TEXTOS = {
    "es": {
        "ping_respuesta": "🏓 Pong! Latencia: **{ms}ms**",
        "saludo": "¡Hola, {usuario}! 🎉",
        "limpiar_ok": "🗑️ Se borraron **{n}** mensajes.",
        "anuncio_ok": "✅ Anuncio enviado a {canal}",
        "antilink_on": "✅ Anti-link activado en {canal}",
        "antilink_off": "❌ Anti-link desactivado en {canal}",
        "antilink_aviso": "🚫 {usuario} no se permiten links aquí.",
        "warn_titulo": "Advertencia - Usuario Aislado",
        "warn_usuario": "Usuario",
        "warn_duracion": "Duración",
        "warn_canal": "Canal",
        "warn_motivo": "Motivo",
        "warn_motivo_val": "Se detectó la palabra prohibida **{palabra}** en su mensaje.",
        "warn_explicacion": "Explicación",
        "warn_explicacion_val": "El servidor no permite el uso de lenguaje ofensivo, vulgar o discriminatorio. El usuario ha sido aislado temporalmente por violar las normas del servidor.",
        "warn_footer": "El aislamiento se levantará automáticamente en {min} minutos.",
        "verificar_ya": "Ya estás verificado. ✅",
        "verificar_ok": "¡Verificado! 🎉 Ahora tienes el rol **{rol}**.",
        "ticket_existente": "Ya tienes un ticket abierto: {canal}",
        "ticket_titulo": "🎫 Ticket Abierto",
        "ticket_desc": "Hola {usuario}, el staff te atenderá pronto.\nPara cerrar el ticket usa el botón de abajo.",
        "ticket_creado": "✅ Ticket creado: {canal}",
        "cerrar_ticket": "Cerrando ticket en 5 segundos...",
        "panel_verif_ok": "✅ Panel de verificación creado.",
        "panel_ticket_ok": "✅ Panel de tickets creado.",
        "panel_bienvenida_ok": "✅ Panel de bienvenida creado y canales configurados.",
        "idioma_cambiado": "✅ Idioma cambiado a **Español** 🇪🇸",
        "info_titulo": "📋 Información del Bot",
        "info_desc": "Aquí tienes todo lo que necesitas saber sobre mí.",
        "info_nombre": "🤖 Nombre",
        "info_version": "📦 Versión",
        "info_version_val": "1.0.0",
        "info_idioma": "🌐 Idioma actual",
        "info_idioma_val": "Español 🇪🇸",
        "info_latencia": "📡 Latencia",
        "info_servidores": "🌍 Servidores",
        "info_comandos": "⚙️ Comandos disponibles",
        "info_comandos_val": (
            "`/ping` — Latencia del bot\n"
            "`/saludar` — Saluda a un usuario\n"
            "`/info` — Info del servidor\n"
            "`/limpiar` — Borra mensajes\n"
            "`/anuncio` — Envía un anuncio\n"
            "`/antilink` — Activa/desactiva anti-link\n"
            "`/panel-bienvenida` — Panel de bienvenida\n"
            "`/panel-verificacion` — Panel de verificación\n"
            "`/panel-ticket` — Panel de tickets\n"
            "`/bot-info` — Este panel"
        ),
        "info_footer": "Usa los botones de abajo para cambiar el idioma del bot.",
    },
    "en": {
        "ping_respuesta": "🏓 Pong! Latency: **{ms}ms**",
        "saludo": "Hello, {usuario}! 🎉",
        "limpiar_ok": "🗑️ Deleted **{n}** messages.",
        "anuncio_ok": "✅ Announcement sent to {canal}",
        "antilink_on": "✅ Anti-link enabled in {canal}",
        "antilink_off": "❌ Anti-link disabled in {canal}",
        "antilink_aviso": "🚫 {usuario} links are not allowed here.",
        "warn_titulo": "Warning - Isolated User",
        "warn_usuario": "User",
        "warn_duracion": "Duration",
        "warn_canal": "Channel",
        "warn_motivo": "Reason",
        "warn_motivo_val": "Forbidden word **{palabra}** was detected in their message.",
        "warn_explicacion": "Explanation",
        "warn_explicacion_val": "The server does not allow offensive, vulgar or discriminatory language. The user has been temporarily isolated for violating server rules.",
        "warn_footer": "The isolation will be lifted automatically in {min} minutes.",
        "verificar_ya": "You are already verified. ✅",
        "verificar_ok": "Verified! 🎉 You now have the role **{rol}**.",
        "ticket_existente": "You already have an open ticket: {canal}",
        "ticket_titulo": "🎫 Ticket Opened",
        "ticket_desc": "Hello {usuario}, staff will attend you shortly.\nUse the button below to close the ticket.",
        "ticket_creado": "✅ Ticket created: {canal}",
        "cerrar_ticket": "Closing ticket in 5 seconds...",
        "panel_verif_ok": "✅ Verification panel created.",
        "panel_ticket_ok": "✅ Ticket panel created.",
        "panel_bienvenida_ok": "✅ Welcome panel created and channels configured.",
        "idioma_cambiado": "✅ Language changed to **English** 🇬🇧",
        "info_titulo": "📋 Bot Information",
        "info_desc": "Here's everything you need to know about me.",
        "info_nombre": "🤖 Name",
        "info_version": "📦 Version",
        "info_version_val": "1.0.0",
        "info_idioma": "🌐 Current language",
        "info_idioma_val": "English 🇬🇧",
        "info_latencia": "📡 Latency",
        "info_servidores": "🌍 Servers",
        "info_comandos": "⚙️ Available commands",
        "info_comandos_val": (
            "`/ping` — Bot latency\n"
            "`/saludar` — Greet a user\n"
            "`/info` — Server info\n"
            "`/limpiar` — Delete messages\n"
            "`/anuncio` — Send announcement\n"
            "`/antilink` — Enable/disable anti-link\n"
            "`/panel-bienvenida` — Welcome panel\n"
            "`/panel-verificacion` — Verification panel\n"
            "`/panel-ticket` — Ticket panel\n"
            "`/bot-info` — This panel"
        ),
        "info_footer": "Use the buttons below to change the bot language.",
    },
    "pt": {
        "ping_respuesta": "🏓 Pong! Latência: **{ms}ms**",
        "saludo": "Olá, {usuario}! 🎉",
        "limpiar_ok": "🗑️ **{n}** mensagens apagadas.",
        "anuncio_ok": "✅ Anúncio enviado para {canal}",
        "antilink_on": "✅ Anti-link ativado em {canal}",
        "antilink_off": "❌ Anti-link desativado em {canal}",
        "antilink_aviso": "🚫 {usuario} links não são permitidos aqui.",
        "warn_titulo": "Aviso - Usuário Isolado",
        "warn_usuario": "Usuário",
        "warn_duracion": "Duração",
        "warn_canal": "Canal",
        "warn_motivo": "Motivo",
        "warn_motivo_val": "A palavra proibida **{palabra}** foi detectada na sua mensagem.",
        "warn_explicacion": "Explicação",
        "warn_explicacion_val": "O servidor não permite linguagem ofensiva, vulgar ou discriminatória. O usuário foi temporariamente isolado por violar as regras do servidor.",
        "warn_footer": "O isolamento será levantado automaticamente em {min} minutos.",
        "verificar_ya": "Você já está verificado. ✅",
        "verificar_ok": "Verificado! 🎉 Agora você tem o cargo **{rol}**.",
        "ticket_existente": "Você já tem um ticket aberto: {canal}",
        "ticket_titulo": "🎫 Ticket Aberto",
        "ticket_desc": "Olá {usuario}, a equipe irá te atender em breve.\nUse o botão abaixo para fechar o ticket.",
        "ticket_creado": "✅ Ticket criado: {canal}",
        "cerrar_ticket": "Fechando ticket em 5 segundos...",
        "panel_verif_ok": "✅ Painel de verificação criado.",
        "panel_ticket_ok": "✅ Painel de tickets criado.",
        "panel_bienvenida_ok": "✅ Painel de boas-vindas criado e canais configurados.",
        "idioma_cambiado": "✅ Idioma alterado para **Português** 🇧🇷",
        "info_titulo": "📋 Informações do Bot",
        "info_desc": "Aqui está tudo que você precisa saber sobre mim.",
        "info_nombre": "🤖 Nome",
        "info_version": "📦 Versão",
        "info_version_val": "1.0.0",
        "info_idioma": "🌐 Idioma atual",
        "info_idioma_val": "Português 🇧🇷",
        "info_latencia": "📡 Latência",
        "info_servidores": "🌍 Servidores",
        "info_comandos": "⚙️ Comandos disponíveis",
        "info_comandos_val": (
            "`/ping` — Latência do bot\n"
            "`/saludar` — Cumprimentar usuário\n"
            "`/info` — Info do servidor\n"
            "`/limpiar` — Apagar mensagens\n"
            "`/anuncio` — Enviar anúncio\n"
            "`/antilink` — Ativar/desativar anti-link\n"
            "`/panel-bienvenida` — Painel de boas-vindas\n"
            "`/panel-verificacion` — Painel de verificação\n"
            "`/panel-ticket` — Painel de tickets\n"
            "`/bot-info` — Este painel"
        ),
        "info_footer": "Use os botões abaixo para mudar o idioma do bot.",
    }
}

def t(guild_id, clave, **kwargs):
    lang = idioma_servidor.get(guild_id, "es")
    texto = TEXTOS[lang].get(clave, TEXTOS["es"].get(clave, clave))
    return texto.format(**kwargs) if kwargs else texto


# ── Configuración IDs del servidor ────────────────────────
GUILD_ID = 1515896622587052122
ROL_CC_ID = 1515899229388673144
CANAL_POSTULACIONES_ID = 1515899874137215046

# ── Estado de postulaciones activas por DM ────────────────
# Guarda el estado de cada usuario que está en proceso de postulación
# formato: { user_id: { "paso": 1, "respuestas": {} } }
postulaciones_activas = {}

# ── Requisitos CC ─────────────────────────────────────────
REQUISITOS = {
    "min_seguidores": 1000,   # Mínimo 1k seguidores
    "videos_semana": 3,       # 3 videos por semana
    "min_views": 1000,        # 1k+ average views
    "seguir_tiktok": True,    # Debe seguir el TikTok oficial
}

TIKTOK_OFICIAL = "@starhurbanstudio"  # TikTok que deben seguir


@client.event
async def on_ready():
    await tree.sync()
    print(f"✅ Bot conectado como: {client.user}")
    await client.change_presence(activity=discord.Game(name="/bot-info"))


@tree.command(name="ping", description="Muestra la latencia del bot")
async def ping(interaction: discord.Interaction):
    ms = round(client.latency * 1000)
    await interaction.response.send_message(t(interaction.guild.id, "ping_respuesta", ms=ms))

@tree.command(name="saludar", description="Saluda a un usuario")
async def saludar(interaction: discord.Interaction, usuario: discord.Member = None):
    usuario = usuario or interaction.user
    await interaction.response.send_message(t(interaction.guild.id, "saludo", usuario=usuario.mention))

@tree.command(name="info", description="Muestra información del servidor")
async def info(interaction: discord.Interaction):
    servidor = interaction.guild
    embed = discord.Embed(title="📋 Info de " + servidor.name, color=discord.Color.blue())
    embed.add_field(name="Miembros", value=servidor.member_count)
    embed.add_field(name="Canales", value=len(servidor.channels))
    await interaction.response.send_message(embed=embed)

@tree.command(name="limpiar", description="Borra mensajes del canal")
@app_commands.checks.has_permissions(manage_messages=True)
async def limpiar(interaction: discord.Interaction, cantidad: int = 5):
    await interaction.channel.purge(limit=cantidad)
    await interaction.response.send_message(t(interaction.guild.id, "limpiar_ok", n=cantidad), ephemeral=True)

@tree.command(name="anuncio", description="Envía un anuncio a un canal específico")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(
    canal="Canal donde enviar el anuncio",
    mensaje="Mensaje del anuncio",
    link="Link opcional",
    texto_link="Texto visible del link (por defecto: Ver más)"
)
async def anuncio(
    interaction: discord.Interaction,
    canal: discord.TextChannel,
    mensaje: str,
    link: str = None,
    texto_link: str = "Ver más"
):
    await interaction.response.defer(ephemeral=True)
    embed = discord.Embed(description=mensaje, color=discord.Color.red())
    embed.set_author(name="📢 Anuncio")
    if link:
        embed.add_field(name="🔗 Link", value="[" + texto_link + "](" + link + ")", inline=False)
    await canal.send(embed=embed)
    await interaction.followup.send(t(interaction.guild.id, "anuncio_ok", canal=canal.mention), ephemeral=True)


# ── Anti Link ──────────────────────────────────────────────
canales_antilink = set()

@tree.command(name="antilink", description="Activa o desactiva el anti-link en un canal")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(canal="Canal donde aplicar el anti-link", activar="True para activar, False para desactivar")
async def antilink(interaction: discord.Interaction, canal: discord.TextChannel, activar: bool):
    gid = interaction.guild.id
    if activar:
        canales_antilink.add(canal.id)
        await interaction.response.send_message(t(gid, "antilink_on", canal=canal.mention), ephemeral=True)
    else:
        canales_antilink.discard(canal.id)
        await interaction.response.send_message(t(gid, "antilink_off", canal=canal.mention), ephemeral=True)


# ── Malas palabras ─────────────────────────────────────────
MALAS_PALABRAS = ["mierda", "puta", "idiota", "imbecil", "pendejo", "cabron", "puto"]
DURACION_AISLAMIENTO = 8


# ── Lógica de postulación CC paso a paso ──────────────────
async def iniciar_postulacion(message):
    """Inicia el proceso de postulación pregunta por pregunta."""
    user_id = message.author.id
    postulaciones_activas[user_id] = {"paso": 1, "respuestas": {}}

    embed = discord.Embed(
        title="🎬 Programa de Creadores de Contenido — Street Bronx",
        description=(
            "¡Gracias por tu interés! Vamos a revisar si cumples los requisitos.\n\n"
            "**📋 REQ CC — Requisitos:**\n"
            "✅ Seguir **@starhurbanstudio** en TikTok\n"
            "✅ Mínimo **3 videos por semana**\n"
            "✅ Mínimo **1,000 seguidores** (o 5,000)\n"
            "✅ Mínimo **1,000 views promedio**\n\n"
            "Responde las siguientes preguntas una por una. ¡Empecemos!"
        ),
        color=discord.Color.from_rgb(255, 50, 50)
    )
    embed.set_footer(text="Street Bronx — Content Creator Program")
    await message.channel.send(embed=embed)
    await asyncio.sleep(1)
    await message.channel.send("**1️⃣ ¿Cuál es tu nombre de usuario de Roblox?**")


async def procesar_respuesta_cc(message):
    """Procesa cada respuesta del formulario paso a paso."""
    user_id = message.author.id
    estado = postulaciones_activas[user_id]
    paso = estado["paso"]
    respuestas = estado["respuestas"]

    if paso == 1:
        respuestas["roblox"] = message.content
        estado["paso"] = 2
        await message.channel.send("**2️⃣ ¿En qué plataforma creas contenido?** (YouTube, TikTok, Twitch, etc.)")

    elif paso == 2:
        respuestas["plataforma"] = message.content
        estado["paso"] = 3
        await message.channel.send("**3️⃣ ¿Cuántos seguidores o suscriptores tienes actualmente?** (escribe solo el número)")

    elif paso == 3:
        # Intentar extraer número de seguidores
        num_str = message.content.replace(",", "").replace(".", "").strip()
        try:
            seguidores = int("".join(filter(str.isdigit, num_str)))
        except:
            seguidores = 0
        respuestas["seguidores"] = seguidores
        respuestas["seguidores_raw"] = message.content
        estado["paso"] = 4
        await message.channel.send("**4️⃣ ¿Cuántos views promedio tienen tus videos/streams?** (escribe solo el número)")

    elif paso == 4:
        num_str = message.content.replace(",", "").replace(".", "").strip()
        try:
            views = int("".join(filter(str.isdigit, num_str)))
        except:
            views = 0
        respuestas["views"] = views
        respuestas["views_raw"] = message.content
        estado["paso"] = 5
        await message.channel.send("**5️⃣ ¿Cuántos videos subes por semana aproximadamente?** (escribe solo el número)")

    elif paso == 5:
        num_str = message.content.strip()
        try:
            videos = int("".join(filter(str.isdigit, num_str)))
        except:
            videos = 0
        respuestas["videos_semana"] = videos
        estado["paso"] = 6
        await message.channel.send("**6️⃣ ¿Sigues a " + TIKTOK_OFICIAL + " en TikTok?** (responde: sí / no)")

    elif paso == 6:
        sigue = message.content.lower().strip()
        respuestas["sigue_tiktok"] = "si" in sigue or "sí" in sigue or "yes" in sigue
        estado["paso"] = 7
        await message.channel.send("**7️⃣ Comparte el enlace a tu canal o perfil principal.**")

    elif paso == 7:
        respuestas["link"] = message.content
        estado["paso"] = 8
        await message.channel.send("**8️⃣ ¿Por qué te gustaría representar a Street Bronx?**")

    elif paso == 8:
        respuestas["motivacion"] = message.content
        # Postulación completa — evaluar requisitos
        del postulaciones_activas[user_id]
        await evaluar_postulacion(message, respuestas)


async def evaluar_postulacion(message, respuestas):
    """Evalúa si el usuario cumple los requisitos y actúa en consecuencia."""
    seguidores = respuestas.get("seguidores", 0)
    views = respuestas.get("views", 0)
    videos = respuestas.get("videos_semana", 0)
    sigue_tiktok = respuestas.get("sigue_tiktok", False)

    cumple_seguidores = seguidores >= REQUISITOS["min_seguidores"]
    cumple_views = views >= REQUISITOS["min_views"]
    cumple_videos = videos >= REQUISITOS["videos_semana"]
    cumple_tiktok = sigue_tiktok

    aprobado = cumple_seguidores and cumple_views and cumple_videos and cumple_tiktok

    # Embed resumen de postulación para el canal de staff
    guild = discord.utils.get(client.guilds, id=GUILD_ID)
    canal_staff = client.get_channel(CANAL_POSTULACIONES_ID) if CANAL_POSTULACIONES_ID else None

    if canal_staff and guild:
        embed_staff = discord.Embed(
            title="📥 Nueva Postulación CC — " + message.author.name,
            color=discord.Color.green() if aprobado else discord.Color.orange(),
        )
        embed_staff.add_field(name="👤 Usuario Discord", value=message.author.mention + " (" + message.author.name + ")", inline=False)
        embed_staff.add_field(name="🎮 Roblox", value=respuestas.get("roblox", "N/A"), inline=True)
        embed_staff.add_field(name="📱 Plataforma", value=respuestas.get("plataforma", "N/A"), inline=True)
        embed_staff.add_field(name="👥 Seguidores", value=respuestas.get("seguidores_raw", "N/A") + (" ✅" if cumple_seguidores else " ❌"), inline=True)
        embed_staff.add_field(name="👁️ Views Promedio", value=respuestas.get("views_raw", "N/A") + (" ✅" if cumple_views else " ❌"), inline=True)
        embed_staff.add_field(name="🎬 Videos/Semana", value=str(respuestas.get("videos_semana", "N/A")) + (" ✅" if cumple_videos else " ❌"), inline=True)
        embed_staff.add_field(name="📲 Sigue TikTok Oficial", value=("Sí ✅" if cumple_tiktok else "No ❌"), inline=True)
        embed_staff.add_field(name="🔗 Link", value=respuestas.get("link", "N/A"), inline=False)
        embed_staff.add_field(name="💬 Motivación", value=respuestas.get("motivacion", "N/A"), inline=False)
        embed_staff.add_field(name="📊 Resultado", value="✅ **APROBADO AUTOMÁTICAMENTE**" if aprobado else "⏳ **PENDIENTE — Revisión manual**", inline=False)
        embed_staff.set_thumbnail(url=message.author.display_avatar.url)
        await canal_staff.send(embed=embed_staff)

    if aprobado:
        # Dar rol automáticamente
        member = guild.get_member(message.author.id) if guild else None
        rol_cc = guild.get_role(ROL_CC_ID) if guild else None

        if member and rol_cc:
            await member.add_roles(rol_cc)

            # Cambiar nickname agregando [CC]
            try:
                nuevo_nick = "[✅] " + (member.nick or member.name) + " [CC]"
                await member.edit(nick=nuevo_nick[:32])  # Discord límite 32 chars
            except discord.Forbidden:
                pass  # Sin permisos para cambiar nick

        # Mensaje de aprobación al usuario por DM
        embed_aprobado = discord.Embed(
            title="🎉 ¡Felicitaciones! Eres parte del equipo de Creadores",
            description=(
                "¡Bienvenido/a a la comunidad de Creadores de Contenido de **Street Bronx**! 🎬\n\n"
                "Se te ha asignado el rol **Content Creator** y tu identificador **[CC]**.\n\n"
                "**🎬 BENEFICIOS PARA CREADORES DE CONTENIDO 🎬**\n\n"
                "💰 **Pago por Colaboraciones**\n"
                "Recibirás hasta **$5.000.000** dentro del juego todos los meses.\n\n"
                "🎟️ **Acceso a Eventos Privados**\n"
                "Participa en eventos exclusivos junto al Staff, invitados especiales y otros creadores.\n\n"
                "⭐ **Rango Exclusivo de Creador**\n"
                "Obtén un rango único que te destacará dentro del servidor y la comunidad.\n\n"
                "🎁 **Recompensas Especiales**\n"
                "Recibe vehículos exclusivos, objetos únicos y premios especiales para tus videos.\n\n"
                "📢 **Promoción Oficial**\n"
                "Tu contenido podrá ser compartido en <#1504542925097271316>.\n\n"
                "¡Gracias por representar a Street Bronx! 🚀"
            ),
            color=discord.Color.gold()
        )
        embed_aprobado.set_footer(text="Street Bronx — Content Creator Program ✅")
        await message.channel.send(embed=embed_aprobado)



    else:
        # No cumple requisitos — mensaje al usuario
        faltantes = []
        if not cumple_seguidores:
            faltantes.append("• Mínimo **1,000 seguidores** (tienes: " + str(respuestas.get("seguidores", 0)) + ")")
        if not cumple_views:
            faltantes.append("• Mínimo **1,000 views promedio** (tienes: " + str(respuestas.get("views", 0)) + ")")
        if not cumple_videos:
            faltantes.append("• Mínimo **3 videos por semana** (tienes: " + str(respuestas.get("videos_semana", 0)) + ")")
        if not cumple_tiktok:
            faltantes.append("• Seguir **" + TIKTOK_OFICIAL + "** en TikTok")

        embed_rechazado = discord.Embed(
            title="⏳ Postulación en Revisión",
            description=(
                "Gracias por postularte a **Street Bronx Content Creator**.\n\n"
                "Parece que aún no cumples todos los requisitos automáticos:\n\n" +
                "\n".join(faltantes) +
                "\n\n📨 Tu postulación ha sido enviada al **Staff** para revisión manual.\n"
                "Te contactaremos pronto con una respuesta. ¡Sigue creando contenido! 💪"
            ),
            color=discord.Color.orange()
        )
        embed_rechazado.set_footer(text="Street Bronx — Content Creator Program")
        await message.channel.send(embed=embed_rechazado)


@client.event
async def on_message(message):
    if message.author.bot:
        return

    # ── DM: Sistema de postulación CC ─────────────────────
    if isinstance(message.channel, discord.DMChannel):
        user_id = message.author.id

        # Si el usuario ya está en proceso de postulación, procesar su respuesta
        if user_id in postulaciones_activas:
            await procesar_respuesta_cc(message)
            return

        # Si el mensaje contiene palabras clave, iniciar postulación
        contenido_dm = message.content.lower()
        if any(x in contenido_dm for x in [
            "creador", "creator", "contenido", "content creator",
            "youtube", "tiktok", "streamer", "postulacion", "postulación", "aplicar", "apply"
        ]):
            await iniciar_postulacion(message)
        return

    # ── Mensajes en servidor ───────────────────────────────
    gid = message.guild.id if message.guild else None

    if message.channel.id in canales_antilink:
        if "http://" in message.content or "https://" in message.content or "discord.gg" in message.content:
            await message.delete()
            aviso = await message.channel.send(t(gid, "antilink_aviso", usuario=message.author.mention))
            await asyncio.sleep(5)
            await aviso.delete()
            return

    contenido = message.content.lower()
    for palabra in MALAS_PALABRAS:
        if palabra in contenido:
            await message.delete()

            rol_aislado = discord.utils.get(message.guild.roles, name="Aislado")
            if not rol_aislado:
                rol_aislado = await message.guild.create_role(name="Aislado")
                for channel in message.guild.channels:
                    await channel.set_permissions(rol_aislado, send_messages=False, speak=False)
            await message.author.add_roles(rol_aislado)

            canal_advertencia = discord.utils.get(message.guild.text_channels, name="advertencia")
            if canal_advertencia:
                embed = discord.Embed(
                    title=t(gid, "warn_titulo"),
                    color=discord.Color.from_rgb(255, 80, 80)
                )
                embed.add_field(name=t(gid, "warn_usuario"), value=message.author.mention + " (" + message.author.name + ")", inline=False)
                embed.add_field(name=t(gid, "warn_duracion"), value=str(DURACION_AISLAMIENTO) + " minutos", inline=False)
                embed.add_field(name=t(gid, "warn_canal"), value=message.channel.mention, inline=False)
                embed.add_field(name=t(gid, "warn_motivo"), value=t(gid, "warn_motivo_val", palabra=palabra), inline=False)
                embed.add_field(name=t(gid, "warn_explicacion"), value=t(gid, "warn_explicacion_val"), inline=False)
                embed.set_footer(text=t(gid, "warn_footer", min=DURACION_AISLAMIENTO))
                embed.set_thumbnail(url=message.author.display_avatar.url)
                await canal_advertencia.send(embed=embed)

            await asyncio.sleep(DURACION_AISLAMIENTO * 60)
            await message.author.remove_roles(rol_aislado)
            break


# ── Configuración ──────────────────────────────────────────
config = {}


# ── Panel de bienvenida ────────────────────────────────────
@tree.command(name="panel-bienvenida", description="Crea un panel de bienvenida en un canal")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(
    canal="Canal donde mostrar el panel",
    nombre_servidor="Nombre del servidor",
    descripcion_servidor="Descripción corta del servidor",
    roles="Roles disponibles",
    canal_reglas="Canal de reglas",
    canal_anuncios="Canal de anuncios",
    canal_chat="Canal de chat",
    canal_bienvenida="Canal de bienvenidas",
    canal_despedida="Canal de despedidas"
)
async def panel_bienvenida(
    interaction: discord.Interaction,
    canal: discord.TextChannel,
    nombre_servidor: str,
    descripcion_servidor: str,
    roles: str,
    canal_reglas: discord.TextChannel,
    canal_anuncios: discord.TextChannel,
    canal_chat: discord.TextChannel,
    canal_bienvenida: discord.TextChannel,
    canal_despedida: discord.TextChannel
):
    config[interaction.guild.id] = {
        "bienvenida": canal_bienvenida.id,
        "despedida": canal_despedida.id,
        "nombre_servidor": nombre_servidor,
        "descripcion_servidor": descripcion_servidor,
        "roles": roles,
        "canal_reglas": canal_reglas.id,
        "canal_anuncios": canal_anuncios.id,
        "canal_chat": canal_chat.id
    }
    descripcion = (
        "🏙️ Has llegado a **" + nombre_servidor + "**, " + descripcion_servidor + ".\n"
        "Aquí podrás convertirte en quien quieras: " + roles + "\n\n"
        "📋 **Pasos importantes para empezar:**\n"
        "1️⃣ Lee las reglas en " + canal_reglas.mention + "\n"
        "2️⃣ Mira las novedades en " + canal_anuncios.mention + "\n"
        "3️⃣ Pasa por " + canal_chat.mention + "\n\n"
        "🎭 **Recuerda:**\n"
        "• El respeto es fundamental 🙌\n"
        "• Juega con creatividad y realismo 🎬\n"
        "• Cumple las normas para no recibir sanciones 🚫\n\n"
        "🚀 ¡Gracias por unirte a nuestra comunidad! 🎉"
    )
    embed = discord.Embed(
        title="✨ Panel de Bienvenida — " + nombre_servidor + " ✨",
        description=descripcion,
        color=discord.Color.green()
    )
    embed.set_footer(text="🎉 Bienvenidas en #" + canal_bienvenida.name + " | Despedidas en #" + canal_despedida.name)
    embed.set_thumbnail(url=interaction.guild.icon.url if interaction.guild.icon else None)
    await canal.send(embed=embed)
    await interaction.response.send_message(t(interaction.guild.id, "panel_bienvenida_ok"), ephemeral=True)


@client.event
async def on_member_join(member):
    guild_config = config.get(member.guild.id)
    if guild_config:
        canal = client.get_channel(guild_config["bienvenida"])
        nombre_servidor = guild_config.get("nombre_servidor", member.guild.name)
        roles = guild_config.get("roles", "policía 🚓, médico 🚑, bombero 🔥")
        canal_reglas_mention = "<#" + str(guild_config.get("canal_reglas")) + ">" if guild_config.get("canal_reglas") else "#reglas"
        canal_anuncios_mention = "<#" + str(guild_config.get("canal_anuncios")) + ">" if guild_config.get("canal_anuncios") else "#anuncios"
        canal_chat_mention = "<#" + str(guild_config.get("canal_chat")) + ">" if guild_config.get("canal_chat") else "#chat"
        if canal:
            descripcion = (
                "🏙️ Has llegado a **" + nombre_servidor + "**.\n"
                "Aquí podrás convertirte en quien quieras: " + roles + "\n\n"
                "📋 **Pasos importantes para empezar:**\n"
                "1️⃣ Lee las reglas en " + canal_reglas_mention + "\n"
                "2️⃣ Mira las novedades en " + canal_anuncios_mention + "\n"
                "3️⃣ Pasa por " + canal_chat_mention + "\n\n"
                "🎭 **Recuerda:**\n"
                "• El respeto es fundamental 🙌\n"
                "• Juega con creatividad y realismo 🎬\n"
                "• Cumple las normas para no recibir sanciones 🚫\n\n"
                "🚀 ¡Tu segunda vida comienza ahora en **" + nombre_servidor + "**! 🎉"
            )
            embed = discord.Embed(
                title="✨ Bienvenido/a " + member.name + " ✨",
                description=descripcion,
                color=discord.Color.green()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            await canal.send(embed=embed)


@client.event
async def on_member_remove(member):
    guild_config = config.get(member.guild.id)
    if guild_config:
        canal = client.get_channel(guild_config["despedida"])
        nombre_servidor = guild_config.get("nombre_servidor", member.guild.name)
        if canal:
            descripcion = (
                "🏙️ Hoy nos despedimos de un ciudadano más de **" + nombre_servidor + "**.\n"
                "Quizás su historia termine aquí, o tal vez solo sea una pausa.\n\n"
                "💭 Cada rol deja recuerdos:\n"
                "• Risas compartidas 😂\n"
                "• Aventuras vividas 🚀\n"
                "• Amistades creadas 🤝\n\n"
                "✨ Las puertas siempre estarán abiertas para volver.\n"
                "🚪 ¡Hasta pronto, viajero!"
            )
            embed = discord.Embed(
                title="👋 Adiós, " + member.name,
                description=descripcion,
                color=discord.Color.red()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            await canal.send(embed=embed)


client.run(os.getenv("DISCORD_TOKEN"))
