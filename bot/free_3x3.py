from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import all_lang
import db
import options
from options import free_skip
from options import prize, bomb, skip, stop, close


def finish(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    if s1 == 0:
        t1 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s1 == 1:
        t1 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t1 = InlineKeyboardButton(text=prize, callback_data='done')
    if s2 == 0:
        t2 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s2 == 1:
        t2 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t2 = InlineKeyboardButton(text=prize, callback_data='done')
    if s3 == 0:
        t3 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s3 == 1:
        t3 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t3 = InlineKeyboardButton(text=prize, callback_data='done')
    if s4 == 0:
        t4 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s4 == 1:
        t4 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t4 = InlineKeyboardButton(text=prize, callback_data='done')
    if s5 == 0:
        t5 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s5 == 1:
        t5 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t5 = InlineKeyboardButton(text=prize, callback_data='done')
    if s6 == 0:
        t6 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s6 == 1:
        t6 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t6 = InlineKeyboardButton(text=prize, callback_data='done')
    if s7 == 0:
        t7 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s7 == 1:
        t7 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t7 = InlineKeyboardButton(text=prize, callback_data='done')
    if s8 == 0:
        t8 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s8 == 1:
        t8 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t8 = InlineKeyboardButton(text=prize, callback_data='done')
    if s9 == 0:
        t9 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s9 == 1:
        t9 = InlineKeyboardButton(text=bomb, callback_data='done')
    else:
        t9 = InlineKeyboardButton(text=prize, callback_data='done')
    return t1, t2, t3, t4, t5, t6, t7, t8, t9


def finish_god(user_id):
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = db.index_string_nine(user_id)
    if s1 == 0:
        t1 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s1 == 1:
        t1 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t1 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s2 == 0:
        t2 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s2 == 1:
        t2 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t2 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s3 == 0:
        t3 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s3 == 1:
        t3 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t3 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s4 == 0:
        t4 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s4 == 1:
        t4 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t4 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s5 == 0:
        t5 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s5 == 1:
        t5 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t5 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s6 == 0:
        t6 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s6 == 1:
        t6 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t6 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s7 == 0:
        t7 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s7 == 1:
        t7 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t7 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s8 == 0:
        t8 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s8 == 1:
        t8 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t8 = InlineKeyboardButton(text=bomb, callback_data='done')
    if s9 == 0:
        t9 = InlineKeyboardButton(text=skip, callback_data='done')
    elif s9 == 1:
        t9 = InlineKeyboardButton(text=prize, callback_data='done')
    else:
        t9 = InlineKeyboardButton(text=bomb, callback_data='done')
    return t1, t2, t3, t4, t5, t6, t7, t8, t9


def game(user_id):
    save = db.get_save(user_id)
    free_game = db.get_free_game(user_id)
    res = db.get_res(user_id)
    if save == "game_free":
        count = free_game
    else:
        count = int(res // free_skip)
    if count < 0:
        count = 0
    text = options.game_start(user_id, count)
    cb = 'tg_mode'
    back = all_lang.button_back(user_id, cb)
    markup = InlineKeyboardMarkup(row_width=3)
    t1 = InlineKeyboardButton(text=close, callback_data='f1')
    t2 = InlineKeyboardButton(text=close, callback_data='f2')
    t3 = InlineKeyboardButton(text=close, callback_data='f3')
    t4 = InlineKeyboardButton(text=close, callback_data='f4')
    t5 = InlineKeyboardButton(text=close, callback_data='f5')
    t6 = InlineKeyboardButton(text=close, callback_data='f6')
    t7 = InlineKeyboardButton(text=close, callback_data='f7')
    t8 = InlineKeyboardButton(text=close, callback_data='f8')
    t9 = InlineKeyboardButton(text=close, callback_data='f9')
    markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    markup.add(back)
    return text, markup
