import os
import hashlib

from dotenv import load_dotenv

"""
Por seguridad, se encriptan los datos de los usuarios. De esta forma, se refuerza la seguridad del bot
"""

load_dotenv()
SECRET_WORD = os.getenv("SECRET_WORD") #Palabra secreta para encriptar el id del usuario, guardada en .env

#Función que genera un id único para cada usuario partiendo del chat id
def generate_id(chat_id):
    bin_id = f"{chat_id}{SECRET_WORD}".encode()
    id = hashlib.sha256(bin_id).hexdigest()

    return id[:12]