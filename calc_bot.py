from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Привіт {update.effective_user.username}! Це бот, який вміє виконувати нескладні арифметичні операції. Введіить щось типу 3+5, і я надам відповідь")


async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    result = 0
    if '+' in text:
        arr = text.split('+')
        result = int(arr[0]) + int(arr[1])
    elif '-' in text:
        arr = text.split('-')
        result = int(arr[0]) - int(arr[1])
    elif '*' in text:
        arr = text.split('*')
        result = int(arr[0]) * int(arr[1])
    elif '/' in text:
        arr = text.split('/')
        if int(arr[1]) == 0:
            result="На 0 ділити не можна!"
        else:
            result = int(arr[0]) / int(arr[1])
    elif '^' in text:
        arr = text.split('^')
        result = int(arr[0]) ** int(arr[1])

    await update.message.reply_text(f"{text}={result}")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Тут буде інфо як користуватись ботом, і його функціями")

app = ApplicationBuilder().token('7612141725:AAHxzKAO7vCIznkil_-k9mx5SFilzDXuVTA').build()
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

app.run_polling()
