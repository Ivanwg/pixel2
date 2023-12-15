from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import all_lang
import free_3x3
import options
from options import prize, bomb, skip, stop, close
import db


def f6(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s6 == 0:
        text = options.free_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='f6_f1')
        t2 = InlineKeyboardButton(text=close, callback_data='f6_f2')
        t3 = InlineKeyboardButton(text=close, callback_data='f6_f3')
        t4 = InlineKeyboardButton(text=close, callback_data='f6_f4')
        t5 = InlineKeyboardButton(text=close, callback_data='f6_f5')
        t6 = InlineKeyboardButton(text=skip, callback_data='skip')
        t7 = InlineKeyboardButton(text=close, callback_data='f6_f7')
        t8 = InlineKeyboardButton(text=close, callback_data='f6_f8')
        t9 = InlineKeyboardButton(text=close, callback_data='f6_f9')
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9)
        markup.add(back)
    else:
        if god_mode:
            if s6 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s6 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def f6_f1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.free_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=skip, callback_data='skip')
        t2 = InlineKeyboardButton(text=close, callback_data='f6_f1_f2')
        t3 = InlineKeyboardButton(text=close, callback_data='f6_f1_f3')
        t4 = InlineKeyboardButton(text=close, callback_data='f6_f1_f4')
        t5 = InlineKeyboardButton(text=close, callback_data='f6_f1_f5')
        t6 = InlineKeyboardButton(text=skip, callback_data='skip')
        t7 = InlineKeyboardButton(text=close, callback_data='f6_f1_f7')
        t8 = InlineKeyboardButton(text=close, callback_data='f6_f1_f8')
        t9 = InlineKeyboardButton(text=close, callback_data='f6_f1_f9')
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9)
        markup.add(back)
    else:
        if god_mode:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def f6_f1_f2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f1_f3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f1_f4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f1_f5(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s5 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f1_f7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f1_f8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f1_f9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.free_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='f6_f2_f1')
        t2 = InlineKeyboardButton(text=skip, callback_data='skip')
        t3 = InlineKeyboardButton(text=close, callback_data='f6_f2_f3')
        t4 = InlineKeyboardButton(text=close, callback_data='f6_f2_f4')
        t5 = InlineKeyboardButton(text=close, callback_data='f6_f2_f5')
        t6 = InlineKeyboardButton(text=skip, callback_data='skip')
        t7 = InlineKeyboardButton(text=close, callback_data='f6_f2_f7')
        t8 = InlineKeyboardButton(text=close, callback_data='f6_f2_f8')
        t9 = InlineKeyboardButton(text=close, callback_data='f6_f2_f9')
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9)
        markup.add(back)
    else:
        if god_mode:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def f6_f2_f1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f2_f3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f2_f4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f2_f5(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s5 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f2_f7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f2_f8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f2_f9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.free_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='f6_f3_f1')
        t2 = InlineKeyboardButton(text=close, callback_data='f6_f3_f2')
        t3 = InlineKeyboardButton(text=skip, callback_data='skip')
        t4 = InlineKeyboardButton(text=close, callback_data='f6_f3_f4')
        t5 = InlineKeyboardButton(text=close, callback_data='f6_f3_f5')
        t6 = InlineKeyboardButton(text=skip, callback_data='skip')
        t7 = InlineKeyboardButton(text=close, callback_data='f6_f3_f7')
        t8 = InlineKeyboardButton(text=close, callback_data='f6_f3_f8')
        t9 = InlineKeyboardButton(text=close, callback_data='f6_f3_f9')
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9)
        markup.add(back)
    else:
        if god_mode:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def f6_f3_f1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f3_f2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f3_f4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f3_f5(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s5 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f3_f7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f3_f8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f3_f9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.free_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='f6_f4_f1')
        t2 = InlineKeyboardButton(text=close, callback_data='f6_f4_f2')
        t3 = InlineKeyboardButton(text=close, callback_data='f6_f4_f3')
        t4 = InlineKeyboardButton(text=skip, callback_data='skip')
        t5 = InlineKeyboardButton(text=close, callback_data='f6_f4_f5')
        t6 = InlineKeyboardButton(text=skip, callback_data='skip')
        t7 = InlineKeyboardButton(text=close, callback_data='f6_f4_f7')
        t8 = InlineKeyboardButton(text=close, callback_data='f6_f4_f8')
        t9 = InlineKeyboardButton(text=close, callback_data='f6_f4_f9')
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9)
        markup.add(back)
    else:
        if god_mode:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def f6_f4_f1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f4_f2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f4_f3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f4_f5(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s5 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f4_f7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f4_f8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f4_f9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f5(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s5 == 0:
        text = options.free_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='f6_f5_f1')
        t2 = InlineKeyboardButton(text=close, callback_data='f6_f5_f2')
        t3 = InlineKeyboardButton(text=close, callback_data='f6_f5_f3')
        t4 = InlineKeyboardButton(text=close, callback_data='f6_f5_f4')
        t5 = InlineKeyboardButton(text=skip, callback_data='skip')
        t6 = InlineKeyboardButton(text=skip, callback_data='skip')
        t7 = InlineKeyboardButton(text=close, callback_data='f6_f5_f7')
        t8 = InlineKeyboardButton(text=close, callback_data='f6_f5_f8')
        t9 = InlineKeyboardButton(text=close, callback_data='f6_f5_f9')
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9)
        markup.add(back)
    else:
        if god_mode:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def f6_f5_f1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f5_f2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f5_f3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f5_f4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f5_f7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f5_f8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f5_f9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.free_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='f6_f7_f1')
        t2 = InlineKeyboardButton(text=close, callback_data='f6_f7_f2')
        t3 = InlineKeyboardButton(text=close, callback_data='f6_f7_f3')
        t4 = InlineKeyboardButton(text=close, callback_data='f6_f7_f4')
        t5 = InlineKeyboardButton(text=close, callback_data='f6_f7_f5')
        t6 = InlineKeyboardButton(text=skip, callback_data='skip')
        t7 = InlineKeyboardButton(text=skip, callback_data='skip')
        t8 = InlineKeyboardButton(text=close, callback_data='f6_f7_f8')
        t9 = InlineKeyboardButton(text=close, callback_data='f6_f7_f9')
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9)
        markup.add(back)
    else:
        if god_mode:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def f6_f7_f1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f7_f2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f7_f3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f7_f4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f7_f5(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s5 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f7_f8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f7_f9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.free_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='f6_f8_f1')
        t2 = InlineKeyboardButton(text=close, callback_data='f6_f8_f2')
        t3 = InlineKeyboardButton(text=close, callback_data='f6_f8_f3')
        t4 = InlineKeyboardButton(text=close, callback_data='f6_f8_f4')
        t5 = InlineKeyboardButton(text=close, callback_data='f6_f8_f5')
        t6 = InlineKeyboardButton(text=skip, callback_data='skip')
        t7 = InlineKeyboardButton(text=close, callback_data='f6_f8_f7')
        t8 = InlineKeyboardButton(text=skip, callback_data='skip')
        t9 = InlineKeyboardButton(text=close, callback_data='f6_f8_f9')
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9)
        markup.add(back)
    else:
        if god_mode:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def f6_f8_f1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f8_f2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f8_f3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f8_f4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f8_f5(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s5 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f8_f7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f8_f9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f9(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s9 == 0:
        text = options.free_3x3_step(user_id)
        t1 = InlineKeyboardButton(text=close, callback_data='f6_f9_f1')
        t2 = InlineKeyboardButton(text=close, callback_data='f6_f9_f2')
        t3 = InlineKeyboardButton(text=close, callback_data='f6_f9_f3')
        t4 = InlineKeyboardButton(text=close, callback_data='f6_f9_f4')
        t5 = InlineKeyboardButton(text=close, callback_data='f6_f9_f5')
        t6 = InlineKeyboardButton(text=skip, callback_data='skip')
        t7 = InlineKeyboardButton(text=close, callback_data='f6_f9_f7')
        t8 = InlineKeyboardButton(text=close, callback_data='f6_f9_f8')
        t9 = InlineKeyboardButton(text=skip, callback_data='skip')
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9)
        markup.add(back)
    else:
        if god_mode:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s9 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
        cn = 'game_free'
        cb = 'tg_mode'
        new_game = all_lang.button_new_game(user_id, cn)
        back = all_lang.button_back(user_id, cb)
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
        markup.add(back)

    return text, markup


def f6_f9_f1(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s1 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s1 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f9_f2(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s2 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s2 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f9_f3(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s3 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s3 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f9_f4(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s4 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s4 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f9_f5(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s5 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s5 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f9_f7(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s7 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s7 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup


def f6_f9_f8(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    god_mode = db.get_god_mode(user_id)
    markup = InlineKeyboardMarkup(row_width=3)
    if s8 == 0:
        text = options.free_3x3_lucky(user_id)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    else:
        if god_mode:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
            else:
                text = options.free_3x3_loss(user_id)
                t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish_god(user_id)
        else:
            if s8 == 1:
                text = options.free_3x3_loss(user_id)
            else:
                text = options.free_3x3_win(user_id)
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = free_3x3.finish(user_id)
    cn = 'game_free'
    cb = 'tg_mode'
    new_game = all_lang.button_new_game(user_id, cn)
    back = all_lang.button_back(user_id, cb)
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, new_game)
    markup.add(back)

    return text, markup
