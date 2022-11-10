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
CLIENTE_UNICO = '14561365'
DISTRIBUIDOR = 'WA78'

#Configuración del driver
chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('se:name','Prueba Ingreso Solicitud' )

driver = webdriver.Remote(command_executor = URL_SELENIUM, options = chrome_options)
driver.maximize_window()
driver.get(URL_WEBSISATEL)

#Clase encargada de correr las pruebas
class IngresoSolicitud(BaseCase):
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
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:j_idt27').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='atelBuscarCliente:frmBuscarCliente:txtBuscarClienteNombre').send_keys('EFRAIN')
        
            sleep(2)
            driver.find_element(by= By.ID, value='atelBuscarCliente:frmBuscarCliente:txtBuscarClienteApellido').send_keys('RAMIREZ AGUILAR')
        
            sleep(2)
            driver.find_element(by= By.ID, value='atelBuscarCliente:frmBuscarCliente:btnBuscar').click()
        
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='.ui-datatable-even > td:nth-child(1)').click()
        
            sleep(4)
            driver.find_element(by= By.ID, value='atelBuscarCliente:frmBuscarCliente:btnConfirmar').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:txtNombre').send_keys('NOMBRE PRUEBA')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:txtApellido').send_keys('APELLIDO PRUEBA')

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:txtDistribuidor').send_keys(DISTRIBUIDOR)
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:selOrigenSolicitud').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:selOrigenSolicitud_2').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:selPlan').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:selPlan_2').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:selFormaPagoRef').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:selFormaPagoRef_1').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selTipoPago').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selTipoPago_2').click()
        

            #SE AÑADE INFORMACION DE LA DIRECCION
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='li.ui-state-default:nth-child(3)').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtDireccion').send_keys('DIRECCION PRUEBA')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtZona_input').send_keys('1')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selDepartamento').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selDepartamento_7').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selMunicipio').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selMunicipio_5').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selLocalidad').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selLocalidad_1').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtCodigoPostal').send_keys('01001')


            #SE AÑADE INFORMACION DE CONTACTO
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='li.ui-state-default:nth-child(4)').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:imTelefonoContacto').send_keys('58502430')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtNombreContacto').send_keys('CONTACTO PRUEBA')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtObservContacto').send_keys('OBSERVACION PRUEBA')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:btnAgregarContacto').click()
        
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='#frmIngresoSolicitud\:tabviewInfoAdicional\:plContactoLocal > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1)').click()
        
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='#frmIngresoSolicitud\:tabviewInfoAdicional\:plContactoLocal > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)').click()
        
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='#frmIngresoSolicitud\:tabviewInfoAdicional\:plContactoUsa > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1)').click()
        
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='#frmIngresoSolicitud\:tabviewInfoAdicional\:plContactoUsa > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:btnConfirmar').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmConfirmarSolicitud:btnIngresar').click()


            #Se guarda un screenshot al terminar la prueba
            sleep(10)
            driver.save_screenshot('Prueba_Exitosa_IngresoSolicitud.png')
            print("Se realizó la prueba correctamente.")

            sleep(3)
            cerrarSesion()

        except Exception:
            sleep(2)
            driver.save_screenshot('Prueba_Fallida_IngresoSolicitud.png')
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
            if(aplicacionMenu.text == "INGRESO DE SOLICITUDES"):
                aplicacionMenu.click()
                
    except Exception:
        print("Sucedió un error al momento de seleccionar la aplicación del menu")

