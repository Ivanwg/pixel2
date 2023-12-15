from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import all_lang
import db
import lists

from options import f_base_2x2_step, f_bronze_2x2_step, f_silver_2x2_step, f_gold_2x2_step, f_vip_2x2_step, f_base_2x3_step, f_bronze_2x3_step, f_silver_2x3_step, f_gold_2x3_step, f_vip_2x3_step, f_base_3x3_step, f_bronze_3x3_step, f_silver_3x3_step, f_gold_3x3_step, f_vip_3x3_step, f_base_four_loss, f_bronze_four_loss, f_silver_four_loss, f_gold_four_loss, f_vip_four_loss, f_base_six_loss, f_bronze_six_loss, f_silver_six_loss, f_gold_six_loss, f_vip_six_loss, f_base_nine_loss, f_bronze_nine_loss, f_silver_nine_loss, f_gold_nine_loss, f_vip_nine_loss
from options import s_base_2x2_step, s_bronze_2x2_step, s_silver_2x2_step, s_gold_2x2_step, s_vip_2x2_step, s_base_2x3_step, s_bronze_2x3_step, s_silver_2x3_step, s_gold_2x3_step, s_vip_2x3_step, s_base_3x3_step, s_bronze_3x3_step, s_silver_3x3_step, s_gold_3x3_step, s_vip_3x3_step, s_base_four_loss, s_bronze_four_loss, s_silver_four_loss, s_gold_four_loss, s_vip_four_loss, s_base_six_loss, s_bronze_six_loss, s_silver_six_loss, s_gold_six_loss, s_vip_six_loss, s_base_nine_loss, s_bronze_nine_loss, s_silver_nine_loss, s_gold_nine_loss, s_vip_nine_loss
from options import t_base_2x2_step, t_bronze_2x2_step, t_silver_2x2_step, t_gold_2x2_step, t_vip_2x2_step, t_base_2x3_step, t_bronze_2x3_step, t_silver_2x3_step, t_gold_2x3_step, t_vip_2x3_step, t_base_3x3_step, t_bronze_3x3_step, t_silver_3x3_step, t_gold_3x3_step, t_vip_3x3_step, t_base_four_loss, t_bronze_four_loss, t_silver_four_loss, t_gold_four_loss, t_vip_four_loss, t_base_six_loss, t_bronze_six_loss, t_silver_six_loss, t_gold_six_loss, t_vip_six_loss, t_base_nine_loss, t_bronze_nine_loss, t_silver_nine_loss, t_gold_nine_loss, t_vip_nine_loss
from options import fo_base_2x2_step, fo_bronze_2x2_step, fo_silver_2x2_step, fo_gold_2x2_step, fo_vip_2x2_step, fo_base_2x3_step, fo_bronze_2x3_step, fo_silver_2x3_step, fo_gold_2x3_step, fo_vip_2x3_step, fo_base_3x3_step, fo_bronze_3x3_step, fo_silver_3x3_step, fo_gold_3x3_step, fo_vip_3x3_step, fo_base_four_loss, fo_bronze_four_loss, fo_silver_four_loss, fo_gold_four_loss, fo_vip_four_loss, fo_base_six_loss, fo_bronze_six_loss, fo_silver_six_loss, fo_gold_six_loss, fo_vip_six_loss, fo_base_nine_loss, fo_bronze_nine_loss, fo_silver_nine_loss, fo_gold_nine_loss, fo_vip_nine_loss


def norm_base_four(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_base_2x2_step)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_base_2x2_step)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_base_2x2_step)
    else:
        count = int(balance // fo_base_2x2_step)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    nl = 'base'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='norm_bronze_four')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    name_size = InlineKeyboardButton(text='2x2', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='norm_base_six')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_base_four'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_bronze_four(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_bronze_2x2_step)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_bronze_2x2_step)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_bronze_2x2_step)
    else:
        count = int(balance // fo_bronze_2x2_step)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='norm_base_four')
    nl = 'bronze'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='norm_silver_four')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    name_size = InlineKeyboardButton(text='2x2', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='norm_bronze_six')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_bronze_four'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_silver_four(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_silver_2x2_step)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_silver_2x2_step)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_silver_2x2_step)
    else:
        count = int(balance // fo_silver_2x2_step)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='norm_bronze_four')
    nl = 'silver'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='norm_gold_four')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    name_size = InlineKeyboardButton(text='2x2', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='norm_silver_six')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_silver_four'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_gold_four(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_gold_2x2_step)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_gold_2x2_step)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_gold_2x2_step)
    else:
        count = int(balance // fo_gold_2x2_step)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='norm_silver_four')
    nl = 'gold'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='norm_vip_four')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    name_size = InlineKeyboardButton(text='2x2', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='norm_gold_six')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_gold_four'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_vip_four(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
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
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='norm_gold_four')
    nl = 'vip'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    name_size = InlineKeyboardButton(text='2x2', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='norm_vip_six')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_vip_four'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_base_six(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_base_2x3_step)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_base_2x3_step)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_base_2x3_step)
    else:
        count = int(balance // fo_base_2x3_step)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    nl = 'base'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='norm_bronze_six')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='norm_base_four')
    name_size = InlineKeyboardButton(text='2x3', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='norm_base_nine')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_base_six'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_bronze_six(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_bronze_2x3_step)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_bronze_2x3_step)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_bronze_2x3_step)
    else:
        count = int(balance // fo_bronze_2x3_step)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='norm_base_six')
    nl = 'bronze'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='norm_silver_six')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='norm_bronze_four')
    name_size = InlineKeyboardButton(text='2x3', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='norm_bronze_nine')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_bronze_six'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_silver_six(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_silver_2x3_step)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_silver_2x3_step)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_silver_2x3_step)
    else:
        count = int(balance // fo_silver_2x3_step)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='norm_bronze_six')
    nl = 'silver'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='norm_gold_six')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='norm_silver_four')
    name_size = InlineKeyboardButton(text='2x3', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='norm_silver_nine')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_silver_six'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_gold_six(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_gold_2x3_step)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_gold_2x3_step)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_gold_2x3_step)
    else:
        count = int(balance // fo_gold_2x3_step)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='norm_silver_six')
    nl = 'gold'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='norm_vip_six')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='norm_gold_four')
    name_size = InlineKeyboardButton(text='2x3', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='norm_gold_nine')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_gold_six'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_vip_six(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
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
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='norm_gold_six')
    nl = 'vip'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='norm_vip_four')
    name_size = InlineKeyboardButton(text='2x3', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='norm_vip_nine')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_vip_six'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_base_nine(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_base_3x3_step)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_base_3x3_step)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_base_3x3_step)
    else:
        count = int(balance // fo_base_3x3_step)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    nl = 'base'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='norm_bronze_nine')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='norm_base_six')
    name_size = InlineKeyboardButton(text='3x3', callback_data='false')
    second_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_base_nine'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_bronze_nine(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_bronze_3x3_step)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_bronze_3x3_step)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_bronze_3x3_step)
    else:
        count = int(balance // fo_bronze_3x3_step)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='norm_base_nine')
    nl = 'bronze'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='norm_silver_nine')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='norm_bronze_six')
    name_size = InlineKeyboardButton(text='3x3', callback_data='false')
    second_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_bronze_nine'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_silver_nine(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_silver_3x3_step)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_silver_3x3_step)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_silver_3x3_step)
    else:
        count = int(balance // fo_silver_3x3_step)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='norm_bronze_nine')
    nl = 'silver'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='norm_gold_nine')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='norm_silver_six')
    name_size = InlineKeyboardButton(text='3x3', callback_data='false')
    second_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_silver_nine'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_gold_nine(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_gold_3x3_step)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_gold_3x3_step)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_gold_3x3_step)
    else:
        count = int(balance // fo_gold_3x3_step)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='norm_silver_nine')
    nl = 'gold'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='norm_vip_nine')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='norm_gold_six')
    name_size = InlineKeyboardButton(text='3x3', callback_data='false')
    second_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_gold_nine'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def norm_vip_nine(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
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
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='norm_gold_nine')
    nl = 'vip'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='norm_vip_six')
    name_size = InlineKeyboardButton(text='3x3', callback_data='false')
    second_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_vip_nine'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_base_four(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_base_four_loss)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_base_four_loss)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_base_four_loss)
    else:
        count = int(balance // fo_base_four_loss)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    nl = 'base'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='risk_bronze_four')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    name_size = InlineKeyboardButton(text='3x3', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='risk_base_six')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_base_four'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_base_six(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_base_six_loss)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_base_six_loss)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_base_six_loss)
    else:
        count = int(balance // fo_base_six_loss)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    nl = 'base'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='risk_bronze_six')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='risk_base_four')
    name_size = InlineKeyboardButton(text='4x4', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='risk_base_nine')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_base_six'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_base_nine(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_base_nine_loss)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_base_nine_loss)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_base_nine_loss)
    else:
        count = int(balance // fo_base_nine_loss)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    nl = 'base'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='risk_bronze_nine')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='risk_base_six')
    name_size = InlineKeyboardButton(text='5x5', callback_data='false')
    second_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_base_nine'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_bronze_four(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_bronze_four_loss)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_bronze_four_loss)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_bronze_four_loss)
    else:
        count = int(balance // fo_bronze_four_loss)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='risk_base_four')
    nl = 'bronze'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='risk_silver_four')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    name_size = InlineKeyboardButton(text='3x3', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='risk_bronze_six')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_bronze_four'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_bronze_six(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_bronze_six_loss)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_bronze_six_loss)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_bronze_six_loss)
    else:
        count = int(balance // fo_bronze_six_loss)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='risk_base_six')
    nl = 'bronze'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='risk_silver_six')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='risk_bronze_four')
    name_size = InlineKeyboardButton(text='4x4', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='risk_bronze_nine')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_bronze_six'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_bronze_nine(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_bronze_nine_loss)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_bronze_nine_loss)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_bronze_nine_loss)
    else:
        count = int(balance // fo_bronze_nine_loss)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='risk_base_nine')
    nl = 'bronze'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='risk_silver_nine')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='risk_bronze_six')
    name_size = InlineKeyboardButton(text='5x5', callback_data='false')
    second_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_bronze_nine'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_silver_four(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_silver_four_loss)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_silver_four_loss)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_silver_four_loss)
    else:
        count = int(balance // fo_silver_four_loss)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='risk_bronze_four')
    nl = 'silver'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='risk_gold_four')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    name_size = InlineKeyboardButton(text='3x3', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='risk_silver_six')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_silver_four'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_silver_six(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_silver_six_loss)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_silver_six_loss)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_silver_six_loss)
    else:
        count = int(balance // fo_silver_six_loss)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='risk_bronze_six')
    nl = 'silver'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='risk_gold_six')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='risk_silver_four')
    name_size = InlineKeyboardButton(text='4x4', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='risk_silver_nine')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_silver_six'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_silver_nine(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_silver_nine_loss)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_silver_nine_loss)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_silver_nine_loss)
    else:
        count = int(balance // fo_silver_nine_loss)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='risk_bronze_nine')
    nl = 'silver'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='risk_gold_nine')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='risk_silver_six')
    name_size = InlineKeyboardButton(text='5x5', callback_data='false')
    second_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_silver_nine'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_gold_four(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_gold_four_loss)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_gold_four_loss)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_gold_four_loss)
    else:
        count = int(balance // fo_gold_four_loss)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='risk_silver_four')
    nl = 'gold'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='risk_vip_four')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    name_size = InlineKeyboardButton(text='3x3', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='risk_gold_six')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_gold_four'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_gold_six(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_gold_six_loss)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_gold_six_loss)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_gold_six_loss)
    else:
        count = int(balance // fo_gold_six_loss)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='risk_silver_six')
    nl = 'gold'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='risk_vip_six')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='risk_gold_four')
    name_size = InlineKeyboardButton(text='4x4', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='risk_gold_nine')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_gold_six'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_gold_nine(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        count = int(balance // f_gold_nine_loss)
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        count = int(balance // s_gold_nine_loss)
    elif currency == "EGP" or currency == "INR":
        count = int(balance // t_gold_nine_loss)
    else:
        count = int(balance // fo_gold_nine_loss)
    if count < 0:
        count = 0
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='risk_silver_nine')
    nl = 'gold'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text='>', callback_data='risk_vip_nine')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='risk_gold_six')
    name_size = InlineKeyboardButton(text='5x5', callback_data='false')
    second_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_gold_nine'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_vip_four(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
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
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='risk_gold_four')
    nl = 'vip'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text=' ', callback_data='bye')
    name_size = InlineKeyboardButton(text='3x3', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='risk_vip_six')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_vip_four'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_vip_six(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
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
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='risk_gold_six')
    nl = 'vip'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='risk_vip_four')
    name_size = InlineKeyboardButton(text='4x4', callback_data='false')
    second_plus = InlineKeyboardButton(text='>', callback_data='risk_vip_nine')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_vip_six'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


def risk_vip_nine(user_id):
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
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
    text = all_lang.text_count(user_id, count)
    markup = InlineKeyboardMarkup(row_width=3)
    level = all_lang.button_level(user_id)
    first_minus = InlineKeyboardButton(text='<', callback_data='risk_gold_nine')
    nl = 'vip'
    name_level = all_lang.button_name_level(user_id, nl)
    first_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    size = all_lang.button_field_size(user_id)
    second_minus = InlineKeyboardButton(text='<', callback_data='risk_vip_six')
    name_size = InlineKeyboardButton(text='5x5', callback_data='false')
    second_plus = InlineKeyboardButton(text=' ', callback_data='bye')
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    cp = 'game_risk_vip_nine'
    play = all_lang.button_play(user_id, cp)
    markup.add(level)
    markup.add(first_minus, name_level, first_plus)
    markup.add(size)
    markup.add(second_minus, name_size, second_plus)
    markup.add(back, play)
    return text, markup


# def free_four(user_id):
#     if count < 0:
#         count = 0
#     text = all_lang.text_count(user_id, count)
#     markup = InlineKeyboardMarkup(row_width=3)
#     size = all_lang.button_field_size(user_id)
#     second_minus = InlineKeyboardButton(text=' ', callback_data='false')
#     name_size = InlineKeyboardButton(text='2x2', callback_data='false')
#     second_plus = InlineKeyboardButton(text='>', callback_data='free_six')
#     cb = 'tg_mode'
#     back = all_lang.button_back(user_id, cb)
#     play = InlineKeyboardButton(text='💎 Играть', callback_data='game_free_four')
#     markup.add(size)
#     markup.add(second_minus, name_size, second_plus)
#     markup.add(back, play)
#     return text, markup
#
#
# def free_six(user_id):
#     if count < 0:
#         count = 0
#     text = all_lang.text_count(user_id, count)
#     markup = InlineKeyboardMarkup(row_width=3)
#     size = all_lang.button_field_size(user_id)
#     second_minus = InlineKeyboardButton(text='<', callback_data='free_four')
#     name_size = InlineKeyboardButton(text='2x3', callback_data='false')
#     second_plus = InlineKeyboardButton(text='>', callback_data='free_nine')
#     cb = 'tg_mode'
#     play = InlineKeyboardButton(text='💎 Играть', callback_data='game_free_six')
#     markup.add(size)
#     markup.add(second_minus, name_size, second_plus)
#     markup.add(back, play)
#     return text, markup


def free_nine(language):
    # text = all_lang.text_count(user_id, count)
    # markup = InlineKeyboardMarkup(row_width=3)
    # size = all_lang.button_field_size(user_id)
    # second_minus = InlineKeyboardButton(text='<', callback_data='free_six')
    # name_size = InlineKeyboardButton(text='3x3', callback_data='false')
    # second_plus = InlineKeyboardButton(text=' ', callback_data='false')
    # cb = 'tg_mode'
    # back = all_lang.button_back(user_id, cb)
    # play = InlineKeyboardButton(text='💎 Играть', callback_data='game_free_nine')
    # markup.add(size)
    # markup.add(second_minus, name_size, second_plus)
    # markup.add(back, play)
    # if count < 0:
    #     count = 0
    text, markup = lists.tg_mode(language)
    return text, markup
