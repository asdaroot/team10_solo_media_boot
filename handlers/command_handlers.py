import json

from telegram import Update,KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from config.openai_client import client
from config.openai_client import generate_response

async def start_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # # объект обновления
    # update_obj = json.dumps(update.to_dict(), indent=4)

    # # ответ
    # reply = "*update object*\n\n" + "```json\n" + update_obj + "\n```"

    # # перенаправление ответа в Telegram
    # await update.message.reply_text(reply, parse_mode="Markdown")

    # print("assistant:", reply)

    # Установить режим диалога по умолчанию
    context.user_data['mode'] = 'dialog'
    
    # Сообщение о возможностях бота
    start_message = (
        "Привет! Я бот Solo, который может выполнять различные задачи с использованием модели GPT3.5. "
        "Вот что я умею:\n\n"
        "/start - Показать это сообщение :)\n"
        "/joke - Рассказать шутку про специалистов по Data Science, Machine Learning и иных Разработчиков.\n"
        "/dialog - Перейти в режим диалога с GPT.\n"
        "/translate - Перевести текст с учетом контекста для специалистов по Data Science, Machine Learning и Developers.\n"
        "/summary_text - Сделать summary из текста.\n"
        "/summary_pdf - Сделать summary из PDF файла.\n"
        "/summary_image - Сделать описание картинки (фото).\n"
        "/summary_video - Сделать описание короткого видео (<20MB)).\n\n"
        "По умолчанию я нахожусь в режиме диалога, и вы можете смело задать мне любой вопрос, а я постарюсь на него ответить."
    )

    reply = start_message

    await update.message.reply_text(reply)

    print("assistant:", reply)


async def joke_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Сформировать промпт для генерации шутки
    prompt = (
        "Расскажи шутку про специалистов по data science, "
        "машинное обучение и программистов. Шутка должна быть "
        "забавной, но не оскорбительной."
    )

    # Генерация шутки с помощью OpenAI
    joke = generate_response(prompt)

    # Отправка шутки пользователю в Telegram
    await update.message.reply_text(joke)

    # Вывод шутки в консоль для отладки
    print("assistant:", joke)
    
    print("assistant:", "Переход в режим по умолчанию (dialog).")
    context.user_data['mode'] = 'dialog'

async def dialog_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Установка состояния в режим диалога
    context.user_data['mode'] = 'dialog'
    await update.message.reply_text("Вы вошли в режим диалога >>>")


async def translate_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Установка состояния в режим перевода
    context.user_data['mode'] = 'translate'
    await update.message.reply_text("Вы вошли в режим перевода. Пожалуйста, отправьте текст для перевода.")


async def summary_text_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Установка состояния в режим summary_text
    context.user_data['mode'] = 'summary_text'
    await update.message.reply_text("Вы вошли в режим summary (text). Пожалуйста, отправьте текст для подготовки краткого содержания.")    


async def summary_pdf_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Установка состояния в режим обработки PDF
    context.user_data['mode'] = 'summary_pdf'
    await update.message.reply_text("Пожалуйста, загрузите PDF файл для создания summary (pdf).")


async def summary_image_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Установка состояния в режим обработки image
    context.user_data['mode'] = 'summary_image'
    await update.message.reply_text("Пожалуйста, отправьте картинку для создания summary (image).")


async def summary_video_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Установка состояния в режим обработки image
    context.user_data['mode'] = 'summary_video'
    await update.message.reply_text("Пожалуйста, отправьте небольшое видео (<20MB) для создания summary (video).")
