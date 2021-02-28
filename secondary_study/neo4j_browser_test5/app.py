from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)
app.debug = True

chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument("--kiosk")

@app.route('/')
def home():
  driver = webdriver.Chrome(options=chromeOptions)
  driver.implicitly_wait(10)
  select = driver.find_element_by_css_selector
  driver.get("http://localhost:8003")
  select("input[data-testid='username']").send_keys("neo4j")
  select("input[data-testid='password']").send_keys("testing321")
  select("button[type='submit']").click()
  select("button[type='submit']").click()
  select("pre.CodeMirror-line[role='presentation']").click()
  select("body").send_keys("Hello")

  return "OK"

if __name__=='__main__':
  app.run()