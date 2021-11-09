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

    cantidad_intentos =  0
    while cantidad_intentos < 2:

        try:
            obtener_informacion = requests.get("https://internal-api.mercadolibre.com/shipping/holidays/dump/all")
            conversion_a_diccionario = obtener_informacion.json()
            dias_feriados  = conversion_a_diccionario['values']
            cantidad_intentos = 2
        except Exception:
            dias_feriados = list()
            cantidad_intentos+=1

    return dias_feriados


def obtener_fecha_actual() ->str:

    #PRE:No recibimos ningun argumento.
    #POST:Retornamos como str la fecha actual.

    fecha_actual = datetime.now()
    fecha_actual_string = str(fecha_actual.date())
    
    return fecha_actual_string
