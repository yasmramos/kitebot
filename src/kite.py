#!/usr/bin/env python
# pylint: disable=unused-argument

import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# habilitar logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

class Kite(object):

    def __init__(self, token: str) -> None:
        self.token = token
        #Crear la aplicacion y pasar el Token
        self.application = Application.builder().token(token).build()
        #Añadiendo manejadores de comandos
        self.application.add_handler(CommandHandler(["start", "help"], self.start))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Envia explicacion de como se usa el bot."""
        await update.message.reply_text("Hi! Use /help to get all comands")
    
    async def run(self):
        """Ejecuta el bot"""
        self.application.run_polling()