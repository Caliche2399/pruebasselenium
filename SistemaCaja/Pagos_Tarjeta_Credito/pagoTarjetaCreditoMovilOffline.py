from seleniumbase import BaseCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#Constantes
URL_SELENIUM = 'http://192.168.50.146:4444'
USUARIO = 'CAR4173AT'
CONTRASEÑA = 'CalichE33'
URL_WEBSISATEL = 'http://192.168.50.61:7002/WSEG_0001/faces/jsflogin.xhtml'
NUMERO_CUENTA = '772908134'
NUMERO_TARJETA = '4111111111111111'
CVV = '123'
FECHA_EXPIRACION = '052025'

#Configuración del driver
chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('se:name','Prueba Pago Tarjeta Credito Movil Offline' )

driver = webdriver.Remote(command_executor = URL_SELENIUM, options = chrome_options)
driver.maximize_window()
driver.get(URL_WEBSISATEL)

#Clase encargada de correr las pruebas
class PagoTarjetaCreditoMovilOffline(BaseCase):
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
            driver.find_element(by= By.ID, value='frmSeleccionModo:j_idt17').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmBusquedaServicio:j_idt33').send_keys(NUMERO_CUENTA)

            sleep(2)
            driver.find_element(by= By.ID, value='frmBusquedaServicio:btnBuscar').click()

            listadoTabla = driver.find_elements(by= By.TAG_NAME, value="td")

            for opcion in listadoTabla:
                if(opcion.text == "MOVIL"):
                    opcion.click() 

            sleep(2)
            driver.find_element(by= By.ID, value='frmMetodoPagoOffline:itNumeroTarjeta').send_keys(NUMERO_TARJETA)

            sleep(2)
            driver.find_element(by= By.ID, value='frmMetodoPagoOffline:itFecha').send_keys(FECHA_EXPIRACION)

            sleep(2)
            driver.find_element(by= By.ID, value='frmMetodoPagoOffline:CCV').send_keys(CVV)

            sleep(2)
            driver.find_element(by= By.ID, value='frmDatosFacturacion:itNombre').send_keys('TEST')

            sleep(2)
            driver.find_element(by= By.ID, value='frmDatosFacturacion:itApellido').send_keys('TEST')

            sleep(2)
            driver.find_element(by= By.ID, value='frmDatosFacturacion:imTelefono').send_keys('8485432222')

            sleep(2)
            driver.find_element(by= By.ID, value='frmDatosFacturacion:itCodigoPostal').clear()

            sleep(2)
            driver.find_element(by= By.ID, value='frmDatosFacturacion:itCodigoPostal').send_keys('01522')

            sleep(2)
            driver.find_element(by= By.ID, value='frmDatosFacturacion:itObservaciones').send_keys('OBSERVACIONES PAGO OFFLINE MOVIL')

            sleep(2)
            driver.find_element(by= By.ID, value='j_idt229').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmDlgConfirmaPago:btAceptarPago').click()

            sleep(5)
            driver.find_element(by= By.ID, value='frmDlgPagoExitoso:j_idt295').click()


            #Se guarda un screenshot al terminar la prueba
            sleep(5)
            driver.save_screenshot('Prueba_Exitosa_PagoTarjetaCreditoMovilOffline.png')
            print("Se realizó la prueba correctamente.")

            sleep(3)
            cerrarSesion()

        except Exception:
            sleep(2)
            driver.save_screenshot('Prueba_Fallida_PagoTarjetaCreditoMovilOffline.png')
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
            if(opcionMenu.text == "CAJA"):
                opcionMenu.click() 

        for aplicacionMenu in listadoMenu:
            if(aplicacionMenu.text == "PAGOS CON TARJETA DE CREDITO"):
                aplicacionMenu.click()
                
    except Exception:
        print("Sucedió un error al momento de seleccionar la aplicación del menu")

