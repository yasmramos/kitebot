#!/usr/bin/env python
# pylint: disable=unused-argument

from kite import Kite
import os

TOKEN = os.getenv('TOKEN')

if __name__ == "__main__":
    kite = Kite(TOKEN)
    kite.run()