import pyowm
import telebot
from pyowm.exceptions import api_response_error

owm = pyowm.OWM('de3e9e792e8435bed44e8a0d4b1e6745')
bot = telebot.TeleBot("1126635895:AAFKHG3Bt2F2iiXz5UyF98fBl5mgJ2bs0_4")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    try:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')['temp']
        time = w.get_reference_time
        rava=w.get_status()
        answer = ('В місті '+message.text+', температура становить ' + str (temp)+"°С.\n")
        if rava == "Rain":
            answer = (answer + 'Стан погоди: дощ. ')
        elif rava == "Clouds":
            answer = (answer +'Стан погоди: хмарно. ')
        elif rava == "Clear":
            answer =(answer +' Стан погоди: ясно. ')
        elif rava == 'Hail':
            answer =(answer +' Стан погоди: град. ')
        elif rava== 'Show':
            answer =(answer +'Стан погоди: cніжно. ')
        else:
            answer =('Помилка погоди.')
    except api_response_error.NotFoundError:
        answer = 'Місто введено не корректно'
 



    bot.send_message(message.chat.id, answer)
bot.polling (none_stop = True)
