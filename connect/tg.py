from telegram import Bot
from telegram.error import TelegramError
import os
from datetime import datetime

token = os.getenv("TG_API_TOKEN")
chat_id = os.getenv("TG_CHAT_ID")

async def send_message(message: str):
    try:
        bot = Bot(str(token))
        # Create task for non-blocking message sending
        await bot.sendMessage(chat_id=str(chat_id), text=message)
    except TelegramError as e:
        print(f"Telegram sending error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error while sending telegram message: {str(e)}")

async def send_error(error_message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"❌ ERROR [{timestamp}]:\n{error_message}"
    # Create task for non-blocking error message
    await send_message(full_message)

async def send_info(info_message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"😎 [{timestamp}]:\n{info_message}"
    # Create task for non-blocking info message
    await send_message(full_message)
