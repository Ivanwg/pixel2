from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import all_lang
import db
import options
import risk_games
from options import prize, bomb, skip, stop, close

from options import f_base_four_loss, f_bronze_four_loss, f_silver_four_loss, f_gold_four_loss, f_vip_four_loss
from options import s_base_four_loss, s_bronze_four_loss, s_silver_four_loss, s_gold_four_loss, s_vip_four_loss
from options import t_base_four_loss, t_bronze_four_loss, t_silver_four_loss, t_gold_four_loss, t_vip_four_loss
from options import fo_base_four_loss, fo_bronze_four_loss, fo_silver_four_loss, fo_gold_four_loss, fo_vip_four_loss


def game_risk_four(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    save = db.get_save(user_id)
    if save == "game_risk_base_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_four_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_four_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_four_loss)
        else:
            count = int(balance // fo_base_four_loss)
    elif save == "game_risk_bronze_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_four_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_four_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_four_loss)
        else:
            count = int(balance // fo_bronze_four_loss)
    elif save == "game_risk_silver_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_four_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_four_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_four_loss)
        else:
            count = int(balance // fo_silver_four_loss)
    elif save == "game_risk_gold_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_four_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_four_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_four_loss)
        else:
            count = int(balance // fo_gold_four_loss)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_vip_four_loss)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_vip_four_loss)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_vip_four_loss)
        else:
            count = int(balance // fo_vip_four_loss)
    if count < 0:
        count = 0
    text = options.game_start(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    r1 = InlineKeyboardButton(text=close, callback_data='rf1')
    r2 = InlineKeyboardButton(text=close, callback_data='rf2')
    r3 = InlineKeyboardButton(text=close, callback_data='rf3')
    r4 = InlineKeyboardButton(text=close, callback_data='rf4')
    r5 = InlineKeyboardButton(text=close, callback_data='rf5')
    r6 = InlineKeyboardButton(text=close, callback_data='rf6')
    r7 = InlineKeyboardButton(text=close, callback_data='rf7')
    r8 = InlineKeyboardButton(text=close, callback_data='rf8')
    r9 = InlineKeyboardButton(text=close, callback_data='rf9')
    # new_game = InlineKeyboardButton(text='Новая игра', callback_data='done')
    if save == "game_risk_base_four":
        cn = 'game_risk_base_four'
        cb = 'risk_base_four'
    elif save == "game_risk_bronze_four":
        cn = 'game_risk_bronze_four'
        cb = 'risk_bronze_four'
    elif save == "game_risk_silver_four":
        cn = 'game_risk_silver_four'
        cb = 'risk_silver_four'
    elif save == "game_risk_gold_four":
        cn = 'game_risk_gold_four'
        cb = 'risk_gold_four'
    else:
        cn = 'game_risk_vip_four'
        cb = 'risk_vip_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(r1, r2, r3, r4, r5, r6, r7, r8, r9)
    markup.add(back)
    return text, markup


def rf1(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if god_mode:
        if q1 == 0:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3_god(user_id)
        elif q1 == 1:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    else:
        if q1 == 0:
            text = options.risk_3x3_win(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    right = db.new_game(user_id)
    if save == "game_risk_base_four":
        cn = 'game_risk_base_four'
        cb = 'risk_base_four'
    elif save == "game_risk_bronze_four":
        cn = 'game_risk_bronze_four'
        cb = 'risk_bronze_four'
    elif save == "game_risk_silver_four":
        cn = 'game_risk_silver_four'
        cb = 'risk_silver_four'
    elif save == "game_risk_gold_four":
        cn = 'game_risk_gold_four'
        cb = 'risk_gold_four'
    else:
        cn = 'game_risk_vip_four'
        cb = 'risk_vip_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)
    return text, markup


def rf2(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if god_mode:
        if q2 == 0:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3_god(user_id)
        elif q2 == 1:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    else:
        if q2 == 0:
            text = options.risk_3x3_win(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    right = db.new_game(user_id)
    if save == "game_risk_base_four":
        cn = 'game_risk_base_four'
        cb = 'risk_base_four'
    elif save == "game_risk_bronze_four":
        cn = 'game_risk_bronze_four'
        cb = 'risk_bronze_four'
    elif save == "game_risk_silver_four":
        cn = 'game_risk_silver_four'
        cb = 'risk_silver_four'
    elif save == "game_risk_gold_four":
        cn = 'game_risk_gold_four'
        cb = 'risk_gold_four'
    else:
        cn = 'game_risk_vip_four'
        cb = 'risk_vip_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)
    return text, markup


def rf3(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if god_mode:
        if q3 == 0:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3_god(user_id)
        elif q3 == 1:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    else:
        if q3 == 0:
            text = options.risk_3x3_win(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    right = db.new_game(user_id)
    if save == "game_risk_base_four":
        cn = 'game_risk_base_four'
        cb = 'risk_base_four'
    elif save == "game_risk_bronze_four":
        cn = 'game_risk_bronze_four'
        cb = 'risk_bronze_four'
    elif save == "game_risk_silver_four":
        cn = 'game_risk_silver_four'
        cb = 'risk_silver_four'
    elif save == "game_risk_gold_four":
        cn = 'game_risk_gold_four'
        cb = 'risk_gold_four'
    else:
        cn = 'game_risk_vip_four'
        cb = 'risk_vip_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)
    return text, markup


def rf4(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if god_mode:
        if q4 == 0:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3_god(user_id)
        elif q4 == 1:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    else:
        if q4 == 0:
            text = options.risk_3x3_win(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    right = db.new_game(user_id)
    if save == "game_risk_base_four":
        cn = 'game_risk_base_four'
        cb = 'risk_base_four'
    elif save == "game_risk_bronze_four":
        cn = 'game_risk_bronze_four'
        cb = 'risk_bronze_four'
    elif save == "game_risk_silver_four":
        cn = 'game_risk_silver_four'
        cb = 'risk_silver_four'
    elif save == "game_risk_gold_four":
        cn = 'game_risk_gold_four'
        cb = 'risk_gold_four'
    else:
        cn = 'game_risk_vip_four'
        cb = 'risk_vip_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)
    return text, markup


def rf5(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if god_mode:
        if q5 == 0:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3_god(user_id)
        elif q5 == 1:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    else:
        if q5 == 0:
            text = options.risk_3x3_win(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    right = db.new_game(user_id)
    if save == "game_risk_base_four":
        cn = 'game_risk_base_four'
        cb = 'risk_base_four'
    elif save == "game_risk_bronze_four":
        cn = 'game_risk_bronze_four'
        cb = 'risk_bronze_four'
    elif save == "game_risk_silver_four":
        cn = 'game_risk_silver_four'
        cb = 'risk_silver_four'
    elif save == "game_risk_gold_four":
        cn = 'game_risk_gold_four'
        cb = 'risk_gold_four'
    else:
        cn = 'game_risk_vip_four'
        cb = 'risk_vip_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)
    return text, markup


def rf6(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if god_mode:
        if q6 == 0:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3_god(user_id)
        elif q6 == 1:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    else:
        if q6 == 0:
            text = options.risk_3x3_win(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    right = db.new_game(user_id)
    if save == "game_risk_base_four":
        cn = 'game_risk_base_four'
        cb = 'risk_base_four'
    elif save == "game_risk_bronze_four":
        cn = 'game_risk_bronze_four'
        cb = 'risk_bronze_four'
    elif save == "game_risk_silver_four":
        cn = 'game_risk_silver_four'
        cb = 'risk_silver_four'
    elif save == "game_risk_gold_four":
        cn = 'game_risk_gold_four'
        cb = 'risk_gold_four'
    else:
        cn = 'game_risk_vip_four'
        cb = 'risk_vip_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)
    return text, markup


def rf7(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if god_mode:
        if q7 == 0:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3_god(user_id)
        elif q7 == 1:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    else:
        if q7 == 0:
            text = options.risk_3x3_win(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    right = db.new_game(user_id)
    if save == "game_risk_base_four":
        cn = 'game_risk_base_four'
        cb = 'risk_base_four'
    elif save == "game_risk_bronze_four":
        cn = 'game_risk_bronze_four'
        cb = 'risk_bronze_four'
    elif save == "game_risk_silver_four":
        cn = 'game_risk_silver_four'
        cb = 'risk_silver_four'
    elif save == "game_risk_gold_four":
        cn = 'game_risk_gold_four'
        cb = 'risk_gold_four'
    else:
        cn = 'game_risk_vip_four'
        cb = 'risk_vip_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)
    return text, markup


def rf8(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if god_mode:
        if q8 == 0:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3_god(user_id)
        elif q8 == 1:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    else:
        if q8 == 0:
            text = options.risk_3x3_win(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    right = db.new_game(user_id)
    if save == "game_risk_base_four":
        cn = 'game_risk_base_four'
        cb = 'risk_base_four'
    elif save == "game_risk_bronze_four":
        cn = 'game_risk_bronze_four'
        cb = 'risk_bronze_four'
    elif save == "game_risk_silver_four":
        cn = 'game_risk_silver_four'
        cb = 'risk_silver_four'
    elif save == "game_risk_gold_four":
        cn = 'game_risk_gold_four'
        cb = 'risk_gold_four'
    else:
        cn = 'game_risk_vip_four'
        cb = 'risk_vip_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)
    return text, markup


def rf9(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    q1, q2, q3, q4, q5, q6, q7, q8, q9 = db.index_strings_four(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if god_mode:
        if q9 == 0:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3_god(user_id)
        elif q9 == 1:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    else:
        if q9 == 0:
            text = options.risk_3x3_win(user_id)
        else:
            text = options.risk_3x3_loss(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = risk_games.finish_3x3(user_id)
    right = db.new_game(user_id)
    if save == "game_risk_base_four":
        cn = 'game_risk_base_four'
        cb = 'risk_base_four'
    elif save == "game_risk_bronze_four":
        cn = 'game_risk_bronze_four'
        cb = 'risk_bronze_four'
    elif save == "game_risk_silver_four":
        cn = 'game_risk_silver_four'
        cb = 'risk_silver_four'
    elif save == "game_risk_gold_four":
        cn = 'game_risk_gold_four'
        cb = 'risk_gold_four'
    else:
        cn = 'game_risk_vip_four'
        cb = 'risk_vip_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)
    return text, markup
