from selenium.webdriver import Firefox
import time

def before_all(context):
    context.browser = Firefox()
    context.browser.get("https://projetofinal.jogajuntoinstituto.org/")
    context.email = "hermesteste4@gmail.com"
    context.password = "senha123"

def after_all(context):
    time.sleep(5)
    context.browser.quit()