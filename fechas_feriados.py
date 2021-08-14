from datetime import datetime
import requests


def validando_feriados(feriados_de_hoy:list, fecha_actual:str, dias_feriados_a_validar:list) ->None:

    #PRE:Recibimos la fecha actual, los feriados de todos los paises y la lista donde se agregaran los feriados de el dia actual.
    #POST:Al ser un procedimiento, retornamos un valor None.

    for id_feriado in range(len(dias_feriados_a_validar)):
        if dias_feriados_a_validar[id_feriado]['holiday'] == fecha_actual:
            feriados_de_hoy.append((fecha_actual, dias_feriados_a_validar[id_feriado]['site_id'], dias_feriados_a_validar[id_feriado]['description']))


def obtener_fechas_feriados() ->list:

    #PRE:No recibimos ningun argumento.
    #POST:Retornamos la lista con los feriados de todos los paises.

    try:
        obtener_informacion = requests.get("https://internal-api.mercadolibre.com//shipping/holidays/dump/all")
        conversion_a_diccionario = obtener_informacion.json()
        dias_feriados  = conversion_a_diccionario['values']

    except Exception:
        dias_feriados = list()

    return dias_feriados


def obtener_fecha_actual_paises() ->str:

    #PRE:No recibimos ningun argumento.
    #POST:Retornamos como str la fecha actual de todos los paises.

    informacion_fecha = datetime.now()
    obtener_fecha_actual_paises = str(informacion_fecha.date())
    
    return obtener_fecha_actual_paises
