from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import all_lang
import db
import options

from options import f_base_2x2_step, f_bronze_2x2_step, f_silver_2x2_step, f_gold_2x2_step, f_vip_2x2_step
from options import s_base_2x2_step, s_bronze_2x2_step, s_silver_2x2_step, s_gold_2x2_step, s_vip_2x2_step
from options import t_base_2x2_step, t_bronze_2x2_step, t_silver_2x2_step, t_gold_2x2_step, t_vip_2x2_step
from options import fo_base_2x2_step, fo_bronze_2x2_step, fo_silver_2x2_step, fo_gold_2x2_step, fo_vip_2x2_step
from options import prize, bomb, skip, stop, close


def finish(user_id):
    f1, f2, f3, f4 = db.index_string_four(user_id)
    if f1 == 0:
        s1 = InlineKeyboardButton(text=skip, callback_data='done')
    elif f1 == 1:
        s1 = InlineKeyboardButton(text=bomb, callback_data='done')
    elif f1 == 2:
        s1 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        s1 = InlineKeyboardButton(text=stop, callback_data='done')
    if f2 == 0:
        s2 = InlineKeyboardButton(text=skip, callback_data='done')
    elif f2 == 1:
        s2 = InlineKeyboardButton(text=bomb, callback_data='done')
    elif f2 == 2:
        s2 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        s2 = InlineKeyboardButton(text=stop, callback_data='done')
    if f3 == 0:
        s3 = InlineKeyboardButton(text=skip, callback_data='done')
    elif f3 == 1:
        s3 = InlineKeyboardButton(text=bomb, callback_data='done')
    elif f3 == 2:
        s3 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        s3 = InlineKeyboardButton(text=stop, callback_data='done')
    if f4 == 0:
        s4 = InlineKeyboardButton(text=skip, callback_data='done')
    elif f4 == 1:
        s4 = InlineKeyboardButton(text=bomb, callback_data='done')
    elif f4 == 2:
        s4 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        s4 = InlineKeyboardButton(text=stop, callback_data='done')
    return s1, s2, s3, s4


def finish_god(user_id):
    f1, f2, f3, f4 = db.index_string_four(user_id)
    if f1 == 0:
        s1 = InlineKeyboardButton(text=skip, callback_data='done')
    elif f1 == 1:
        s1 = InlineKeyboardButton(text=prize, callback_data='done')
    elif f1 == 2:
        s1 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        s1 = InlineKeyboardButton(text=stop, callback_data='done')
    if f2 == 0:
        s2 = InlineKeyboardButton(text=skip, callback_data='done')
    elif f2 == 1:
        s2 = InlineKeyboardButton(text=prize, callback_data='done')
    elif f2 == 2:
        s2 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        s2 = InlineKeyboardButton(text=stop, callback_data='done')
    if f3 == 0:
        s3 = InlineKeyboardButton(text=skip, callback_data='done')
    elif f3 == 1:
        s3 = InlineKeyboardButton(text=prize, callback_data='done')
    elif f3 == 2:
        s3 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        s3 = InlineKeyboardButton(text=stop, callback_data='done')
    if f4 == 0:
        s4 = InlineKeyboardButton(text=skip, callback_data='done')
    elif f4 == 1:
        s4 = InlineKeyboardButton(text=prize, callback_data='done')
    elif f4 == 2:
        s4 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        s4 = InlineKeyboardButton(text=stop, callback_data='done')
    return s1, s2, s3, s4


def game(user_id):
    balance = db.get_balance(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_base_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_2x2_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_2x2_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_2x2_step)
        else:
            count = int(balance // fo_base_2x2_step)
    elif save == "game_bronze_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_2x2_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_2x2_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_2x2_step)
        else:
            count = int(balance // fo_bronze_2x2_step)
    elif save == "game_silver_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_2x2_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_2x2_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_2x2_step)
        else:
            count = int(balance // fo_silver_2x2_step)
    elif save == "game_gold_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_2x2_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_2x2_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_2x2_step)
        else:
            count = int(balance // fo_gold_2x2_step)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_vip_2x2_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_vip_2x2_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_vip_2x2_step)
        else:
            count = int(balance // fo_vip_2x2_step)
    if count < 0:
        count = 0
    text = options.game_start(user_id, count)
    markup = InlineKeyboardMarkup(row_width=2)
    s1 = InlineKeyboardButton(text=close, callback_data='sf1')
    s2 = InlineKeyboardButton(text=close, callback_data='sf2')
    s3 = InlineKeyboardButton(text=close, callback_data='sf3')
    s4 = InlineKeyboardButton(text=close, callback_data='sf4')
    # new_game = InlineKeyboardButton(text='Новая игра', callback_data='done')
    if save == "game_base_four":
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cb = 'norm_gold_four'
    else:
        cb = 'norm_vip_four'
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4)
    markup.add(back)
    return text, markup


def sf1(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if f1 == 0:
        text = options.norm_2x2_step(user_id)
        s1 = InlineKeyboardButton(text=skip, callback_data='skip')
        s2 = InlineKeyboardButton(text=close, callback_data='sf1_sf2')
        s3 = InlineKeyboardButton(text=close, callback_data='sf1_sf3')
        s4 = InlineKeyboardButton(text=close, callback_data='sf1_sf4')
        if save == "game_base_four":
            cn = 'game_base_four'
            cb = 'norm_base_four'
        elif save == "game_bronze_four":
            cn = 'game_bronze_four'
            cb = 'norm_bronze_four'
        elif save == "game_silver_four":
            cn = 'game_silver_four'
            cb = 'norm_silver_four'
        elif save == "game_gold_four":
            cn = 'game_gold_four'
            cb = 'norm_gold_four'
        elif save == "game_vip_four":
            cn = 'game_vip_four'
            cb = 'norm_vip_four'
        else:
            cn = 'game_free_four'
            cb = 'free_four'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(s1, s2, s3, s4)
        markup.add(back)
    else:
        if god_mode:
            if f1 == 1:
                text = options.norm_2x2_loss(user_id)
                s1, s2, s3, s4 = finish(user_id)
            elif f1 == 2:
                text = options.norm_2x2_loss(user_id)
                s1, s2, s3, s4 = finish_god(user_id)
            else:
                text = options.norm_2x2_stop(user_id)
                s1, s2, s3, s4 = finish(user_id)

        else:
            if f1 == 1:
                text = options.norm_2x2_loss(user_id)
            elif f1 == 2:
                text = options.norm_2x2_win(user_id)
            else:
                text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
        right = db.new_game(user_id)
        if save == "game_base_four":
            cn = 'game_base_four'
            cb = 'norm_base_four'
        elif save == "game_bronze_four":
            cn = 'game_bronze_four'
            cb = 'norm_bronze_four'
        elif save == "game_silver_four":
            cn = 'game_silver_four'
            cb = 'norm_silver_four'
        elif save == "game_gold_four":
            cn = 'game_gold_four'
            cb = 'norm_gold_four'
        elif save == "game_vip_four":
            cn = 'game_vip_four'
            cb = 'norm_vip_four'
        else:
            cn = 'game_free_four'
            cb = 'free_four'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(s1, s2, s3, s4, new_game)
        markup.add(back)
    return text, markup


def sf1_sf2(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if god_mode:
        if f2 == 1:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish(user_id)
        elif f2 == 2:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish_god(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
    else:
        if f2 == 1:
            text = options.norm_2x2_loss(user_id)
        elif f2 == 2:
            text = options.norm_2x2_win(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
        s1, s2, s3, s4 = finish(user_id)
    right = db.new_game(user_id)
    if save == "game_base_four":
        cn = 'game_base_four'
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cn = 'game_bronze_four'
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cn = 'game_silver_four'
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cn = 'game_gold_four'
        cb = 'norm_gold_four'
    elif save == "game_vip_four":
        cn = 'game_vip_four'
        cb = 'norm_vip_four'
    else:
        cn = 'game_free_four'
        cb = 'free_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, new_game)
    markup.add(back)
    return text, markup


def sf1_sf3(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if god_mode:
        if f3 == 1:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish(user_id)
        elif f3 == 2:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish_god(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
    else:
        if f3 == 1:
            text = options.norm_2x2_loss(user_id)
        elif f3 == 2:
            text = options.norm_2x2_win(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
        s1, s2, s3, s4 = finish(user_id)
    right = db.new_game(user_id)
    if save == "game_base_four":
        cn = 'game_base_four'
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cn = 'game_bronze_four'
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cn = 'game_silver_four'
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cn = 'game_gold_four'
        cb = 'norm_gold_four'
    elif save == "game_vip_four":
        cn = 'game_vip_four'
        cb = 'norm_vip_four'
    else:
        cn = 'game_free_four'
        cb = 'free_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, new_game)
    markup.add(back)
    return text, markup


def sf1_sf4(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if god_mode:
        if f4 == 1:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish(user_id)
        elif f4 == 2:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish_god(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
    else:
        if f4 == 1:
            text = options.norm_2x2_loss(user_id)
        elif f4 == 2:
            text = options.norm_2x2_win(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
        s1, s2, s3, s4 = finish(user_id)
    right = db.new_game(user_id)
    if save == "game_base_four":
        cn = 'game_base_four'
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cn = 'game_bronze_four'
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cn = 'game_silver_four'
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cn = 'game_gold_four'
        cb = 'norm_gold_four'
    elif save == "game_vip_four":
        cn = 'game_vip_four'
        cb = 'norm_vip_four'
    else:
        cn = 'game_free_four'
        cb = 'free_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, new_game)
    markup.add(back)
    return text, markup


def sf2(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if f2 == 0:
        text = options.norm_2x2_step(user_id)
        s1 = InlineKeyboardButton(text=close, callback_data='sf2_sf1')
        s2 = InlineKeyboardButton(text=skip, callback_data='skip')
        s3 = InlineKeyboardButton(text=close, callback_data='sf2_sf3')
        s4 = InlineKeyboardButton(text=close, callback_data='sf2_sf4')
        if save == "game_base_four":
            cn = 'game_base_four'
            cb = 'norm_base_four'
        elif save == "game_bronze_four":
            cn = 'game_bronze_four'
            cb = 'norm_bronze_four'
        elif save == "game_silver_four":
            cn = 'game_silver_four'
            cb = 'norm_silver_four'
        elif save == "game_gold_four":
            cn = 'game_gold_four'
            cb = 'norm_gold_four'
        elif save == "game_vip_four":
            cn = 'game_vip_four'
            cb = 'norm_vip_four'
        else:
            cn = 'game_free_four'
            cb = 'free_four'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(s1, s2, s3, s4)
        markup.add(back)
    else:
        if god_mode:
            if f2 == 1:
                text = options.norm_2x2_loss(user_id)
                s1, s2, s3, s4 = finish(user_id)
            elif f2 == 2:
                text = options.norm_2x2_loss(user_id)
                s1, s2, s3, s4 = finish_god(user_id)
            else:
                text = options.norm_2x2_stop(user_id)
                s1, s2, s3, s4 = finish(user_id)
        else:
            if f2 == 1:
                text = options.norm_2x2_loss(user_id)
            elif f2 == 2:
                text = options.norm_2x2_win(user_id)
            else:
                text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
        right = db.new_game(user_id)
        if save == "game_base_four":
            cn = 'game_base_four'
            cb = 'norm_base_four'
        elif save == "game_bronze_four":
            cn = 'game_bronze_four'
            cb = 'norm_bronze_four'
        elif save == "game_silver_four":
            cn = 'game_silver_four'
            cb = 'norm_silver_four'
        elif save == "game_gold_four":
            cn = 'game_gold_four'
            cb = 'norm_gold_four'
        elif save == "game_vip_four":
            cn = 'game_vip_four'
            cb = 'norm_vip_four'
        else:
            cn = 'game_free_four'
            cb = 'free_four'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(s1, s2, s3, s4, new_game)
        markup.add(back)
    return text, markup


def sf2_sf1(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if god_mode:
        if f1 == 1:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish(user_id)
        elif f1 == 2:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish_god(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
    else:
        if f1 == 1:
            text = options.norm_2x2_loss(user_id)
        elif f1 == 2:
            text = options.norm_2x2_win(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
        s1, s2, s3, s4 = finish(user_id)
    right = db.new_game(user_id)
    if save == "game_base_four":
        cn = 'game_base_four'
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cn = 'game_bronze_four'
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cn = 'game_silver_four'
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cn = 'game_gold_four'
        cb = 'norm_gold_four'
    elif save == "game_vip_four":
        cn = 'game_vip_four'
        cb = 'norm_vip_four'
    else:
        cn = 'game_free_four'
        cb = 'free_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, new_game)
    markup.add(back)
    return text, markup


def sf2_sf3(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if god_mode:
        if f3 == 1:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish(user_id)
        elif f3 == 2:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish_god(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
    else:
        if f3 == 1:
            text = options.norm_2x2_loss(user_id)
        elif f3 == 2:
            text = options.norm_2x2_win(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
        s1, s2, s3, s4 = finish(user_id)
    right = db.new_game(user_id)
    if save == "game_base_four":
        cn = 'game_base_four'
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cn = 'game_bronze_four'
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cn = 'game_silver_four'
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cn = 'game_gold_four'
        cb = 'norm_gold_four'
    elif save == "game_vip_four":
        cn = 'game_vip_four'
        cb = 'norm_vip_four'
    else:
        cn = 'game_free_four'
        cb = 'free_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, new_game)
    markup.add(back)
    return text, markup


def sf2_sf4(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if god_mode:
        if f4 == 1:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish(user_id)
        elif f4 == 2:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish_god(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
    else:
        if f4 == 1:
            text = options.norm_2x2_loss(user_id)
        elif f4 == 2:
            text = options.norm_2x2_win(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
        s1, s2, s3, s4 = finish(user_id)
    right = db.new_game(user_id)
    if save == "game_base_four":
        cn = 'game_base_four'
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cn = 'game_bronze_four'
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cn = 'game_silver_four'
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cn = 'game_gold_four'
        cb = 'norm_gold_four'
    elif save == "game_vip_four":
        cn = 'game_vip_four'
        cb = 'norm_vip_four'
    else:
        cn = 'game_free_four'
        cb = 'free_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, new_game)
    markup.add(back)
    return text, markup


def sf3(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if f3 == 0:
        text = options.norm_2x2_step(user_id)
        s1 = InlineKeyboardButton(text=close, callback_data='sf3_sf1')
        s2 = InlineKeyboardButton(text=close, callback_data='sf3_sf2')
        s3 = InlineKeyboardButton(text=skip, callback_data='skip')
        s4 = InlineKeyboardButton(text=close, callback_data='sf3_sf4')
        if save == "game_base_four":
            cn = 'game_base_four'
            cb = 'norm_base_four'
        elif save == "game_bronze_four":
            cn = 'game_bronze_four'
            cb = 'norm_bronze_four'
        elif save == "game_silver_four":
            cn = 'game_silver_four'
            cb = 'norm_silver_four'
        elif save == "game_gold_four":
            cn = 'game_gold_four'
            cb = 'norm_gold_four'
        elif save == "game_vip_four":
            cn = 'game_vip_four'
            cb = 'norm_vip_four'
        else:
            cn = 'game_free_four'
            cb = 'free_four'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(s1, s2, s3, s4)
        markup.add(back)
    else:
        if god_mode:
            if f3 == 1:
                text = options.norm_2x2_loss(user_id)
                s1, s2, s3, s4 = finish(user_id)
            elif f3 == 2:
                text = options.norm_2x2_loss(user_id)
                s1, s2, s3, s4 = finish_god(user_id)
            else:
                text = options.norm_2x2_stop(user_id)
                s1, s2, s3, s4 = finish(user_id)
        else:
            if f3 == 1:
                text = options.norm_2x2_loss(user_id)
            elif f3 == 2:
                text = options.norm_2x2_win(user_id)
            else:
                text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
        right = db.new_game(user_id)
        if save == "game_base_four":
            cn = 'game_base_four'
            cb = 'norm_base_four'
        elif save == "game_bronze_four":
            cn = 'game_bronze_four'
            cb = 'norm_bronze_four'
        elif save == "game_silver_four":
            cn = 'game_silver_four'
            cb = 'norm_silver_four'
        elif save == "game_gold_four":
            cn = 'game_gold_four'
            cb = 'norm_gold_four'
        elif save == "game_vip_four":
            cn = 'game_vip_four'
            cb = 'norm_vip_four'
        else:
            cn = 'game_free_four'
            cb = 'free_four'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(s1, s2, s3, s4, new_game)
        markup.add(back)
    return text, markup


def sf3_sf1(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if god_mode:
        if f1 == 1:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish(user_id)
        elif f1 == 2:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish_god(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
    else:
        if f1 == 1:
            text = options.norm_2x2_loss(user_id)
        elif f1 == 2:
            text = options.norm_2x2_win(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
        s1, s2, s3, s4 = finish(user_id)
    right = db.new_game(user_id)
    if save == "game_base_four":
        cn = 'game_base_four'
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cn = 'game_bronze_four'
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cn = 'game_silver_four'
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cn = 'game_gold_four'
        cb = 'norm_gold_four'
    elif save == "game_vip_four":
        cn = 'game_vip_four'
        cb = 'norm_vip_four'
    else:
        cn = 'game_free_four'
        cb = 'free_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, new_game)
    markup.add(back)

    return text, markup


def sf3_sf2(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if god_mode:
        if f2 == 1:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish(user_id)
        elif f2 == 2:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish_god(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
    else:
        if f2 == 1:
            text = options.norm_2x2_loss(user_id)
        elif f2 == 2:
            text = options.norm_2x2_win(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
        s1, s2, s3, s4 = finish(user_id)
    right = db.new_game(user_id)
    if save == "game_base_four":
        cn = 'game_base_four'
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cn = 'game_bronze_four'
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cn = 'game_silver_four'
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cn = 'game_gold_four'
        cb = 'norm_gold_four'
    elif save == "game_vip_four":
        cn = 'game_vip_four'
        cb = 'norm_vip_four'
    else:
        cn = 'game_free_four'
        cb = 'free_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, new_game)
    markup.add(back)
    return text, markup


def sf3_sf4(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if god_mode:
        if f4 == 1:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish(user_id)
        elif f4 == 2:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish_god(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
    else:
        if f4 == 1:
            text = options.norm_2x2_loss(user_id)
        elif f4 == 2:
            text = options.norm_2x2_win(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
        s1, s2, s3, s4 = finish(user_id)
    right = db.new_game(user_id)
    if save == "game_base_four":
        cn = 'game_base_four'
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cn = 'game_bronze_four'
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cn = 'game_silver_four'
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cn = 'game_gold_four'
        cb = 'norm_gold_four'
    elif save == "game_vip_four":
        cn = 'game_vip_four'
        cb = 'norm_vip_four'
    else:
        cn = 'game_free_four'
        cb = 'free_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, new_game)
    markup.add(back)
    return text, markup


def sf4(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if f4 == 0:
        text = options.norm_2x2_step(user_id)
        s1 = InlineKeyboardButton(text=close, callback_data='sf4_sf1')
        s2 = InlineKeyboardButton(text=close, callback_data='sf4_sf2')
        s3 = InlineKeyboardButton(text=close, callback_data='sf4_sf3')
        s4 = InlineKeyboardButton(text=skip, callback_data='skip')
        if save == "game_base_four":
            cn = 'game_base_four'
            cb = 'norm_base_four'
        elif save == "game_bronze_four":
            cn = 'game_bronze_four'
            cb = 'norm_bronze_four'
        elif save == "game_silver_four":
            cn = 'game_silver_four'
            cb = 'norm_silver_four'
        elif save == "game_gold_four":
            cn = 'game_gold_four'
            cb = 'norm_gold_four'
        elif save == "game_vip_four":
            cn = 'game_vip_four'
            cb = 'norm_vip_four'
        else:
            cn = 'game_free_four'
            cb = 'free_four'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(s1, s2, s3, s4)
        markup.add(back)
    else:
        if god_mode:
            if f4 == 1:
                text = options.norm_2x2_loss(user_id)
                s1, s2, s3, s4 = finish(user_id)
            elif f4 == 2:
                text = options.norm_2x2_loss(user_id)
                s1, s2, s3, s4 = finish_god(user_id)
            else:
                text = options.norm_2x2_stop(user_id)
                s1, s2, s3, s4 = finish(user_id)
        else:
            if f4 == 1:
                text = options.norm_2x2_loss(user_id)
            elif f4 == 2:
                text = options.norm_2x2_win(user_id)
            else:
                text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
        right = db.new_game(user_id)
        if save == "game_base_four":
            cn = 'game_base_four'
            cb = 'norm_base_four'
        elif save == "game_bronze_four":
            cn = 'game_bronze_four'
            cb = 'norm_bronze_four'
        elif save == "game_silver_four":
            cn = 'game_silver_four'
            cb = 'norm_silver_four'
        elif save == "game_gold_four":
            cn = 'game_gold_four'
            cb = 'norm_gold_four'
        elif save == "game_vip_four":
            cn = 'game_vip_four'
            cb = 'norm_vip_four'
        else:
            cn = 'game_free_four'
            cb = 'free_four'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(s1, s2, s3, s4, new_game)
        markup.add(back)
    return text, markup


def sf4_sf1(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if god_mode:
        if f1 == 1:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish(user_id)
        elif f1 == 2:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish_god(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
    else:
        if f1 == 1:
            text = options.norm_2x2_loss(user_id)
        elif f1 == 2:
            text = options.norm_2x2_win(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
        s1, s2, s3, s4 = finish(user_id)
    right = db.new_game(user_id)
    if save == "game_base_four":
        cn = 'game_base_four'
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cn = 'game_bronze_four'
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cn = 'game_silver_four'
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cn = 'game_gold_four'
        cb = 'norm_gold_four'
    elif save == "game_vip_four":
        cn = 'game_vip_four'
        cb = 'norm_vip_four'
    else:
        cn = 'game_free_four'
        cb = 'free_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, new_game)
    markup.add(back)
    return text, markup


def sf4_sf2(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if god_mode:
        if f2 == 1:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish(user_id)
        elif f2 == 2:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish_god(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
    else:
        if f2 == 1:
            text = options.norm_2x2_loss(user_id)
        elif f2 == 2:
            text = options.norm_2x2_win(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
        s1, s2, s3, s4 = finish(user_id)
    right = db.new_game(user_id)
    if save == "game_base_four":
        cn = 'game_base_four'
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cn = 'game_bronze_four'
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cn = 'game_silver_four'
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cn = 'game_gold_four'
        cb = 'norm_gold_four'
    elif save == "game_vip_four":
        cn = 'game_vip_four'
        cb = 'norm_vip_four'
    else:
        cn = 'game_free_four'
        cb = 'free_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, new_game)
    markup.add(back)
    return text, markup


def sf4_sf3(user_id):
    save = db.get_save(user_id)
    god_mode = db.get_god_mode(user_id)
    f1, f2, f3, f4 = db.index_string_four(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    if god_mode:
        if f3 == 1:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish(user_id)
        elif f3 == 2:
            text = options.norm_2x2_loss(user_id)
            s1, s2, s3, s4 = finish_god(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
            s1, s2, s3, s4 = finish(user_id)
    else:
        if f3 == 1:
            text = options.norm_2x2_loss(user_id)
        elif f3 == 2:
            text = options.norm_2x2_win(user_id)
        else:
            text = options.norm_2x2_stop(user_id)
        s1, s2, s3, s4 = finish(user_id)
    right = db.new_game(user_id)
    if save == "game_base_four":
        cn = 'game_base_four'
        cb = 'norm_base_four'
    elif save == "game_bronze_four":
        cn = 'game_bronze_four'
        cb = 'norm_bronze_four'
    elif save == "game_silver_four":
        cn = 'game_silver_four'
        cb = 'norm_silver_four'
    elif save == "game_gold_four":
        cn = 'game_gold_four'
        cb = 'norm_gold_four'
    elif save == "game_vip_four":
        cn = 'game_vip_four'
        cb = 'norm_vip_four'
    else:
        cn = 'game_free_four'
        cb = 'free_four'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(s1, s2, s3, s4, new_game)
    markup.add(back)
    return text, markup
