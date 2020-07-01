from selenium import webdriver
from time import sleep
from tkinter import Tk, Label, Button, Entry

root = Tk()
root.title("Whatsapp Bot")
contatos = []

#Definindo as funções (ações) dos botões:
def addcadaContato():
    #Testa se o input está vazio e, se não estiver, adiciona o contato à lista:
    if nomeContato.get() != '':
        contatos.append(nomeContato.get())
        nomeContato.delete(first=0, last=len(nomeContato.get()))
    else:
        pass

def entrarEnviar():
    #Testa se o input do usuário está vazio por garantia e adiciona o último input à lista:
    if nomeContato.get() not in contatos and nomeContato.get() != '':
        contatos.append(nomeContato.get())
    else:
        pass
    
    webdriver.ChromeOptions().add_argument("lang=pt-br")
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    sleep(20)
    
    for cadaContato in contatos:
        
        pesquisaContatos = driver.find_element_by_xpath("//span[@data-icon='chat']")
        sleep(3)
        pesquisaContatos.click()

        barraPesquisa = driver.find_element_by_class_name('_3FRCZ')
        sleep(3)
        barraPesquisa.click()
        barraPesquisa.send_keys(f"{cadaContato}")
        sleep(3)

        contato = driver.find_element_by_xpath(f"//span[@title='{cadaContato}']")
        sleep(3)
        contato.click()

        mensagem = driver.find_element_by_class_name('_3uMse')
        sleep(3)
        mensagem.click()
        mensagem.send_keys(f"{inputMensagem.get()}")

        botao = driver.find_element_by_xpath("//span[@data-icon='send']")
        sleep(3)
        botao.click()
        sleep(5)
    
    driver.quit()
    contatos.clear()
    
#Criando a interface gráfica do programa:
labelContato = Label(root, text="Informe o nome do contato para o qual deseja enviar a mensagem:")
labelContato.grid(row=0, column=0, padx=(20, 10), pady=(10, 0))

nomeContato = Entry(root, width=50, borderwidth=3)
nomeContato.grid(row=1, column=0, padx=(0, 30), pady=(5, 0))

botaoAdd = Button(root, text="+ 1", command=addcadaContato)
botaoAdd.grid(row=1, column=0, padx=(325, 10), pady=(5, 0))


labelMensagem = Label(root, text="Digite a mensagem que deseja enviar:")
labelMensagem.grid(row=2, column=0, padx=(20, 10), pady=(10, 0))

inputMensagem = Entry(root, width=50, borderwidth=3)
inputMensagem.grid(row=3, column=0, padx=(0, 30), pady=(5, 0))

botaoEnviar = Button(root, text="Entrar e Enviar", command=entrarEnviar)
botaoEnviar.grid(row=4, column=0, pady=(6, 10))

root.mainloop()
