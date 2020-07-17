import telebot

def delete_message(message):
    bot.delete_message(message.chat.id, message.message_id)
