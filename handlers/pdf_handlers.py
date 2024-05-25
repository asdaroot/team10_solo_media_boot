import os
from telegram import Update
from config.openai_client import client
import fitz  # PyMuPDF
from config.openai_client import generate_response_more_tokens

async def pdf_file_reply(update, context):

        pdf_file = await context.bot.get_file(update.message.document.file_id)

        data = await context.bot.get_file(file_id=pdf_file)
        await data.download_to_drive(custom_path='tmp.pdf')

        # Преобразование PDF в текст
        text = ""
        with fitz.open('tmp.pdf') as doc:
            count = 0
            for page in doc:
                if count > 4:   # в среднем 900 токенов на страницу, используем первые 4 страницы
                    break
                text += page.get_text()
                count += 1

        # Формирование промпта для GPT
        prompt = f"Составь резюме для следующего текста из PDF:\n\n{text}"

        # Генерация резюме с помощью OpenAI
        summary = generate_response_more_tokens(prompt)

        # Отправка резюме пользователю в Telegram
        await update.message.reply_text(summary)

        # Вывод текста и резюме в консоль для отладки
        print("user PDF text:", text)
        print("assistant summary:", summary)