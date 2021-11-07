import datetime
import pyttsx3
import speech_recognition as sr
import pywhatkit




texto_fala = pyttsx3.init()

def falar(audio):
  rate = texto_fala.getProperty('rate')
  texto_fala.setProperty("rate",191)
  voices = texto_fala.getProperty('voices')
  texto_fala.setProperty('voice',voices[0].id)

  texto_fala.say(audio)
  texto_fala.runAndWait()





som = sr.Recognizer()

def executa_comando():    
    
  try:

         with sr.Microphone() as source:
          print("reconhecendo...")
          voz = som.listen(source)
          comando = som.recognize_google(voz, language='pt-br')
          comando = comando.lower()
          comando = comando.replace('')
          print(comando)
          falar(comando)
          texto_fala.runAndWait()
          

  except:
       print('não está pegando')   

  return comando 

def comando_usuario():
      
     comando = executa_comando()
     if 'horas' in comando:
         hora = datetime.datetime.now().strftime('%H:%M')
         falar('senhor eduardo, agora são:' + hora)
         texto_fala.runAndWait()

     elif 'toque' in comando:
          musica = comando.replace('toque','')
          resultado = pywhatkit.playonyt(musica)
          falar('tocando musica')
          texto_fala.runAndWait()


comando_usuario()         
         








    
           


        

        
        

      
      
              

