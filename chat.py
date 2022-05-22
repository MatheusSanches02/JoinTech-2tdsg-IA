#from chatterbot.trainers import ListTrainer
#from chatterbot import ChatBot
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
#from spacy.cli import download

"""
download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

 elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        maquina.say(resultado)
"""

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'meraki' in comando:
                comando = comando.replace('meraki', '')
                maquina.runAndWait()    
    except:
        print("bot: Isso nao funcionou")
    return comando

def comando_voz_usuario():
    
    while True:

        comando = executa_comando()
        if 'horas' in comando:
            hora = datetime.datetime.now().strftime('%H:%M')
            maquina.say('Agora são' + hora)
            maquina.say('Te ajudo em algo mais?')
            maquina.runAndWait()
        elif 'procure por' in comando:
            pesquisa = comando.replace('procure por', '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(pesquisa, 2)
            print(resultado)
            maquina.say(resultado)
            maquina.say('Te ajudo em algo mais?')
            maquina.runAndWait()
        elif 'toque' in comando:
            musica = comando.replace('toque', '')
            resultado = pywhatkit.playonyt(musica)
            maquina.say('Tocando Música')
            maquina.say('Te ajudo em algo mais?')
            maquina.runAndWait()
        elif 'diário' in comando:
            diario = comando.replace('diário', '')
            maquina.say('Escrevendo diário')
            print(diario)
            maquina.say('Você escreveu ' + diario)
            maquina.say('Deseja salvar alterações no banco de dados?')
            maquina.runAndWait()
        elif 'olá' in comando:
            maquina.say('Olá, como você está hoje?')
            maquina.runAndWait()
        elif 'respiração' in comando:
            maquina.say('por quanto tempo?')
            maquina.runAndWait()
            tempo = int(input('Digite o tempo: '))
            i =0
            while i < tempo:
                tempo-=1
                maquina.say('Inspira')
                print('inspira')
                maquina.say('Expire')
                print('expire')
                maquina.runAndWait()
        elif 'sair' in comando:
            maquina.say('Foi um prazer falar com você')
            maquina.runAndWait()
            break
        else:
            maquina.say('Desculpe, não consigo entender ou não tenho resposta para isso!')
comando_voz_usuario()