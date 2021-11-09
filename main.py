import time
import fechas_feriados
import bot_slack_meli


def escribir_log(estado_ejecucion:str) ->None:

    #PRE:Recibimos como string el mensaje del log
    #POST:Al ser procedimiento se retorna un tipo de dato NONE.

    with open("archivo","a") as log:
        log.writelines((estado_ejecucion,"\n"))
        

def main() ->None:
    
    detener_ejecucion = False
    while not detener_ejecucion:
        feriados_de_hoy = list()
        fecha_actual = fechas_feriados.obtener_fecha_actual()
        dias_feriados_api = fechas_feriados.obtener_fechas_feriados()

        if len(dias_feriados_api) == 0:
            estado_ejecucion = f"{fecha_actual} ---- Fallido, no se pudo obtener la informacion de la api."
        else:
            fechas_feriados.validando_feriados(feriados_de_hoy, fecha_actual, dias_feriados_api)
            bot_slack_meli.enviar_mensajes_feriados(feriados_de_hoy)
            estado_ejecucion = f"{fecha_actual} --- Exitoso, se ha enviado la notificacion."
        
        escribir_log(estado_ejecucion)
        time.sleep(43200)


main()
