# Database to store data across crashes and restarts

import sqlite3
import os
import time
from pathlib import Path

class Database:
  # Singleton class
  __instance = None
  conn = None

  @staticmethod
  def getInstance():
    if Database.__instance == None:
      Database()
    return Database.__instance
    
  # Private constructor
  def __init__(self):
    if Database.__instance != None:
      raise Exception("""Cannot create multiple Database class instances, \
use Database.getInstance instead""")
    else:
      Database.__instance = self

  def close(self):
      self.conn.commit()
      self.conn.close()
  
  def connect(self, path):
    if self.conn != None:
      raise Exception("Database connection already open")

    self.path = path
    self.conn = sqlite3.connect(path)

    print("Opened database at: " + path)

    self.initDatabase()
    


  def initDatabase(self):
    c = self.conn.cursor()

    c.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='config';")
    
    exists = c.fetchone() != None

    if exists:
      return
    
    
    print("Database doesn't exist, creating now...")

    # Execute the schema file to populate db
    whereami = Path(__file__).parent.absolute()
    schemapath = os.path.join(whereami, "schema.sql")

    with open(schemapath, "r") as fh:
      script = "".join(fh.readlines())

      c.executescript(script)

      self.conn.commit()
    
  

  def setSecret(self, name, value):
    name = name.lower()
    c = self.conn.cursor()

    c.execute("SELECT 1 FROM secrets WHERE name=?;", (name.lower(), ))
    exists = c.fetchone() != None
    
    now = round(time.time())

    if exists:
      c.execute("UPDATE secrets SET value=? WHERE name=?;", (value, name))
      c.execute("UPDATE secrets SET updated=? WHERE name=?;", (now, name))
    else:
      val = (name, value, now)
      c.execute("INSERT INTO secrets (name, value, updated) VALUES (?,?,?);", val)

    self.conn.commit()


  def setConfig(self, setting, value):
    setting = setting.lower()
    c = self.conn.cursor()

    c.execute("SELECT 1 FROM config WHERE setting=?;", (setting,))
    exists = c.fetchone() != None
    
    now = round(time.time())

    if exists:
      c.execute("UPDATE config SET value=? WHERE setting=?;", (value, setting))
      c.execute("UPDATE config SET updated=? WHERE setting=?;", (now, setting))
    else:
      val = (setting, value, now)
      c.execute("INSERT INTO config (setting, value, updated) VALUES (?,?,?);", val)

    self.conn.commit()


  # Returns iterable of secrets
  def getSecrets(self):
    c = self.conn.cursor()

    return c.execute("SELECT name, value FROM secrets;")
  
  # Returns iterable of secrets
  def getConfig(self):
    c = self.conn.cursor()

    return c.execute("SELECT setting, value FROM config;")

  def deleteSecret(self, name):
    name = name.lower()

    c = self.conn.cursor()
    c.execute("DELETE FROM secrets WHERE name=?;", (name,))
    self.conn.commit()

  def deleteConfig(self, setting):
    setting = setting.lower()

    c = self.conn.cursor()
    c.execute("DELETE FROM config WHERE setting=?;", (setting,))
    self.conn.commit()
