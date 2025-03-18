from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class TesteShopee:
    def __init__(self):
        self.SITE_LINK = "https://shopee.com.br/"

        self.SITE_MAP = {
            "buttons": {
                "cadastrar": {
                    "xpath": "/html/body/div[1]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[3]/div/a"
                }
            },
            "inputs": {
                "telefone": {"xpath": "//input[@name='phone']"},
                "username": {"xpath": "//input[@name='username']"},
                "email": {"xpath": "//input[@name='email']"},
                "password": {"xpath": "//input[@name='password']"},
                "confirm_password": {"xpath": "//input[@name='confirm_password']"}
            },
            "submit": {
                "xpath": "//button[@type='submit']"
            }
        }

        chrome_driver_path = "C:\\chromedriver.exe"
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def abrir_site(self):
        self.driver.get(self.SITE_LINK)
        time.sleep(10)

    def realizar_cadastro(self):
        wait = WebDriverWait(self.driver, 15)  # Aumentado para 15 segundos

        # Clicar no botão "Cadastrar"
        wait.until(EC.element_to_be_clickable((By.XPATH, self.SITE_MAP["buttons"]["cadastrar"]["xpath"]))).click()
        time.sleep(5)

        # Esperar que o campo de telefone apareça
        wait.until(EC.visibility_of_element_located((By.XPATH, self.SITE_MAP["inputs"]["telefone"]["xpath"]))).send_keys("98 984627656")

        # Preenche os outros campos de cadastro
        wait.until(EC.visibility_of_element_located((By.XPATH, self.SITE_MAP["inputs"]["username"]["xpath"]))).send_keys("MeuUsuarioTeste")
        wait.until(EC.visibility_of_element_located((By.XPATH, self.SITE_MAP["inputs"]["email"]["xpath"]))).send_keys("teste123@email.com")
        wait.until(EC.visibility_of_element_located((By.XPATH, self.SITE_MAP["inputs"]["password"]["xpath"]))).send_keys("SenhaForte123!")
        wait.until(EC.visibility_of_element_located((By.XPATH, self.SITE_MAP["inputs"]["confirm_password"]["xpath"]))).send_keys("SenhaForte123!")

        # Clicar no botão "Registrar"
        wait.until(EC.element_to_be_clickable((By.XPATH, self.SITE_MAP["submit"]["xpath"]))).click()
        time.sleep(5)


shopee = TesteShopee()
shopee.abrir_site()
shopee.realizar_cadastro()
