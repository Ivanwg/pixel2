from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import all_lang
import db
import options
import risk_games
from options import prize, bomb, skip, stop, close

from options import f_base_nine_loss, f_bronze_nine_loss, f_silver_nine_loss, f_gold_nine_loss, f_vip_nine_loss
from options import s_base_nine_loss, s_bronze_nine_loss, s_silver_nine_loss, s_gold_nine_loss, s_vip_nine_loss
from options import t_base_nine_loss, t_bronze_nine_loss, t_silver_nine_loss, t_gold_nine_loss, t_vip_nine_loss
from options import fo_base_nine_loss, fo_bronze_nine_loss, fo_silver_nine_loss, fo_gold_nine_loss, fo_vip_nine_loss


def game_risk_nine(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    save = db.get_save(user_id)
    if save == "game_risk_base_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_nine_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_nine_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_nine_loss)
        else:
            count = int(balance // fo_base_nine_loss)
    elif save == "game_risk_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_nine_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_nine_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_nine_loss)
        else:
            count = int(balance // fo_bronze_nine_loss)
    elif save == "game_risk_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_nine_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_nine_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_nine_loss)
        else:
            count = int(balance // fo_silver_nine_loss)
    elif save == "game_risk_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_nine_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_nine_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_nine_loss)
        else:
            count = int(balance // fo_gold_nine_loss)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_vip_nine_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_vip_nine_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_vip_nine_loss)
        else:
            count = int(balance // fo_vip_nine_loss)
    if count < 0:
        count = 0
    text = options.game_start(user_id, count)
    markup = InlineKeyboardMarkup(row_width=5)
    r1 = InlineKeyboardButton(text=close, callback_data='rn1')
    r2 = InlineKeyboardButton(text=close, callback_data='rn2')
    r3 = InlineKeyboardButton(text=close, callback_data='rn3')
    r4 = InlineKeyboardButton(text=close, callback_data='rn4')
    r5 = InlineKeyboardButton(text=close, callback_data='rn5')
    r6 = InlineKeyboardButton(text=close, callback_data='rn6')
    r7 = InlineKeyboardButton(text=close, callback_data='rn7')
    r8 = InlineKeyboardButton(text=close, callback_data='rn8')
    r9 = InlineKeyboardButton(text=close, callback_data='rn9')
    r10 = InlineKeyboardButton(text=close, callback_data='rn10')
    r11 = InlineKeyboardButton(text=close, callback_data='rn11')
    r12 = InlineKeyboardButton(text=close, callback_data='rn12')
    r13 = InlineKeyboardButton(text=close, callback_data='rn13')
    r14 = InlineKeyboardButton(text=close, callback_data='rn14')
    r15 = InlineKeyboardButton(text=close, callback_data='rn15')
    r16 = InlineKeyboardButton(text=close, callback_data='rn16')
    r17 = InlineKeyboardButton(text=close, callback_data='rn17')
    r18 = InlineKeyboardButton(text=close, callback_data='rn18')
    r19 = InlineKeyboardButton(text=close, callback_data='rn19')
    r20 = InlineKeyboardButton(text=close, callback_data='rn20')
    r21 = InlineKeyboardButton(text=close, callback_data='rn21')
    r22 = InlineKeyboardButton(text=close, callback_data='rn22')
    r23 = InlineKeyboardButton(text=close, callback_data='rn23')
    r24 = InlineKeyboardButton(text=close, callback_data='rn24')
    r25 = InlineKeyboardButton(text=close, callback_data='rn25')
    # new_game = InlineKeyboardButton(text='Новая игра', callback_data='done')
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22,
               r23, r24, r25)
    markup.add(back)
    return text, markup


def rn1(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e1 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e1 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e1 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn2(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e2 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e2 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e2 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn3(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e3 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e3 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e3 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn4(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e4 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e4 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e4 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn5(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e5 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e5 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e5 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn6(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e6 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e6 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e6 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn7(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e7 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e7 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e7 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn8(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e8 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e8 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e8 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn9(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e9 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e9 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e9 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn10(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e10 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e10 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e10 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn11(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e11 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e11 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e11 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn12(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e12 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e12 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e12 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn13(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e13 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e13 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e13 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn14(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e14 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e14 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e14 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn15(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e15 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e15 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e15 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn16(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e16 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e16 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e16 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn17(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e17 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e17 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e17 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn18(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e18 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e18 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e18 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn19(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e19 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e19 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e19 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn20(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e20 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e20 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e20 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn21(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e21 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e21 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e21 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn22(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e22 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e22 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e22 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn23(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e23 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e23 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e23 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn24(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e24 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e24 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e24 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup


def rn25(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25 = db.index_strings_nine(user_id)
    markup = InlineKeyboardMarkup(row_width=5)
    if god_mode:
        if e25 == 0:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5_god(user_id)
        elif e25 == 1:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
    else:
        if e25 == 0:
            text = options.risk_5x5_win(user_id)
        else:
            text = options.risk_5x5_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 = risk_games.finish_5x5(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_nine":
        cn = 'game_risk_base_nine'
        cb = 'risk_base_nine'
    elif save == "game_risk_bronze_nine":
        cn = 'game_risk_bronze_nine'
        cb = 'risk_bronze_nine'
    elif save == "game_risk_silver_nine":
        cn = 'game_risk_silver_nine'
        cb = 'risk_silver_nine'
    elif save == "game_risk_gold_nine":
        cn = 'game_risk_gold_nine'
        cb = 'risk_gold_nine'
    else:
        cn = 'game_risk_vip_nine'
        cb = 'risk_vip_nine'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, new_game)
    markup.add(back)
    return text, markup
