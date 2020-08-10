#!/usr/bin/python3

# Creates a migration in the cwd

import time
import os
from pathlib import Path

whereami = Path(__file__).parent.absolute()
name = os.path.join(whereami, "migrations", str(time.time()) + ".sql")

Path(name).touch(exist_ok=True)

print("Created migration at: " + name)
