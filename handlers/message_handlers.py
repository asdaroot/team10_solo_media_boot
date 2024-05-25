from telegram import Update
from config.openai_client import client
from config.openai_client import generate_response

async def chatgpt_reply(update: Update, context):
    # текст входящего сообщения
    text = update.message.text
    
    # Проверка режима 
    if context.user_data.get('mode') == 'dialog':        
        # ответ
        reply = generate_response(text)

        # перенаправление ответа в Telegram
        await update.message.reply_text(reply)

        print("user:", text)
        print("assistant:", reply)

    # Проверка режима
    if context.user_data.get('mode') == 'translate':

        # Сформировать промпт для перевода с контекстом
        prompt = (
             f"Translate the following text from English into Russian."
             f"Keep technical terminology and emphasis for data scientists,"
             f"machine learning and programming: \"{text}\""
        )

        # Генерация перевода с помощью OpenAI
        translation = generate_response(prompt)

        # Отправка перевода пользователю в Telegram
        await update.message.reply_text(translation)

        # Вывод текста и перевода в консоль для отладки
        print("user:", text)
        print("assistant:", translation)









