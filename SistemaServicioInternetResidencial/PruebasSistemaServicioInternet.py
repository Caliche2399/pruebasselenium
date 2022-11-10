from seleniumbase import BaseCase

from Ingreso_Solicitudes.ingresoSolicitud import IngresoSolicitud
from Modificacion_SIM_Enrutador.asignarSim import AsignacionSIM
from Reportes_Internet.reporteCuentasInstaladasCsv import ReporteCuentasInstaladasCsv
from Reportes_Internet.reporteCuentasInstaladasExcel import ReporteCuentasInstaladasExcel
from Reportes_Internet.reporteCuentasInstaladasPdf import ReporteCuentasInstaladasPdf
from Reportes_Internet.reporteCuentasReasignadasCsv import ReporteCuentasReasignadasCsv
from Reportes_Internet.reporteCuentasReasignadasExcel import ReporteCuentasReasignadasExcel
from Reportes_Internet.reporteCuentasReasignadasPdf import ReporteCuentasReasignadasPdf


class PruebasSistemaInternetResidencial(BaseCase):

    def pruebaIngresoMembresia(self):
        IngresoSolicitud.runTest(self)

    def pruebaConsultaPagoTarjetaCreditoPorNombreApellido(self):
        AsignacionSIM.runTest(self)

    def pruebaConsultaPagoTarjetaCreditoPorUltimosDigitosTarjeta(self):
        ReporteCuentasInstaladasCsv.runTest(self)

    def pruebaAnulacionPagoTarjetaVisa(self):
        ReporteCuentasInstaladasExcel.runTest(self)

    def pruebaModificacionPagoTarjetaVisa(self):
        ReporteCuentasInstaladasPdf.runTest(self)

    def pruebaPagoElectronicoTarjetaVisa(self):
        ReporteCuentasReasignadasCsv.runTest(self)

    def pruebaPagoElectronicoTarjetaVisaBilletera(self):
        ReporteCuentasReasignadasExcel.runTest(self)

    def pruebaPagoElectronicoTarjetaVisaBilleteraGlobal(self):
        ReporteCuentasReasignadasPdf.runTest(self)