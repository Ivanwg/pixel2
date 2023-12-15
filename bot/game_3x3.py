from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import all_lang
import db
import options
from options import f_base_3x3_step, f_bronze_3x3_step, f_silver_3x3_step, f_gold_3x3_step, f_vip_3x3_step
from options import s_base_3x3_step, s_bronze_3x3_step, s_silver_3x3_step, s_gold_3x3_step, s_vip_3x3_step
from options import t_base_3x3_step, t_bronze_3x3_step, t_silver_3x3_step, t_gold_3x3_step, t_vip_3x3_step
from options import fo_base_3x3_step, fo_bronze_3x3_step, fo_silver_3x3_step, fo_gold_3x3_step, fo_vip_3x3_step
from options import prize, bomb, skip, stop, close


def finish(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    if s1 == 0:
        t1 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s1 == 1:
        t1 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t1 = InlineKeyboardButton(text=prize, callback_data='done')
    if s2 == 0:
        t2 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s2 == 1:
        t2 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t2 = InlineKeyboardButton(text=prize, callback_data='done')
    if s3 == 0:
        t3 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s3 == 1:
        t3 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t3 = InlineKeyboardButton(text=prize, callback_data='done')
    if s4 == 0:
        t4 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s4 == 1:
        t4 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t4 = InlineKeyboardButton(text=prize, callback_data='done')
    if s5 == 0:
        t5 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s5 == 1:
        t5 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t5 = InlineKeyboardButton(text=prize, callback_data='done')
    if s6 == 0:
        t6 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s6 == 1:
        t6 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t6 = InlineKeyboardButton(text=prize, callback_data='done')
    if s7 == 0:
        t7 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s7 == 1:
        t7 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t7 = InlineKeyboardButton(text=prize, callback_data='done')
    if s8 == 0:
        t8 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s8 == 1:
        t8 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t8 = InlineKeyboardButton(text=prize, callback_data='done')
    if s9 == 0:
        t9 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s9 == 1:
        t9 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t9 = InlineKeyboardButton(text=prize, callback_data='done')
    return t1, t2, t3, t4, t5, t6, t7, t8, t9


def finish_god(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    if s1 == 0:
        t1 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s1 == 1:
        t1 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t1 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s2 == 0:
        t2 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s2 == 1:
        t2 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t2 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s3 == 0:
        t3 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s3 == 1:
        t3 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t3 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s4 == 0:
        t4 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s4 == 1:
        t4 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t4 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s5 == 0:
        t5 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s5 == 1:
        t5 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t5 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s6 == 0:
        t6 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s6 == 1:
        t6 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t6 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s7 == 0:
        t7 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s7 == 1:
        t7 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t7 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s8 == 0:
        t8 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s8 == 1:
        t8 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t8 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s9 == 0:
        t9 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s9 == 1:
        t9 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t9 = InlineKeyboardButton(text=bomb, callback_data='done')
    return t1, t2, t3, t4, t5, t6, t7, t8, t9


def game(user_id):
    balance = db.get_balance(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_base_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_3x3_step)
        else:
            count = int(balance // fo_base_3x3_step)
    elif save == "game_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_3x3_step)
        else:
            count = int(balance // fo_bronze_3x3_step)
    elif save == "game_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_3x3_step)
        else:
            count = int(balance // fo_silver_3x3_step)
    elif save == "game_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_3x3_step)
        else:
            count = int(balance // fo_gold_3x3_step)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_vip_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_vip_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_vip_3x3_step)
        else:
            count = int(balance // fo_vip_3x3_step)
    if count < 0:
        count = 0
    text = options.game_start(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    t1 = InlineKeyboardButton(text=close, callback_data='st1')
    t2 = InlineKeyboardButton(text=close, callback_data='st2')
    t3 = InlineKeyboardButton(text=close, callback_data='st3')
    t4 = InlineKeyboardButton(text=close, callback_data='st4')
    t5 = InlineKeyboardButton(text=close, callback_data='st5')
    t6 = InlineKeyboardButton(text=close, callback_data='st6')
    t7 = InlineKeyboardButton(text=close, callback_data='st7')
    t8 = InlineKeyboardButton(text=close, callback_data='st8')
    t9 = InlineKeyboardButton(text=close, callback_data='st9')
    # new_game = InlineKeyboardButton(text='Новая игра', callback_data='done')
    if save == "game_base_nine":
        cn = 'game_base_nine'
        cb = 'norm_base_nine'
    elif save == "game_bronze_nine":
        cn = 'game_bronze_nine'
        cb = 'norm_bronze_nine'
    elif save == "game_silver_nine":
        cn = 'game_silver_nine'
        cb = 'norm_silver_nine'
    elif save == "game_gold_nine":
        cn = 'game_gold_nine'
        cb = 'norm_gold_nine'
    elif save == "game_vip_nine":
        cn = 'game_vip_nine'
        cb = 'norm_vip_nine'
    else:
        cn = 'game_free_nine'
        cb = 'free_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    markup.add(back)
    return text, markup
