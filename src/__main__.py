
# Host application for crisscross guests
# This runs on all crisscross agents

import os
import pathlib

from Database import Database


# Make sure homestore is there
homestore = os.path.expanduser("~/.crisscross/")
os.makedirs(homestore, exist_ok=True)

print(homestore)

# Initialize or load db
db = Database.getInstance()
db.connect(os.path.join(homestore, "store.db"))


