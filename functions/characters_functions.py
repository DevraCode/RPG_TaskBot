from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler


import data.persistence as persistence
from functions.basic_functions import generate_id

def generate_character_id(character):
    character_list = ["male_warrior","female_warrior","male_mage","female_mage"]

    if character in character_list:
        return character_list.index(character) + 1
        

async def show_male_mage(update:Update,context):
    chat_id = update.effective_chat.id
    await context.bot.send_sticker(chat_id = chat_id, sticker = "assets/characters/mage/female_mage_01.webm")



#Función para mostrar la galeria de personajes
async def show_characters(update:Update,context:CallbackContext):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)

    keyboard = []

    #Comprobar que el usuario existe
    if user_id not in persistence.CHARACTER[user_id]:
        await context.bot.send_message(chat_id=chat_id, text=f"Debes registrarte primero")

    else:
        
        buttons = [
            InlineKeyboardButton("Next", callback_data="NEXT")
        ]

        keyboard.append(buttons)
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(show_male_mage(), reply_markup=reply_markup)




