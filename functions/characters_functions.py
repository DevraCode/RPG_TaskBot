

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMedia
from telegram.ext import CallbackContext, ConversationHandler

from telegram.constants import ParseMode

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
import data.persistence as persistence
from functions.basic_functions import generate_id
from functions.characters_data import male_warrior_01, female_warrior_01, male_mage_01, female_mage_01
#from functions.characters_data import male_warrior, female_warrior, male_mage, female_mage

character_list = [male_warrior_01,female_warrior_01,male_mage_01,female_mage_01]


#Función que SOLO MUESTRA la galeria de personajes
async def show_characters(update:Update,context:CallbackContext):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)

    keyboard = []

    #Se comprueba que el usuario existe, si existe, se le muestra la galeria
    if user_id not in persistence.REGISTERED_USERS:
        await context.bot.send_message(chat_id=chat_id, text=f"Debes registrarte primero")

    #Botones de Anterior, Siguiente y Seleccionar
    else:

        index = 0
        keyboard = [
            [
                InlineKeyboardButton("Previous", callback_data=f"PREV_{index}"),
                InlineKeyboardButton("Next", callback_data=f"NEXT_{index}")
            ],
            [InlineKeyboardButton("Select", callback_data=f"SELECT_{index}")]
        ]
    
        reply_markup = InlineKeyboardMarkup(keyboard)
        

        #Se muestra el primer personaje de la lista, y con los botones pasaremos a los demás
        await context.bot.send_sticker(
        chat_id=chat_id, 
        sticker=character_list[index],
        reply_markup=reply_markup
    )

        


