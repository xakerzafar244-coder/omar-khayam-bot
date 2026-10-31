import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")

keyboard = [
    ["📍 Приход на работу", "🚪 Уход с работы"],
    ["👥 Сотрудники", "📅 График работы"],
    ["📋 Мои задания", "📊 Отчёты"],
    ["❓ Помощь"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Добро пожаловать в OMAR KHAYAM!\n\n"
        "Система управления сотрудниками ресторана.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )

async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Ваш Telegram ID: {update.effective_user.id}"
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Раздел пока находится в разработке. Скоро он будет доступен."
    )

def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("myid", myid))
    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    print("OMAR KHAYAM bot запущен")
    app.run_polling()

if __name__ == "__main__":
    main()
