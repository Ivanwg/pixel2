from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import all_lang
import db
import options
from options import f_base_2x3_step, f_bronze_2x3_step, f_silver_2x3_step, f_gold_2x3_step, f_vip_2x3_step
from options import s_base_2x3_step, s_bronze_2x3_step, s_silver_2x3_step, s_gold_2x3_step, s_vip_2x3_step
from options import t_base_2x3_step, t_bronze_2x3_step, t_silver_2x3_step, t_gold_2x3_step, t_vip_2x3_step
from options import fo_base_2x3_step, fo_bronze_2x3_step, fo_silver_2x3_step, fo_gold_2x3_step, fo_vip_2x3_step
from options import prize, bomb, skip, stop, close


def finish(user_id):
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    if i1 == 0:
        s1 = InlineKeyboardButton(text=skip, callback_data='done')
    elif i1 == 1:
        s1 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        s1 = InlineKeyboardButton(text=prize, callback_data='done')
    if i2 == 0:
        s2 = InlineKeyboardButton(text=skip, callback_data='done')
    elif i2 == 1:
        s2 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        s2 = InlineKeyboardButton(text=prize, callback_data='done')
    if i3 == 0:
        s3 = InlineKeyboardButton(text=skip, callback_data='done')
    elif i3 == 1:
        s3 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        s3 = InlineKeyboardButton(text=prize, callback_data='done')
    if i4 == 0:
        s4 = InlineKeyboardButton(text=skip, callback_data='done')
    elif i4 == 1:
        s4 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        s4 = InlineKeyboardButton(text=prize, callback_data='done')
    if i5 == 0:
        s5 = InlineKeyboardButton(text=skip, callback_data='done')
    elif i5 == 1:
        s5 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        s5 = InlineKeyboardButton(text=prize, callback_data='done')
    if i6 == 0:
        s6 = InlineKeyboardButton(text=skip, callback_data='done')
    elif i6 == 1:
        s6 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        s6 = InlineKeyboardButton(text=prize, callback_data='done')
    return s1, s2, s3, s4, s5, s6


def finish_god(user_id):
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    if i1 == 0:
        s1 = InlineKeyboardButton(text=skip, callback_data='done')
    elif i1 == 1:
        s1 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        s1 = InlineKeyboardButton(text=bomb, callback_data='done')
    if i2 == 0:
        s2 = InlineKeyboardButton(text=skip, callback_data='done')
    elif i2 == 1:
        s2 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        s2 = InlineKeyboardButton(text=bomb, callback_data='done')
    if i3 == 0:
        s3 = InlineKeyboardButton(text=skip, callback_data='done')
    elif i3 == 1:
        s3 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        s3 = InlineKeyboardButton(text=bomb, callback_data='done')
    if i4 == 0:
        s4 = InlineKeyboardButton(text=skip, callback_data='done')
    elif i4 == 1:
        s4 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        s4 = InlineKeyboardButton(text=bomb, callback_data='done')
    if i5 == 0:
        s5 = InlineKeyboardButton(text=skip, callback_data='done')
    elif i5 == 1:
        s5 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        s5 = InlineKeyboardButton(text=bomb, callback_data='done')
    if i6 == 0:
        s6 = InlineKeyboardButton(text=skip, callback_data='done')
    elif i6 == 1:
        s6 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        s6 = InlineKeyboardButton(text=bomb, callback_data='done')
    return s1, s2, s3, s4, s5, s6


def game(user_id):
    balance = db.get_balance(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_base_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_2x3_step)
        else:
            count = int(balance // fo_base_2x3_step)
    elif save == "game_bronze_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_2x3_step)
        else:
            count = int(balance // fo_bronze_2x3_step)
    elif save == "game_silver_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_2x3_step)
        else:
            count = int(balance // fo_silver_2x3_step)
    elif save == "game_gold_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_2x3_step)
        else:
            count = int(balance // fo_gold_2x3_step)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_vip_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_vip_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_vip_2x3_step)
        else:
            count = int(balance // fo_vip_2x3_step)
    if count < 0:
        count = 0
    text = options.game_start(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    s1 = InlineKeyboardButton(text=close, callback_data='ss1')
    s2 = InlineKeyboardButton(text=close, callback_data='ss2')
    s3 = InlineKeyboardButton(text=close, callback_data='ss3')
    s4 = InlineKeyboardButton(text=close, callback_data='ss4')
    s5 = InlineKeyboardButton(text=close, callback_data='ss5')
    s6 = InlineKeyboardButton(text=close, callback_data='ss6')
    # new_game = InlineKeyboardButton(text='Новая игра', callback_data='done')
    if save == "game_base_six":
        cn = 'game_base_six'
        cb = 'norm_base_six'
    elif save == "game_bronze_six":
        cn = 'game_bronze_six'
        cb = 'norm_bronze_six'
    elif save == "game_silver_six":
        cn = 'game_silver_six'
        cb = 'norm_silver_six'
    elif save == "game_gold_six":
        cn = 'game_gold_six'
        cb = 'norm_gold_six'
    elif save == "game_vip_six":
        cn = 'game_vip_six'
        cb = 'norm_vip_six'
    else:
        cn = 'game_free_six'
        cb = 'free_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, s5, s6)
    markup.add(back)
    return text, markup
