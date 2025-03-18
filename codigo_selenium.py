from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# abrir navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("http://www.shopee.com.br")

# colocar o navegador em tela cheia
navegador.maximize_window()

# selecionar um elemento na tela
botao_cadastrar = navegador.find_element(By.CLASS_NAME, "JOxeOr")

# clicar em um elemento
botao_cadastrar.click()

time.sleep(10)