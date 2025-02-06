from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import requests

TOKEN = "7555046044:AAG_ZQyFJ6QrLjO6zb1LdDfKSh7ZkzMCqgk"

async def start(update: Update, context):
    await update.message.reply_text("Send me a TikTok video link, and I'll download it!")

async def download_tiktok(update: Update, context):
    url = update.message.text
    if "tiktok.com" not in url:
        await update.message.reply_text("Please send a valid TikTok link!")
        return

    api_url = f"https://www.tikwm.com/api/?url={url}"
    response = requests.get(api_url).json()

    if response["code"] == 0:
        video_url = response["data"]["play"]
        await update.message.reply_video(video=video_url, caption="Brown kid's Download bot")
    else:
        await update.message.reply_text("Failed to download the video.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_tiktok))

app.run_polling()
