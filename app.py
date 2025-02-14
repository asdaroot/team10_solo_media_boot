from telegram.ext import MessageHandler, CommandHandler, filters
from config.telegram_bot import application
from handlers.command_handlers import start_reply, joke_reply, dialog_reply, translate_reply, \
    summary_text_reply, summary_pdf_reply, summary_image_reply, summary_video_reply
from handlers.message_handlers import chatgpt_reply
from handlers.audio_handlers import audio_reply
from handlers.video_note_handlers import video_note_reply
from handlers.image_file_handlers import image_file_reply
from handlers.video_file_handlers import video_file_reply
from handlers.pdf_handlers import pdf_file_reply

# Регистрация обработчиков команд
start_handler = CommandHandler("start", start_reply)
joke_handler = CommandHandler("joke", joke_reply)
dialog_handler = CommandHandler("dialog", dialog_reply)
translate_handler = CommandHandler("translate", translate_reply)
summary_text_handler = CommandHandler("summary_text", summary_text_reply)
summary_pdf_handler = CommandHandler("summary_pdf", summary_pdf_reply)
summary_image_handler = CommandHandler("summary_image", summary_image_reply)
summary_video_handler = CommandHandler("summary_video", summary_video_reply)
application.add_handler(start_handler)
application.add_handler(joke_handler)
application.add_handler(dialog_handler)
application.add_handler(translate_handler)
application.add_handler(summary_text_handler)
application.add_handler(summary_image_handler)
application.add_handler(summary_video_handler)

# Регистрация обработчика PDF файлов
pdf_handler = MessageHandler(filters.Document.MimeType("application/pdf"), pdf_file_reply)
application.add_handler(pdf_handler)

# Регистрация обработчика текстовых сообщений
message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, chatgpt_reply)
application.add_handler(message_handler)

# Регистрация обработчика аудио сообщений
audio_handler = MessageHandler(filters.VOICE, audio_reply)
application.add_handler(audio_handler)

# Регистрация обработчика видео сообщений
video_note_handler = MessageHandler(filters.VIDEO_NOTE, video_note_reply)
application.add_handler(video_note_handler)

# Регистрация обработчика изображений
photo_handler = MessageHandler(filters.PHOTO, image_file_reply)
application.add_handler(photo_handler)

# Регистрация обработчика видео
video_handler = MessageHandler(filters.VIDEO, video_file_reply)
application.add_handler(video_handler)

# Запуск бота
application.run_polling()
