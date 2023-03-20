import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests

def talk(text):
    engine.say(text)
    engine.runAndWait()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)

def run_venom():
    import time
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'venom' in command:
                command = command.replace('venom', '')
                print(command)
                if 'play' in command:
                    song = command.replace('play', '')
                    talk('playing ' + song)
                    pywhatkit.playonyt(song)
                elif 'time' in command:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    talk('Current time is ' + time)
                elif 'weather'in command:
                    city = 'chennai'
                    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
                    json_data = requests.get(api).json()
                    condition = json_data['weather'][0]['main']
                    temp = int(json_data['main']['temp'] - 273.15)
                    min_temp = int(json_data['main']['temp_min'] - 273.15)
                    max_temp = int(json_data['main']['temp_max'] - 273.15)
                    pressure = json_data['main']['pressure']
                    humidity = json_data['main']['humidity']
                    wind = json_data['wind']['speed']
                    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
                    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
                    talk("\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset)
                elif 'who is' in command:
                    person = command.replace('who is', '')
                    info = wikipedia.summary(person, 1)
                    print(info)
                    talk(info)
                elif 'repeat' in command:
                    print(command)
                    talk(command)
                elif 'google' in command:
                    person = command.replace('google', '')
                    import pywhatkit as pwt
                    pwt.search(person)
                elif 'date' in command:
                    talk('sorry, I have a headache')
                elif 'are you single' in command:
                    talk('I am in a relationship with wifi')
                elif 'joke' in command:
                    talk(pyjokes.get_joke())
                elif 'shut up' in command:
                    talk('what a jerk')
                    time.sleep(2)
                    exit()
                elif 'where are you' in command:
                    talk('inside your computer bud')
                else:
                    talk('Please say the command again.')
    except sr.UnknownValueError:
        talk('Please say the command again.')
    return command

run_venom()
