from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


import pyperclip
import time
import os

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get('https://web.whatsapp.com/')

time.sleep(40)



mensagem = """
Olá, tudo bem? Estou fazendo um teste de automação de mensagens no whatsapp.
Caso tenha recebido essa mensagem, por favor, me responda para que eu possa saber se funcionou.
Obrigado!
"""

lista_contatos = ['Opcao 2', 'Opcao 3', 'Opcao 4', 'Opcao 5', 'Eu e eu', 'José Leandro Vilela']

#enviar mensagem para o meu propio numero para depois encaminhar
#clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
#digitar o nome do contato
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys("Vilelajlimports")
#dar enter
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys(Keys.ENTER)
time.sleep(2)

#digitar a mensagem
pyperclip.copy(mensagem)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + "v")
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)




qtde_contatos = len(lista_contatos)

if qtde_contatos % 5 == 0:
    qtde_blocos = qtde_contatos / 5
else:
    qtde_blocos = int(qtde_contatos / 5) + 1


for i in range(qtde_blocos):
    #rodar o codigo de encaminhar
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]

    #selecionar quem vai receber a mensagem
    list_elements = nav.find_elements('class name', '_amk4')
    for item in list_elements:
        mensagem = mensagem.replace('\n', "")
        texto = item.text.replace('\n', "")
        if mensagem in texto:
            elemento = item
            

    #selecionar a mensagem para enviar
    ActionChains(nav).move_to_element(elemento).perform()
    elemento.find_element('class name', '_ahkm').click()
    time.sleep(0.5)
    #encaminhar para os outros contatos
    nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[4]/div').click()
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[5]/span').click()
    time.sleep(1)

    for nome in lista_enviar:
        #selecionar os 5 contatos para enviar
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/p').send_keys(nome)
        time.sleep(0.7)
        #dar enter
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/p').send_keys(Keys.ENTER)
        time.sleep(0.5)
        #apagar nome do contato
        
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/p').send_keys(Keys.BACKSPACE)
        time.sleep(0.5)
    
    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div').click()
    time.sleep(3)