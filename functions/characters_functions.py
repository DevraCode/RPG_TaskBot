from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler


import data.persistence as persistence
from functions.basic_functions import generate_id


""" persistence.CHARACTER[user_id] = {
             'character_id': "",
             'character_name':user,
             'charatcer_img': "",
             'character_type':"",
             'character_exp': 0,
             'character_level': 0
        } """


async def male_mage(update:Update,context):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)
    user = update.effective_user.first_name

    #persistence.CHARACTER[user_id]['character_id'] = "01"

    persistence.CHARACTER[user_id] = {
             'character_id': "01",
             'character_name':user,
             'character_img': "assets/characters/mage/male_mage_01.webm",
             'character_type':"male_mage",
             'character_exp': 0,
             'character_level': 0
    }

    await context.bot.send_sticker(chat_id = chat_id, sticker = persistence.CHARACTER[user_id]['character_img'])



#Función para mostrar la galeria de personajes
async def show_characters(update:Update,context:CallbackContext):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)

    keyboard = []

    #Se comprueba que el usuario existe, si existe, se le muestra la galeria
    if user_id not in persistence.CHARACTER[user_id]:
        await context.bot.send_message(chat_id=chat_id, text=f"Debes registrarte primero")

    else:
        
        buttons = [
            InlineKeyboardButton("Next", callback_data="NEXT")
        ]

        keyboard.append(buttons)
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(show_male_mage(), reply_markup=reply_markup)

