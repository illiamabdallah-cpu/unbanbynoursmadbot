from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = "8201369697:AAFuqSILz0C6WTV2iqK2hwRe164HXChKaLE
Keep y"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك 👋\n\n"
        "أرسل رسالة الدعم أو لقطة شاشة وسأساعدك بفهمها وصياغة رد مهني باللغة الإنجليزية."
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    await update.message.reply_text(
        f"تم استلام الرسالة:\n\n{user_text}\n\n"
        "سيتم لاحقاً ربط البوت بالذكاء الاصطناعي لتحليلها."
    )

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "تم استلام الصورة بنجاح 📷"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    app.run_polling()

if __name__ == "__main__":
    main()
