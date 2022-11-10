from seleniumbase import BaseCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime, timedelta

#Constantes
URL_SELENIUM = 'http://192.168.50.146:4444'
USUARIO = 'CAR4173AT'
CONTRASEÑA = 'CalichE33'
URL_WEBSISATEL = 'http://192.168.50.61:7002/WSEG_0001/faces/jsflogin.xhtml'
NUMERO_SOLICITUD = '778551745'

#Configuración del driver
chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('se:name','Prueba Asignacion SIM' )

driver = webdriver.Remote(command_executor = URL_SELENIUM, options = chrome_options)
driver.maximize_window()
driver.get(URL_WEBSISATEL)

#Clase encargada de correr las pruebas
class AsignacionSIM(BaseCase):
    def runTest(self):  
        try:
            #Se inicia sesion en WebSisAtel
            iniciarSesion()

            #Se selecciona la aplicación en el menu
            seleccionarAplicacionMenu()

            sleep(1.5)
            #Se realiza un cambio al iframe de la aplicación
            iFramePanel = driver.find_element(by= By.CSS_SELECTOR,value='#Contenido>iframe')
            driver.switch_to.frame(iFramePanel)
        
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='#frmBuscarSim\:selectEstadosSim > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmBuscarSim:btnBuscar').click()

            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='tr.ui-widget-content:nth-child(1)').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmBotonesComando:btnAsignar').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmAsignarCuenta:numeroCuentaBusqueda').send_keys(NUMERO_SOLICITUD)
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmAsignarCuenta:buscarCuenta').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmAsignarCuenta:latitudUbicacion').send_keys('11')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmAsignarCuenta:longitudUbicacion').send_keys('11')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmAsignarCuenta:asignarSimCuenta').click()


            #Se guarda un screenshot al terminar la prueba
            sleep(10)
            driver.save_screenshot('Prueba_Exitosa_AsignacionSIM.png')
            print("Se realizó la prueba correctamente.")

            sleep(4)
            cerrarSesion()

        except Exception:
            sleep(2)
            driver.save_screenshot('Prueba_Fallida_AsignacionSIM.png')
            print("Sucedió un error en la prueba")
            cerrarSesion()





#Método encargado de cerrar sesion del WebSisAtel
def cerrarSesion():
    print('Cerrando sesion del WebSisAtel')
    driver.switch_to.default_content()
    driver.find_element(by= By.ID, value = "iconosalir").click()

    print('Se cerró sesion del WebSisAtel')
    #Se cierra la sesion de Selenium
    driver.quit()

#Método encargado de iniciar sesion en WebSisAtel
def iniciarSesion():
    print("Iniciando Sesion")
    driver.find_element(by = By.ID, value="frmLogin:intextUsername").send_keys(USUARIO)
    driver.find_element(by = By.ID, value="frmLogin:intextPassword").send_keys(CONTRASEÑA)
    driver.find_element(by = By.NAME, value="frmLogin:btnAceptar").click()

def seleccionarAplicacionMenu():

    try:
        driver.find_element(by= By.CLASS_NAME, value='layout-tabmenu-nav').click()

        listadoMenu = driver.find_elements(by= By.TAG_NAME, value="li")

        for opcionMenu in listadoMenu:
            if(opcionMenu.text == "SERVICIO DE INTERNET RESIDENCIAL"):
                opcionMenu.click() 

        for aplicacionMenu in listadoMenu:
            if(aplicacionMenu.text == "MODIFICACION SIM ENRUTADOR"):
                aplicacionMenu.click()
                
    except Exception:
        print("Sucedió un error al momento de seleccionar la aplicación del menu")

