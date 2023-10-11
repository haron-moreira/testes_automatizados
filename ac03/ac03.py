from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


navegador = webdriver.Edge()

navegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

time.sleep(2)
cep = '88701260' # minha antiga residencia kkkkk

caixa = navegador.find_element(By.NAME, 'endereco')
caixa.send_keys(cep)
caixa.submit()

button = navegador.find_element(By.XPATH, "//button[text()='Buscar']")
button.click()

table = navegador.find_element(By.ID, "resultado-DNEC")

time.sleep(3)

endereco = table.find_element(By.XPATH, ".//tbody/tr[1]/td[1]").text
bairro = table.find_element(By.XPATH, ".//tbody/tr[1]/td[2]").text
cidade = table.find_element(By.XPATH, ".//tbody/tr[1]/td[3]").text

navegador.close()
navegador.quit()

os.system('cls' if os.name == 'nt' else 'clear')
print(f"Logradouro: {endereco}, Bairro: {bairro}, Cidade: {cidade}")