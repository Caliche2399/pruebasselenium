from seleniumbase import BaseCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#Constantes
URL_SELENIUM = 'http://192.168.50.146:4444'
USUARIO = 'CAR4173AT'
CONTRASEÑA = 'CalichE33'
URL_WEBSISATEL = 'http://192.168.50.61:7002/WSEG_0001/faces/jsflogin.xhtml'
NUMERO_MEMBRESIA = '788084666'
NOMBRE_SOLICITUD_ASOCIAR = 'MARIA'
APELLIDO_SOLICITUD_ASOCIAR = 'VICENTE CHO'

#Configuración del driver
chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('se:name','Prueba Envio SMS' )

driver = webdriver.Remote(command_executor = URL_SELENIUM, options = chrome_options)
driver.maximize_window()
driver.get(URL_WEBSISATEL)

#Clase encargada de correr las pruebas
class asociacionMembresia(BaseCase):
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
            driver.find_element(by= By.ID, value='frmMonitoreoSolicitudes:txtNoMembresia').send_keys(NUMERO_MEMBRESIA)
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmMonitoreoSolicitudes:btnBuscar').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmMonitoreoSolicitudes:tvResultados:tblResultados:btnAsociacion').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmAsociacionMembresiasMonitoreo:j_idt19:txtNombre').send_keys(NOMBRE_SOLICITUD_ASOCIAR)
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmAsociacionMembresiasMonitoreo:j_idt19:txtApellido').send_keys(APELLIDO_SOLICITUD_ASOCIAR)
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmAsociacionMembresiasMonitoreo:j_idt19:btnBuscar').click()
        
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='.ui-picklist-item > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1)').click()
        
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='#frmAsociacionMembresiasMonitoreo\:j_idt19\:sorDatoConfirmacion > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > div:nth-child(1) > div:nth-child(2)').click()
        
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='button.ui-button-icon-only:nth-child(1)').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmAsociacionMembresiasMonitoreo:btnGuardarCambios').click()


            #Se guarda un screenshot al terminar la prueba
            sleep(5)
            driver.save_screenshot('Prueba_Exitosa_AsociacionMembresia.png')
            print("Se realizó la prueba correctamente.")

            cerrarSesion()

        except Exception:
            sleep(2)
            driver.save_screenshot('Prueba_Fallida_AsociacionMembresia.png')
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
            if(opcionMenu.text == "TARJETA VISA LOCAL"):
                opcionMenu.click() 

        for aplicacionMenu in listadoMenu:
            if(aplicacionMenu.text == "MONITOREO MEMBRESIAS"):
                aplicacionMenu.click()
                
    except Exception:
        print("Sucedió un error al momento de seleccionar la aplicación del menu")

