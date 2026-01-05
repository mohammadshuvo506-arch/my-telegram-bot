import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

# আপনার তথ্য (এগুলো পরিবর্তন করার দরকার নেই, আমরা সিক্রেট ব্যবহার করছি)
import os
API_ID = int(os.getenv("API_ID", "31291220"))
API_HASH = os.getenv("API_HASH", "f8a900d9d3382b157b47c5564656f9f0")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_STRING = os.getenv("SESSION_STRING")

# বট এবং ইউজার ক্লায়েন্ট সেটআপ
bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client("my_user", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("হ্যালো! আপনার অটো-ফরওয়ার্ড বটটি সচল আছে।")

@user.on_message(filters.chat(-1002360580971)) # সোর্স চ্যানেল
async def forward(client, message):
    try:
        # ডেস্টিনেশন চ্যানেলে ফরওয়ার্ড (-1003660478356)
        await message.forward("-1003660478356")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    await bot.start()
    await user.start()
    print("বট সফলভাবে চালু হয়েছে!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
