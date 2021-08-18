
import logging
from aiogram import Bot, Dispatcher, executor, types

from oxfordLookup import getDefinitions
from googletrans import Translator


translator = Translator()
API_TOKEN = '1950732302:AAGejQPhpRUm4_FkrwWzs7Gx4TQmdfMv-4Y'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(1919023351, {message.from_user.username})
    await message.reply(f"<b>Assalomu alaykum {message.from_user.first_name} \nBizni tanlaganingiz uchun raxmat 😊\nBotdan foydalanish uchun biror so'z yoki matn yuboring</b> 😉",parse_mode='HTML')


@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text,dest='en').text
        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"<b>Word: {word_id} \nDefinitions:\n{lookup['definitions']}</b>",parse_mode='HTML')
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("<b>....Natija topilmadi 🥺</b>",parse_mode='HTML')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




