import os
import slack
import time

def enviar_mensajes_feriados(lista_feriados:list, fecha_actual:str) ->None:

    #PRE:Recibimos los dias feriados en una lista.
    #POST:Al ser un procedimiento retornamos un valor None.

    feriados_no_enviados = list()
    mensaje_enviado = False
    client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

    if len(lista_feriados) != 0:
        for id_feriado in range(len(lista_feriados)): 

            contador_intentos = 0
            while contador_intentos < 2:
                
                try:
                    client.chat_postMessage(channel='#team-smo-helpdesk', text= f"FERIADO: {lista_feriados[id_feriado][0]} / {lista_feriados[id_feriado][1]} / {lista_feriados[id_feriado][2]}")
                    contador_intentos = 2 #Queda ver acomodar esta parte.    
                except Exception:
                    mensaje_enviado = False
                    contador_intentos+=1

                    if contador_intentos == 2:
                        feriados_no_enviados.append((lista_feriados[id_feriado][0],lista_feriados[id_feriado][1],lista_feriados[id_feriado][2]))

    if len(feriados_no_enviados) == 0 and len(lista_feriados) != 0:
        mensaje_enviado = True
        estado_ejecucion = f"{fecha_actual} ---- Mensaje enviado con exito."
    
    elif len(feriados_no_enviados) != 0 and len(lista_feriados) != 0:
        mensaje_enviado = True
        estado_ejecucion = f"{fecha_actual} --- Mensaje de feriados no enviados."
        
    if mensaje_enviado == False:

        contador_intentos = 0
        while contador_intentos < 2:

            try:
                client.chat_postMessage(channel='#prueba_bot_jose', text= "HOY NO HAY FERIADO EN NINGUN SITE.")
                contador_intentos = 2
                estado_ejecucion = f"{fecha_actual}  --- Mensaje enviado con exito."
            except Exception:
                contador_intentos+=1
                estado_ejecucion = f"{fecha_actual}  --- Mensaje fallido, no se ha podido enviar el mensaje de dia no feriado."
    
    return estado_ejecucion
      