import telebot

# Вставь сюда свой токен от BotFather (между кавычками)
TOKEN = '8540249379:AAFlim2GNMdLTan1vhHcmt_KcGGNRskc_0g'

bot = telebot.TeleBot(TOKEN)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой первый Telegram-бот на Питоне 😎 Напиши мне что-нибудь!")

# Обработка всех остальных текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: {message.text}\nА я пока просто учусь!")

print("Бот успешно запущен и ждет сообщений...")
# Эта команда заставляет бота работать бесконечно и проверять новые сообщения
bot.infinity_polling()