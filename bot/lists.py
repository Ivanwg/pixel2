from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import all_lang
import config
import db

from exchange import fir1, fir2, fir3, fir4, sec1, sec2, sec3, sec4, thi1, thi2, thi3, thi4, fou1, fou2, fou3, fou4, fif1, fif2, fif3, fif4, six1, six2, six3, six4, sev1, sev2, sev3, sev4

from options import f_base_2x2_step, f_bronze_2x2_step, f_silver_2x2_step, f_gold_2x2_step, f_vip_2x2_step, f_base_2x3_step, f_bronze_2x3_step, f_silver_2x3_step, f_gold_2x3_step, f_vip_2x3_step, f_base_3x3_step, f_bronze_3x3_step, f_silver_3x3_step, f_gold_3x3_step, f_vip_3x3_step, f_base_four_loss, f_bronze_four_loss, f_silver_four_loss, f_gold_four_loss, f_vip_four_loss, f_base_six_loss, f_bronze_six_loss, f_silver_six_loss, f_gold_six_loss, f_vip_six_loss, f_base_nine_loss, f_bronze_nine_loss, f_silver_nine_loss, f_gold_nine_loss, f_vip_nine_loss
from options import s_base_2x2_step, s_bronze_2x2_step, s_silver_2x2_step, s_gold_2x2_step, s_vip_2x2_step, s_base_2x3_step, s_bronze_2x3_step, s_silver_2x3_step, s_gold_2x3_step, s_vip_2x3_step, s_base_3x3_step, s_bronze_3x3_step, s_silver_3x3_step, s_gold_3x3_step, s_vip_3x3_step, s_base_four_loss, s_bronze_four_loss, s_silver_four_loss, s_gold_four_loss, s_vip_four_loss, s_base_six_loss, s_bronze_six_loss, s_silver_six_loss, s_gold_six_loss, s_vip_six_loss, s_base_nine_loss, s_bronze_nine_loss, s_silver_nine_loss, s_gold_nine_loss, s_vip_nine_loss
from options import t_base_2x2_step, t_bronze_2x2_step, t_silver_2x2_step, t_gold_2x2_step, t_vip_2x2_step, t_base_2x3_step, t_bronze_2x3_step, t_silver_2x3_step, t_gold_2x3_step, t_vip_2x3_step, t_base_3x3_step, t_bronze_3x3_step, t_silver_3x3_step, t_gold_3x3_step, t_vip_3x3_step, t_base_four_loss, t_bronze_four_loss, t_silver_four_loss, t_gold_four_loss, t_vip_four_loss, t_base_six_loss, t_bronze_six_loss, t_silver_six_loss, t_gold_six_loss, t_vip_six_loss, t_base_nine_loss, t_bronze_nine_loss, t_silver_nine_loss, t_gold_nine_loss, t_vip_nine_loss
from options import fo_base_2x2_step, fo_bronze_2x2_step, fo_silver_2x2_step, fo_gold_2x2_step, fo_vip_2x2_step, fo_base_2x3_step, fo_bronze_2x3_step, fo_silver_2x3_step, fo_gold_2x3_step, fo_vip_2x3_step, fo_base_3x3_step, fo_bronze_3x3_step, fo_silver_3x3_step, fo_gold_3x3_step, fo_vip_3x3_step, fo_base_four_loss, fo_bronze_four_loss, fo_silver_four_loss, fo_gold_four_loss, fo_vip_four_loss, fo_base_six_loss, fo_bronze_six_loss, fo_silver_six_loss, fo_gold_six_loss, fo_vip_six_loss, fo_base_nine_loss, fo_bronze_nine_loss, fo_silver_nine_loss, fo_gold_nine_loss, fo_vip_nine_loss
from options import free_skip


def webapp():
    webs = types.WebAppInfo(url=config.WEB_URL)
    return webs


def add_user(user_id, message):
    lang = message.from_user.language_code
    if lang == "ar":
        value = "AED"
        lang = "en"
    elif lang == "be":
        value = "BYN"
        lang = "ru"
    elif lang == "ca":
        value = "EUR"
        lang = "es"
    elif lang == "hr":
        value = "EUR"
        lang = "en"
    elif lang == "cs":
        value = "EUR"
        lang = "en"
    elif lang == "nl":
        value = "EUR"
        lang = "en"
    elif lang == "fi":
        value = "EUR"
        lang = "en"
    elif lang == "fr":
        value = "EUR"
        lang = "en"
    elif lang == "de":
        value = "EUR"
        lang = "en"
    elif lang == "hu":
        value = "EUR"
        lang = "en"
    elif lang == "id":
        value = "IDR"
        lang = "id"
    elif lang == "it":
        value = "EUR"
        lang = "it"
    elif lang == "kk":
        value = "KZT"
        lang = "ru"
    elif lang == "ko":
        value = "KRW"
        lang = "ko"
    elif lang == "ms":
        value = "MYR"
        lang = "en"
    elif lang == "nb":
        value = "NOK"
        lang = "en"
    elif lang == "fa":
        value = "USD"
        lang = "fa"
    elif lang == "pl":
        value = "PLN"
        lang = "en"
    elif lang == "pt-br":
        value = "BRL"
        lang = "en"
    elif lang == "ru":
        value = "RUB"
        lang = "ru"
    elif lang == "sr":
        value = "RSD"
        lang = "en"
    elif lang == "sk":
        value = "EUR"
        lang = "en"
    elif lang == "es":
        value = "EUR"
        lang = "es"
    elif lang == "sv":
        value = "SEK"
        lang = "en"
    elif lang == "tr":
        value = "TRY"
        lang = "tr"
    elif lang == "uk":
        value = "UAH"
        lang = "ru"
    elif lang == "uz":
        value = "USD"
        lang = "uz"
    else:
        value = "USD"
        lang = "en"
    reg = True
    currency = db.new_currency(user_id, value)
    language = db.new_language(user_id, lang)
    registry = db.new_registry(user_id, reg)
    return language, currency, registry


def start(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text = all_lang.text_start(user_id)
    wal, jac, instruction, sett, game = all_lang.button_start(user_id)
    markup.add(wal, jac, instruction, sett, game)
    return text, markup


def wallet(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text = all_lang.text_wallet(user_id)
    top, wit, buy_ton, ch, faq, back = all_lang.button_wallet(user_id)
    markup.add(top, wit, buy_ton)
    markup.add(ch)
    markup.add(faq)
    markup.add(back)
    return text, markup


def change(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text, pixel, ton, back = all_lang.text_change(user_id)
    markup.add(pixel, ton, back)
    return text, markup


def pixel_change(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    text, back, a, b, c, d, e, f, g = all_lang.text_pixel_change(user_id)
    markup.add(a, b, c, d, e, f, g)
    markup.add(back)
    return text, markup


def pixel_change_first_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_pixel_change_done(user_id)
    done = all_lang.button_pixel_first_done(user_id)
    markup.add(done, back)
    return text, markup


def pixel_change_second_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_pixel_change_done(user_id)
    done = all_lang.button_pixel_second_done(user_id)
    markup.add(done, back)
    return text, markup


def pixel_change_third_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_pixel_change_done(user_id)
    done = all_lang.button_pixel_third_done(user_id)
    markup.add(done, back)
    return text, markup


def pixel_change_fourth_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_pixel_change_done(user_id)
    done = all_lang.button_pixel_fourth_done(user_id)
    markup.add(done, back)
    return text, markup


def pixel_change_fifth_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_pixel_change_done(user_id)
    done = all_lang.button_pixel_fifth_done(user_id)
    markup.add(done, back)
    return text, markup


def pixel_change_sixth_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_pixel_change_done(user_id)
    done = all_lang.button_pixel_sixth_done(user_id)
    markup.add(done, back)
    return text, markup


def pixel_change_seventh_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_pixel_change_done(user_id)
    done = all_lang.button_pixel_seventh_done(user_id)
    markup.add(done, back)
    return text, markup


def argument_pixel_change_first(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 3
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 5
    elif currency == "EGP" or currency == "INR":
        argument = 1
    else:
        argument = 10
    return argument


def argument_pixel_change_second(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 6
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 10
    elif currency == "EGP" or currency == "INR":
        argument = 2
    else:
        argument = 20
    return argument


def argument_pixel_change_third(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 12
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 20
    elif currency == "EGP" or currency == "INR":
        argument = 4
    else:
        argument = 40
    return argument


def argument_pixel_change_fourth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 18
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 30
    elif currency == "EGP" or currency == "INR":
        argument = 6
    else:
        argument = 60
    return argument


def argument_pixel_change_fifth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 30
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 50
    elif currency == "EGP" or currency == "INR":
        argument = 10
    else:
        argument = 100
    return argument


def argument_pixel_change_sixth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 60
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 100
    elif currency == "EGP" or currency == "INR":
        argument = 20
    else:
        argument = 200
    return argument


def argument_pixel_change_seventh(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 600
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 1000
    elif currency == "EGP" or currency == "INR":
        argument = 200
    else:
        argument = 2000
    return argument


def pixel_change_first(user_id):
    ton = db.get_ton(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    argument = argument_pixel_change_first(user_id)
    if ton >= argument:
        text = all_lang.text_pixel_change_first(user_id)
        a, b, c, d, e, f, g = all_lang.button_pixel_change_first(user_id)
        back = all_lang.back_to_pixel(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_pixel_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def pixel_change_second(user_id):
    ton = db.get_ton(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    argument = argument_pixel_change_second(user_id)
    if ton >= argument:
        text = all_lang.text_pixel_change_second(user_id)
        a, b, c, d, e, f, g = all_lang.button_pixel_change_second(user_id)
        back = all_lang.back_to_pixel(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_pixel_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def pixel_change_third(user_id):
    ton = db.get_ton(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    argument = argument_pixel_change_third(user_id)
    if ton >= argument:
        text = all_lang.text_pixel_change_third(user_id)
        a, b, c, d, e, f, g = all_lang.button_pixel_change_third(user_id)
        back = all_lang.back_to_pixel(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_pixel_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def pixel_change_fourth(user_id):
    ton = db.get_ton(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    argument = argument_pixel_change_fourth(user_id)
    if ton >= argument:
        text = all_lang.text_pixel_change_fourth(user_id)
        a, b, c, d, e, f, g = all_lang.button_pixel_change_fourth(user_id)
        back = all_lang.back_to_pixel(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_pixel_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def pixel_change_fifth(user_id):
    ton = db.get_ton(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    argument = argument_pixel_change_fifth(user_id)
    if ton >= argument:
        text = all_lang.text_pixel_change_fifth(user_id)
        a, b, c, d, e, f, g = all_lang.button_pixel_change_fifth(user_id)
        back = all_lang.back_to_pixel(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_pixel_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def pixel_change_sixth(user_id):
    ton = db.get_ton(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    argument = argument_pixel_change_sixth(user_id)
    if ton >= argument:
        text = all_lang.text_pixel_change_sixth(user_id)
        a, b, c, d, e, f, g = all_lang.button_pixel_change_sixth(user_id)
        back = all_lang.back_to_pixel(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_pixel_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def pixel_change_seventh(user_id):
    ton = db.get_ton(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    argument = argument_pixel_change_seventh(user_id)
    if ton >= argument:
        text = all_lang.text_pixel_change_seventh(user_id)
        a, b, c, d, e, f, g = all_lang.button_pixel_change_seventh(user_id)
        back = all_lang.back_to_pixel(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_pixel_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def min_max_pixel(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        minimum = 300
        maximum = 60000
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        minimum = 500
        maximum = 100000
    elif currency == "EGP" or currency == "INR":
        minimum = 100
        maximum = 20000
    else:
        minimum = 1000
        maximum = 200000
    return minimum, maximum


def ton_change(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    text = all_lang.text_ton_change(user_id)
    a, b, c, d, e, f, g = all_lang.button_ton_change(user_id)
    back = all_lang.back_to_ton(user_id)
    markup.add(a, b, c, d, e, f, g)
    markup.add(back)
    return text, markup


def argument_ton_change_first(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 300
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 500
    elif currency == "EGP" or currency == "INR":
        argument = 100
    else:
        argument = 1000
    return argument


def argument_ton_change_second(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 600
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 1000
    elif currency == "EGP" or currency == "INR":
        argument = 200
    else:
        argument = 2000
    return argument


def argument_ton_change_third(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 1200
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 2000
    elif currency == "EGP" or currency == "INR":
        argument = 400
    else:
        argument = 4000
    return argument


def argument_ton_change_fourth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 1800
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 3000
    elif currency == "EGP" or currency == "INR":
        argument = 600
    else:
        argument = 6000
    return argument


def argument_ton_change_fifth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 3000
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 5000
    elif currency == "EGP" or currency == "INR":
        argument = 1000
    else:
        argument = 10000
    return argument


def argument_ton_change_sixth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 6000
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 10000
    elif currency == "EGP" or currency == "INR":
        argument = 2000
    else:
        argument = 20000
    return argument


def argument_ton_change_seventh(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 60000
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 100000
    elif currency == "EGP" or currency == "INR":
        argument = 20000
    else:
        argument = 200000
    return argument


def ton_change_first(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    balance = db.get_balance(user_id)
    argument = argument_ton_change_first(user_id)
    if balance >= argument:
        text = all_lang.text_ton_change_first(user_id)
        a, b, c, d, e, f, g = all_lang.button_ton_change_first(user_id)
        back = all_lang.back_to_ton_change(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_ton_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def ton_change_first_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_ton_change_all_done(user_id)
    done = all_lang.button_ton_change_first_done(user_id)
    markup.add(done, back)
    return text, markup


def ton_change_second(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    balance = db.get_balance(user_id)
    argument = argument_ton_change_second(user_id)
    if balance >= argument:
        text = all_lang.text_ton_change_second(user_id)
        a, b, c, d, e, f, g = all_lang.button_ton_change_second(user_id)
        back = all_lang.back_to_ton_change(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_ton_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def ton_change_second_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_ton_change_all_done(user_id)
    done = all_lang.button_ton_change_second_done(user_id)
    markup.add(done, back)
    return text, markup


def ton_change_third(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    balance = db.get_balance(user_id)
    argument = argument_ton_change_third(user_id)
    if balance >= argument:
        text = all_lang.text_ton_change_third(user_id)
        a, b, c, d, e, f, g = all_lang.button_ton_change_third(user_id)
        back = all_lang.back_to_ton_change(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_ton_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def ton_change_third_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_ton_change_all_done(user_id)
    done = all_lang.button_ton_change_third_done(user_id)
    markup.add(done, back)
    return text, markup


def ton_change_fourth(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    balance = db.get_balance(user_id)
    argument = argument_ton_change_fourth(user_id)
    if balance >= argument:
        text = all_lang.text_ton_change_fourth(user_id)
        a, b, c, d, e, f, g = all_lang.button_ton_change_fourth(user_id)
        back = all_lang.back_to_ton_change(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_ton_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def ton_change_fourth_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_ton_change_all_done(user_id)
    done = all_lang.button_ton_change_fourth_done(user_id)
    markup.add(done, back)
    return text, markup


def ton_change_fifth(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    balance = db.get_balance(user_id)
    argument = argument_ton_change_fifth(user_id)
    if balance >= argument:
        text = all_lang.text_ton_change_fifth(user_id)
        a, b, c, d, e, f, g = all_lang.button_ton_change_fifth(user_id)
        back = all_lang.back_to_ton_change(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_ton_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def ton_change_fifth_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_ton_change_all_done(user_id)
    done = all_lang.button_ton_change_fifth_done(user_id)
    markup.add(done, back)
    return text, markup


def ton_change_sixth(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    balance = db.get_balance(user_id)
    argument = argument_ton_change_sixth(user_id)
    if balance >= argument:
        text = all_lang.text_ton_change_sixth(user_id)
        a, b, c, d, e, f, g = all_lang.button_ton_change_sixth(user_id)
        back = all_lang.back_to_ton_change(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_ton_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def ton_change_sixth_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_ton_change_all_done(user_id)
    done = all_lang.button_ton_change_sixth_done(user_id)
    markup.add(done, back)
    return text, markup


def ton_change_seventh(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    balance = db.get_balance(user_id)
    argument = argument_ton_change_seventh(user_id)
    if balance >= argument:
        text = all_lang.text_ton_change_seventh(user_id)
        a, b, c, d, e, f, g = all_lang.button_ton_change_seventh(user_id)
        back = all_lang.back_to_ton_change(user_id)
        markup.add(a, b, c, d, e, f, g)
        markup.add(back)
    else:
        text, dep, back = all_lang.back_ton_change(user_id)
        markup.add(dep)
        markup.add(back)
    return text, markup


def ton_change_seventh_done(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, back = all_lang.text_ton_change_all_done(user_id)
    done = all_lang.button_ton_change_seventh_done(user_id)
    markup.add(done, back)
    return text, markup


def tg_mode(user_id):
    markup = InlineKeyboardMarkup()
    text = all_lang.text_tg_mode(user_id)
    game_norm, game_risk, game_free, back, rul = all_lang.button_tg_mode(user_id)
    markup.add(game_norm)
    markup.add(game_risk)
    markup.add(game_free)
    markup.add(back, rul)
    return text, markup


def settings(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text = all_lang.text_settings(user_id)
    lang, value, ow, back = all_lang.button_settings(user_id)
    markup.add(lang, value, ow, back)
    return text, markup


def change_lang(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text = all_lang.text_change_lang(user_id)
    gb = InlineKeyboardButton(text='🇬🇧 English', callback_data='settings_en')
    ru = InlineKeyboardButton(text='🇷🇺 Русский', callback_data='settings_ru')
    bah = InlineKeyboardButton(text='🇮🇩 Bahasa Indonesia', callback_data='settings_id')
    es = InlineKeyboardButton(text='🇪🇸 Español', callback_data='settings_es')
    kr = InlineKeyboardButton(text='🇰🇷 한국어', callback_data='settings_ko')
    it = InlineKeyboardButton(text='🇮🇹 Italiano', callback_data='settings_it')
    cn = InlineKeyboardButton(text='🇨🇳 中文（简体）', callback_data='settings_ch')
    tw = InlineKeyboardButton(text='🇹🇼 中文（繁體）', callback_data='settings_ta')
    ir = InlineKeyboardButton(text='🇮🇷 فارسی', callback_data='settings_fa')
    tr = InlineKeyboardButton(text='🇹🇷 Türkçe', callback_data='settings_tr')
    uz = InlineKeyboardButton(text='🇺🇿 Oʻzbekcha', callback_data='settings_uz')
    be = InlineKeyboardButton(text='🇮🇳 বাংলা', callback_data='settings_be')
    hi = InlineKeyboardButton(text='🇮🇳 हिंदी', callback_data='settings_hi')
    back = InlineKeyboardButton(text='< Назад', callback_data='settings')
    markup.add(gb, ru, bah, es, kr, it, cn, tw, ir, tr, uz, be, hi)
    markup.add(back)
    return text, markup


def change_currency(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    text, back = all_lang.text_change_currency(user_id)
    usd = InlineKeyboardButton(text='USD', callback_data='change_currency_usd')
    eur = InlineKeyboardButton(text='EUR', callback_data='change_currency_eur')
    rub = InlineKeyboardButton(text='RUB', callback_data='change_currency_rub')
    gbp = InlineKeyboardButton(text='GBP', callback_data='change_currency_gbp')
    uah = InlineKeyboardButton(text='UAH', callback_data='change_currency_uah')
    kzt = InlineKeyboardButton(text='KZT', callback_data='change_currency_kzt')
    byn = InlineKeyboardButton(text='BYN', callback_data='change_currency_byn')
    krw = InlineKeyboardButton(text='KRW', callback_data='change_currency_krw')
    ils = InlineKeyboardButton(text='ILS', callback_data='change_currency_ils')
    idr = InlineKeyboardButton(text='IDR', callback_data='change_currency_idr')
    aed = InlineKeyboardButton(text='AED', callback_data='change_currency_aed')
    gel = InlineKeyboardButton(text='GEL', callback_data='change_currency_gel')
    twd = InlineKeyboardButton(text='TWD', callback_data='change_currency_twd')
    tri = InlineKeyboardButton(text='TRY', callback_data='change_currency_try')
    hkd = InlineKeyboardButton(text='HKD', callback_data='change_currency_hkd')
    inr = InlineKeyboardButton(text='INR', callback_data='change_currency_inr')
    cad = InlineKeyboardButton(text='CAD', callback_data='change_currency_cad')
    amd = InlineKeyboardButton(text='AMD', callback_data='change_currency_amd')
    aud = InlineKeyboardButton(text='AUD', callback_data='change_currency_aud')
    pln = InlineKeyboardButton(text='PLN', callback_data='change_currency_pln')
    cop = InlineKeyboardButton(text='COP', callback_data='change_currency_cop')
    brl = InlineKeyboardButton(text='BRL', callback_data='change_currency_brl')
    chf = InlineKeyboardButton(text='CHF', callback_data='change_currency_chf')
    mxn = InlineKeyboardButton(text='MXN', callback_data='change_currency_mxn')
    ars = InlineKeyboardButton(text='ARS', callback_data='change_currency_ars')
    sgd = InlineKeyboardButton(text='SGD', callback_data='change_currency_sgd')
    sar = InlineKeyboardButton(text='SAR', callback_data='change_currency_sar')
    mdl = InlineKeyboardButton(text='MDL', callback_data='change_currency_mdl')
    jpy = InlineKeyboardButton(text='JPY', callback_data='change_currency_jpy')
    ron = InlineKeyboardButton(text='RON', callback_data='change_currency_ron')
    sek = InlineKeyboardButton(text='SEK', callback_data='change_currency_sek')
    azn = InlineKeyboardButton(text='AZN', callback_data='change_currency_azn')
    rsd = InlineKeyboardButton(text='RSD', callback_data='change_currency_rsd')
    nok = InlineKeyboardButton(text='NOK', callback_data='change_currency_nok')
    myr = InlineKeyboardButton(text='MYR', callback_data='change_currency_myr')
    bgn = InlineKeyboardButton(text='BGN', callback_data='change_currency_bgn')
    egp = InlineKeyboardButton(text='EGP', callback_data='change_currency_egp')
    gtq = InlineKeyboardButton(text='GTQ', callback_data='change_currency_gtq')
    clp = InlineKeyboardButton(text='CLP', callback_data='change_currency_clp')
    nzd = InlineKeyboardButton(text='NZD', callback_data='change_currency_nzd')
    markup.add(usd, eur, rub, gbp, uah, kzt, byn, krw, ils, idr, aed, gel, twd, tri, hkd, inr, cad, amd,
               aud, pln, cop, brl, chf, mxn, ars, sgd, sar, mdl, jpy, ron, sek, azn, rsd, nok, myr, bgn,
               egp, gtq, clp, nzd)
    markup.add(back)
    return text, markup


def promo_code(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, invite, play, back = all_lang.text_promo_code(user_id)
    markup.add(invite, play, back)
    return text, markup


def deposit(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text, cards, ton_c, back = all_lang.text_deposit(user_id)
    markup.add(cards, ton_c, back)
    return text, markup


def network_currency(user_id):
    currency = db.get_currency(user_id)
    if currency == "EUR":
        net = "Euro - EUR"
    elif currency == "RUB":
        net = "Russian Ruble - RUB"
    elif currency == "GBP":
        net = "Pound sterling - GBP"
    elif currency == "UAH":
        net = "Ukrainian hryvnia - UAH"
    elif currency == "KZT":
        net = "Kazakhstani Tenge - KZT"
    elif currency == "BYN":
        net = "Belarusian Ruble - BYN"
    elif currency == "KRW":
        net = "South Korean won - KRW"
    elif currency == "ILS":
        net = "Israeli New Shekel - ILS"
    elif currency == "IDR":
        net = "Indonesian Rupiah - IDR"
    elif currency == "AED":
        net = "United Arab Emirates Dirham - AED"
    elif currency == "GEL":
        net = "Georgian Lari - GEL"
    elif currency == "TWD":
        net = "New Taiwan dollar - TWD"
    elif currency == "TRY":
        net = "turkish lira - TRY"
    elif currency == "HKD":
        net = "Hong Kong Dollar - HKD"
    elif currency == "INR":
        net = "Indian Rupee - INR"
    elif currency == "CAD":
        net = "Canadian Dollar - CAD"
    elif currency == "AMD":
        net = "Armenian Dram - AMD"
    elif currency == "AUD":
        net = "Australian Dollar - AUD"
    elif currency == "PLN":
        net = "Polish Zloty - PLN"
    elif currency == "COP":
        net = "Colombian Peso - COP"
    elif currency == "BRL":
        net = "Brazilian Real - BRL"
    elif currency == "CHF":
        net = "Swiss Franc - CH"
    elif currency == "MXN":
        net = "Mexican Peso - MXN"
    elif currency == "ARS":
        net = "Argentine Peso - ARS"
    elif currency == "SGD":
        net = "Singapore Dollar - SGD"
    elif currency == "SAR":
        net = "Saudi Riyal - SAR"
    elif currency == "MDL":
        net = "Moldovan Leu - MDL"
    elif currency == "JPY":
        net = "Japanese Yen - JPY"
    elif currency == "RON":
        net = "Romanian Leu - RON"
    elif currency == "SEK":
        net = "Swedish Krona - SEK"
    elif currency == "AZN":
        net = "Azerbaijani Manat - AZN"
    elif currency == "RSD":
        net = "Serbian Dinar - RSD"
    elif currency == "NOK":
        net = "Norwegian Krone - NOK"
    elif currency == "MYR":
        net = "Malaysian Ringgit - MYR"
    elif currency == "BGN":
        net = "Bulgarian Lev - BGN"
    elif currency == "EGP":
        net = "Egyptian Pound - EGP"
    elif currency == "GTQ":
        net = "Guatemalan Quetzal - GTQ"
    elif currency == "CLP":
        net = "Chilean Peso - CLP"
    elif currency == "NZD":
        net = "New Zealand Dollar - NZD"
    else:
        net = "United States Dollar - USD"
    return net


# def get_cu(user_id):
#     currency = db.get_currency(user_id)
#     cu = exchange.get_price(currency)
#     return cu


def card(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text, back = all_lang.text_card(user_id)
    first, second, third, fourth, fifth, sixth, seventh = all_lang.button_card(user_id)
    markup.add(first, second, third, fourth, fifth, sixth, seventh)
    markup.add(back)
    return text, markup


def exchange_first(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
       ex = fir1
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        ex = fir2
    elif currency == "EGP" or currency == "INR":
        ex = fir3
    else:
        ex = fir4
    return ex


def exchange_second(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        ex = sec1
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        ex = sec2
    elif currency == "EGP" or currency == "INR":
        ex = sec3
    else:
        ex = sec4
    return ex


def exchange_third(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        ex = thi1
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        ex = thi2
    elif currency == "EGP" or currency == "INR":
        ex = thi3
    else:
        ex = thi4
    return ex


def exchange_fourth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        ex = fou1
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        ex = fou2
    elif currency == "EGP" or currency == "INR":
        ex = fou3
    else:
        ex = fou4
    return ex


def exchange_fifth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        ex = fif1
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        ex = fif2
    elif currency == "EGP" or currency == "INR":
        ex = fif3
    else:
        ex = fif4
    return ex


def exchange_sixth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        ex = six1
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        ex = six2
    elif currency == "EGP" or currency == "INR":
        ex = six3
    else:
        ex = six4
    return ex


def exchange_seventh(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        ex = sev1
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        ex = sev2
    elif currency == "EGP" or currency == "INR":
        ex = sev3
    else:
        ex = sev4
    return ex


def first_card(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text = all_lang.text_first_card(user_id)
    first, second, third, fourth, fifth, sixth, seventh = all_lang.button_first_card(user_id)
    back = all_lang.back_to_card(user_id)
    markup.add(first, second, third, fourth, fifth, sixth, seventh)
    markup.add(back)
    return text, markup


def second_card(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text = all_lang.text_second_card(user_id)
    back = all_lang.back_to_card(user_id)
    first, second, third, fourth, fifth, sixth, seventh = all_lang.button_second_card(user_id)
    markup.add(first, second, third, fourth, fifth, sixth, seventh)
    markup.add(back)
    return text, markup


def third_card(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text = all_lang.text_third_card(user_id)
    back = all_lang.back_to_card(user_id)
    first, second, third, fourth, fifth, sixth, seventh = all_lang.button_third_card(user_id)
    markup.add(first, second, third, fourth, fifth, sixth, seventh)
    markup.add(back)
    return text, markup


def fourth_card(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text = all_lang.text_fourth_card(user_id)
    back = all_lang.back_to_card(user_id)
    first, second, third, fourth, fifth, sixth, seventh = all_lang.button_fourth_card(user_id)
    markup.add(first, second, third, fourth, fifth, sixth, seventh)
    markup.add(back)
    return text, markup


def fifth_card(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text = all_lang.text_fifth_card(user_id)
    back = all_lang.back_to_card(user_id)
    first, second, third, fourth, fifth, sixth, seventh = all_lang.button_fifth_card(user_id)
    markup.add(first, second, third, fourth, fifth, sixth, seventh)
    markup.add(back)
    return text, markup


def sixth_card(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text = all_lang.text_sixth_card(user_id)
    back = all_lang.back_to_card(user_id)
    first, second, third, fourth, fifth, sixth, seventh = all_lang.button_sixth_card(user_id)
    markup.add(first, second, third, fourth, fifth, sixth, seventh)
    markup.add(back)
    return text, markup


def seventh_card(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text = all_lang.text_seventh_card(user_id)
    back = all_lang.back_to_card(user_id)
    first, second, third, fourth, fifth, sixth, seventh = all_lang.button_seventh_card(user_id)
    markup.add(first, second, third, fourth, fifth, sixth, seventh)
    markup.add(back)
    return text, markup


def ton_coin(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text, back = all_lang.text_ton_coin(user_id)
    b1, b2, b3, b4, b5, b6, b7 = all_lang.button_ton_coin(user_id)
    markup.add(b1, b2, b3, b4, b5, b6, b7)
    markup.add(back)
    return text, markup


def first_buy_ton(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text, back = all_lang.text_first_buy_ton(user_id)
    b1, b2, b3, b4, b5, b6, b7 = all_lang.button_first_buy_ton(user_id)
    markup.add(b1, b2, b3, b4, b5, b6, b7)
    markup.add(back)
    return text, markup


def first_buy_ton_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text = all_lang.text_first_buy_ton_ok(user_id)
    pay, back = all_lang.button_first_buy_ton_ok(user_id)
    markup.add(pay, back)
    return text, markup


def second_buy_ton(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text, back = all_lang.text_second_buy_ton(user_id)
    b1, b2, b3, b4, b5, b6, b7 = all_lang.button_second_buy_ton(user_id)
    markup.add(b1, b2, b3, b4, b5, b6, b7)
    markup.add(back)
    return text, markup


def second_buy_ton_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text = all_lang.text_second_buy_ton_ok(user_id)
    pay, back = all_lang.button_second_buy_ton_ok(user_id)
    markup.add(pay, back)
    return text, markup


def third_buy_ton(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text, back = all_lang.text_third_buy_ton(user_id)
    b1, b2, b3, b4, b5, b6, b7 = all_lang.button_third_buy_ton(user_id)
    markup.add(b1, b2, b3, b4, b5, b6, b7)
    markup.add(back)
    return text, markup


def third_buy_ton_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text = all_lang.text_third_buy_ton_ok(user_id)
    pay, back = all_lang.button_third_buy_ton_ok(user_id)
    markup.add(pay, back)
    return text, markup


def fourth_buy_ton(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text, back = all_lang.text_fourth_buy_ton(user_id)
    b1, b2, b3, b4, b5, b6, b7 = all_lang.button_fourth_buy_ton(user_id)
    markup.add(b1, b2, b3, b4, b5, b6, b7)
    markup.add(back)
    return text, markup


def fourth_buy_ton_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text = all_lang.text_fourth_buy_ton_ok(user_id)
    pay, back = all_lang.button_fourth_buy_ton_ok(user_id)
    markup.add(pay, back)
    return text, markup


def fifth_buy_ton(user_id):
    language = db.get_language(user_id)
    markup = InlineKeyboardMarkup(row_width=2)
    text, back = all_lang.text_fifth_buy_ton(user_id)
    b1, b2, b3, b4, b5, b6, b7 = all_lang.button_fifth_buy_ton(user_id)
    markup.add(b1, b2, b3, b4, b5, b6, b7)
    markup.add(back)
    return text, markup


def fifth_buy_ton_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text = all_lang.text_fifth_buy_ton_ok(user_id)
    pay, back = all_lang.button_fifth_buy_ton_ok(user_id)
    markup.add(pay, back)
    return text, markup


def sixth_buy_ton(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text, back = all_lang.text_sixth_buy_ton(user_id)
    b1, b2, b3, b4, b5, b6, b7 = all_lang.button_sixth_buy_ton(user_id)
    markup.add(b1, b2, b3, b4, b5, b6, b7)
    markup.add(back)
    return text, markup


def sixth_buy_ton_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text = all_lang.text_sixth_buy_ton_ok(user_id)
    pay, back = all_lang.button_sixth_buy_ton_ok(user_id)
    markup.add(pay, back)
    return text, markup


def seventh_buy_ton(user_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text, back = all_lang.text_seventh_buy_ton(user_id)
    b1, b2, b3, b4, b5, b6, b7 = all_lang.button_seventh_buy_ton(user_id)
    markup.add(b1, b2, b3, b4, b5, b6, b7)
    markup.add(back)
    return text, markup


def seventh_buy_ton_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text = all_lang.text_seventh_buy_ton_ok(user_id)
    pay, back = all_lang.button_seventh_buy_ton_ok(user_id)
    markup.add(pay, back)
    return text, markup


# def cu_rub_list(user_id):
#     currency = db.get_currency(user_id)
#     cu = exchange.get_price(currency)
#     return cu


# def cu_ils_list(user_id):
#     currency = db.get_currency(user_id)
#     cu = exchange.get_price(currency)
#     return cu
#
#
# def cu_egp_list(user_id):
#     currency = db.get_currency(user_id)
#     cu = exchange.get_price(currency)
#     return cu
#
#
# def cu_usd_list(user_id):
#     currency = db.get_currency(user_id)
#     cu = exchange.get_price(currency)
#     return cu


def withdraw(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    text, back = all_lang.text_withdraw(user_id)
    b1, b2, b3, b4, b5, b6 = all_lang.button_withdraw(user_id)
    markup.add(b1, b2, b3, b4, b5, b6, back)
    return text, markup


def argument_withdraw_first(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 6
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 10
    elif currency == "EGP" or currency == "INR":
        argument = 6
    else:
        argument = 20
    return argument


def argument_withdraw_second(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 12
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 20
    elif currency == "EGP" or currency == "INR":
        argument = 8
    else:
        argument = 40
    return argument


def argument_withdraw_third(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 18
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 30
    elif currency == "EGP" or currency == "INR":
        argument = 10
    else:
        argument = 60
    return argument


def argument_withdraw_fourth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 30
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 50
    elif currency == "EGP" or currency == "INR":
        argument = 15
    else:
        argument = 100
    return argument


def argument_withdraw_fifth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 60
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 100
    elif currency == "EGP" or currency == "INR":
        argument = 20
    else:
        argument = 200
    return argument


def argument_withdraw_sixth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        argument = 600
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        argument = 1000
    elif currency == "EGP" or currency == "INR":
        argument = 200
    else:
        argument = 2000
    return argument


def withdraw_first(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    ton = db.get_ton(user_id)
    argument = argument_withdraw_first(user_id)
    if ton >= argument:
        text, back = all_lang.text_withdraw_first(user_id)
        b1, b2, b3, b4, b5, b6 = all_lang.button_withdraw_first(user_id)
        markup.add(b1, b2, b3, b4, b5, b6, back)
    else:
        text, top, back = all_lang.back_no_wallet(user_id)
        markup.add(top)
        markup.add(back)
    return text, markup


def withdraw_first_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    ton = db.get_ton(user_id)
    argument = argument_withdraw_first(user_id)
    if ton >= argument:
        text = all_lang.text_withdraw_first_ok(user_id)
        pay, back = all_lang.button_withdraw_first_ok(user_id)
        markup.add(pay)
        markup.add(back)
    else:
        text, top, back = all_lang.back_no_wallet(user_id)
        markup.add(top)
        markup.add(back)
    return text, markup


def withdraw_second(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    argument = argument_withdraw_second(user_id)
    ton = db.get_ton(user_id)
    if ton >= argument:
        text, back = all_lang.text_withdraw_second(user_id)
        b1, b2, b3, b4, b5, b6 = all_lang.button_withdraw_second(user_id)
        markup.add(b1, b2, b3, b4, b5, b6, back)
    else:
        text, top, back = all_lang.back_no_wallet(user_id)
        markup.add(top)
        markup.add(back)
    return text, markup


def withdraw_second_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    ton = db.get_ton(user_id)
    argument = argument_withdraw_second(user_id)
    if ton >= argument:
        text = all_lang.text_withdraw_second_ok(user_id)
        pay, back = all_lang.button_withdraw_second_ok(user_id)
        markup.add(pay)
        markup.add(back)
    else:
        text, top, back = all_lang.back_no_wallet(user_id)
        markup.add(top)
        markup.add(back)
    return text, markup


def withdraw_third(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    argument = argument_withdraw_third(user_id)
    ton = db.get_ton(user_id)
    if ton >= argument:
        text, back = all_lang.text_withdraw_third(user_id)
        b1, b2, b3, b4, b5, b6 = all_lang.button_withdraw_third(user_id)
        markup.add(b1, b2, b3, b4, b5, b6, back)
    else:
        text, top, back = all_lang.back_no_wallet(user_id)
        markup.add(top)
        markup.add(back)
    return text, markup


def withdraw_third_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    ton = db.get_ton(user_id)
    argument = argument_withdraw_third(user_id)
    if ton >= argument:
        text = all_lang.text_withdraw_third_ok(user_id)
        pay, back = all_lang.button_withdraw_third_ok(user_id)
        markup.add(pay)
        markup.add(back)
    else:
        text, top, back = all_lang.back_no_wallet(user_id)
        markup.add(top)
        markup.add(back)
    return text, markup


def withdraw_fourth(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    argument = argument_withdraw_fourth(user_id)
    ton = db.get_ton(user_id)
    if ton >= argument:
        text, back = all_lang.text_withdraw_fourth(user_id)
        b1, b2, b3, b4, b5, b6 = all_lang.button_withdraw_fourth(user_id)
        markup.add(b1, b2, b3, b4, b5, b6, back)
    else:
        text, top, back = all_lang.back_no_wallet(user_id)
        markup.add(top)
        markup.add(back)
    return text, markup


def withdraw_fourth_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    ton = db.get_ton(user_id)
    argument = argument_withdraw_fourth(user_id)
    if ton >= argument:
        text = all_lang.text_withdraw_fourth_ok(user_id)
        pay, back = all_lang.button_withdraw_fourth_ok(user_id)
        markup.add(pay)
        markup.add(back)
    else:
        text, top, back = all_lang.back_no_wallet(user_id)
        markup.add(top)
        markup.add(back)
    return text, markup


def withdraw_fifth(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    ton = db.get_ton(user_id)
    argument = argument_withdraw_fifth(user_id)
    if ton >= argument:
        text, back = all_lang.text_withdraw_fifth(user_id)
        b1, b2, b3, b4, b5, b6 = all_lang.button_withdraw_fifth(user_id)
        markup.add(b1, b2, b3, b4, b5, b6, back)
    else:
        text, top, back = all_lang.back_no_wallet(user_id)
        markup.add(top)
        markup.add(back)
    return text, markup


def withdraw_fifth_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    ton = db.get_ton(user_id)
    argument = argument_withdraw_fifth(user_id)
    if ton >= argument:
        text = all_lang.text_withdraw_fifth_ok(user_id)
        pay, back = all_lang.button_withdraw_fifth_ok(user_id)
        markup.add(pay)
        markup.add(back)
    else:
        text, top, back = all_lang.back_no_wallet(user_id)
        markup.add(top)
        markup.add(back)
    return text, markup


def withdraw_sixth(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    argument = argument_withdraw_sixth(user_id)
    ton = db.get_ton(user_id)
    if ton >= argument:
        text, back = all_lang.text_withdraw_sixth(user_id)
        b1, b2, b3, b4, b5, b6 = all_lang.button_withdraw_sixth(user_id)
        markup.add(b1, b2, b3, b4, b5, b6, back)
    else:
        text, top, back = all_lang.back_no_wallet(user_id)
        markup.add(top)
        markup.add(back)
    return text, markup


def withdraw_sixth_ok(user_id):
    markup = InlineKeyboardMarkup(row_width=3)
    ton = db.get_ton(user_id)
    argument = argument_withdraw_sixth(user_id)
    if ton >= argument:
        text = all_lang.text_withdraw_sixth_ok(user_id)
        pay, back = all_lang.button_withdraw_sixth_ok(user_id)
        markup.add(pay)
        markup.add(back)
    else:
        text, top, back = all_lang.back_no_wallet(user_id)
        markup.add(top)
        markup.add(back)
    return text, markup


def no_balance(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, dep, back = all_lang.text_no_balance(user_id)
    markup.add(dep, back)
    return text, markup


def no_balance_free(user_id):
    save = db.get_save(user_id)
    res = db.get_res(user_id)
    free_game = db.get_free_game(user_id)
    if save == "game_free":
        strike = 0
        bal = free_game
    else:
        strike = free_skip
        bal = res
    return bal, strike


def no_balance_2x2(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_bronze_2x2_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_bronze_2x2_step
        elif currency == "EGP" or currency == "INR":
            strike = t_bronze_2x2_step
        else:
            strike = fo_bronze_2x2_step
    elif save == "game_silver_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_silver_2x2_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_silver_2x2_step
        elif currency == "EGP" or currency == "INR":
            strike = t_silver_2x2_step
        else:
            strike = fo_silver_2x2_step
    elif save == "game_gold_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_gold_2x2_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_gold_2x2_step
        elif currency == "EGP" or currency == "INR":
            strike = t_gold_2x2_step
        else:
            strike = fo_gold_2x2_step
    elif save == "game_vip_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_vip_2x2_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_vip_2x2_step
        elif currency == "EGP" or currency == "INR":
            strike = t_vip_2x2_step
        else:
            strike = fo_vip_2x2_step
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_base_2x2_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_base_2x2_step
        elif currency == "EGP" or currency == "INR":
            strike = t_base_2x2_step
        else:
            strike = fo_base_2x2_step
    return strike


def no_balance_2x3(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_bronze_2x3_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_bronze_2x3_step
        elif currency == "EGP" or currency == "INR":
            strike = t_bronze_2x3_step
        else:
            strike = fo_bronze_2x3_step
    elif save == "game_silver_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_silver_2x3_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_silver_2x3_step
        elif currency == "EGP" or currency == "INR":
            strike = t_silver_2x3_step
        else:
            strike = fo_silver_2x3_step
    elif save == "game_gold_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_gold_2x3_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_gold_2x3_step
        elif currency == "EGP" or currency == "INR":
            strike = t_gold_2x3_step
        else:
            strike = fo_gold_2x3_step
    elif save == "game_vip_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_vip_2x3_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_vip_2x3_step
        elif currency == "EGP" or currency == "INR":
            strike = t_vip_2x3_step
        else:
            strike = fo_vip_2x3_step
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_base_2x3_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_base_2x3_step
        elif currency == "EGP" or currency == "INR":
            strike = t_base_2x3_step
        else:
            strike = fo_base_2x3_step
    return strike


def no_balance_3x3(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_bronze_3x3_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_bronze_3x3_step
        elif currency == "EGP" or currency == "INR":
            strike = t_bronze_3x3_step
        else:
            strike = fo_bronze_3x3_step
    elif save == "game_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_silver_3x3_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_silver_3x3_step
        elif currency == "EGP" or currency == "INR":
            strike = t_silver_3x3_step
        else:
            strike = fo_silver_3x3_step
    elif save == "game_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_gold_3x3_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_gold_3x3_step
        elif currency == "EGP" or currency == "INR":
            strike = t_gold_3x3_step
        else:
            strike = fo_gold_3x3_step
    elif save == "game_vip_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_vip_3x3_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_vip_3x3_step
        elif currency == "EGP" or currency == "INR":
            strike = t_vip_3x3_step
        else:
            strike = fo_vip_3x3_step
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_base_3x3_step
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_base_3x3_step
        elif currency == "EGP" or currency == "INR":
            strike = t_base_3x3_step
        else:
            strike = fo_base_3x3_step
    return strike


def no_balance_risk_3x3(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_risk_base_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_base_four_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_base_four_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_base_four_loss
        else:
            strike = fo_base_four_loss
    elif save == "game_risk_bronze_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_bronze_four_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_bronze_four_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_bronze_four_loss
        else:
            strike = fo_bronze_four_loss
    elif save == "game_risk_silver_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_silver_four_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_silver_four_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_silver_four_loss
        else:
            strike = fo_silver_four_loss
    elif save == "game_risk_gold_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_gold_four_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_gold_four_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_gold_four_loss
        else:
            strike = fo_gold_four_loss
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_vip_four_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_vip_four_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_vip_four_loss
        else:
            strike = fo_vip_four_loss
    return strike


def no_balance_4x4(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_risk_base_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_base_six_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_base_six_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_base_six_loss
        else:
            strike = fo_base_six_loss
    elif save == "game_risk_bronze_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_bronze_six_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_bronze_six_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_bronze_six_loss
        else:
            strike = fo_bronze_six_loss
    elif save == "game_risk_silver_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_silver_six_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_silver_six_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_silver_six_loss
        else:
            strike = fo_silver_six_loss
    elif save == "game_risk_gold_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_gold_six_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_gold_six_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_gold_six_loss
        else:
            strike = fo_gold_six_loss
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_vip_six_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_vip_six_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_vip_six_loss
        else:
            strike = fo_vip_six_loss
    return strike


def no_balance_5x5(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_risk_base_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_base_nine_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_base_nine_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_base_nine_loss
        else:
            strike = fo_base_nine_loss
    elif save == "game_risk_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_bronze_nine_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_bronze_nine_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_bronze_nine_loss
        else:
            strike = fo_bronze_nine_loss
    elif save == "game_risk_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_silver_nine_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_silver_nine_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_silver_nine_loss
        else:
            strike = fo_silver_nine_loss
    elif save == "game_risk_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_gold_nine_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_gold_nine_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_gold_nine_loss
        else:
            strike = fo_gold_nine_loss
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            strike = f_vip_nine_loss
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
            strike = s_vip_nine_loss
        elif currency == "EGP" or currency == "INR":
            strike = t_vip_nine_loss
        else:
            strike = fo_vip_nine_loss
    return strike


def no_bal(user_id, strike):
    markup = InlineKeyboardMarkup(row_width=1)
    text, dep, back = all_lang.text_no_bal(user_id, strike)
    markup.add(dep, back)
    return text, markup


def no_res(user_id):
    markup = InlineKeyboardMarkup(row_width=1)
    text, dep, back = all_lang.text_no_res(user_id)
    markup.add(dep, back)
    return text, markup
