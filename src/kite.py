import logging
import urllib3
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# habilitar logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


class Kite(object):

    def __init__(self, token: str) -> None:
        self.token = token
        # Crear la aplicacion y pasar el Token
        self.application = Application.builder().token(token).build()
        # Añadiendo manejadores de comandos
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help))
        self.application.add_handler(CommandHandler("echo", self.echo))
        self.application.add_handler(CommandHandler("link", self.link))

    async def link(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        t = update.message.text
        url = urllib3.util.parse_url(t)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Muestra informacion de como se usa el bot."""

        reply_keyboard = [['download']]  # !Para crear los botones

        await update.message.reply_text(
            "Hola, mi nombre es Kite, estoy aqui para ayudarte "
            "envie un comando para empezar"
            "si tienes alguna duda al utilizar los comandos envia /help "
            "para obtener una lista completa.",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard,
                one_time_keyboard=True,
                input_field_placeholder=""
            )
        )

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Echo the user message."""
        await update.message.reply_text(update.message.text)

    async def run(self):
        """Ejecuta el bot"""
        try:
            self.application.run_polling()
        except Exception as ex:
            logger.error(ex)

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Muestra informacion de como se usa el bot."""
        await update.message.reply_text(
            """
            Lista de comando permitidos

            /help - Envie help para ver este mensaje nuevamente
            /start - Iniciar el bot
            /link - 
            """
        )
