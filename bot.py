import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5100369649:AAHC0sA6AqcaKHKSGChXAZhK4ZjcHF-R4q4'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum!\nMen oddiy botman!")

@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga doir maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)