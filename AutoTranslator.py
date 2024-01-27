#AutoTranslator from ABC Discord BitcoinJake09 7/15/2023
import discord
from discord import Intents
from googletrans import Translator
from Tvars import TOKEN, GENERAL_CHANNEL_ID, SPANISH_CHANNEL_ID, MANDARIN_CHANNEL_ID, FRENCH_CHANNEL_ID, GERMAN_CHANNEL_ID, RUSSIAN_CHANNEL_ID, ARABIC_CHANNEL_ID

translator = Translator()

# Define the languages and their respective channel IDs
language_channels = {
    "en": GENERAL_CHANNEL_ID,
    "es": SPANISH_CHANNEL_ID,
    "fr": FRENCH_CHANNEL_ID,
    "de": GERMAN_CHANNEL_ID,
    "ru": RUSSIAN_CHANNEL_ID,
    "ar": ARABIC_CHANNEL_ID,
    "zh-CN": MANDARIN_CHANNEL_ID
}

intents = Intents.default()
intents.guild_messages = True
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")

@bot.event
async def on_message(message):
    print("[AutoTranslater]")
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    # Check if the message is in a language-specific channel
    for src_lang, src_channel_id in language_channels.items():
        if message.channel.id == int(src_channel_id):
            content = message.content
            author = message.author.display_name
            source_channel = message.channel.name

            # Translate the message to other language channels
            for dest_lang, dest_channel_id in language_channels.items():
                if dest_lang == src_lang:
                    continue  # Skip translation to the same language

                translated = translator.translate(content, src=src_lang, dest=dest_lang).text

                # Find the target channel and send the translated message
                channel = discord.utils.get(message.guild.channels, id=int(dest_channel_id))
                await channel.send(f"**{author}** ({source_channel}): {translated}")

bot.run(TOKEN)  # Replace with your Discord bot token
