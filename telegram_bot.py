from API import API_KEY, CHAT_ID
import telebot


def send_msg(message):
    bot = telebot.TeleBot(API_KEY)
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        print("Rezept an Telegram gesendet...")
    except Exception as e:
        print(f"[ERROR] {e}")