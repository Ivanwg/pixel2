from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import all_lang
import db
import options

import risk_games
from options import prize, bomb, skip, stop, close

from options import f_base_six_loss, f_bronze_six_loss, f_silver_six_loss, f_gold_six_loss, f_vip_six_loss
from options import s_base_six_loss, s_bronze_six_loss, s_silver_six_loss, s_gold_six_loss, s_vip_six_loss
from options import t_base_six_loss, t_bronze_six_loss, t_silver_six_loss, t_gold_six_loss, t_vip_six_loss
from options import fo_base_six_loss, fo_bronze_six_loss, fo_silver_six_loss, fo_gold_six_loss, fo_vip_six_loss


def game_risk_six(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    save = db.get_save(user_id)
    if save == "game_risk_base_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_six_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_six_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_six_loss)
        else:
            count = int(balance // fo_base_six_loss)
    elif save == "game_risk_bronze_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_six_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_six_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_six_loss)
        else:
            count = int(balance // fo_bronze_six_loss)
    elif save == "game_risk_silver_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_six_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_six_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_six_loss)
        else:
            count = int(balance // fo_silver_six_loss)
    elif save == "game_risk_gold_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_six_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_six_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_six_loss)
        else:
            count = int(balance // fo_gold_six_loss)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_vip_six_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_vip_six_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_vip_six_loss)
        else:
            count = int(balance // fo_vip_six_loss)
    if count < 0:
        count = 0
    text = options.game_start(user_id, count)
    markup = InlineKeyboardMarkup(row_width=4)
    r1 = InlineKeyboardButton(text=close, callback_data='rs1')
    r2 = InlineKeyboardButton(text=close, callback_data='rs2')
    r3 = InlineKeyboardButton(text=close, callback_data='rs3')
    r4 = InlineKeyboardButton(text=close, callback_data='rs4')
    r5 = InlineKeyboardButton(text=close, callback_data='rs5')
    r6 = InlineKeyboardButton(text=close, callback_data='rs6')
    r7 = InlineKeyboardButton(text=close, callback_data='rs7')
    r8 = InlineKeyboardButton(text=close, callback_data='rs8')
    r9 = InlineKeyboardButton(text=close, callback_data='rs9')
    r10 = InlineKeyboardButton(text=close, callback_data='rs10')
    r11 = InlineKeyboardButton(text=close, callback_data='rs11')
    r12 = InlineKeyboardButton(text=close, callback_data='rs12')
    r13 = InlineKeyboardButton(text=close, callback_data='rs13')
    r14 = InlineKeyboardButton(text=close, callback_data='rs14')
    r15 = InlineKeyboardButton(text=close, callback_data='rs15')
    r16 = InlineKeyboardButton(text=close, callback_data='rs16')
    # new_game = InlineKeyboardButton(text='Новая игра', callback_data='done')
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16)
    markup.add(back)
    return text, markup


def rs1(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w1 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w1 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w1 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs2(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w2 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w2 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w2 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs3(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w3 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w3 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w3 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs4(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w4 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w4 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w4 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs5(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w5 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w5 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w5 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs6(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w6 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w6 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w6 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs7(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w7 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w7 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w7 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs8(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w8 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w8 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w8 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs9(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w9 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w9 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w9 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs10(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w10 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w10 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w10 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs11(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w11 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w11 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w11 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs12(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w12 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w12 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w12 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs13(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w13 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w13 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w13 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs14(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w14 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w14 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w14 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs15(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w15 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w15 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w15 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup


def rs16(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16 = db.index_strings_six(user_id)
    markup = InlineKeyboardMarkup(row_width=4)
    if god_mode:
        if w16 == 0:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4_god(user_id)
        elif w16 == 1:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
    else:
        if w16 == 0:
            text = options.risk_4x4_win(user_id)
        else:
            text = options.risk_4x4_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 = risk_games.finish_4x4(user_id)
        right = db.new_game(user_id)
    if save == "game_risk_base_six":
        cn = 'game_risk_base_six'
        cb = 'risk_base_six'
    elif save == "game_risk_bronze_six":
        cn = 'game_risk_bronze_six'
        cb = 'risk_bronze_six'
    elif save == "game_risk_silver_six":
        cn = 'game_risk_silver_six'
        cb = 'risk_silver_six'
    elif save == "game_risk_gold_six":
        cn = 'game_risk_gold_six'
        cb = 'risk_gold_six'
    else:
        cn = 'game_risk_vip_six'
        cb = 'risk_vip_six'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, new_game)
    markup.add(back)
    return text, markup
