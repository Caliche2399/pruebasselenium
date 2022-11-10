from seleniumbase import BaseCase

from Consulta_Pagos_Tarjeta_Credito.consultaPagoNumeroCuenta import ConsultaPagoTarjetaCreditoPorNumero
from Consulta_Pagos_Tarjeta_Credito.consultaPagoPorNombreApellido import ConsultaPagoTarjetaCreditoPorNombreApellido
from Consulta_Pagos_Tarjeta_Credito.consultaPagoPorUltimosDigitosTarjeta import ConsultaPagoTarjetaCreditoPorUltimosDigitosTarjeta
from Mantenimiento_Pagos_Tarjeta_Visa.anulacionPagoTarjetaVisa import AnulacionPagoTarjetaVisa
from Mantenimiento_Pagos_Tarjeta_Visa.modificacionPagoTarjetaVisa import ModificacionPagoTarjetaVisa
from Pagos_Electronicos_Tarjeta_Visa.pagoElectronicoTarjetaVisa import PagoElectronicoTarjetaVisa
from Pagos_Electronicos_Tarjeta_Visa.pagoElectronicoTarjetaVisaBilletera import PagoElectronicoTarjetaVisaBilletera
from Pagos_Electronicos_Tarjeta_Visa.pagoElectronicoTarjetaVisaBilleteraGlobal import PagoElectronicoTarjetaVisaBilleteraGlobal


class PruebasSistemaCaja(BaseCase):

    def pruebaConsultaPagoTarjetaCreditoPorNumero(self):
        ConsultaPagoTarjetaCreditoPorNumero.runTest(self)

    def pruebaConsultaPagoTarjetaCreditoPorNombreApellido(self):
        ConsultaPagoTarjetaCreditoPorNombreApellido.runTest(self)

    def pruebaConsultaPagoTarjetaCreditoPorUltimosDigitosTarjeta(self):
        ConsultaPagoTarjetaCreditoPorUltimosDigitosTarjeta.runTest(self)

    def pruebaAnulacionPagoTarjetaVisa(self):
        AnulacionPagoTarjetaVisa.runTest(self)

    def pruebaModificacionPagoTarjetaVisa(self):
        ModificacionPagoTarjetaVisa.runTest(self)

    def pruebaPagoElectronicoTarjetaVisa(self):
        PagoElectronicoTarjetaVisa.runTest(self)

    def pruebaPagoElectronicoTarjetaVisaBilletera(self):
        PagoElectronicoTarjetaVisaBilletera.runTest(self)

    def pruebaPagoElectronicoTarjetaVisaBilleteraGlobal(self):
        PagoElectronicoTarjetaVisaBilleteraGlobal.runTest(self)