from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
import asyncio


BOT_TOKEN =
ADMIN_ID =
ADMIN_ID_2 = 

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


keys_users = [

]


pending_payments = {}

class PaymentCallback(CallbackData, prefix="payment"):
    action: str
    user_id: int

@dp.message(Command("start"))
async def start_message(message: Message):
    btn_buy_program = InlineKeyboardButton(text="Купить программу💎", callback_data="btn_buy_program")
    btn_faq = InlineKeyboardButton(text="FAQ❓", callback_data="btn_faq")
    btn_team = InlineKeyboardButton(text="Команда smartPC💻", callback_data="btn_team")
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [btn_buy_program],
        [btn_team, btn_faq]
    ])

    global keys_users
    user_id = message.from_user.id
    username = message.from_user.username or "Неизвестный пользователь"

    await bot.send_message(
        ADMIN_ID_2,
        f"Пользователь @{username}:\n"
        f"Зашёл ✅"
    )

    text = (
        """
🚀 Добро пожаловать в Pay Control | Lexium!

Вы на пороге новых возможностей. Для того чтобы продолжить, выберите нужное действие ниже:"""
    )
    await message.answer(text, reply_markup=markup)

@dp.callback_query(F.data == 'btn_back_start')
async def back_start(call: CallbackQuery):
    await call.message.delete()
    await start_message(call.message)

@dp.callback_query(lambda call: call.data == 'btn_faq')
async def faq(call: types.CallbackQuery):
    await call.message.delete()
    btn_back_start = InlineKeyboardButton(text="🔙 Назад", callback_data="btn_back_start")
    markup_faq = InlineKeyboardMarkup(inline_keyboard=[[btn_back_start]])
    text_faq = (
        "❓ <b>Часто задаваемые вопросы</b> ❓\n\n"
        "• <b>Что я получу после оплаты?</b>\n"
        "После оплаты вы получите уникальный ключ, который вам понадобиться, чтобы запустить smartPC Pro, а также ссылку-приглашение в группу, где найдете подробную инструкцию по установке программы и ответы на популярные вопросы.\n\n"
        "• <b>На какой операционной системе работает программа?</b>\n"
        "Программа совместима с Windows.\n\n"
        "• <b>Насколько сложна установка?</b>\n"
        "Установка проста и понятна, если следовать инструкции, предоставленной в группе.\n\n"
        "• <b>Подойдет ли программа для слабого ПК?</b>\n"
        "Да, программа разработана так, чтобы не нагружать ваш компьютер и работать даже на устройствах с минимальными характеристиками.\n\n"
        "• <b>Что делать, если возникли вопросы или проблемы?</b>\n"
        "Если у вас появились вопросы, вы всегда можете обратиться в техподдержку.\n\n"
        "💡 Если ваш вопрос не освещён здесь, не стесняйтесь спрашивать напрямую!"
    )

    await call.message.answer(text_faq, parse_mode="HTML", reply_markup=markup_faq)


@dp.callback_query(lambda call: call.data == 'btn_team')
async def team(call: types.CallbackQuery):
    await call.message.delete()
    btn_back_start = InlineKeyboardButton(text="🔙 Назад", callback_data="btn_back_start")
    markup_team = InlineKeyboardMarkup(inline_keyboard=[[btn_back_start]])

    text = (
        "👨‍💻 <b>Основатель и разработчик:</b> @lexium_official\n"
        "🛠 <b>Администратор:</b> @EpochaShopES\n"
        "📩 <b>Тех-поддержка:</b> @zdxdq\n\n"
        "Если у вас возникли вопросы или проблемы, не стесняйтесь обращаться! 😊"
    )

    await call.message.answer(text, parse_mode="HTML", reply_markup=markup_team)


@dp.callback_query(F.data == "btn_buy_program")
async def buy_program(call: CallbackQuery):
    await call.message.delete()
    btn_back_start = InlineKeyboardButton(text="🔙 Назад", callback_data="btn_back_start")
    smartpc_pro = InlineKeyboardButton(text="smartPC Pro 💎", callback_data="smartpc_pro")
    markup_buy_program = InlineKeyboardMarkup(inline_keyboard=[[btn_back_start],
                                                               [smartpc_pro]])

    await call.message.answer("Выберите проект, чтобы получить реквизиты:", reply_markup=markup_buy_program)
    await call.answer()


@dp.callback_query(lambda call: call.data == 'smartpc_pro')
async def send_payment_info(call: CallbackQuery):
    await call.message.delete()
    btn_back_main = InlineKeyboardButton(text="🔙 Назад", callback_data="btn_back_main")
    btn_sberbank = InlineKeyboardButton(text="Сбербанк 🇷🇺", callback_data="btn_sberbank")
    btn_crypto = InlineKeyboardButton(text="Криптовалюта 💰", callback_data="btn_crypto")
    btn_sbp = InlineKeyboardButton(text="СБП 🇷🇺", callback_data="btn_sbp")
    markup_main = InlineKeyboardMarkup(inline_keyboard=[
        [btn_back_main],
        [btn_sberbank],
        [btn_crypto],
        [btn_sbp]])

    user_id = call.from_user.id
    username = call.from_user.username or "Неизвестный пользователь"

    await bot.send_message(
        ADMIN_ID_2,
        f"Пользователь @{username}:\n"
        f"smartPC Pro ✅"
    )


    await call.message.answer("Выберите один из способов оплаты:", reply_markup=markup_main)
    await call.answer()

@dp.callback_query(F.data == 'btn_back_main')
async def back_main(call: CallbackQuery):
    await start_message(call.message)

@dp.callback_query(lambda call: call.data == 'btn_sberbank')
async def sberbank(call: types.CallbackQuery):
    await call.message.delete()
    btn_back_sberbank = InlineKeyboardButton(text="🔙 Назад", callback_data="btn_back_sberbank")
    markup_sberbank = InlineKeyboardMarkup(inline_keyboard=[[btn_back_sberbank]])

    text = (
        "💸 *Оплата через Сбербанк* 💸\n\n"
        "💰 *Цена:*\n"
        "• 333 ₽\n\n"
        "💳 *Реквизиты для перевода:*\n"
        "`2202208100738021` (Дмитрий Игоревич)\n\n"
        "📸 *После оплаты:* отправьте сюда скриншот подтверждения!\n\n"
        "🔔 _Оплата проверяется владельцем._"
    )

    await call.message.answer(text, parse_mode="Markdown", reply_markup=markup_sberbank)



@dp.callback_query(F.data == 'btn_back_sberbank')
async def back_sberbank(call: CallbackQuery):
    await send_payment_info(call)


@dp.callback_query(lambda call: call.data == 'btn_crypto')
async def crypto(call: types.CallbackQuery):
    await call.message.delete()
    btn_back = InlineKeyboardButton(text="🔙 Назад", callback_data="btn_back")
    btn_ton = InlineKeyboardButton(text="💎 TON", callback_data="btn_ton")
    btn_usdt_trc = InlineKeyboardButton(text="💰 USDT (TRC-20)", callback_data="btn_usdt_trc")
    btn_usdt_erc = InlineKeyboardButton(text="💰 USDT (ERC-20)", callback_data="btn_usdt_erc")
    btn_btc = InlineKeyboardButton(text="₿ Bitcoin", callback_data="btn_btc")
    btn_eth = InlineKeyboardButton(text="🌐 Ethereum", callback_data="btn_eth")
    markup_crypto = InlineKeyboardMarkup(inline_keyboard=[
        [btn_back],
        [btn_ton],
        [btn_usdt_trc],
        [btn_usdt_erc],
        [btn_btc],
        [btn_eth]])
    await call.message.answer("""Выберите:\n
""", reply_markup=markup_crypto)


@dp.callback_query(F.data == 'btn_back')
async def go_back_ru(call: CallbackQuery):
    await send_payment_info(call)


@dp.callback_query(lambda call: call.data == 'btn_ton')
async def ton(call: types.CallbackQuery):
    await call.message.delete()
    btn_back = InlineKeyboardButton(text="🔙 Назад", callback_data="btn_back_crypto")
    markup_ton = InlineKeyboardMarkup(inline_keyboard=[[btn_back]])

    text = (
        "💳 *Оплата TON* 💳\n\n"
        "💰 *Цена:*\n"
        "• 333 ₽\n"
        "• 3,27 $\n\n"
        "💎 *Адрес для перевода:*\n"
        "`UQA6TbltoThT6ekDec-DdZEetcrSP5ouAdfmAKjvadIG_Yh5`\n\n"
        "📸 *После оплаты:* отправьте сюда скриншот подтверждения!\n\n"
        "🔔 _Оплата проверяется владельцем._"
    )

    await call.message.answer(text, parse_mode="Markdown", reply_markup=markup_ton)


@dp.callback_query(lambda call: call.data == 'btn_usdt_trc')
async def usdt_trc(call: types.CallbackQuery):
    await call.message.delete()
    btn_back = InlineKeyboardButton(text="🔙 Назад", callback_data="btn_back_crypto")
    markup_usdt_trc = InlineKeyboardMarkup(inline_keyboard=[[btn_back]])

    text = (
        "💳 *Оплата USDT (TRC-20)* 💳\n\n"
        "💰 *Цена:*\n"
        "• 333 ₽\n"
        "• 3,27 $\n\n"
        "💎 *Адрес для перевода:*\n"
        "`TG4daRPUtsX6oyMJ9T1APq5Nyoq74iFCUU`\n\n"
        "📸 *После оплаты:* отправьте сюда скриншот подтверждения!\n\n"
        "🔔 _Оплата проверяется владельцем._"
    )

    await call.message.answer(text, parse_mode="Markdown", reply_markup=markup_usdt_trc)


@dp.callback_query(lambda call: call.data == 'btn_usdt_erc')
async def usdt_erc(call: types.CallbackQuery):
    await call.message.delete()
    btn_back = InlineKeyboardButton(text="🔙 Назад", callback_data="btn_back_crypto")
    markup_usdt_erc = InlineKeyboardMarkup(inline_keyboard=[[btn_back]])

    text = (
        "💳 *Оплата USDT (ERC-20)* 💳\n\n"
        "💰 *Цена:*\n"
        "• 333 ₽\n"
        "• 3,27 $\n\n"
        "💎 *Адрес для перевода:*\n"
        "`0xb7363a19645a008db430d37c2ad40cbeddf21805`\n\n"
        "📸 *После оплаты:* отправьте сюда скриншот подтверждения!\n\n"
        "🔔 _Оплата проверяется владельцем._"
    )

    await call.message.answer(text, parse_mode="Markdown", reply_markup=markup_usdt_erc)


@dp.callback_query(lambda call: call.data == 'btn_btc')
async def btc(call: types.CallbackQuery):
    await call.message.delete()
    btn_back = InlineKeyboardButton(text="🔙 Назад", callback_data="btn_back_crypto")
    markup_btc = InlineKeyboardMarkup(inline_keyboard=[[btn_back]])

    text = (
        "💰 *Оплата Bitcoin* 💰\n\n"
        "💰 *Цена:*\n"
        "• 333 ₽\n"
        "• 3,27 $\n\n"
        "🔑 *Адрес для перевода:*\n"
        "`1KXSoU7ojt3i4NoKh5BueAK1m9PGcEUEaT`\n\n"
        "📸 *После оплаты:* отправьте сюда скриншот подтверждения!\n\n"
        "🔔 _Оплата проверяется владельцем._"
    )

    await call.message.answer(text, parse_mode="Markdown", reply_markup=markup_btc)


@dp.callback_query(lambda call: call.data == 'btn_eth')
async def eth(call: types.CallbackQuery):
    await call.message.delete()
    btn_back = InlineKeyboardButton(text="🔙 Назад", callback_data="btn_back_crypto")
    markup_eth = InlineKeyboardMarkup(inline_keyboard=[[btn_back]])

    text = (
        "💰 *Оплата Ethereum (ERC-20)* 💰\n\n"
        "💰 *Цена:*\n"
        "• 333 ₽\n"
        "• 3,27 $\n\n"
        "🔑 *Адрес для перевода:*\n"
        "`0xb7363a19645a008db430d37c2ad40cbeddf21805`\n\n"
        "📸 *После оплаты:* отправьте сюда скриншот подтверждения!\n\n"
        "🔔 _Оплата проверяется владельцем._"
    )

    await call.message.answer(text, parse_mode="Markdown", reply_markup=markup_eth)


@dp.callback_query(F.data == 'btn_back_crypto')
async def go_back_ru(call: CallbackQuery):
    await crypto(call)

@dp.callback_query(lambda call: call.data == 'btn_sbp')
async def sbp(call: types.CallbackQuery):
    await call.message.delete()
    btn_back_sbp = InlineKeyboardButton(text="🔙 Назад", callback_data="btn_back_sbp")
    markup_sbp = InlineKeyboardMarkup(inline_keyboard=[[btn_back_sbp]])

    text = (
        "💸 *Оплата через СБП* 💸\n\n"
        "💰 *Цена:*\n"
        "• 333 ₽\n\n"
        "📱 *Номер для перевода:*\n"
        "Спрашивайте у @lexium_official\n\n"
        "📸 *После оплаты:* отправьте сюда скриншот подтверждения!\n\n"
        "🔔 _Оплата проверяется владельцем._"
    )
    text = text.replace('*', '\\*').replace('_', '\\_')
    await call.message.answer(text, parse_mode="Markdown", reply_markup=markup_sbp)



@dp.callback_query(F.data == 'btn_back_sbp')
async def back_sbp(call: CallbackQuery):
    await send_payment_info(call)


user_payments = {}  # Словарь для хранения данных пользователей


@dp.message(F.photo)
async def handle_payment_confirmation(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "без username"

    if user_id not in pending_payments:
        pending_payments[user_id] = message.photo[-1].file_id

        user_payments[user_id] = {"username": username, "status": "На проверке"}

        await message.answer("Ваше подтверждение отправлено на проверку. Ожидайте ответа.")

        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="✅ Подтвердить",
                        callback_data=PaymentCallback(action="confirm", user_id=user_id).pack(),
                    ),
                    InlineKeyboardButton(
                        text="❌ Отклонить",
                        callback_data=PaymentCallback(action="decline", user_id=user_id).pack(),
                    ),
                ]
            ]
        )

        await bot.send_photo(
            ADMIN_ID,
            photo=message.photo[-1].file_id,
            caption=f"Пользователь @{username} отправил подтверждение оплаты. Проверьте!",
            reply_markup=markup,
        )
    else:
        await message.answer("Вы уже отправили подтверждение. Ожидайте проверки.")


@dp.callback_query(PaymentCallback.filter(F.action.in_({"confirm", "decline"})))
async def handle_admin_response(call: CallbackQuery, callback_data: PaymentCallback):
    global keys_users
    user_id = callback_data.user_id
    action = callback_data.action

    if user_id in pending_payments:
        del pending_payments[user_id]

        if action == "confirm":
            user_payments[user_id]["status"] = "Подтверждено"

            if keys_users:
                key = keys_users.pop(0)

                open_link_button = InlineKeyboardButton(
                    text="🔗 Группа smartPC Pro",
                    url="https://t.me/+xvy47aDrN8s0ZTQy"
                )
                markup = InlineKeyboardMarkup(inline_keyboard=[
                    [open_link_button]
                ])

                await bot.send_message(
                    user_id,
                    f"✅ <b>Ваша оплата подтверждена!</b>\n\n"
                    f"Спасибо за покупку ❤️\n\n"
                    f"<b>Ваш ключ:</b>\n<code>{key}</code>\n\n"
                    f"🔒 <i>(Никому не сообщайте его!)</i>",
                    reply_markup=markup,
                    parse_mode="HTML"
                )

                await call.message.edit_caption(
                    f"{call.message.caption}\n\n✅ Оплата подтверждена.\n🔑 Ваш ключ: <code>{key}</code>",
                    parse_mode="HTML"
                )

                await bot.send_message(
                    ADMIN_ID,
                    f"Пользователь @{user_payments[user_id]['username']}:\n"
                    f"Статус: {user_payments[user_id]['status']} ✅\n"
                    f"🔑 Ключ: <code>{key}</code>",
                    parse_mode="HTML"
                )
            else:
                await bot.send_message(user_id, "Извините, но ключи закончились. Свяжитесь с поддержкой.")
                await call.message.edit_caption(
                    call.message.caption + "\n⚠️ Ключи закончились. Пожалуйста, свяжитесь с поддержкой."
                )
        elif action == "decline":
            user_payments[user_id]["status"] = "Отклонено"
            await bot.send_message(user_id, "❌ Ваша оплата отклонена. Попробуйте снова или свяжитесь с поддержкой.")
            await call.message.edit_caption(
                f"{call.message.caption}\n\n❌ Оплата отклонена.",
                reply_markup=None
            )

            # Лог для администратора
            await bot.send_message(
                ADMIN_ID,
                f"Пользователь @{user_payments[user_id]['username']}:\n"
                f"Статус: {user_payments[user_id]['status']}"
            )

        await call.answer("Действие выполнено.")
    else:
        await call.answer("Этот пользователь не отправлял подтверждение.", show_alert=True)




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Бот запущен!")
    asyncio.run(main())
