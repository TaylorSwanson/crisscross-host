# Host application for crisscross guests
# This runs on all crisscross agents

import os
from pathlib import Path

from Database import Database


# Make sure homestore is there
homestore = os.path.expanduser("~/.crisscross/")
os.makedirs(homestore, exist_ok=True)

# Initialize or load db
db = Database.getInstance()
db.connect(os.path.join(homestore, "store.db"))

for secret in db.getSecrets():
  print(secret)

db.close()
