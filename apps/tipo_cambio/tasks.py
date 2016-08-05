from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from suds.client import Client
from .models import Tipo_Cambio


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name = 'task_save_latest_change',
    ignore_result = True
)
def guardar_tipo_cambio():
    cliente = Client('http://www.banguat.gob.gt/variables/ws/TipoCambio.asmx?WSDL')
    tipo_cambio_dia = cliente.service.TipoCambioDia().CambioDolar.VarDolar[0].referencia
    fecha_tipo_cambio = cliente.service.TipoCambioDia().CambioDolar.VarDolar[0].fecha
    aux = fecha_tipo_cambio.split('/')
    fecha_tipo_cambio = aux[2].strip() + '-' + aux[1].strip() + '-' + aux[0].strip()
    temp =Tipo_Cambio(fecha = fecha_tipo_cambio, cambio = tipo_cambio_dia)
    temp.save()
