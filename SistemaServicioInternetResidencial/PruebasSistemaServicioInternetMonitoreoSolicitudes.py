from seleniumbase import BaseCase

from Monitoreo_Solicitudes.busquedaSolicitudAvanzada import BusquedaSolicitudAvanzada
from Monitoreo_Solicitudes.busquedaSolicitudPorAdministrador import BusquedaSolicitudPorAdministrador
from Monitoreo_Solicitudes.busquedaSolicitudPorDistribuidor import BusquedaSolicitudPorDistribuidor
from Monitoreo_Solicitudes.busquedaSolicitudPorEstados import BusquedaSolicitudPorEstados
from Monitoreo_Solicitudes.busquedaSolicitudPorEventos import BusquedaSolicitudPorEventos
from Monitoreo_Solicitudes.busquedaSolicitudPorNumeroSolicitud import BusquedaSolicitudPorNumero
from Monitoreo_Solicitudes.ingresoEventoSolicitud import IngresoEventoSolicitud
from Monitoreo_Solicitudes.modificacionSolicitud import ModificacionSolicitud
from Monitoreo_Solicitudes.reporteMonitoreoDeSolicitudes import ReporteMonitoreoSolicitudes
from Monitoreo_Solicitudes.reporteMonitoreoDeSolicitudesPorEstados import ReporteMonitoreoSolicitudesPorEstado


class PruebasSistemaInternetResidencialMonitoreoSolicitudes(BaseCase):

    def pruebaBusquedaSolicitudAvanzada(self):
        BusquedaSolicitudAvanzada.runTest(self)

    def pruebaBusquedaSolicitudPorAdministrador(self):
        BusquedaSolicitudPorAdministrador.runTest(self)

    def pruebaBusquedaSolicitudPorDistribuidor(self):
        BusquedaSolicitudPorDistribuidor.runTest(self)

    def pruebaBusquedaSolicitudPorEstados(self):
        BusquedaSolicitudPorEstados.runTest(self)

    def pruebaBusquedaSolicitudPorEventos(self):
        BusquedaSolicitudPorEventos.runTest(self)

    def pruebaBusquedaSolicitudPorNumero(self):
        BusquedaSolicitudPorNumero.runTest(self)

    def pruebaIngresoEventoSolicitud(self):
        IngresoEventoSolicitud.runTest(self)

    def pruebaModificacionSolicitud(self):
        ModificacionSolicitud.runTest(self)

    def pruebaReporteMonitoreoSolicitudes(self):
        ReporteMonitoreoSolicitudes.runTest(self)

    def pruebaReporteMonitoreoSolicitudesPorEstado(self):
        ReporteMonitoreoSolicitudesPorEstado.runTest(self)