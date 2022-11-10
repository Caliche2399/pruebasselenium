from seleniumbase import BaseCase

from Ingreso_Top_Up.compraTopUps import compraTopUp
from Consulta_Anulacion_TopUps.anularTopUp import anularTopUpCliente
from Consulta_Anulacion_TopUps.consultaTopUp import consultaTopUpCliente
from Consulta_Productos_Promociones.consultarProductosYPromociones import consultarProductosYPromociones
from Mantenimiento_Promociones.ingresoPromocion import ingresoPromocionTopUp
from Restricciones_Compra.ingresoRestriccion import ingresoRestriccion
from Restricciones_Compra.busquedaAvanzadaRestriccion import busquedaAvanzadaRestriccion
from Restricciones_Compra.busquedaRestricciones import busquedaRestriccionesDeCompra


class PruebasSistemaTopUps(BaseCase):

    def pruebaIngresoTopUp(self):
        compraTopUp.runTest(self)

    def pruebaAnulacionTopUp(self):
        anularTopUpCliente.runTest(self)

    def pruebaConsultaTopUp(self):
        consultaTopUpCliente.runTest(self)

    def pruebaConsultaProductosPromociones(self):
        consultarProductosYPromociones.runTest(self)
    
    def pruebaIngresoPromocionTopUp(self):
        ingresoPromocionTopUp.runTest(self)

    def pruebaIngresoRestriccionCompra(self):
        ingresoRestriccion.runTest(self)

    def pruebaBusquedaAvanzadaRestriccion(self):
        busquedaAvanzadaRestriccion.runTest(self)
    
    def pruebaBusquedaRestricciones(self):
        busquedaRestriccionesDeCompra.runTest(self)