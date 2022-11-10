from seleniumbase import BaseCase

from Reporte_Ventas_TopUps.reporteTopUpLiquidacionPdf import reporteVentasTopUpLiquidacionPdf
from Reporte_Ventas_TopUps.reporteTopUpLiquidacionExcel import reporteVentasTopUpLiquidacionExcel
from Reporte_Ventas_TopUps.reporteTopUpsExcel import reporteVentasTopUpInternoExcel
from Reporte_Ventas_TopUps.reporteTopUpsPdf import reporteVentasTopUpInternoPdf
from Reporte_Ventas_TarjetasRegalo.reporteTarjetaRegaloExcel import reporteVentasTarjetaRegaloExcel
from Reporte_Ventas_TarjetasRegalo.reporteTarjetaRegaloPdf import reporteVentasTarjetaRegaloPdf


class PruebasSistemaTelemercadeo(BaseCase):

    def pruebaReporteVentaTopUpLiquidacionPdf(self):
        reporteVentasTopUpLiquidacionPdf.runTest(self)

    def pruebaReporteVentaTopUpLiquidacionExcel(self):
        reporteVentasTopUpLiquidacionExcel.runTest(self)

    def pruebaReporteVentasTopUpInternoExcel(self):
        reporteVentasTopUpInternoExcel.runTest(self)

    def pruebaReporteVentasTopUpInternoPdf(self):
        reporteVentasTopUpInternoPdf.runTest(self)

    def pruebaReporteVentasTarjetaRegaloExcel(self):
        reporteVentasTarjetaRegaloExcel.runTest(self)

    def pruebaReporteVentasTarjetaRegaloPdf(self):
        reporteVentasTarjetaRegaloPdf.runTest(self)