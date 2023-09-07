from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get("https://play2048.co/")

body = browser.find_element(By.TAG_NAME, "body")
# gamer_over = browser.find_element(By.CLASS_NAME, "game-over")
body.send_keys(Keys.DOWN)
body.send_keys(Keys.LEFT)
body.send_keys(Keys.RIGHT)
body.send_keys(Keys.UP)

counter = 0

while True:
    if counter != 2000:
        counter += 1
    else:
        break
    body.send_keys(Keys.DOWN)
    body.send_keys(Keys.LEFT)
    body.send_keys(Keys.RIGHT)
    body.send_keys(Keys.UP)

# browser.quit()