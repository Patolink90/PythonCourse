import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

#Escuchar nuestro microfono y devolver el audio como texto

def transformar_audio_en_texto():
    #Almacenar recognizer en variable
    r = sr.Recognizer()

    #Configurar el microfono
    with sr.Microphone() as origen:

        #Tiempo de espera
        r.pause_threshold = 0.8

        #Informar que comienza la grabacion
        print("Ya puedes hablar")

        #guardar lo que escuche como audio

        audio = r.listen(origen)

        try:
            #Buscar en google
            pedido = r.recognize_google(audio, language="es-mx")

            #prueba de que pudo ingresar

            print("Dijiste: " + pedido)

            #devolver pedido
            return pedido

        except sr.UnknownValueError:

            #Prueba de que no comprendio el audio
            print("No entendi que dijiste")
            return "Sigo esperando"
        #En caso de no resolver el pedido
        except sr.RequestError:
            # Prueba de que no comprendio el audio
            print("Ups!, no hay servicio")
            return "Sigo esperando"
        #error inesperado
        except:
            # Prueba de que no comprendio el audio
            print("Ups!, algo ha salido mal")
            return "Sigo esperando"

#Funcion para que el asistente pueda ser escuchado

def hablar(mensaje):

    #Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    #pronunciar mensaje

    engine.say(mensaje)
    engine.runAndWait()

#informa el dia de la semana
def pedir_dia():

    #Crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    #diccionario con nombres de los dias de la semana
    calendario = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }

    #decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


#Informa que hora es
def pedir_hora():
    #crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)
    hablar(hora)

#funcion saludo inicial
def saludo_inicial():
    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos días'
    else:
        momento = 'Buenas Tardes'
    #decir el saludo
    hablar(f"{momento}, Hola Patolin, soy Albedo, tu asistente personal, Por favor, dime en que puedo ayudarte?")

def pedir_cosas():

    #activar saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    #loop central

    while comenzar:
        #activar el micro y guardar el pedido en un string

        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youTube')
            webbrowser.open("https://www.youtube.com")
            continue
        elif 'abrir navegador' in pedido:
            hablar("Claro estoy en eso")
            webbrowser.open("https://www.google.com")
            continue
        elif 'que día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'que hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('wikipedia dice lo siguiente')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar("Ya mismo estoy en eso")
            pedido = pedido.replace("busca en internet", '')
            pywhatkit.search(pedido)
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea ya comienzo a reproducirlo')
            pedido = pedido.replace('reproducir', '')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {
                'apple': 'APPL',
                'amazon': 'AMZN',
                'google': 'GOOGL'
            }

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPreviousClose']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdon pero no la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break


pedir_cosas()