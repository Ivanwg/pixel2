from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import all_lang
import game_2x3
import options
from options import prize, bomb, skip, stop, close
import db


def ss1(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    god_mode = db.get_god_mode(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i1 == 0:
        text = options.norm_2x3_step(user_id)
        s1 = InlineKeyboardButton(text=skip, callback_data='skip')
        s2 = InlineKeyboardButton(text=close, callback_data='ss1_ss2')
        s3 = InlineKeyboardButton(text=close, callback_data='ss1_ss3')
        s4 = InlineKeyboardButton(text=close, callback_data='ss1_ss4')
        s5 = InlineKeyboardButton(text=close, callback_data='ss1_ss5')
        s6 = InlineKeyboardButton(text=close, callback_data='ss1_ss6')
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
    else:
        if god_mode:
            if i1 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i1 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(s1, s2, s3, s4, s5, s6, new_game)
        markup.add(back)

    return text, markup


def ss1_ss2(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i2 == 0:
        text = options.norm_2x3_step(user_id)
        s1 = InlineKeyboardButton(text=skip, callback_data='skip')
        s2 = InlineKeyboardButton(text=skip, callback_data='skip')
        s3 = InlineKeyboardButton(text=close, callback_data='ss1_ss2_ss3')
        s4 = InlineKeyboardButton(text=close, callback_data='ss1_ss2_ss4')
        s5 = InlineKeyboardButton(text=close, callback_data='ss1_ss2_ss5')
        s6 = InlineKeyboardButton(text=close, callback_data='ss1_ss2_ss6')
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
    else:
        if god_mode:
            if i2 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i2 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(s1, s2, s3, s4, s5, s6, new_game)
        markup.add(back)

    return text, markup


def ss1_ss2_ss3(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i3 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i3 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i3 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss2_ss4(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i4 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i4 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i4 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss2_ss5(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i5 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i5 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i5 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss2_ss6(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i6 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i6 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i6 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss3(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i3 == 0:
        text = options.norm_2x3_step(user_id)
        s1 = InlineKeyboardButton(text=skip, callback_data='skip')
        s2 = InlineKeyboardButton(text=close, callback_data='ss1_ss3_ss2')
        s3 = InlineKeyboardButton(text=skip, callback_data='skip')
        s4 = InlineKeyboardButton(text=close, callback_data='ss1_ss3_ss4')
        s5 = InlineKeyboardButton(text=close, callback_data='ss1_ss3_ss5')
        s6 = InlineKeyboardButton(text=close, callback_data='ss1_ss3_ss6')
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
    else:
        if god_mode:
            if i3 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i3 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(s1, s2, s3, s4, s5, s6, new_game)
        markup.add(back)

    return text, markup


def ss1_ss3_ss2(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i2 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i2 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i2 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss3_ss4(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i4 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i4 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i4 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss3_ss5(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i5 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i5 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i5 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss3_ss6(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i6 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i6 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i6 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss4(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i4 == 0:
        text = options.norm_2x3_step(user_id)
        s1 = InlineKeyboardButton(text=skip, callback_data='skip')
        s2 = InlineKeyboardButton(text=close, callback_data='ss1_ss4_ss2')
        s3 = InlineKeyboardButton(text=close, callback_data='ss1_ss4_ss3')
        s4 = InlineKeyboardButton(text=skip, callback_data='skip')
        s5 = InlineKeyboardButton(text=close, callback_data='ss1_ss4_ss5')
        s6 = InlineKeyboardButton(text=close, callback_data='ss1_ss4_ss6')
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
    else:
        if god_mode:
            if i4 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i4 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(s1, s2, s3, s4, s5, s6, new_game)
        markup.add(back)

    return text, markup


def ss1_ss4_ss2(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i2 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i2 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i2 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss4_ss3(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i3 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i3 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i3 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss4_ss5(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i5 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i5 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i5 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss4_ss6(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i6 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i6 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i6 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss5(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i5 == 0:
        text = options.norm_2x3_step(user_id)
        s1 = InlineKeyboardButton(text=skip, callback_data='skip')
        s2 = InlineKeyboardButton(text=close, callback_data='ss1_ss5_ss2')
        s3 = InlineKeyboardButton(text=close, callback_data='ss1_ss5_ss3')
        s4 = InlineKeyboardButton(text=close, callback_data='ss1_ss5_ss4')
        s5 = InlineKeyboardButton(text=skip, callback_data='skip')
        s6 = InlineKeyboardButton(text=close, callback_data='ss1_ss5_ss6')
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
    else:
        if god_mode:
            if i5 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i5 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(s1, s2, s3, s4, s5, s6, new_game)
        markup.add(back)

    return text, markup


def ss1_ss5_ss2(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i2 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i2 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i2 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss5_ss3(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i3 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i3 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i3 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss5_ss4(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i4 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i4 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i4 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss5_ss6(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i6 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i6 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i6 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss6(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i6 == 0:
        text = options.norm_2x3_step(user_id)
        s1 = InlineKeyboardButton(text=skip, callback_data='skip')
        s2 = InlineKeyboardButton(text=close, callback_data='ss1_ss6_ss2')
        s3 = InlineKeyboardButton(text=close, callback_data='ss1_ss6_ss3')
        s4 = InlineKeyboardButton(text=close, callback_data='ss1_ss6_ss4')
        s5 = InlineKeyboardButton(text=close, callback_data='ss1_ss6_ss5')
        s6 = InlineKeyboardButton(text=skip, callback_data='skip')
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
    else:
        if god_mode:
            if i6 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i6 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(s1, s2, s3, s4, s5, s6, new_game)
        markup.add(back)

    return text, markup


def ss1_ss6_ss2(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i2 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i2 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i2 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss6_ss3(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i3 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i3 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i3 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss6_ss4(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i4 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i4 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i4 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup


def ss1_ss6_ss5(user_id):
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    i1, i2, i3, i4, i5, i6 = db.index_string_six(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if i5 == 0:
        text = options.norm_2x3_step(user_id)
        s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    else:
        if god_mode:
            if i5 == 1:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
            else:
                text = options.norm_2x3_loss(user_id)
                s1, s2, s3, s4, s5, s6 = game_2x3.finish_god(user_id)
        else:
            if i5 == 1:
                text = options.norm_2x3_loss(user_id)
            else:
                text = options.norm_2x3_win(user_id)
            s1, s2, s3, s4, s5, s6 = game_2x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(s1, s2, s3, s4, s5, s6, new_game)
    markup.add(back)

    return text, markup
