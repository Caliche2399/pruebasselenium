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

CLIENTE_UNICO = '17320321'
DISTRIBUIDOR = 'WA78'
NOMBRE = 'PRUEBA'
APELLIDO = 'PRUEBA'
NOMBRE_PLASTICO = 'PRUEBA PLASTICO'
CORREO_MEMBRESIA = 'PRUEBA@MAIL.COM'
NUMERO_DOCUMENTO = '30282522201520'

#Configuración del driver
chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('se:name','Prueba Ingreso Membresia' )

driver = webdriver.Remote(command_executor = URL_SELENIUM, options = chrome_options)
driver.maximize_window()
driver.get(URL_WEBSISATEL)

#Clase encargada de correr las pruebas
class ingresoMembresiaTarjetaVisa(BaseCase):
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
            driver.find_element(by= By.ID, value='frmMonitoreoSolicitudes:camposBusquedaAvanzada').send_keys(CLIENTE_UNICO)
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:fsClienteUniversal').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:selProductoMembresia').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:selProductoMembresia_2').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:txtDistribuidor').send_keys(DISTRIBUIDOR)
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:selOrigenSolicitud').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:selOrigenSolicitud_2').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:selFormaPagoElectronico_label').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:selFormaPagoElectronico_1').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:selTipoMembresia').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:selTipoMembresia_1').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:selPaisMembresia').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:selPaisMembresia_1').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:txtNombre').send_keys(NOMBRE)
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:txtApellido').send_keys(APELLIDO)
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:txtNombrePlastico').send_keys(NOMBRE_PLASTICO)
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:cFechaNacimiento_input').send_keys('18/01/1998')
        
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='div.ui-grid-col-6:nth-child(2) > div:nth-child(1) > div:nth-child(2)').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:txtCorreoElectronico').send_keys(CORREO_MEMBRESIA)
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:selActividadEconomica').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:selActividadEconomica_1').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:selTipoDocumento').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:selTipoDocumento_3').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:txtNumeroDocumentoIdentificacion').send_keys(NUMERO_DOCUMENTO)
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:txtDireccionUsa').send_keys('DIRECCION PRUEBA SELENIUM')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:txtCiudadUsa').send_keys('CIUDAD PRUEBA SELENIUM')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:rDetallesMembresia:0:txtCodigoPostalUsa').send_keys('01522')
        

            #SE AÑADE INFORMACION DEL CONTACTO
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='li.ui-state-default:nth-child(2)').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selPaisTelefono').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selPaisTelefono_1').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:imTelefonoContacto').send_keys('8482528293')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtNombreContacto').send_keys('CONTACTO PRUEBA')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtObservContacto').send_keys('OBSERVACIONES CONTACTO PRUEBA')
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:btnAgregarContacto').click()
        
            #SE AÑADE INFORMACION DEL BENEFICIARIO
            sleep(2)
            driver.find_element(by= By.CSS_SELECTOR, value='li.ui-state-default:nth-child(3)').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtNombreBeneficiario').send_keys('BENEFICIARIO PRUEBA')

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtApellidoBeneficiario').send_keys('BENEFICIARIO PRUEBA APELLIDO')

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selPaisTelefonoBeneficiario').click()
            
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selPaisTelefonoBeneficiario_1').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtTelefonoBeneficiario').send_keys('4882526304')
            
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selTipoDocumentoBeneficiario').click()

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:selTipoDocumentoBeneficiario_3').click()
            
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtNumeroDocumentoIdentificacionBenefeiciario').send_keys('465464684464')

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtParentesco').send_keys('FAMILIAR')
            
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:txtPorcentaje_input').send_keys('100')

            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:tabviewInfoAdicional:btnAgregarBeneficiario').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmIngresoSolicitud:btnValidarSolicitudMembresia').click()
        
            sleep(2)
            driver.find_element(by= By.ID, value='frmConfirmarDatos:btnIngresarSolicitudMembresia').click()


            #Se guarda un screenshot al terminar la prueba
            sleep(5)
            driver.save_screenshot('Prueba_Exitosa_IngresoMembresia.png')
            print("Se realizó la prueba correctamente.")

            cerrarSesion()

        except Exception:
            sleep(2)
            driver.save_screenshot('Prueba_Fallida_IngresoMembresia.png')
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
            if(aplicacionMenu.text == "INGRESO MEMBRESIA"):
                aplicacionMenu.click()
                
    except Exception:
        print("Sucedió un error al momento de seleccionar la aplicación del menu")

