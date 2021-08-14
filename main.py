import time
import fechas_feriados
import bot_slack_meli


def main() ->None:

    continuar_ejecutando = False
    while not continuar_ejecutando:
        feriados_de_hoy = list()
        fecha_actual = fechas_feriados.obtener_fecha_actual_paises()
        dias_feriados_a_validar = fechas_feriados.obtener_fechas_feriados()

        while len(dias_feriados_a_validar) == 0:
            dias_feriados_a_validar = fechas_feriados.obtener_fechas_feriados()

        fechas_feriados.validando_feriados(feriados_de_hoy, fecha_actual, dias_feriados_a_validar)
        bot_slack_meli.enviar_mensajes_feriados(feriados_de_hoy)
        time.sleep(3600)#falta ver cada cuantos segundos se enviara el mensaje.


main()
