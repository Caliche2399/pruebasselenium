from seleniumbase import BaseCase

from Impresion_Recibos.impresionRecibo import impresionDeRecibo
from Notas_Credito.anulacionNotaCredito import anulacionNotaCredito
from Notas_Credito.ingresoNotaCreditoOtroIngresoCaja import ingresoNotaCredito
from Notas_Credito.ingresoNotaCreditoTelefoniaLocalResidencial import ingresoNotaDeCreditoTelefonia
from Reportes_Contables.reporteDocumentosContablesFacturados import reporteDocumentosContablesFacturados
from Reportes_Contables.reporteHistorialPagosInternet import reporteHistorialPagosInternet
from Reportes_Contables.reportePagosTarjetaVisaExcel import reportePagosTarjetaVisaExcel
from Reportes_Contables.reportePagosTarjetaVisaPdf import reportePagosTarjetaVisaPdf

class PruebasSistemaContabilidad(BaseCase):

    def pruebaImpresionDeRecibo(self):
        impresionDeRecibo.runTest(self)

    def pruebaAnulacionNotaCredito(self):
        anulacionNotaCredito.runTest(self)

    def pruebaIngresoNotaCredito(self):
        ingresoNotaCredito.runTest(self)

    def pruebaIngresoNotaCreditoTelefonia(self):
        ingresoNotaDeCreditoTelefonia.runTest(self)

    def pruebaReporteDocumentoContablesFacturados(self):
        reporteDocumentosContablesFacturados.runTest(self)

    def pruebaReporteHistorialPagosInternet(self):
        reporteHistorialPagosInternet.runTest(self)

    def pruebaReportePagosTarjetaVisaExcel(self):
        reportePagosTarjetaVisaExcel.runTest(self)

    def pruebaReportePagosTarjetaVisaPdf(self):
        reportePagosTarjetaVisaPdf.runTest(self)