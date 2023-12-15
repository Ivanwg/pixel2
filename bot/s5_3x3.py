from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import all_lang
import game_3x3
import options
from options import prize, bomb, skip, stop, close
import db


def st5(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s5 == 0:
        text = options.norm_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='st5_st1')
        t2 = InlineKeyboardButton(text=close, callback_data='st5_st2')
        t3 = InlineKeyboardButton(text=close, callback_data='st5_st3')
        t4 = InlineKeyboardButton(text=close, callback_data='st5_st4')
        t5 = InlineKeyboardButton(text=skip, callback_data='skip')
        t6 = InlineKeyboardButton(text=close, callback_data='st5_st6')
        t7 = InlineKeyboardButton(text=close, callback_data='st5_st7')
        t8 = InlineKeyboardButton(text=close, callback_data='st5_st8')
        t9 = InlineKeyboardButton(text=close, callback_data='st5_st9')
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
    else:
        if god_mode:
            if s5 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s5 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def st5_st1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.norm_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=skip, callback_data='skip')
        t2 = InlineKeyboardButton(text=close, callback_data='st5_st1_st2')
        t3 = InlineKeyboardButton(text=close, callback_data='st5_st1_st3')
        t4 = InlineKeyboardButton(text=close, callback_data='st5_st1_st4')
        t5 = InlineKeyboardButton(text=skip, callback_data='skip')
        t6 = InlineKeyboardButton(text=close, callback_data='st5_st1_st6')
        t7 = InlineKeyboardButton(text=close, callback_data='st5_st1_st7')
        t8 = InlineKeyboardButton(text=close, callback_data='st5_st1_st8')
        t9 = InlineKeyboardButton(text=close, callback_data='st5_st1_st9')
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
    else:
        if god_mode:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def st5_st1_st2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st1_st3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st1_st4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st1_st6(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s6 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st1_st7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st1_st8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st1_st9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.norm_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='st5_st2_st1')
        t2 = InlineKeyboardButton(text=skip, callback_data='skip')
        t3 = InlineKeyboardButton(text=close, callback_data='st5_st2_st3')
        t4 = InlineKeyboardButton(text=close, callback_data='st5_st2_st4')
        t5 = InlineKeyboardButton(text=skip, callback_data='skip')
        t6 = InlineKeyboardButton(text=close, callback_data='st5_st2_st6')
        t7 = InlineKeyboardButton(text=close, callback_data='st5_st2_st7')
        t8 = InlineKeyboardButton(text=close, callback_data='st5_st2_st8')
        t9 = InlineKeyboardButton(text=close, callback_data='st5_st2_st9')
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
    else:
        if god_mode:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def st5_st2_st1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st2_st3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st2_st4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st2_st6(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s6 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st2_st7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st2_st8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st2_st9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.norm_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='st5_st3_st1')
        t2 = InlineKeyboardButton(text=close, callback_data='st5_st3_st2')
        t3 = InlineKeyboardButton(text=skip, callback_data='skip')
        t4 = InlineKeyboardButton(text=close, callback_data='st5_st3_st4')
        t5 = InlineKeyboardButton(text=skip, callback_data='skip')
        t6 = InlineKeyboardButton(text=close, callback_data='st5_st3_st6')
        t7 = InlineKeyboardButton(text=close, callback_data='st5_st3_st7')
        t8 = InlineKeyboardButton(text=close, callback_data='st5_st3_st8')
        t9 = InlineKeyboardButton(text=close, callback_data='st5_st3_st9')
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
    else:
        if god_mode:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def st5_st3_st1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st3_st2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st3_st4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st3_st6(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s6 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st3_st7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st3_st8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st3_st9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.norm_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='st5_st4_st1')
        t2 = InlineKeyboardButton(text=close, callback_data='st5_st4_st2')
        t3 = InlineKeyboardButton(text=close, callback_data='st5_st4_st3')
        t4 = InlineKeyboardButton(text=skip, callback_data='skip')
        t5 = InlineKeyboardButton(text=skip, callback_data='skip')
        t6 = InlineKeyboardButton(text=close, callback_data='st5_st4_st6')
        t7 = InlineKeyboardButton(text=close, callback_data='st5_st4_st7')
        t8 = InlineKeyboardButton(text=close, callback_data='st5_st4_st8')
        t9 = InlineKeyboardButton(text=close, callback_data='st5_st4_st9')
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
    else:
        if god_mode:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def st5_st4_st1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st4_st2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st4_st3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st4_st6(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s6 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st4_st7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st4_st8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st4_st9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st6(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s6 == 0:
        text = options.norm_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='st5_st6_st1')
        t2 = InlineKeyboardButton(text=close, callback_data='st5_st6_st2')
        t3 = InlineKeyboardButton(text=close, callback_data='st5_st6_st3')
        t4 = InlineKeyboardButton(text=close, callback_data='st5_st6_st4')
        t5 = InlineKeyboardButton(text=skip, callback_data='skip')
        t6 = InlineKeyboardButton(text=skip, callback_data='skip')
        t7 = InlineKeyboardButton(text=close, callback_data='st5_st6_st7')
        t8 = InlineKeyboardButton(text=close, callback_data='st5_st6_st8')
        t9 = InlineKeyboardButton(text=close, callback_data='st5_st6_st9')
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
    else:
        if god_mode:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def st5_st6_st1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st6_st2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st6_st3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st6_st4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st6_st7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st6_st8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st6_st9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.norm_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='st5_st7_st1')
        t2 = InlineKeyboardButton(text=close, callback_data='st5_st7_st2')
        t3 = InlineKeyboardButton(text=close, callback_data='st5_st7_st3')
        t4 = InlineKeyboardButton(text=close, callback_data='st5_st7_st4')
        t5 = InlineKeyboardButton(text=skip, callback_data='skip')
        t6 = InlineKeyboardButton(text=close, callback_data='st5_st7_st6')
        t7 = InlineKeyboardButton(text=skip, callback_data='skip')
        t8 = InlineKeyboardButton(text=close, callback_data='st5_st7_st8')
        t9 = InlineKeyboardButton(text=close, callback_data='st5_st7_st9')
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
    else:
        if god_mode:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def st5_st7_st1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st7_st2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st7_st3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st7_st4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st7_st6(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s6 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st7_st8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st7_st9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.norm_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='st5_st8_st1')
        t2 = InlineKeyboardButton(text=close, callback_data='st5_st8_st2')
        t3 = InlineKeyboardButton(text=close, callback_data='st5_st8_st3')
        t4 = InlineKeyboardButton(text=close, callback_data='st5_st8_st4')
        t5 = InlineKeyboardButton(text=skip, callback_data='skip')
        t6 = InlineKeyboardButton(text=close, callback_data='st5_st8_st6')
        t7 = InlineKeyboardButton(text=close, callback_data='st5_st8_st7')
        t8 = InlineKeyboardButton(text=skip, callback_data='skip')
        t9 = InlineKeyboardButton(text=close, callback_data='st5_st8_st9')
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
    else:
        if god_mode:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def st5_st8_st1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st8_st2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st8_st3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st8_st4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st8_st6(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s6 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st8_st7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st8_st9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.norm_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='st5_st9_st1')
        t2 = InlineKeyboardButton(text=close, callback_data='st5_st9_st2')
        t3 = InlineKeyboardButton(text=close, callback_data='st5_st9_st3')
        t4 = InlineKeyboardButton(text=close, callback_data='st5_st9_st4')
        t5 = InlineKeyboardButton(text=skip, callback_data='skip')
        t6 = InlineKeyboardButton(text=close, callback_data='st5_st9_st6')
        t7 = InlineKeyboardButton(text=close, callback_data='st5_st9_st7')
        t8 = InlineKeyboardButton(text=close, callback_data='st5_st9_st8')
        t9 = InlineKeyboardButton(text=skip, callback_data='skip')
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
    else:
        if god_mode:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
        right = db.new_game(user_id)
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
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def st5_st9_st1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st9_st2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st9_st3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st9_st4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st9_st6(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s6 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s6 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st9_st7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def st5_st9_st8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    save = db.get_save(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.norm_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
            else:
                text = options.norm_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.norm_3x3_loss(user_id)
            else:
                text = options.norm_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = game_3x3.finish(user_id)
    right = db.new_game(user_id)
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
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup
