from django.http import HttpResponse
from django.template import loader
from suds.client import Client
# Create your views here.

def tipo_cambio(request):

    template = loader.get_template('tipo_cambio/index.html')
    cliente = Client('http://www.banguat.gob.gt/variables/ws/TipoCambio.asmx?WSDL')
    tipo_cambio_dia = cliente.service.TipoCambioDia().CambioDolar.VarDolar[0].referencia
    fecha_tipo_cambio = cliente.service.TipoCambioDia().CambioDolar.VarDolar[0].fecha
    context = {
        'cambio_dia': tipo_cambio_dia,
        'fecha':  fecha_tipo_cambio
    }
    return HttpResponse(template.render(context,request))
