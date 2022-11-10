from seleniumbase import BaseCase

from Envio_Consulta_SMS.envioSMS import envioSmsLocal
from Envio_Consulta_SMS.consultaSms import consultaSMS
from Mantenimiento_Lista_Negra.ingresoListaNegra import ingresoRegistroListaNegra
from Mantenimiento_Lista_Negra.busquedaAvanzadaListaNegra import busquedaAvanzadaListaNegra

class PruebasSistemaServiciosGenerales(BaseCase):

    def pruebaEnvioSmsLocal(self):
        envioSmsLocal.runTest(self)

    def pruebaConsultaSMS(self):
        consultaSMS.runTest(self)

    def pruebaIngresoRegistroListaNegra(self):
        ingresoRegistroListaNegra.runTest(self)

    def pruebaBusquedaAvanzadaListaNegra(self):
        busquedaAvanzadaListaNegra.runTest(self)