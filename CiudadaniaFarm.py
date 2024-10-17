import requests
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Setup de navegador

browserDriver = webdriver.Chrome("C:/Users/Flori/Desktop/Cucu/Cosas/msedgedriver.exe")
browserDriver.get("https://prenotami.esteri.it/Home?ReturnUrl=%2fServices")

# Iniciar sesión

email = ""
contraseña = ""

input_email = '//*[@id="login-email"]'
input_contraseña = '//*[@id="login-password"]'

browserDriver.find_element(By.XPATH, input_email).send_keys(email)
browserDriver.find_element(By.XPATH, input_contraseña).send_keys(contraseña)

iniciarSesion = browserDriver.find_element(By.XPATH , '//*[@id="login-form"]/button')
iniciarSesion.click()

time.sleep(2)

# Hacer click en el botón de reserva

boton = browserDriver.find_element(By.XPATH,'//*[@id="dataTableServices"]/tbody/tr[3]/td[4]/a/button')
boton.click()

# Función que retorna true si se accedió al formulario, y false si no.

def validacion():
    try:
        browserDriver.find_element(By.ID, "jconfirm-box96825")
    except:
        return False

    return True

# Si se pudo acceder al formulario, se ingresan los datos

if(validacion()):
    print("Entré c:")

else:
    print("No entré :c")


