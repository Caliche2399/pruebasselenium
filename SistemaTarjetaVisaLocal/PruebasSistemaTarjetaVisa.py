from seleniumbase import BaseCase

from Ingreso_Membresia.ingresoMembresia import ingresoMembresiaTarjetaVisa

from Monitoreo_Membresias.busquedaPorNumeroMembresia import busquedaPorNumeroMembresia
from Monitoreo_Membresias.busquedaAvanzada import busquedaAvanzadaMembresia
from Monitoreo_Membresias.busquedaPorAdministrador import busquedaPorAdministrador
from Monitoreo_Membresias.busquedaPorDistribuidor import busquedaPorCodigoDistribuidor
from Monitoreo_Membresias.busquedaPorEstados import busquedaPorEstados
from Monitoreo_Membresias.busquedaPorEventos import busquedaPorEventos
from Monitoreo_Membresias.asociarMembresia import asociacionMembresia
from Monitoreo_Membresias.IngresoEstadoMembresia import ingresoEventoMembresia
from Monitoreo_Membresias.modificarMembresia import modificacionMembresia
from Monitoreo_Membresias.reporteMonitoreoMembresia import reporteMonitoreoMembresia
from Monitoreo_Membresias.reporteMonitoreoMembresiaPorEstados import reporteMonitoreoMembresiaPorEstados
from Monitoreo_Membresias.visualizarMembresia import visualizarMembresia


class PruebasSistemaTarjetaVisaLocal(BaseCase):

    def pruebaIngresoMembresia(self):
        ingresoMembresiaTarjetaVisa.runTest(self)

    def pruebaConsultaPagoTarjetaCreditoPorNombreApellido(self):
        busquedaPorNumeroMembresia.runTest(self)

    def pruebaConsultaPagoTarjetaCreditoPorUltimosDigitosTarjeta(self):
        busquedaAvanzadaMembresia.runTest(self)

    def pruebaAnulacionPagoTarjetaVisa(self):
        busquedaPorAdministrador.runTest(self)

    def pruebaModificacionPagoTarjetaVisa(self):
        busquedaPorCodigoDistribuidor.runTest(self)

    def pruebaPagoElectronicoTarjetaVisa(self):
        busquedaPorEstados.runTest(self)

    def pruebaPagoElectronicoTarjetaVisaBilletera(self):
        busquedaPorEventos.runTest(self)

    def pruebaPagoElectronicoTarjetaVisaBilleteraGlobal(self):
        asociacionMembresia.runTest(self)

    def pruebaIngresoMembresia(self):
        visualizarMembresia.runTest(self)

    def pruebaConsultaPagoTarjetaCreditoPorNombreApellido(self):
        ingresoEventoMembresia.runTest(self)

    def pruebaConsultaPagoTarjetaCreditoPorUltimosDigitosTarjeta(self):
        modificacionMembresia.runTest(self)

    def pruebaAnulacionPagoTarjetaVisa(self):
        reporteMonitoreoMembresia.runTest(self)

    def pruebaModificacionPagoTarjetaVisa(self):
        reporteMonitoreoMembresiaPorEstados.runTest(self)