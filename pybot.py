from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://web.whatsapp.com/')

quant = int(input('Digite a quantidade'))
mensagem = input('Qual Mensagem voce deseja enviar')

for i in range(quant):
    time.sleep(5)
    chamada = driver.find_element_by_xpath('//div[contains(@class,"ZKn2B")]') 
    chamada.click()

    




#clicar na mensagem não lida
#<div class="ZKn2B"><span class="_31gEB" aria-label="1 mensagem não lida">1</span></div>

#campo de mensagem
#<div class="_3FRCZ copyable-text selectable-text" contenteditable="true" data-tab="1" dir="ltr" spellcheck="true"></div>