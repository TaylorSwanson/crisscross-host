# Talks with the guest application

from lib.bottle import route, run
from Database import Database

db = Database.getInstance()

@route("/api")
def api():
  return "API is available for your application"

@route("/secrets")
def secrets():
  return " ".join(db.getSecrets())
  

def start():
  run(host="localhost", port=5006)
