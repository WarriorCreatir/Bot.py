import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

token = "6234374883:AAFjSSTWzCgqbhxGxlBir4yRG4O9NeWA3Lg"
openai_api_key = "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"

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def handle_message(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:",
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"],
    )
    await message.answer(response["choices"][0]["text"])


executor.start_polling(dp, skip_updates=True)
