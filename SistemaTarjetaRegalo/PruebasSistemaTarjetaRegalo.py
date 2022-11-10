from seleniumbase import BaseCase

from Compra_Tarjeta_Regalo.compraTarjetaRegalo import compraTarjetaRegalo
from Configuraciones.modificarDiferencialCambiario import modificacionDiferencialCambiario
from Consulta_Catalogos.consultaCatalogosTarjetas import consultaCatalogosTarjetaRegalo
from Consulta_Cuentas.consultaCuentaTarjetaRegalo import consultaCuentasTarjetaRegalo

class PruebasSistemaTarjetaRegalo(BaseCase):

    def pruebaCompraTarjetaRegalo(self):
        compraTarjetaRegalo.runTest(self)

    def pruebaModificacionDiferencialCambiario(self):
        modificacionDiferencialCambiario.runTest(self)

    def pruebaConsultaCatalogosTarjetaRegalo(self):
        consultaCatalogosTarjetaRegalo.runTest(self)

    def pruebaConsultaCuentasTarjetaRegalo(self):
        consultaCuentasTarjetaRegalo.runTest(self)