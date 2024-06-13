import telebot
from telebot import types

# Conexión con nuestro bot.

TOKEN = 'tutoken'
bot = telebot.TeleBot(TOKEN)


# Creación de comandos simples como '/start' y 'help'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola! soy tu primer bot creado con Telebot.')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Puedes interactuar usando comandos. Por ahora, solo respondo a los comandos: /start y /help')


#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)


@bot.message_handler(commands=['pizza'])
def send_options(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    #Creación de botones para el bot.
    btn_si = types.InlineKeyboardButton('Si', callback_data='pizza_si')
    btn_no = types.InlineKeyboardButton('No', callback_data='pizza_no')

    #Agregar botones.
    markup.add(btn_si, btn_no)

    #Enviar mensaje con los botones
    bot.send_message(message.chat.id, "¿Te gusta la pizza?", reply_markup=markup)

#Crear un decorador
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    if call.data == 'pizza_si':
        bot.answer_callback_query(call.id, 'A mi tambien !')
    elif call.data == 'pizza_no':
        bot.answer_callback_query(call.id, 'Bueno es cosa de gustos !')

@bot.message_handler(commands=['foto'])
def send_image(message):
    img_url='https://www.devacademy.es/wp-content/uploads/2018/10/python-logo.png'
    bot.send_photo(chat_id=message.chat.id, photo=img_url, caption='Aqui tienes tu imagen.')

if __name__ == "__main__":
    bot.polling(none_stop=True)
