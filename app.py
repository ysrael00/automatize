from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui as py

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# Abre a URL especificada
driver.get('https://precos-de-produtos.netlify.app/')
sleep(5)  # Aguarda 5 segundos para garantir que a página seja carregada

# Rola a página para baixo até o final para carregar mais produtos
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(5)  # Aguarda alguns segundos para que o conteúdo seja carregado

# Encontra o botão "Carregar Mais" usando XPath
botao_carregar_mais = driver.find_element(By.XPATH, "//button[@id='loadMoreButton']")
sleep(2)  # Aguarda 2 segundos para garantir que o botão esteja visível

# Clica no botão "Carregar Mais"
botao_carregar_mais.click()
sleep(2)  # Aguarda 2 segundos para que os novos itens sejam carregados

# Rola a página para baixo novamente para carregar mais produtos
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(2)  # Aguarda 2 segundos para garantir que o conteúdo seja carregado

# Rola de volta para o topo da página
driver.execute_script('window.scrollTo(0, 0);')
sleep(2)  # Aguarda 2 segundos

sleep(2)
# 5 -- Clicar em Subir planilha de preços
botao_carregar_planilha_de_produtos = driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-custom']")
sleep(2)
botao_carregar_planilha_de_produtos.click()
sleep(5)
# 6 -- Carregar planilha "precos-produtos-atualizados.xlsx"
py.write(r'C:\Users\ysrae\Downloads\precos-produtos-atualizados.xlsx')
sleep(2)
py.press('enter')
input('Aperte enter no terminal para fechar o programa')



