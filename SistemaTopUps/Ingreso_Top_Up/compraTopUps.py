from seleniumbase import BaseCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime

#Constantes
URL_SELENIUM = 'http://192.168.50.146:4444'
USUARIO = 'CAR4173AT'
CONTRASEÑA = 'CalichE33'
URL_WEBSISATEL = 'http://192.168.50.61:7002/WSEG_0001/faces/jsflogin.xhtml'
CLIENTE_UNICO = '15624079'
TELEFONO_TOPUP = '58504820'

#Configuración del driver
chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('se:name','Prueba Compra Top-Up' )

driver = webdriver.Remote(command_executor = URL_SELENIUM, options = chrome_options)
driver.maximize_window()
driver.get(URL_WEBSISATEL)

#Clase encargada de correr las pruebas
class compraTopUp(BaseCase):
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
            driver.find_element(by= By.ID, value='frmIngresaRecarga:imClienteUnico').send_keys(CLIENTE_UNICO)

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresaRecarga:pnlDatosCompra_content').click()

            sleep(5)
            driver.find_element(by= By.ID, value='frmIngresaRecarga:somPaisOperador').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresaRecarga:somPaisOperador_2').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresaRecarga:somOperadores').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresaRecarga:somOperadores_2').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresaRecarga:somCategoria').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresaRecarga:somCategoria_1').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresaRecarga:somProductos').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresaRecarga:somProductos_1').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresaRecarga:imTelefonoReceptor').send_keys(TELEFONO_TOPUP)

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresaRecarga:btnAgregar').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmDetalleRecargas:btnProcesar').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmDetalleRecargas:j_idt121').click()

            #Se guarda un screenshot al terminar la prueba
            sleep(2)
            driver.save_screenshot('Prueba_Exitosa_CompraTopUp.png')
            print("Se realizó la prueba correctamente.")

            cerrarSesion()

        except Exception:
            sleep(2)
            driver.save_screenshot('Prueba_Fallida_CompraTopUp.png')
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
            if(opcionMenu.text == "TOP-UPS"):
                opcionMenu.click() 

        for aplicacionMenu in listadoMenu:
            if(aplicacionMenu.text == "INGRESO Y PROCESO DE TOP-UPS"):
                aplicacionMenu.click()
                
    except Exception:
        print("Sucedió un error al momento de seleccionar la aplicación del menu")

