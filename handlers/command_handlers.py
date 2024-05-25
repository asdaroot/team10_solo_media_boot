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
        "/start - Показать это сообщение.\n"
        "/joke - Рассказать шутку про специалистов по data science, машинное обучение и программистов.\n"
        "/dialog - Перевести бота в режим диалога с GPT.\n"
        "/translate - Перевести текст с учетом контекста для специалистов по data science, машинное обучение и программированию.\n\n"
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