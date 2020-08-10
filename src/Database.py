# Does db work

import sqlite3

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
      raise Exception("Cannot create multiple Database class instances, use Database.getInstance instead")
    else:
      Database.__instance = self
  
  def connect(self, path):
    if self.conn != None:
      raise Exception("Database connection already open")

    self.path = path
    self.conn = sqlite3.connect(path)

    print("Opened database at: " + path)
    

  # def migrate(self):
  #   # Run all migration scripts

