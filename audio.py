# Instalar biblioteca de reconhecimento de fala:
# pip install SpeechRecognition

# Instalar biblioteca de captura de som:
# pip install pyaudio
# Se não funcionar, visitar: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio e baixar o arquivo correspondente a sua versão do Python.

import speech_recognition as sr

# Função para ouvir o áudio do microfone
def ouvir_microfone():

    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:

        # Reduz ruídos no som com um algoritmo
        microfone.adjust_for_ambient_noise(source)

        # Pede a entrada do usuário
        print("-> Diga alguma coisa!")

        # Armazena o que foi dito
        audio = microfone.listen(source)

    try:

        # Passa a variável para o algoritmo de reconhecer padrões da Google
        frase = microfone.recognize_google(audio, language='pt-BR')

        # Retorna a frase pronunciada
        print(frase)
        return frase

    # Se não reconheceu o padrão de fala, exibe a mensagem:
    except sr.UnknownValueError:
        print("-> Não foi possível identificar a fala.")