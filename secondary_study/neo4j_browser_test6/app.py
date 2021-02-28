from flask import Flask, request
from flask_cors import CORS
import pyautogui as pg

app = Flask(__name__)
app.debug = True
CORS(app)

@app.route('/')
def home():
  return "OK"

@app.route('/execute/')
def execute():
  query_box = pg.locateCenterOnScreen('screenshots/query_box.png')
  data = dict(request.args)
  query = data['query']
  pg.click(query_box.x, query_box.y)
  pg.typewrite(query)
  pg.sleep(0.1)
  pg.hotkey('enter')
  return "Executed"

if __name__=='__main__':
  app.run()