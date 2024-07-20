from selenium.webdriver import Firefox
from behave import given,when,then
from selenium.webdriver.common.by import By
import requests
import time

@given(u'usuário estar na area de cadastro')
def step_click_cadastre_se(context):
    browser_title = context.browser.title
    assert "Joga Junto" in browser_title, "titulo nao encontrado"
    btn_cadastre_se = context.browser.find_element(By.XPATH,"/html/body/div/main/form/div[6]/span[2]/a")
    btn_cadastre_se.click()

@when(u'o usuário preencher os campos com as credenciais')
def step_fill_cadastro(context):
    context.browser.find_element(By.NAME, "email").send_keys(context.email)
    context.browser.find_element(By.NAME,"password").send_keys(context.password)
    context.browser.find_element(By.NAME,"confirmPassword").send_keys(context.password)

@when(u'clicar no botão "criar conta"')
def step_submit_cadastro(context):
    btn_cadastro = context.browser.find_element(By.XPATH," /html/body/div/div/form/button")
    btn_cadastro.submit()
   
@then(u'o usuário cadastra com sucesso')
def step_cadastro_sucess(context):
    response = requests.get("https://projetofinal.jogajuntoinstituto.org/register")
    if response.status_code == 200 or response.status_code == 201:
        time.sleep(3)
        link_entrar = context.browser.find_element(By.XPATH, "/html/body/div/div/form/span/a")
        link_entrar.click()
    time.sleep(10)