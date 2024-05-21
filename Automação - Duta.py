import pyautogui
import time

pyautogui.PAUSE = 2  


# Abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(3)
pyautogui.press("enter")
time.sleep(5)
pyautogui.hotkey("ctrl", "t")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)


# Fazer login
pyautogui.press("tab")
pyautogui.write("dutinhapressaum@gmail.com")
pyautogui.press("tab")
pyautogui.write("dutinha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)


# Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")


# Cadastrar 1 produto
for linha in tabela.index:

    pyautogui.press("tab")

    # codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) 
    pyautogui.press("tab")

    # preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Obs 
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")

    # voltar ao inicio
    for i in range(8):
        pyautogui.hotkey("shift", "tab")