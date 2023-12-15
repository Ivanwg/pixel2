import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.message import ContentType
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.types import CallbackQuery

import all_lang
import db
import exchange
import f1_3x3
import f2_3x3
import f3_3x3
import f4_3x3
import f5_3x3
import f6_3x3
import f7_3x3
import f8_3x3
import f9_3x3

import free_3x3
from exchange import fir1, sec1, thi1, fou1, fif1, six1, sev1, fir2, sec2, thi2, fou2, fif2, six2, sev2, fir3, sec3, \
    thi3, fou3, fif3, six3, sev3, fir4, sec4, thi4, fou4, fif4, six4, sev4

import game_2x2
import game_2x3
import game_3x3
import game_settings
import config
import lists
# log
import payments
import r1_2x3
import r2_2x3
import r3_2x3
import r4_2x3
import r5_2x3
import r6_2x3
import risk_3x3
import risk_4x4
import risk_5x5
import s1_3x3
import s2_3x3
import s3_3x3
import s4_3x3
import s5_3x3
import s6_3x3
import s7_3x3
import s8_3x3
import s9_3x3

logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.TOKEN)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start', 'menu', 'wallet', 'play', 'settings'])
async def start(message: types.Message):
    chat_id = message.chat.id
    user_id = message.chat.id
    msg = message.text
    print(message.from_user.username, "->", msg[:6])
    if message.chat.type == "private":
        if msg[:6] == "/start":
            registry = db.get_registry(user_id)
            if not registry:
                referrer_id = str(msg[7:])
                if str(referrer_id) != "":
                    if str(referrer_id) != str(message.from_user.id):
                        try:
                            markup = InlineKeyboardMarkup(row_width=1)
                            play, back = all_lang.button_go_friend(user_id)
                            text = all_lang.text_go_friend(user_id)
                            markup.add(play, back)
                            await bot.send_message(referrer_id,
                                                   text,
                                                   reply_markup=markup, parse_mode='html')
                        except:
                            pass
                        language, currency, registry = lists.add_user(user_id, message)
                        my_promo = db.new_my_promo(user_id, referrer_id)
                        free_game = db.new_user_yes(user_id)
                        # ! выдать бесплатные игры для айди ниже и выдать +1 приглашённый пользователь по команде count_friend
                        # free_game = db.ref_user(referrer_id)
                        # count_friend = db.new_count_friend(user_id)
                        text, markup = lists.start(user_id)
                        await bot.send_message(chat_id, text,
                                               reply_markup=markup, parse_mode='html', disable_web_page_preview=True)
                    else:
                        markup = InlineKeyboardMarkup()
                        text, again = all_lang.text_no_use(user_id)
                        markup.add(again)
                        await bot.send_message(chat_id, text,
                                               reply_markup=markup)
                else:
                    language, currency, registry = lists.add_user(user_id, message)
                    free_game = db.new_user_no(user_id)
                    text, markup = lists.start(user_id)
                    await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html', disable_web_page_preview=True)
            else:
                text, markup = lists.start(user_id)
                await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html', disable_web_page_preview=True)


@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    print(web_app_message)
    msg, user_id = web_app_message.web_app_data.data.split()
    user_id = int(user_id)
    print(msg, user_id)
    if msg == "wallet":
        text, markup = lists.wallet(user_id)
    elif msg == "change":
        text, markup = lists.change(user_id)
    elif msg == "withdraw":
        text, markup = lists.withdraw(user_id)
    else:
        return
    await bot.send_message(chat_id=user_id, text=text, reply_markup=markup, parse_mode='html')


@dp.callback_query_handler(lambda c: c.data)
async def inlines(c):
    msg = c.data
    chat_id = c.message.chat.id
    message_id = c.message.message_id
    print(c.from_user.username, "->", msg)
    user_id = c.from_user.id
    if msg == "back":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text,
                               reply_markup=markup, parse_mode='html', disable_web_page_preview=True)
    elif msg == "wallet":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.wallet(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.change(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_first":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_first(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_first_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_first_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_first_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        ton = db.get_ton(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if ton >= 3:
                ba = 300
                to = 3
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if ton >= 5:
                ba = 500
                to = 5
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if ton >= 1:
                ba = 100
                to = 1
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if ton >= 10:
                ba = 1000
                to = 10
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_second":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_second(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_second_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_second_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_second_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        ton = db.get_ton(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if ton >= 6:
                ba = 600
                to = 6
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if ton >= 10:
                ba = 1000
                to = 10
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if ton >= 2:
                ba = 200
                to = 2
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if ton >= 20:
                ba = 2000
                to = 20
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_third":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_third(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_third_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_third_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_third_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        ton = db.get_ton(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if ton >= 12:
                ba = 1200
                to = 12
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if ton >= 20:
                ba = 2000
                to = 20
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if ton >= 4:
                ba = 400
                to = 4
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if ton >= 40:
                ba = 4000
                to = 40
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_fourth":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_fourth(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_fourth_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_fourth_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_fourth_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        ton = db.get_ton(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if ton >= 18:
                ba = 1800
                to = 18
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if ton >= 30:
                ba = 3000
                to = 30
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if ton >= 6:
                ba = 600
                to = 6
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if ton >= 60:
                ba = 6000
                to = 60
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_fifth":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_fifth(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_fifth_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_fifth_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_fifth_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        ton = db.get_ton(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if ton >= 30:
                ba = 3000
                to = 30
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if ton >= 50:
                ba = 5000
                to = 50
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if ton >= 10:
                ba = 1000
                to = 10
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if ton >= 100:
                ba = 10000
                to = 100
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_sixth":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_sixth(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_sixth_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_sixth_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_sixth_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        ton = db.get_ton(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if ton >= 60:
                ba = 6000
                to = 60
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if ton >= 100:
                ba = 10000
                to = 100
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if ton >= 20:
                ba = 2000
                to = 20
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if ton >= 200:
                ba = 20000
                to = 200
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_seventh":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_seventh(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_seventh_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.pixel_change_seventh_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "pixel_change_seventh_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        ton = db.get_ton(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if ton >= 600:
                ba = 60000
                to = 600
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if ton >= 1000:
                ba = 100000
                to = 1000
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if ton >= 200:
                ba = 20000
                to = 200
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if ton >= 2000:
                ba = 200000
                to = 2000
                balance = db.new_balance_plus(user_id, ba)
                ton = db.new_ton_minus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_first":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_first(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_first_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_first_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_first_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        balance = db.get_balance(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if balance >= 300:
                ba = 300
                to = 3
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if balance >= 500:
                ba = 500
                to = 5
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if balance >= 100:
                ba = 100
                to = 1
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if balance >= 1000:
                ba = 1000
                to = 10
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_second":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_second(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_second_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_second_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_second_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        balance = db.get_balance(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if balance >= 600:

                ba = 600
                to = 6
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if balance >= 1000:
                ba = 1000
                to = 10
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if balance >= 200:

                ba = 200
                to = 2
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if balance >= 2000:

                ba = 2000
                to = 20
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)

        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_third":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_third(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_third_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_third_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_third_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        balance = db.get_balance(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if balance >= 1200:

                ba = 1200
                to = 12
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" \
                or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" \
                or currency == "MXN":
            if balance >= 2000:

                ba = 2000
                to = 20
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if balance >= 400:

                ba = 400
                to = 4
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if balance >= 4000:

                ba = 4000
                to = 40
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)

        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_fourth":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_fourth(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_fourth_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_fourth_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_fourth_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        balance = db.get_balance(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if balance >= 1800:

                ba = 1800
                to = 18
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if balance >= 3000:

                ba = 3000
                to = 30
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if balance >= 600:

                ba = 600
                to = 6
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if balance >= 6000:

                ba = 6000
                to = 60
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)

        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_fifth":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_fifth(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_fifth_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_fifth_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_fifth_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        balance = db.get_balance(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if balance >= 3000:

                ba = 3000
                to = 30
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if balance >= 5000:

                ba = 5000
                to = 50
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if balance >= 1000:
                ba = 1000
                to = 10
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if balance >= 10000:
                ba = 10000
                to = 100
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_sixth":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_sixth(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_sixth_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_sixth_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_sixth_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        balance = db.get_balance(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if balance >= 6000:
                ba = 6000
                to = 60
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if balance >= 10000:
                ba = 10000
                to = 100
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if balance >= 2000:
                ba = 2000
                to = 20
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if balance >= 20000:
                ba = 20000
                to = 200
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_seventh":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_seventh(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_seventh_done":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_change_seventh_done(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_change_seventh_finish":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        currency = db.get_currency(user_id)
        balance = db.get_balance(user_id)
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or \
                currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" \
                or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            if balance >= 60000:
                ba = 60000
                to = 600
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or \
                currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            if balance >= 100000:
                ba = 100000
                to = 1000
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        elif currency == "EGP" or currency == "INR":
            if balance >= 20000:
                ba = 20000
                to = 200
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        else:
            if balance >= 200000:
                ba = 200000
                to = 2000
                balance = db.new_balance_minus(user_id, ba)
                ton = db.new_ton_plus(user_id, to)
                text, markup = lists.wallet(user_id)
            else:
                markup = InlineKeyboardMarkup(row_width=1)
                text, top, back = all_lang.back_no_wallet(user_id)
                markup.add(top)
                markup.add(back)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "settings":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "settings_en":
        lang = 'en'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_en(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)
    elif msg == "settings_ru":
        lang = 'ru'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_ru(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)
    elif msg == "settings_id":
        lang = 'id'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_id(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)

    elif msg == "settings_es":
        lang = 'es'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_es(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)

    elif msg == "settings_ko":
        lang = 'ko'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_ko(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)

    elif msg == "settings_it":
        lang = 'it'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_it(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)

    elif msg == "settings_ch":
        lang = 'ch'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_ch(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)

    elif msg == "settings_ta":
        lang = 'ta'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_ta(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)

    elif msg == "settings_fa":
        lang = 'fa'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_fa(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)

    elif msg == "settings_tr":
        lang = 'tr'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_tr(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)

    elif msg == "settings_uz":
        lang = 'uz'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_uz(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)

    elif msg == "settings_be":
        lang = 'be'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_be(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)

    elif msg == "settings_hi":
        lang = 'hi'
        language = db.new_language(user_id, lang)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
            # text, markup = lists.settings_hi(user_id)
        text, markup = lists.start(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)
    elif msg == "change_lang":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.change_lang(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "promo_code":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.promo_code(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html',
                               disable_web_page_preview=True)
    elif msg == "deposit":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.deposit(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "card":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.card(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "first_card":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.first_card(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "second_card":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.second_card(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "third_card":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.third_card(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "fourth_card":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.fourth_card(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "fifth_card":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.fifth_card(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "sixth_card":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.sixth_card(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "seventh_card":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.seventh_card(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "ton_coin":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.ton_coin(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "first_buy_ton":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.first_buy_ton(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "first_buy_ton_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.first_buy_ton_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "second_buy_ton":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.second_buy_ton(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "second_buy_ton_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.second_buy_ton_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "third_buy_ton":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.third_buy_ton(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "third_buy_ton_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.third_buy_ton_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "fourth_buy_ton":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.fourth_buy_ton(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "fourth_buy_ton_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.fourth_buy_ton_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "fifth_buy_ton":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.fifth_buy_ton(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "fifth_buy_ton_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.fifth_buy_ton_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "sixth_buy_ton":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.sixth_buy_ton(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "sixth_buy_ton_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.sixth_buy_ton_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "seventh_buy_ton":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.seventh_buy_ton(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "seventh_buy_ton_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.seventh_buy_ton_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw_first":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw_first(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw_first_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw_first_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw_second":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw_second(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw_second_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw_second_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw_third":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw_third(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw_third_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw_third_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw_fourth":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw_fourth(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw_fourth_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw_fourth_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw_fifth":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw_fifth(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw_fifth_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw_fifth_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw_sixth":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw_sixth(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "withdraw_sixth_ok":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.withdraw_sixth_ok(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency":
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.change_currency(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_usd":
        value = 'USD'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_eur":
        value = 'EUR'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_rub":
        value = 'RUB'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_gbp":
        value = 'GBP'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_uah":
        value = 'UAH'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_kzt":
        value = 'KZT'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_byn":
        value = 'BYN'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_krw":
        value = 'KRW'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_ils":
        value = 'ILS'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_idr":
        value = 'IDR'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_aed":
        value = 'AED'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_gel":
        value = 'GEL'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_twd":
        value = 'TWD'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_try":
        value = 'TRY'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_hkd":
        value = 'HKD'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_inr":
        value = 'INR'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_cad":
        value = 'CAD'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_amd":
        value = 'AMD'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_aud":
        value = 'AUD'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_pln":
        value = 'PLN'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_cop":
        value = 'COP'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_brl":
        value = 'BRL'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_chf":
        value = 'CHF'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_mxn":
        value = 'MXN'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_ars":
        value = 'ARS'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_sgd":
        value = 'SGD'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_sar":
        value = 'SAR'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_mdl":
        value = 'MDL'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_jpy":
        value = 'JPY'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_ron":
        value = 'RON'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_sek":
        value = 'SEK'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_azn":
        value = 'AZN'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_rsd":
        value = 'RSD'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_nok":
        value = 'NOK'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')
    elif msg == "change_currency_myr":
        value = 'MYR'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_bgn":
        value = 'BGN'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_egp":
        value = 'EGP'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_gtq":
        value = 'GTQ'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_clp":
        value = 'CLP'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "change_currency_nzd":
        value = 'NZD'
        currency = db.new_currency(user_id, value)
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass
        text, markup = lists.settings(user_id)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode='html')

    elif msg == "tg_mode":
        text, markup = lists.tg_mode(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "norm_base_four":
        text, markup = game_settings.norm_base_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)
    elif msg == "norm_base_six":
        text, markup = game_settings.norm_base_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "norm_base_nine":
        text, markup = game_settings.norm_base_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "norm_bronze_four":
        text, markup = game_settings.norm_bronze_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "norm_bronze_six":
        text, markup = game_settings.norm_bronze_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "norm_bronze_nine":
        text, markup = game_settings.norm_bronze_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "norm_silver_four":
        text, markup = game_settings.norm_silver_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)
    elif msg == "norm_silver_six":
        text, markup = game_settings.norm_silver_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)
    elif msg == "norm_silver_nine":
        text, markup = game_settings.norm_silver_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "norm_gold_four":
        text, markup = game_settings.norm_gold_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)
    elif msg == "norm_gold_six":
        text, markup = game_settings.norm_gold_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "norm_gold_nine":
        text, markup = game_settings.norm_gold_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "norm_vip_four":
        text, markup = game_settings.norm_vip_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)
    elif msg == "norm_vip_six":
        text, markup = game_settings.norm_vip_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "norm_vip_nine":
        text, markup = game_settings.norm_vip_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "first_pay":
        key = "first_pay"
        price, title, description, provider_token, currencies, photo_url, photo_width, photo_height, photo_size, \
        is_flexible, prices, start_parameter, payload = payments.pay(user_id, key)
        await bot.send_invoice(chat_id,
                               title=title,
                               description=description,
                               provider_token=provider_token,
                               currency=currencies,
                               photo_url=photo_url,
                               photo_width=photo_width,
                               photo_height=photo_height,
                               # photo_size=photo_size,
                               is_flexible=is_flexible,
                               prices=prices,
                               start_parameter=start_parameter,
                               payload=payload)

    elif msg == "second_pay":
        key = "second_pay"
        price, title, description, provider_token, currencies, photo_url, photo_width, photo_height, photo_size, \
        is_flexible, prices, start_parameter, payload = payments.pay(user_id, key)
        await bot.send_invoice(chat_id,
                               title=title,
                               description=description,
                               provider_token=provider_token,
                               currency=currencies,
                               photo_url=photo_url,
                               photo_width=photo_width,
                               photo_height=photo_height,
                               # photo_size=photo_size,
                               is_flexible=is_flexible,
                               prices=prices,
                               start_parameter=start_parameter,
                               payload=payload)
    elif msg == "third_pay":
        key = "third_pay"
        price, title, description, provider_token, currencies, photo_url, photo_width, photo_height, photo_size, \
        is_flexible, prices, start_parameter, payload = payments.pay(user_id, key)
        await bot.send_invoice(chat_id,
                               title=title,
                               description=description,
                               provider_token=provider_token,
                               currency=currencies,
                               photo_url=photo_url,
                               photo_width=photo_width,
                               photo_height=photo_height,
                               # photo_size=photo_size,
                               is_flexible=is_flexible,
                               prices=prices,
                               start_parameter=start_parameter,
                               payload=payload)
    elif msg == "fourth_pay":
        key = "fourth_pay"
        price, title, description, provider_token, currencies, photo_url, photo_width, photo_height, photo_size, \
        is_flexible, prices, start_parameter, payload = payments.pay(user_id, key)
        await bot.send_invoice(chat_id,
                               title=title,
                               description=description,
                               provider_token=provider_token,
                               currency=currencies,
                               photo_url=photo_url,
                               photo_width=photo_width,
                               photo_height=photo_height,
                               # photo_size=photo_size,
                               is_flexible=is_flexible,
                               prices=prices,
                               start_parameter=start_parameter,
                               payload=payload)
    elif msg == "fifth_pay":
        key = "fifth_pay"
        price, title, description, provider_token, currencies, photo_url, photo_width, photo_height, photo_size, \
        is_flexible, prices, start_parameter, payload = payments.pay(user_id, key)
        await bot.send_invoice(chat_id,
                               title=title,
                               description=description,
                               provider_token=provider_token,
                               currency=currencies,
                               photo_url=photo_url,
                               photo_width=photo_width,
                               photo_height=photo_height,
                               # photo_size=photo_size,
                               is_flexible=is_flexible,
                               prices=prices,
                               start_parameter=start_parameter,
                               payload=payload)
    elif msg == "sixth_pay":
        key = "sixth_pay"
        price, title, description, provider_token, currencies, photo_url, photo_width, photo_height, photo_size, \
        is_flexible, prices, start_parameter, payload = payments.pay(user_id, key)
        await bot.send_invoice(chat_id,
                               title=title,
                               description=description,
                               provider_token=provider_token,
                               currency=currencies,
                               photo_url=photo_url,
                               photo_width=photo_width,
                               photo_height=photo_height,
                               # photo_size=photo_size,
                               is_flexible=is_flexible,
                               prices=prices,
                               start_parameter=start_parameter,
                               payload=payload)
    elif msg == "seventh_pay":
        key = "seventh_pay"
        price, title, description, provider_token, currencies, photo_url, photo_width, photo_height, photo_size, \
        is_flexible, prices, start_parameter, payload = payments.pay(user_id, key)
        await bot.send_invoice(chat_id,
                               title=title,
                               description=description,
                               provider_token=provider_token,
                               currency=currencies,
                               photo_url=photo_url,
                               photo_width=photo_width,
                               photo_height=photo_height,
                               # photo_size=photo_size,
                               is_flexible=is_flexible,
                               prices=prices,
                               start_parameter=start_parameter,
                               payload=payload)

    elif msg == "game_risk_base_four":
        save = db.new_save(user_id, msg)
        strings_four = db.new_strings_four(user_id)
        q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
        text, markup = risk_3x3.game_risk_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_bronze_four":
        save = db.new_save(user_id, msg)
        strings_four = db.new_strings_four(user_id)
        q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
        text, markup = risk_3x3.game_risk_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_silver_four":
        save = db.new_save(user_id, msg)
        strings_four = db.new_strings_four(user_id)
        q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
        text, markup = risk_3x3.game_risk_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_gold_four":
        save = db.new_save(user_id, msg)
        strings_four = db.new_strings_four(user_id)
        q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
        text, markup = risk_3x3.game_risk_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_vip_four":
        save = db.new_save(user_id, msg)
        strings_four = db.new_strings_four(user_id)
        q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
        text, markup = risk_3x3.game_risk_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rf1":
        strike = lists.no_balance_risk_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_3x3.rf1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rf2":
        strike = lists.no_balance_risk_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_3x3.rf2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rf3":
        strike = lists.no_balance_risk_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_3x3.rf3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rf4":
        strike = lists.no_balance_risk_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_3x3.rf4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rf5":
        strike = lists.no_balance_risk_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_3x3.rf5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rf6":
        strike = lists.no_balance_risk_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_3x3.rf6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rf7":
        strike = lists.no_balance_risk_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_3x3.rf7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rf8":
        strike = lists.no_balance_risk_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_3x3.rf8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rf9":
        strike = lists.no_balance_risk_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_3x3.rf9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_base_six":
        save = db.new_save(user_id, msg)
        strings_six = db.new_strings_six(user_id)
        w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
        text, markup = risk_4x4.game_risk_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_bronze_six":
        save = db.new_save(user_id, msg)
        strings_six = db.new_strings_six(user_id)
        w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
        text, markup = risk_4x4.game_risk_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_silver_six":
        save = db.new_save(user_id, msg)
        strings_six = db.new_strings_six(user_id)
        w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
        text, markup = risk_4x4.game_risk_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_gold_six":
        save = db.new_save(user_id, msg)
        strings_six = db.new_strings_six(user_id)
        w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
        text, markup = risk_4x4.game_risk_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_vip_six":
        save = db.new_save(user_id, msg)
        strings_six = db.new_strings_six(user_id)
        w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
        w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
        text, markup = risk_4x4.game_risk_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs1":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs2":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs3":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs4":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs5":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs6":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs7":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs8":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs9":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs10":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs10(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs11":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs11(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs12":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs12(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs13":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs13(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs14":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs14(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs15":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs15(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rs16":
        strike = lists.no_balance_4x4(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_4x4.rs16(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_base_nine":
        save = db.new_save(user_id, msg)
        strings_nine = db.new_strings_nine(user_id)
        e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(
            user_id)
        text, markup = risk_5x5.game_risk_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_bronze_nine":
        save = db.new_save(user_id, msg)
        strings_nine = db.new_strings_nine(user_id)
        e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(
            user_id)
        text, markup = risk_5x5.game_risk_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_silver_nine":
        save = db.new_save(user_id, msg)
        strings_nine = db.new_strings_nine(user_id)
        e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(
            user_id)
        text, markup = risk_5x5.game_risk_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_gold_nine":
        save = db.new_save(user_id, msg)
        strings_nine = db.new_strings_nine(user_id)
        e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(
            user_id)
        text, markup = risk_5x5.game_risk_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_risk_vip_nine":
        save = db.new_save(user_id, msg)
        strings_nine = db.new_strings_nine(user_id)
        e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(
            user_id)
        text, markup = risk_5x5.game_risk_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn1":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn2":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn3":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn4":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn5":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn6":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn7":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn8":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn9":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn10":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn10(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn11":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn11(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn12":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn12(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn13":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn13(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn14":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn14(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn15":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn15(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn16":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn16(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn17":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn17(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn18":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn18(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn19":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn19(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn20":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn20(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn21":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn21(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn22":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn22(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn23":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn23(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn24":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn24(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "rn25":
        strike = lists.no_balance_5x5(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = risk_5x5.rn25(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "risk_base_four":
        text, markup = game_settings.risk_base_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)
    elif msg == "risk_base_six":
        text, markup = game_settings.risk_base_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "risk_base_nine":
        text, markup = game_settings.risk_base_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "risk_bronze_four":
        text, markup = game_settings.risk_bronze_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "risk_bronze_six":
        text, markup = game_settings.risk_bronze_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "risk_bronze_nine":
        text, markup = game_settings.risk_bronze_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "risk_silver_four":
        text, markup = game_settings.risk_silver_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)
    elif msg == "risk_silver_six":
        text, markup = game_settings.risk_silver_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)
    elif msg == "risk_silver_nine":
        text, markup = game_settings.risk_silver_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "risk_gold_four":
        text, markup = game_settings.risk_gold_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)
    elif msg == "risk_gold_six":
        text, markup = game_settings.risk_gold_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "risk_gold_nine":
        text, markup = game_settings.risk_gold_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "risk_vip_four":
        text, markup = game_settings.risk_vip_four(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)
    elif msg == "risk_vip_six":
        text, markup = game_settings.risk_vip_six(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "risk_vip_nine":
        text, markup = game_settings.risk_vip_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html', disable_web_page_preview=True)

    elif msg == "free_nine":
        text, markup = game_settings.free_nine(user_id)
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                    parse_mode='html')

    elif msg == "game_base_four":
        save = db.new_save(user_id, msg)
        string_four = db.new_string_four(user_id)
        f1, f2, f3, f4 = db.index_string_four(user_id)
        text, markup = game_2x2.game(user_id)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    elif msg == "game_bronze_four":
        save = db.new_save(user_id, msg)
        string_four = db.new_string_four(user_id)
        f1, f2, f3, f4 = db.index_string_four(user_id)
        text, markup = game_2x2.game(user_id)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    elif msg == "game_silver_four":

        save = db.new_save(user_id, msg)
        string_four = db.new_string_four(user_id)
        f1, f2, f3, f4 = db.index_string_four(user_id)
        text, markup = game_2x2.game(user_id)
        # else:
        #     text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    elif msg == "game_gold_four":

        save = db.new_save(user_id, msg)
        string_four = db.new_string_four(user_id)
        f1, f2, f3, f4 = db.index_string_four(user_id)
        text, markup = game_2x2.game(user_id)
        # else:
        #     text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    elif msg == "game_vip_four":

        save = db.new_save(user_id, msg)
        string_four = db.new_string_four(user_id)
        f1, f2, f3, f4 = db.index_string_four(user_id)
        text, markup = game_2x2.game(user_id)
        # else:
        #     text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    elif msg == "game_base_six":

        save = db.new_save(user_id, msg)
        string_six = db.new_string_six(user_id)
        i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
        text, markup = game_2x3.game(user_id)
        # else:
        #     text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    elif msg == "game_bronze_six":

        save = db.new_save(user_id, msg)
        string_six = db.new_string_six(user_id)
        i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
        text, markup = game_2x3.game(user_id)
        # else:
        #     text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    elif msg == "game_silver_six":

        save = db.new_save(user_id, msg)
        string_six = db.new_string_six(user_id)
        i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
        text, markup = game_2x3.game(user_id)
        # else:
        #     text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    elif msg == "game_gold_six":
        save = db.new_save(user_id, msg)
        string_six = db.new_string_six(user_id)
        i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
        text, markup = game_2x3.game(user_id)
        # else:
        #     text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "game_vip_six":
        save = db.new_save(user_id, msg)
        string_six = db.new_string_six(user_id)
        i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
        text, markup = game_2x3.game(user_id)
        # else:
        #     text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "game_base_nine":
        save = db.new_save(user_id, msg)
        string_nine = db.new_string_nine(user_id)
        s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
        text, markup = game_3x3.game(user_id)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "game_bronze_nine":
        save = db.new_save(user_id, msg)
        string_nine = db.new_string_nine(user_id)
        s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
        text, markup = game_3x3.game(user_id)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "game_silver_nine":
        save = db.new_save(user_id, msg)
        string_nine = db.new_string_nine(user_id)
        s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
        text, markup = game_3x3.game(user_id)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "game_gold_nine":
        save = db.new_save(user_id, msg)
        string_nine = db.new_string_nine(user_id)
        s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
        text, markup = game_3x3.game(user_id)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "game_vip_nine":
        save = db.new_save(user_id, msg)
        string_nine = db.new_string_nine(user_id)
        s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
        text, markup = game_3x3.game(user_id)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    # -----------------------------------------------------------------------------------------------------------------
    elif msg == "sf1":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "sf1_sf2":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf1_sf2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "sf1_sf3":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf1_sf3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "sf1_sf4":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf1_sf4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "sf2":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "sf2_sf1":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf2_sf1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "sf2_sf3":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf2_sf3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "sf2_sf4":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf2_sf4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "sf3":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "sf3_sf1":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf3_sf1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "sf3_sf2":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf3_sf2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "sf3_sf4":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf3_sf4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "sf4":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "sf4_sf1":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf4_sf1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "sf4_sf2":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf4_sf2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "sf4_sf3":
        strike = lists.no_balance_2x2(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = game_2x2.sf4_sf3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # --------------------------------------------------------------------------------------------------------------------

    elif msg == "ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss1_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss1_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss1_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss1_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss1_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss1_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss1_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss1_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss6_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss2_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss2_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss2_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss2_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss2_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss2_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss2_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss2_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss6_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss3_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss3_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss3_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss3_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss3_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss3_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss3_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss3_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss6_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss4_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss4_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss4_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss4_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss4_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss4_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss4_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss4_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss6_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss5_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss5_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss5_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss5_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss5_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss5_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss6_ss5_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r6_2x3.ss6_ss5_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss1_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss1_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss1_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss1_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss1_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss1_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss1_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss1_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss5_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss2_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss2_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss2_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss2_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss2_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss2_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss2_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss2_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss5_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss3_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss3_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss3_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss3_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss3_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss3_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss3_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss3_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss5_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss4_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss4_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss4_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss4_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss4_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss4_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss4_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss4_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss5_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss6_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss6_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss6_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss6_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss6_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss6_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss5_ss6_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r5_2x3.ss5_ss6_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss1_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss1_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss1_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss1_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss1_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss1_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss1_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss1_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss4_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss2_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss2_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss2_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss2_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss2_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss2_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss2_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss2_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss4_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss3_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss3_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss3_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss3_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss3_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss3_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss3_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss3_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss4_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss5_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss5_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss5_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss5_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss5_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss5_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss5_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss5_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss4_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss6_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss6_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss6_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss6_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss6_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss6_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss4_ss6_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r4_2x3.ss4_ss6_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss1_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss1_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss1_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss1_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss1_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss1_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss1_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss1_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss3_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss2_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss2_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss2_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss2_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss2_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss2_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss2_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss2_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss3_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss4_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss4_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss4_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss4_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss4_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss4_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss4_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss4_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss3_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss5_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss5_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss5_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss5_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss5_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss5_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss5_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss5_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss3_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss6_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss6_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss6_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss6_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss6_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss6_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss3_ss6_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r3_2x3.ss3_ss6_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss1_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss1_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss1_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss1_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss1_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss1_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss1_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss1_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss2_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss3_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss3_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss3_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss3_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss3_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss3_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss3_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss3_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss2_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss4_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss4_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss4_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss4_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss4_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss4_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss4_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss4_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss2_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss5_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss5_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss5_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss5_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss5_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss5_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss5_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss5_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss2_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss6_ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss6_ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss6_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss6_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss6_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss6_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss2_ss6_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r2_2x3.ss2_ss6_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss1":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss2_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss2_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss2_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss2_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss2_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss2_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss2_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss2_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "ss1_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss3_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss3_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss3_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss3_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss3_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss3_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss3_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss3_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # -------------------------------------------------------------------------------------------------------------

    elif msg == "ss1_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss4_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss4_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss4_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss4_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss4_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss4_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss4_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss4_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ----------------------------------------------------------------------------------------------------------------

    elif msg == "ss1_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss5_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss5_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss5_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss5_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss5_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss5_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss5_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss5_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "ss1_ss6":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss6_ss2":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss6_ss2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss6_ss3":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss6_ss3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss6_ss4":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss6_ss4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "ss1_ss6_ss5":
        strike = lists.no_balance_2x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = r1_2x3.ss1_ss6_ss5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st9_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st9_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st9_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st9_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st9_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st9_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st9_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st9_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st9_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st9_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st9_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st9_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st9_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st9_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st1_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st8_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st8_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st8_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st8_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st8_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st8_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st8_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st8_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st8_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st8_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st8_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st8_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st8_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st8_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st1_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st7_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st7_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st7_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st7_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st7_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st7_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st7_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st7_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st7_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st7_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st7_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st7_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st7_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st7_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st1_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st6_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st6_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st6_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st6_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st6_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st6_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st6_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st6_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st6_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st6_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st6_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st6_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st6_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st6_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st1_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st5_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st5_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st5_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st5_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st5_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st5_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st5_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st5_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st5_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st5_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st5_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st5_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st5_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st5_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st1_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st4_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st4_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st4_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st4_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st4_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st4_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st4_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st4_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st4_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st4_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st4_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st4_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st4_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st4_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st1_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st3_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st3_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st3_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st3_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st3_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st3_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st3_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st3_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st3_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st3_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st3_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st3_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st3_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st3_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st1_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st2_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st2_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st2_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st2_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st2_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st2_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st2_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st2_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st2_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st2_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st2_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st2_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st1_st2_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s1_3x3.st1_st2_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ----------------------------------------------------------------------------------------------------------------

    elif msg == "st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st9_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st9_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st9_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st9_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st9_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st9_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st9_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st9_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st9_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st9_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st9_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st9_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st9_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st9_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st2_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st8_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st8_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st8_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st8_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st8_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st8_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st8_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st8_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st8_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st8_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st8_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st8_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st8_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st8_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st2_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st7_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st7_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st7_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st7_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st7_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st7_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st7_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st7_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st7_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st7_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st7_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st7_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st7_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st7_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st2_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st6_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st6_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st6_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st6_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st6_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st6_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st6_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st6_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st6_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st6_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st6_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st6_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st6_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st6_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st2_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st5_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st5_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st5_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st5_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st5_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st5_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st5_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st5_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st5_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st5_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st5_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st5_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st5_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st5_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st2_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st4_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st4_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st4_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st4_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st4_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st4_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st4_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st4_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st4_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st4_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st4_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st4_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st4_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st4_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st2_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st3_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st3_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st3_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st3_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st3_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st3_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st3_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st3_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st3_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st3_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st3_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st3_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st3_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st3_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st2_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st1_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st1_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st1_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st1_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st1_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st1_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st1_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st1_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st1_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st1_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st1_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st1_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st2_st1_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s2_3x3.st2_st1_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st9_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st9_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st9_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st9_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st9_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st9_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st9_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st9_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st9_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st9_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st9_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st9_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st9_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st9_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st3_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st8_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st8_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st8_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st8_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st8_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st8_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st8_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st8_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st8_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st8_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st8_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st8_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st8_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st8_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st3_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st7_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st7_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st7_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st7_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st7_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st7_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st7_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st7_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st7_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st7_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st7_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st7_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st7_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st7_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st3_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st6_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st6_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st6_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st6_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st6_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st6_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st6_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st6_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st6_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st6_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st6_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st6_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st6_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st6_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st3_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st5_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st5_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st5_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st5_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st5_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st5_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st5_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st5_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st5_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st5_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st5_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st5_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st5_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st5_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st3_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st4_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st4_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st4_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st4_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st4_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st4_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st4_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st4_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st4_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st4_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st4_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st4_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st4_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st4_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st3_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st2_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st2_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st2_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st2_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st2_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st2_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st2_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st2_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st2_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st2_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st2_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st2_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st2_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st2_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st3_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st1_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st1_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st1_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st1_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st1_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st1_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st1_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st1_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st1_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st1_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st1_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st1_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st3_st1_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s3_3x3.st3_st1_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st9_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st9_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st9_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st9_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st9_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st9_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st9_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st9_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st9_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st9_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st9_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st9_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st9_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st9_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st4_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st8_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st8_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st8_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st8_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st8_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st8_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st8_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st8_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st8_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st8_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st8_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st8_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st8_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st8_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st4_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st7_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st7_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st7_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st7_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st7_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st7_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st7_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st7_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st7_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st7_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st7_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st7_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st7_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st7_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st4_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st6_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st6_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st6_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st6_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st6_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st6_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st6_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st6_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st6_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st6_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st6_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st6_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st6_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st6_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st4_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st5_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st5_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st5_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st5_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st5_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st5_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st5_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st5_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st5_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st5_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st5_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st5_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st5_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st5_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st4_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st3_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st3_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st3_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st3_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st3_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st3_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st3_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st3_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st3_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st3_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st3_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st3_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st3_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st3_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st4_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st2_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st2_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st2_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st2_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st2_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st2_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st2_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st2_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st2_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st2_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st2_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st2_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st2_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st2_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st4_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st1_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st1_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st1_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st1_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st1_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st1_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st1_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st1_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st1_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st1_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st1_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st1_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st4_st1_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s4_3x3.st4_st1_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st9_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st9_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st9_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st9_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st9_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st9_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st9_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st9_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st9_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st9_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st9_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st9_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st9_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st9_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st5_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st8_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st8_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st8_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st8_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st8_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st8_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st8_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st8_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st8_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st8_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st8_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st8_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st8_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st8_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st5_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st7_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st7_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st7_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st7_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st7_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st7_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st7_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st7_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st7_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st7_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st7_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st7_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st7_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st7_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st5_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st6_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st6_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st6_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st6_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st6_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st6_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st6_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st6_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st6_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st6_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st6_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st6_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st6_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st6_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st5_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st4_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st4_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st4_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st4_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st4_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st4_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st4_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st4_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st4_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st4_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st4_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st4_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st4_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st4_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st5_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st3_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st3_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st3_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st3_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st3_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st3_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st3_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st3_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st3_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st3_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st3_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st3_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st3_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st3_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st5_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st2_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st2_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st2_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st2_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st2_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st2_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st2_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st2_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st2_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st2_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st2_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st2_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st2_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st2_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st5_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st1_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st1_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st1_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st1_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st1_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st1_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st1_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st1_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st1_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st1_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st1_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st1_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st5_st1_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s5_3x3.st5_st1_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st9_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st9_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st9_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st9_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st9_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st9_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st9_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st9_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st9_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st9_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st9_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st9_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st9_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st9_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st6_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st8_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st8_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st8_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st8_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st8_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st8_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st8_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st8_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st8_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st8_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st8_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st8_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st8_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st8_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st6_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st7_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st7_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st7_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st7_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st7_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st7_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st7_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st7_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st7_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st7_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st7_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st7_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st7_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st7_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st6_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st5_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st5_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st5_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st5_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st5_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st5_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st5_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st5_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st5_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st5_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st5_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st5_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st5_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st5_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st6_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st4_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st4_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st4_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st4_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st4_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st4_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st4_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st4_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st4_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st4_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st4_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st4_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st4_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st4_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st6_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st3_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st3_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st3_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st3_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st3_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st3_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st3_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st3_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st3_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st3_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st3_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st3_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st3_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st3_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st6_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st2_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st2_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st2_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st2_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st2_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st2_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st2_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st2_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st2_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st2_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st2_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st2_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st2_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st2_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st6_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st1_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st1_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st1_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st1_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st1_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st1_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st1_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st1_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st1_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st1_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st1_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st1_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st6_st1_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s6_3x3.st6_st1_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st9_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st9_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st9_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st9_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st9_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st9_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st9_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st9_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st9_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st9_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st9_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st9_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st9_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st9_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st7_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st8_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st8_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st8_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st8_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st8_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st8_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st8_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st8_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st8_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st8_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st8_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st8_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st8_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st8_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st7_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st6_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st6_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st6_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st6_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st6_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st6_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st6_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st6_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st6_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st6_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st6_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st6_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st6_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st6_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st7_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st5_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st5_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st5_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st5_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st5_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st5_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st5_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st5_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st5_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st5_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st5_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st5_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st5_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st5_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st7_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st4_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st4_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st4_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st4_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st4_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st4_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st4_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st4_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st4_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st4_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st4_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st4_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st4_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st4_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st7_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st3_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st3_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st3_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st3_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st3_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st3_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st3_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st3_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st3_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st3_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st3_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st3_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st3_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st3_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st7_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st2_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st2_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st2_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st2_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st2_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st2_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st2_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st2_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st2_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st2_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st2_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st2_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st2_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st2_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st7_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st1_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st1_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st1_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st1_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st1_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st1_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st1_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st1_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st1_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st1_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st1_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st1_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st7_st1_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s7_3x3.st7_st1_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st9_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st9_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st9_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st9_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st9_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st9_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st9_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st9_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st9_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st9_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st9_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st9_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st9_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st9_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st8_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st7_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st7_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st7_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st7_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st7_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st7_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st7_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st7_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st7_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st7_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st7_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st7_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st7_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st7_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st8_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st6_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st6_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st6_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st6_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st6_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st6_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st6_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st6_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st6_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st6_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st6_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st6_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st6_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st6_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st8_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st5_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st5_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st5_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st5_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st5_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st5_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st5_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st5_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st5_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st5_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st5_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st5_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st5_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st5_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st8_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st4_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st4_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st4_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st4_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st4_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st4_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st4_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st4_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st4_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st4_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st4_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st4_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st4_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st4_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st8_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st3_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st3_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st3_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st3_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st3_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st3_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st3_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st3_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st3_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st3_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st3_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st3_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st3_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st3_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st8_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st2_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st2_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st2_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st2_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st2_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st2_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st2_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st2_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st2_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st2_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st2_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st2_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st2_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st2_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st8_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st1_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st1_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st1_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st1_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st1_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st1_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st1_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st1_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st1_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st1_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st1_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st1_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st8_st1_st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s8_3x3.st8_st1_st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st9":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st8_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st8_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st8_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st8_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st8_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st8_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st8_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st8_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st8_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st8_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st8_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st8_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st8_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st8_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st9_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st7_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st7_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st7_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st7_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st7_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st7_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st7_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st7_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st7_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st7_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st7_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st7_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st7_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st7_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st9_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st6_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st6_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st6_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st6_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st6_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st6_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st6_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st6_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st6_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st6_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st6_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st6_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st6_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st6_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st9_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st5_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st5_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st5_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st5_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st5_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st5_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st5_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st5_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st5_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st5_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st5_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st5_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st5_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st5_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st9_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st4_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st4_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st4_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st4_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st4_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st4_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st4_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st4_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st4_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st4_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st4_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st4_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st4_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st4_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st9_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st3_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st3_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st3_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st3_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st3_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st3_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st3_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st3_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st3_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st3_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st3_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st3_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st3_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st3_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st9_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st2_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st2_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st2_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st2_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st2_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st2_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st2_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st2_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st2_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st2_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st2_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st2_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st2_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st2_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "st9_st1":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st1(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st1_st2":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st1_st2(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st1_st3":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st1_st3(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st1_st4":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st1_st4(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st1_st5":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st1_st5(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st1_st6":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st1_st6(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st1_st7":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st1_st7(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "st9_st1_st8":
        strike = lists.no_balance_3x3(user_id)
        balance = db.get_balance(user_id)
        if balance >= strike:
            text, markup = s9_3x3.st9_st1_st8(user_id)
        else:
            text, markup = lists.no_bal(user_id, strike)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "game_free":
        free_game = db.get_free_game(user_id)
        if free_game > 0:
            save = db.new_save(user_id, msg)
        else:
            # save = "reserve"
            save = db.new_save(user_id, "reserve")
        string_nine = db.new_string_nine(user_id)
        s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
        text, markup = free_3x3.game(user_id)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    elif msg == "f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f9_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f9_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f9_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f9_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f9_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f9_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f9_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f9_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f9_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f9_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f9_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f9_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f9_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f9_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f1_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f8_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f8_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f8_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f8_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f8_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f8_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f8_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f8_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f8_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f8_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f8_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f8_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f8_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f8_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f1_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f7_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f7_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f7_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f7_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f7_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f7_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f7_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f7_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f7_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f7_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f7_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f7_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f7_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f7_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f1_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f6_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f6_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f6_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f6_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f6_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f6_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f6_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f6_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f6_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f6_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f6_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f6_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f6_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f6_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f1_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f5_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f5_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f5_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f5_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f5_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f5_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f5_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f5_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f5_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f5_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f5_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f5_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f5_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f5_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f1_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f4_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f4_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f4_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f4_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f4_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f4_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f4_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f4_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f4_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f4_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f4_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f4_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f4_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f4_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f1_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f3_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f3_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f3_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f3_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f3_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f3_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f3_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f3_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f3_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f3_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f3_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f3_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f3_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f3_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f1_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f2_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f2_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f2_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f2_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f2_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f2_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f2_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f2_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f2_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f2_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f2_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f2_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f1_f2_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f1_3x3.f1_f2_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ----------------------------------------------------------------------------------------------------------------

    elif msg == "f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f9_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f9_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f9_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f9_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f9_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f9_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f9_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f9_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f9_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f9_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f9_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f9_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f9_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f9_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f2_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f8_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f8_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f8_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f8_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f8_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f8_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f8_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f8_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f8_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f8_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f8_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f8_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f8_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f8_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f2_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f7_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f7_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f7_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f7_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f7_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f7_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f7_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f7_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f7_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f7_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f7_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f7_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f7_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f7_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f2_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f6_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f6_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f6_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f6_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f6_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f6_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f6_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f6_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f6_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f6_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f6_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f6_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f6_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f6_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f2_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f5_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f5_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f5_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f5_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f5_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f5_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f5_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f5_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f5_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f5_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f5_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f5_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f5_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f5_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f2_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f4_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f4_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f4_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f4_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f4_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f4_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f4_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f4_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f4_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f4_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f4_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f4_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f4_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f4_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f2_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f3_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f3_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f3_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f3_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f3_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f3_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f3_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f3_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f3_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f3_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f3_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f3_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f3_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f3_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f2_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f1_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f1_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f1_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f1_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f1_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f1_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f1_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f1_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f1_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f1_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f1_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f1_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f2_f1_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f2_3x3.f2_f1_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f9_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f9_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f9_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f9_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f9_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f9_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f9_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f9_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f9_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f9_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f9_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f9_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f9_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f9_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f3_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f8_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f8_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f8_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f8_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f8_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f8_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f8_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f8_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f8_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f8_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f8_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f8_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f8_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f8_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f3_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f7_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f7_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f7_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f7_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f7_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f7_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f7_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f7_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f7_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f7_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f7_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f7_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f7_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f7_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f3_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f6_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f6_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f6_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f6_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f6_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f6_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f6_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f6_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f6_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f6_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f6_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f6_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f6_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f6_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f3_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f5_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f5_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f5_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f5_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f5_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f5_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f5_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f5_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f5_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f5_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f5_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f5_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f5_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f5_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f3_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f4_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f4_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f4_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f4_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f4_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f4_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f4_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f4_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f4_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f4_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f4_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f4_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f4_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f4_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f3_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f2_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f2_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f2_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f2_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f2_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f2_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f2_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f2_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f2_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f2_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f2_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f2_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f2_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f2_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f3_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f1_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f1_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f1_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f1_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f1_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f1_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f1_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f1_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f1_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f1_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f1_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f1_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f3_f1_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f3_3x3.f3_f1_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f9_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f9_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f9_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f9_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f9_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f9_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f9_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f9_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f9_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f9_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f9_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f9_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f9_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f9_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f4_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f8_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f8_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f8_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f8_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f8_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f8_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f8_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f8_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f8_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f8_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f8_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f8_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f8_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f8_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f4_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f7_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f7_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f7_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f7_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f7_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f7_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f7_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f7_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f7_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f7_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f7_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f7_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f7_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f7_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f4_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f6_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f6_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f6_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f6_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f6_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f6_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f6_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f6_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f6_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f6_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f6_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f6_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f6_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f6_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f4_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f5_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f5_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f5_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f5_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f5_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f5_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f5_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f5_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f5_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f5_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f5_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f5_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f5_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f5_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f4_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f3_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f3_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f3_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f3_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f3_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f3_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f3_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f3_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f3_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f3_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f3_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f3_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f3_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f3_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f4_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f2_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f2_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f2_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f2_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f2_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f2_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f2_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f2_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f2_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f2_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f2_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f2_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f2_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f2_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f4_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f1_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f1_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f1_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f1_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f1_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f1_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f1_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f1_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f1_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f1_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f1_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f1_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f4_f1_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f4_3x3.f4_f1_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f9_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f9_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f9_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f9_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f9_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f9_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f9_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f9_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f9_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f9_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f9_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f9_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f9_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f9_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f5_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f8_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f8_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f8_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f8_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f8_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f8_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f8_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f8_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f8_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f8_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f8_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f8_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f8_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f8_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f5_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f7_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f7_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f7_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f7_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f7_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f7_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f7_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f7_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f7_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f7_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f7_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f7_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f7_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f7_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f5_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f6_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f6_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f6_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f6_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f6_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f6_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f6_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f6_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f6_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f6_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f6_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f6_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f6_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f6_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f5_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f4_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f4_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f4_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f4_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f4_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f4_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f4_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f4_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f4_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f4_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f4_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f4_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f4_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f4_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f5_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f3_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f3_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f3_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f3_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f3_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f3_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f3_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f3_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f3_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f3_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f3_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f3_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f3_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f3_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f5_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f2_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f2_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f2_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f2_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f2_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f2_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f2_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f2_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f2_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f2_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f2_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f2_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f2_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f2_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f5_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f1_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f1_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f1_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f1_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f1_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f1_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f1_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f1_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f1_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f1_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f1_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f1_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f5_f1_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f5_3x3.f5_f1_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f9_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f9_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f9_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f9_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f9_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f9_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f9_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f9_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f9_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f9_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f9_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f9_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f9_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f9_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f6_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f8_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f8_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f8_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f8_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f8_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f8_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f8_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f8_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f8_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f8_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f8_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f8_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f8_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f8_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f6_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f7_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f7_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f7_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f7_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f7_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f7_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f7_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f7_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f7_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f7_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f7_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f7_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f7_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f7_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f6_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f5_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f5_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f5_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f5_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f5_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f5_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f5_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f5_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f5_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f5_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f5_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f5_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f5_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f5_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f6_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f4_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f4_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f4_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f4_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f4_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f4_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f4_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f4_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f4_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f4_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f4_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f4_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f4_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f4_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f6_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f3_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f3_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f3_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f3_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f3_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f3_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f3_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f3_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f3_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f3_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f3_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f3_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f3_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f3_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f6_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f2_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f2_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f2_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f2_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f2_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f2_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f2_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f2_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f2_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f2_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f2_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f2_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f2_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f2_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f6_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f1_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f1_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f1_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f1_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f1_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f1_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f1_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f1_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f1_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f1_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f1_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f1_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f6_f1_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f6_3x3.f6_f1_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f9_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f9_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f9_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f9_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f9_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f9_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f9_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f9_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f9_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f9_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f9_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f9_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f9_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f9_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f7_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f8_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f8_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f8_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f8_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f8_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f8_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f8_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f8_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f8_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f8_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f8_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f8_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f8_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f8_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f7_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f6_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f6_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f6_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f6_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f6_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f6_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f6_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f6_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f6_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f6_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f6_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f6_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f6_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f6_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f7_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f5_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f5_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f5_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f5_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f5_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f5_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f5_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f5_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f5_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f5_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f5_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f5_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f5_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f5_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f7_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f4_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f4_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f4_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f4_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f4_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f4_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f4_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f4_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f4_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f4_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f4_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f4_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f4_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f4_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f7_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f3_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f3_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f3_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f3_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f3_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f3_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f3_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f3_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f3_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f3_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f3_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f3_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f3_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f3_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f7_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f2_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f2_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f2_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f2_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f2_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f2_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f2_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f2_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f2_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f2_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f2_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f2_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f2_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f2_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f7_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f1_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f1_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f1_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f1_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f1_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f1_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f1_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f1_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f1_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f1_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f1_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f1_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f7_f1_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f7_3x3.f7_f1_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f9_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f9_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f9_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f9_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f9_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f9_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f9_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f9_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f9_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f9_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f9_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f9_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f9_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f9_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f8_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f7_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f7_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f7_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f7_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f7_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f7_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f7_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f7_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f7_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f7_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f7_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f7_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f7_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f7_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f8_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f6_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f6_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f6_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f6_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f6_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f6_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f6_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f6_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f6_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f6_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f6_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f6_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f6_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f6_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f8_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f5_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f5_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f5_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f5_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f5_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f5_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f5_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f5_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f5_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f5_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f5_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f5_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f5_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f5_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f8_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f4_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f4_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f4_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f4_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f4_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f4_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f4_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f4_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f4_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f4_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f4_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f4_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f4_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f4_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f8_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f3_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f3_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f3_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f3_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f3_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f3_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f3_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f3_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f3_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f3_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f3_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f3_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f3_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f3_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f8_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f2_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f2_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f2_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f2_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f2_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f2_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f2_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f2_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f2_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f2_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f2_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f2_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f2_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f2_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f8_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f1_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f1_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f1_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f1_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f1_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f1_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f1_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f1_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f1_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f1_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f1_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f1_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f8_f1_f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f8_3x3.f8_f1_f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f9":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f8_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f8_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f8_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f8_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f8_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f8_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f8_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f8_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f8_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f8_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f8_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f8_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f8_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f8_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f9_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f7_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f7_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f7_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f7_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f7_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f7_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f7_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f7_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f7_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f7_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f7_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f7_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f7_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f7_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f9_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f6_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f6_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f6_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f6_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f6_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f6_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f6_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f6_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f6_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f6_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f6_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f6_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f6_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f6_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f9_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f5_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f5_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f5_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f5_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f5_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f5_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f5_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f5_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f5_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f5_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f5_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f5_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f5_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f5_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f9_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f4_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f4_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f4_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f4_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f4_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f4_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f4_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f4_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f4_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f4_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f4_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f4_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f4_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f4_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f9_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f3_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f3_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f3_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f3_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f3_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f3_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f3_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f3_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f3_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f3_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f3_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f3_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f3_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f3_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f9_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f2_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f2_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f2_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f2_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f2_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f2_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f2_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f2_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f2_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f2_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f2_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f2_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f2_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f2_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')

    # ---------------------------------------------------------------------------------------------------------------

    elif msg == "f9_f1":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f1(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f1_f2":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f1_f2(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f1_f3":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f1_f3(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f1_f4":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f1_f4(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f1_f5":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f1_f5(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f1_f6":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f1_f6(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f1_f7":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f1_f7(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')
    elif msg == "f9_f1_f8":
        bal, strike = lists.no_balance_free(user_id)
        if bal >= strike:
            text, markup = f9_3x3.f9_f1_f8(user_id)
        else:
            text, markup = lists.no_res(user_id)

        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup,
                                        parse_mode='html')
        except:
            await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')


# pre checkout  (must be answered in 10 seconds)
@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    if currency == "KRW" or currency == "CLP" or currency == "JPY":
        suc = message.successful_payment.total_amount
    else:
        suc = round(message.successful_payment.total_amount / 100, 2)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        if suc == round(rate * fir1 / 10, 2):
            ba = fir1 * 10
        elif suc == round(rate * sec1 / 10, 2):
            ba = sec1 * 10
        elif suc == round(rate * thi1 / 10, 2):
            ba = thi1 * 10
        elif suc == round(rate * fou1 / 10, 2):
            ba = fou1 * 10
        elif suc == round(rate * fif1 / 10, 2):
            ba = fif1 * 10
        elif suc == round(rate * six1 / 10, 2):
            ba = six1 * 10
        elif suc == round(rate * sev1 / 10, 2):
            ba = sev1 * 10
        else:
            ba = 0
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        if suc == round(rate * fir2 / 10, 2):
            ba = fir2 * 10
        elif suc == round(rate * sec2 / 10, 2):
            ba = sec2 * 10
        elif suc == round(rate * thi2 / 10, 2):
            ba = thi2 * 10
        elif suc == round(rate * fou2 / 10, 2):
            ba = fou2 * 10
        elif suc == round(rate * fif2 / 10, 2):
            ba = fif2 * 10
        elif suc == round(rate * six2 / 10, 2):
            ba = six2 * 10
        elif suc == round(rate * sev2 / 10, 2):
            ba = sev2 * 10
        else:
            ba = 0
    elif currency == "EGP" or currency == "INR":
        if suc == round(rate * fir3 / 10, 2):
            ba = fir3 * 10
        elif suc == round(rate * sec3 / 10, 2):
            ba = sec3 * 10
        elif suc == round(rate * thi3 / 10, 2):
            ba = thi3 * 10
        elif suc == round(rate * fou3 / 10, 2):
            ba = fou3 * 10
        elif suc == round(rate * fif3 / 10, 2):
            ba = fif3 * 10
        elif suc == round(rate * six3 / 10, 2):
            ba = six3 * 10
        elif suc == round(rate * sev3 / 10, 2):
            ba = sev3 * 10
        else:
            ba = 0
    elif currency == "KRW" or currency == "CLP" or currency == "JPY":
        if int(suc) == int(rate * fir4 / 10):
            ba = fir4 * 10
        elif int(suc) == int(rate * sec4 / 10):
            ba = sec4 * 10
        elif int(suc) == int(rate * thi4 / 10):
            ba = thi4 * 10
        elif int(suc) == int(rate * fou4 / 10):
            ba = fou4 * 10
        elif int(suc) == int(rate * fif4 / 10):
            ba = fif4 * 10
        elif int(suc) == int(rate * six4 / 10):
            ba = six4 * 10
        elif int(suc) == int(rate * sev4 / 10):
            ba = sev4 * 10
        else:
            ba = 0
    else:
        if suc == round(rate * fir4 / 10, 2):
            ba = fir4 * 10
        elif suc == round(rate * sec4 / 10, 2):
            ba = sec4 * 10
        elif suc == round(rate * thi4 / 10, 2):
            ba = thi4 * 10
        elif suc == round(rate * fou4 / 10, 2):
            ba = fou4 * 10
        elif suc == round(rate * fif4 / 10, 2):
            ba = fif4 * 10
        elif suc == round(rate * six4 / 10, 2):
            ba = six4 * 10
        elif suc == round(rate * sev4 / 10, 2):
            ba = sev4 * 10
        else:
            ba = 0
    balance = db.new_balance_plus(user_id, ba)
    sum_deposit = db.new_sum_deposit(user_id, ba)
    count_deposit = db.new_count_deposit(user_id)
    text, markup = lists.wallet(user_id)
    await bot.send_message(chat_id, text, reply_markup=markup, parse_mode='html')


# run long-polling
if __name__ == "__main__":
    # executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
    executor.start_polling(dp, skip_updates=True)
