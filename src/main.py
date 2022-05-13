from kite import Kite
import os

from zipmanager import ZipManager

#Get token from heroku
TOKEN = os.getenv('TOKEN')

if __name__ == "__main__":
    kite = Kite(TOKEN)
    kite.run()
