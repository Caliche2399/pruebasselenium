from seleniumbase import BaseCase

from Pagos_Tarjeta_Credito.pagoTarjetaCreditoBilleteraOffline import PagoTarjetaCreditoBilleteraOffline
from Pagos_Tarjeta_Credito.pagoTarjetaCreditoInternetOffline import PagoTarjetaCreditoInternetOffline
from Pagos_Tarjeta_Credito.pagoTarjetaCreditoMovilOffline import PagoTarjetaCreditoMovilOffline
from Pagos_Tarjeta_Credito.pagoTarjetaCreditoTarjetaVisaOffline import PagoTarjetaCreditoTarjetaVisaOffline

from Pagos_Tarjeta_Credito.pagoTarjetaCreditoBilleteraOnline import PagoTarjetaCreditoBilleteraOnline
from Pagos_Tarjeta_Credito.pagoTarjetaCreditoInternetOnline import PagoTarjetaCreditoInternetOnline
from Pagos_Tarjeta_Credito.pagoTarjetaCreditoMovilOnline import PagoTarjetaCreditoMovilOnline
from Pagos_Tarjeta_Credito.pagoTarjetaCreditoTarjetaVisaOnline import PagoTarjetaCreditoTarjetaDebitoOnline
from Pagos_Tarjeta_Credito.pagoTarjetaCreditoTopUpOnline import PagoTarjetaCreditoTopUpOnline


class PruebasSistemaCajaPagoTarjetaCredito(BaseCase):

    #PRUEBAS MODO OFFLINE

    def pruebaPagoTarjetaCreditoBilleteraOffline(self):
        PagoTarjetaCreditoBilleteraOffline.runTest(self)

    def pruebaPagoTarjetaCreditoInternetOffline(self):
        PagoTarjetaCreditoInternetOffline.runTest(self)

    def pruebaPagoTarjetaCreditoMovilOffline(self):
        PagoTarjetaCreditoMovilOffline.runTest(self)

    def pruebaPagoTarjetaCreditoTarjetaVisaOffline(self):
        PagoTarjetaCreditoTarjetaVisaOffline.runTest(self)
        
    #PRUEBAS MODO ONLINE

    def pruebaPagoTarjetaCreditoBilleteraOnline(self):
        PagoTarjetaCreditoBilleteraOnline.runTest(self)

    def pruebaPagoTarjetaCreditoInternetOnline(self):
        PagoTarjetaCreditoInternetOnline.runTest(self)

    def pruebaPagoTarjetaCreditoMovilOnline(self):
        PagoTarjetaCreditoMovilOnline.runTest(self)

    def pruebaPagoTarjetaCreditoTarjetaVisaOnline(self):
        PagoTarjetaCreditoTarjetaDebitoOnline.runTest(self)

    def pruebaPagoTarjetaCreditoTopUpOnline(self):
        PagoTarjetaCreditoTopUpOnline.runTest(self)
    