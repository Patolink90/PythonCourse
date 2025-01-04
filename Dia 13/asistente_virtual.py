import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

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

id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

hablar("Hola Luis. Espero que tengas un buen día")
