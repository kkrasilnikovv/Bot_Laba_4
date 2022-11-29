from telebot import TeleBot
from telebot import types
import requests

bot = TeleBot('5614395122:AAFtkd9sgHikEfsTRXl_7gR_qlE9O9ExYGY')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Бот построен на переосмыслении известного видео-мема. Теперь вы сами решаете '
                                      'куда лететь, полагаюсь на погоду в крупнейших городах этих стран.')
    video = open('media/885852932638.mp4', 'rb')
    bot.send_video(message.chat.id, video)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇺🇲 США")
    btn2 = types.KeyboardButton("🇨🇦 Канада")
    btn3 = types.KeyboardButton("🇲🇿 Африка")
    btn4 = types.KeyboardButton("🇰🇿 Казахстан")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, "Выберите страну, где будете кайфовать", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "🇺🇲 США":
        bot.send_message(message.from_user.id, get_weather(5128581))
        bot.send_photo(message.chat.id, open_photo('media/Нью-Йорк.jpeg'))
        bot.send_message(message.from_user.id, get_weather(5368361))
        bot.send_photo(message.chat.id, open_photo('media/Лос-Анд.png'))
        bot.send_message(message.from_user.id, get_weather(4887398))
        bot.send_photo(message.chat.id, open_photo('media/Чикаго.jpeg'))
    elif message.text == "🇨🇦 Канада":
        bot.send_message(message.from_user.id, get_weather(6167865))
        bot.send_photo(message.chat.id, open_photo('media/Торонто.jpeg'))
        bot.send_message(message.from_user.id, get_weather(6077243))
        bot.send_photo(message.chat.id, open_photo('media/Монреаль.jpeg'))
        bot.send_message(message.from_user.id, get_weather(5913490))
        bot.send_photo(message.chat.id, open_photo('media/Калгари (1).jpeg'))
    elif message.text == "🇲🇿 Африка":
        bot.send_message(message.from_user.id, get_weather(3369157))
        bot.send_photo(message.chat.id, open_photo('media/Кейп.webp'))
        bot.send_message(message.from_user.id, get_weather(1007311))
        bot.send_photo(message.chat.id, open_photo('media/Дубран.jpeg'))
        bot.send_message(message.from_user.id, get_weather(993800))
        bot.send_photo(message.chat.id, open_photo('media/Йоханнесбург .webp'))
    elif message.text == "🇰🇿 Казахстан":
        bot.send_message(message.from_user.id, get_weather(1526384))
        bot.send_photo(message.chat.id, open_photo('media/Алматы.jpeg'))
        bot.send_message(message.from_user.id, get_weather(1526273))
        bot.send_photo(message.chat.id, open_photo('media/Нур-Султан.jpeg'))
        bot.send_message(message.from_user.id, get_weather(1518980))
        bot.send_photo(message.chat.id, open_photo('media/Шымкенте.jpeg'))
    else:
        bot.send_message(message.from_user.id, "Это конечно круто, но может все-таки в Казахстан?")


@bot.message_handler(content_types=['photo'])
def error(message):
    bot.send_message(message.from_user.id, "Это конечно круто, но может все-таки в Казахстан?")


@bot.message_handler(content_types=['voice'])
def error(message):
    bot.send_message(message.from_user.id, "Это конечно круто, но может все-таки в Казахстан?")


def get_weather(city_id):
    api_key = "49dac8630872385244c60b30860c4d91"
    api_url = "https://api.openweathermap.org/data/2.5/weather?id=" + city_id.__str__() \
              + "&lang=ru&units=metric&APPID=" + api_key
    data = requests.get(api_url).json()
    final = data['name'] + '\n'
    final += str(data['weather'][0]['description']).capitalize() + '\n'
    final += "Температура сейчас " + str(int(data['main']['temp'])) + '° C' + '\n'
    final += "Ощущается как " + str(int(data['main']['feels_like'])) + '° C' + '\n'
    final += "Минимальная температура " + str(int(data['main']['temp_min'])) + '° C' + '\n'
    final += "Максимальная температура " + str(int(data['main']['temp_max'])) + '° C' + '\n'
    final += "Скорость ветра " + str(data['wind']['speed']) + ' м/с' + '\n'
    return final


def open_photo(path):
    return open(path, 'rb')


bot.polling(none_stop=True, interval=0)
