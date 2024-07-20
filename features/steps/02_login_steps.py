from behave import given,when,then
from selenium.webdriver.common.by import By
import requests
import json
import time

@given(u'ao usuário estar na página de login')
def step_on_login(context):
    browser_title = context.browser.title
    assert "Joga Junto" in browser_title, "titulo nao encontrado"

@when(u'o usuário preencher os campos com as credenciais corretas')
def step_fill_login(context):
    time.sleep(3)
    context.browser.find_element(By.NAME, "email").send_keys(context.email)
    context.browser.find_element(By.NAME, "password").send_keys(context.password)

@when(u'clicar no botão "iniciar sessão"')
def step_submit_login(context):
    btn_login = context.browser.find_element(By.XPATH, "/html/body/div/main/form/button")
    btn_login.submit()

@then(u'o usuário loga com sucesso')
def step_login_sucess(context):
    response = requests.get("https://projetofinal.jogajuntoinstituto.org/")
    if response.status_code == 200 or response.status_code == 201:
        with open('reposta_login.txt', 'w') as file:
            file.write(f"O status da request foi {response.status_code}")   