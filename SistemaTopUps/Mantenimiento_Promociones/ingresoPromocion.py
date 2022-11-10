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


#Configuración del driver
chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('se:name','Prueba Ingreso Promocion TopUp' )

driver = webdriver.Remote(command_executor = URL_SELENIUM, options = chrome_options)
driver.maximize_window()
driver.get(URL_WEBSISATEL)

#Clase encargada de correr las pruebas
class ingresoPromocionTopUp(BaseCase):
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
        
            sleep(0.5)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:selOneMenuTiposPromocion').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:selOneMenuTiposPromocion_1').click()

            sleep(5)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:selOneMenuPais').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:selOneMenuPais_2').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:selOneMenuOperador').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:selOneMenuOperador_5').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:descripcion').send_keys('PRUEBA SELENIUM')

            sleep(2)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:itMontoMinimo').send_keys('10')

            sleep(2)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:itMontoMaximo').send_keys('20')

            sleep(2)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:fechaInicialVigencia_input').click()

            diaInicioPromocion = datetime.now().strftime('%d')
            listadoDatePicker = driver.find_elements(by= By.TAG_NAME, value="td")

            for opcionFecha in listadoDatePicker:
                if(opcionFecha.text == diaInicioPromocion):
                    opcionFecha.click() 

            sleep(2)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:fechaFinalVigencia_input').click()

            diaFinalPromocion = datetime.now() + timedelta(days=5)
            diaFinalPromocion = diaFinalPromocion.strftime('%d')
            listadoDatePickerFinal = driver.find_elements(by= By.TAG_NAME, value="td")

            for opcionFechaFinal in listadoDatePickerFinal:
                if(opcionFechaFinal.text == diaFinalPromocion):
                    opcionFechaFinal.click() 

            sleep(2)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:observacionesdetalle1').send_keys('PRUEBA PROMOCION SELENIUM')

            sleep(2)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:btnAgregaObservaciones').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmMantenimientoPromociones:btnMostrarConfirmationDialog').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmConfirmacionIngreso:btnEjectuar').click()

            #Se guarda un screenshot al terminar la prueba
            sleep(2)
            driver.save_screenshot('Prueba_Exitosa_IngresoPromocion.png')
            print("Se realizó la prueba correctamente.")

            cerrarSesion()

        except Exception:
            sleep(2)
            driver.save_screenshot('Prueba_Fallida_IngresoPromocion.png')
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
            if(aplicacionMenu.text == "MANTENIMIENTO DE PROMOCIONES"):
                aplicacionMenu.click()
                
    except Exception:
        print("Sucedió un error al momento de seleccionar la aplicación del menu")

