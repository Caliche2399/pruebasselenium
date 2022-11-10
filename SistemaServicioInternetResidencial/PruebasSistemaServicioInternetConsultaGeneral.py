from seleniumbase import BaseCase

from Consulta_General.busquedaCuentaPorNumeroCuenta import BusquedaCuentaPorNumero
from Consulta_General.busquedaCuentaPorDistribuidor import BusquedaCuentaPorDistribuidor
from Consulta_General.busquedaCuentaPorAdministrador import BusquedaCuentaPorAdministrador
from Consulta_General.busquedaCuentaAvanzada import BusquedaCuentaAvanzada
from Consulta_General.busquedaCuentaPorEventos import BusquedaCuentaPorEventos
from Consulta_General.modificacionCuenta import ModificacionCuenta
from Consulta_General.reporteConsultaGeneral import ReporteConsultaGeneral
from Consulta_General.reporteConsultaGeneralPorEstado import ReporteConsultaGeneralPorEstado


class PruebasSistemaInternetResidencialMonitoreoSolicitudes(BaseCase):

    def pruebaBusquedaCuentaPorNumero(self):
        BusquedaCuentaPorNumero.runTest(self)

    def pruebaBusquedaCuentaPorDistribuidor(self):
        BusquedaCuentaPorDistribuidor.runTest(self)

    def pruebaBusquedaCuentaPorAdministrador(self):
        BusquedaCuentaPorAdministrador.runTest(self)

    def pruebaBusquedaCuentaAvanzada(self):
        BusquedaCuentaAvanzada.runTest(self)

    def pruebaBusquedaCuentaPorEventos(self):
        BusquedaCuentaPorEventos.runTest(self)

    def pruebaModificacionCuenta(self):
        ModificacionCuenta.runTest(self)

    def pruebaReporteConsultaGeneral(self):
        ReporteConsultaGeneral.runTest(self)

    def pruebaReporteConsultaGeneralPorEstado(self):
        ReporteConsultaGeneralPorEstado.runTest(self)