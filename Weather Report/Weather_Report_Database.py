import speech_recognition as sr
import pyttsx3
import requests
import time
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database='goutham'
)

print(mydb)

def talk(text):
    engine.say(text)
    engine.runAndWait()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id) 

city=input("Enter the city name: ")
city=city.title()
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
c=("\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + " hPa" + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE CLIMATE (Cities VARCHAR(50),Min_Temp VARCHAR(50),Max_Temp VARCHAR(50),Pressure VARCHAR(50),Humidity int(100),Wind_Speed VARCHAR(50))")
sql = "INSERT INTO climate (Cities,Min_Temp,Max_Temp,Pressure,Humidity,Wind_Speed) VALUES (%s,%s,%s,%s,%s,%s)"
val = (city,str(min_temp)+'°C',str(max_temp)+'°C',str(pressure)+' hPa',humidity,str(wind)+'Km/h')
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
