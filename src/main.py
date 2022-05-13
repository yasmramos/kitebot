from kite import Kite
import os

from zipmanager import ZipManager

TOKEN = os.getenv('TOKEN')

if __name__ == "__main__":
    kite = Kite(TOKEN)
    kite.run()
