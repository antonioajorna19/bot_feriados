import os
import slack


FERIADO_ACTUAL = 0


def enviar_mensajes_feriados(lista_feriados:list) ->None:

    #PRE:Recibimos los dias feriados en una lista.
    #POST:Al ser un procedimiento retornamos un valor None.

    mensaje_enviado = False
    client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

    while len(lista_feriados) != 0:
        for dia,site,descripcion in lista_feriados:

            try:
              client.chat_postMessage(channel='#prueba_bot_jose', text= f"FERIADO: {dia} / {site} / {descripcion}")
              lista_feriados.pop(FERIADO_ACTUAL)
            except Exception:
              mensaje_enviado = False

            if len(lista_feriados) == 0:
                mensaje_enviado = True
    
    if mensaje_enviado == False:
        while not mensaje_enviado:

            try:
                client.chat_postMessage(channel='#prueba_bot_jose', text= "HOY NO HAY FERIADO EN NINGUN SITE.")
                mensaje_enviado = True
            except Exception:
              mensaje_enviado = False
      