from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8539866780:AAEyGsZ4ipat1QUX8g7pSOf9pqNKdkKza6k"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌐 Сайт", url="https://example.com")],
        [InlineKeyboardButton("📋 Меню", url="https://example.com/menu")],
        [InlineKeyboardButton("📍 Локация", url="https://maps.google.com/?q=50.4501,30.5234")],
        [InlineKeyboardButton("⭐ Отзывы", url="https://example.com/reviews")],
        [InlineKeyboardButton("📞 Звонок", url="https://wa.me/380123456789")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Отсоси писюльку:", reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ Бот запущен...")
app.run_polling()

