# import all_lang
import db

prize = '💎'
bomb = '🔥'
skip = '👻'
stop = ' '
close = '⭐'


def game_win(user_id, count):
    language = db.get_language(user_id)
    if language == "ru":
        text_win = f"Игры: <b>{count}</b>\n\nПоздравляю вас! Ты попал в алмаз 💎"
    elif language == "id":
        text_win = f"Permainan: <b>{count}</b>\n\nCongratulations, you hit the diamond 💎"
    elif language == "es":
        text_win = f"Juegos: <b>{count}</b>\n\nCongratulations, you hit the diamond 💎"
    elif language == "ko":
        text_win = f"계략: <b>{count}</b>\n\nCongratulations, you hit the diamond 💎"
    elif language == "it":
        text_win = f"Giochi: <b>{count}</b>\n\nCongratulations, you hit the diamond 💎"
    elif language == "ch":
        text_win = f"遊戲：<b>{count}</b>\n\nCongratulations, you hit the diamond 💎"
    elif language == "ta":
        text_win = f"游戏：<b>{count}</b>\n\nCongratulations, you hit the diamond 💎"
    elif language == "fa":
        text_win = f"بازی ها: <b>{count}</b>\n\nCongratulations, you hit the diamond 💎"
    elif language == "tr":
        text_win = f"Oyunlar: <b>{count}</b>\n\nCongratulations, you hit the diamond 💎"
    elif language == "uz":
        text_win = f"Oʻyinlar: <b>{count}</b>\n\nПоздравляю вас! Ты попал в алмаз 💎"
    elif language == "be":
        text_win = f"গেম: <b>{count}</b>\n\nCongratulations, you hit the diamond 💎"
    elif language == "hi":
        text_win = f"खेल: <b>{count}</b>\n\nCongratulations, you hit the diamond 💎"
    else:
        text_win = f"Games: <b>{count}</b>\n\nCongratulations, you hit the diamond 💎"
    return text_win


def game_loss(user_id, count):
    language = db.get_language(user_id)
    if language == "ru":
        text_loss = f"Игры: <b>{count}</b>\n\nЭх... Ты попал в 🔥, попробуй ещё раз!"
    elif language == "id":
        text_loss = f"Permainan: <b>{count}</b>\n\nOh... You hit the fire 🔥, try playing again!"
    elif language == "es":
        text_loss = f"Juegos: <b>{count}</b>\n\nOh... You hit the fire 🔥, try playing again!"
    elif language == "ko":
        text_loss = f"계략: <b>{count}</b>\n\nOh... You hit the fire 🔥, try playing again!"
    elif language == "it":
        text_loss = f"Giochi: <b>{count}</b>\n\nOh... You hit the fire 🔥, try playing again!"
    elif language == "ch":
        text_loss = f"遊戲：<b>{count}</b>\n\nOh... You hit the fire 🔥, try playing again!"
    elif language == "ta":
        text_loss = f"游戏：<b>{count}</b>\n\nOh... You hit the fire 🔥, try playing again!"
    elif language == "fa":
        text_loss = f"بازی ها: <b>{count}</b>\n\nOh... You hit the fire 🔥, try playing again!"
    elif language == "tr":
        text_loss = f"Oyunlar: <b>{count}</b>\n\nOh... You hit the fire 🔥, try playing again!"
    elif language == "uz":
        text_loss = f"Oʻyinlar: <b>{count}</b>\n\nЭх... Ты попал в 🔥, попробуй ещё раз!"
    elif language == "be":
        text_loss = f"গেম: <b>{count}</b>\n\nOh... You hit the fire 🔥, try playing again!"
    elif language == "hi":
        text_loss = f"खेल: <b>{count}</b>\n\nOh... You hit the fire 🔥, try playing again!"
    else:
        text_loss = f"Games: <b>{count}</b>\n\nOh... You hit the fire 🔥, try playing again!"
    return text_loss


def game_step(user_id, count):
    language = db.get_language(user_id)
    if language == "ru":
        text_step = f"Игры: <b>{count}</b>\n\nАх... Ты попал в 👻, продолжай дальше"
    elif language == "id":
        text_step = f"Permainan: <b>{count}</b>\n\nOpss... You hit the ghost 👻, keep going!"
    elif language == "es":
        text_step = f"Juegos: <b>{count}</b>\n\nOpss... You hit the ghost 👻, keep going!"
    elif language == "ko":
        text_step = f"계략: <b>{count}</b>\n\nOpss... You hit the ghost 👻, keep going!"
    elif language == "it":
        text_step = f"Giochi: <b>{count}</b>\n\nOpss... You hit the ghost 👻, keep going!"
    elif language == "ch":
        text_step = f"遊戲：<b>{count}</b>\n\nOpss... You hit the ghost 👻, keep going!"
    elif language == "ta":
        text_step = f"游戏：<b>{count}</b>\n\nOpss... You hit the ghost 👻, keep going!"
    elif language == "fa":
        text_step = f"بازی ها: <b>{count}</b>\n\nOpss... You hit the ghost 👻, keep going!"
    elif language == "tr":
        text_step = f"Oyunlar: <b>{count}</b>\n\nOpss... You hit the ghost 👻, keep going!"
    elif language == "uz":
        text_step = f"Oʻyinlar: <b>{count}</b>\n\nАх... Ты попал в 👻, продолжай дальше"
    elif language == "be":
        text_step = f"গেম: <b>{count}</b>\n\nOpss... You hit the ghost 👻, keep going!"
    elif language == "hi":
        text_step = f"खेल: <b>{count}</b>\n\nOpss... You hit the ghost 👻, keep going!"
    else:
        text_step = f"Games: <b>{count}</b>\n\nOpss... You hit the ghost 👻, keep going!"
    return text_step


def game_lucky(user_id, count):
    language = db.get_language(user_id)
    if language == "ru":
        text_lucky = f"Игры: <b>{count}</b>\n\nМолодец, ты выбил всех призраков 👻"
    elif language == "id":
        text_lucky = f"Permainan: <b>{count}</b>\n\nWell done, you knocked out all the 👻x3"
    elif language == "es":
        text_lucky = f"Juegos: <b>{count}</b>\n\nWell done, you knocked out all the 👻x3"
    elif language == "ko":
        text_lucky = f"계략: <b>{count}</b>\n\nWell done, you knocked out all the 👻x3"
    elif language == "it":
        text_lucky = f"Giochi: <b>{count}</b>\n\nWell done, you knocked out all the 👻x3"
    elif language == "ch":
        text_lucky = f"遊戲：<b>{count}</b>\n\nWell done, you knocked out all the 👻x3"
    elif language == "ta":
        text_lucky = f"游戏：<b>{count}</b>\n\nWell done, you knocked out all the 👻x3"
    elif language == "fa":
        text_lucky = f"بازی ها: <b>{count}</b>\n\nWell done, you knocked out all the 👻x3"
    elif language == "tr":
        text_lucky = f"Oyunlar: <b>{count}</b>\n\nWell done, you knocked out all the 👻x3"
    elif language == "uz":
        text_lucky = f"Oʻyinlar: <b>{count}</b>\n\nМолодец, ты выбил всех призраков 👻"
    elif language == "be":
        text_lucky = f"গেম: <b>{count}</b>\n\nWell done, you knocked out all the 👻x3"
    elif language == "hi":
        text_lucky = f"खेल: <b>{count}</b>\n\nWell done, you knocked out all the 👻x3"
    else:
        text_lucky = f"Games: <b>{count}</b>\n\nWell done, you knocked out all the 👻x3"
    return text_lucky


def game_empty(user_id, count):
    language = db.get_language(user_id)
    if language == "ru":
        text_empty = f"Игры: <b>{count}</b>\n\nНам очень жаль! Ты попал в пустоту 💭"
    elif language == "id":
        text_empty = f"Permainan: <b>{count}</b>\n\nWe are very sorry! you are in the void 💭"
    elif language == "es":
        text_empty = f"Juegos: <b>{count}</b>\n\nWe are very sorry! you are in the void 💭"
    elif language == "ko":
        text_empty = f"계략: <b>{count}</b>\n\nWe are very sorry! you are in the void 💭"
    elif language == "it":
        text_empty = f"Giochi: <b>{count}</b>\n\nWe are very sorry! you are in the void 💭"
    elif language == "ch":
        text_empty = f"遊戲：<b>{count}</b>\n\nWe are very sorry! you are in the void 💭"
    elif language == "ta":
        text_empty = f"游戏：<b>{count}</b>\n\nWe are very sorry! you are in the void 💭"
    elif language == "fa":
        text_empty = f"بازی ها: <b>{count}</b>\n\nWe are very sorry! you are in the void 💭"
    elif language == "tr":
        text_empty = f"Oyunlar: <b>{count}</b>\n\nWe are very sorry! you are in the void 💭"
    elif language == "uz":
        text_empty = f"Oʻyinlar: <b>{count}</b>\n\nНам очень жаль! Ты попал в пустоту 💭"
    elif language == "be":
        text_empty = f"গেম: <b>{count}</b>\n\nWe are very sorry! you are in the void 💭"
    elif language == "hi":
        text_empty = f"खेल: <b>{count}</b>\n\nWe are very sorry! you are in the void 💭"
    else:
        text_empty = f"Games: <b>{count}</b>\n\nWe are very sorry! you are in the void 💭"
    return text_empty


def game_start(user_id, count):
    language = db.get_language(user_id)
    if language == "ru":
        text_empty = f"Игры: <b>{count}</b>\n\nПопробуй определить, где спрятан 💎"
    elif language == "id":
        text_empty = f"Permainan: <b>{count}</b>\n\nTry to determine where it is diamond 💎"
    elif language == "es":
        text_empty = f"Juegos: <b>{count}</b>\n\nTry to determine where it is diamond 💎"
    elif language == "ko":
        text_empty = f"계략: <b>{count}</b>\n\nTry to determine where it is diamond 💎"
    elif language == "it":
        text_empty = f"Giochi: <b>{count}</b>\n\nTry to determine where it is diamond 💎"
    elif language == "ch":
        text_empty = f"遊戲：<b>{count}</b>\n\nTry to determine where it is diamond 💎"
    elif language == "ta":
        text_empty = f"游戏：<b>{count}</b>\n\nTry to determine where it is diamond 💎"
    elif language == "fa":
        text_empty = f"بازی ها: <b>{count}</b>\n\nTry to determine where it is diamond 💎"
    elif language == "tr":
        text_empty = f"Oyunlar: <b>{count}</b>\n\nTry to determine where it is diamond 💎"
    elif language == "uz":
        text_empty = f"Oʻyinlar: <b>{count}</b>\n\nПопробуй определить, где спрятан 💎"
    elif language == "be":
        text_empty = f"গেম: <b>{count}</b>\n\nTry to determine where it is diamond 💎"
    elif language == "hi":
        text_empty = f"खेल: <b>{count}</b>\n\nTry to determine where it is diamond 💎"
    else:
        text_empty = f"Games: <b>{count}</b>\n\nTry to determine where it is diamond 💎"
    return text_empty


# FREE GAME OR RESERVE
free_win = 5
free_loss = 3
free_lucky = 3
free_skip = 1

# RUB
# 2x2
f_base_2x2_win = 100
f_bronze_2x2_win = 200
f_silver_2x2_win = 600
f_gold_2x2_win = 2000
f_vip_2x2_win = 20000

f_base_2x2_loss = 60
f_bronze_2x2_loss = 120
f_silver_2x2_loss = 360
f_gold_2x2_loss = 1200
f_vip_2x2_loss = 12000

f_base_2x2_stop = 20
f_bronze_2x2_stop = 40
f_silver_2x2_stop = 120
f_gold_2x2_stop = 400
f_vip_2x2_stop = 4000

f_base_2x2_step = 20
f_bronze_2x2_step = 40
f_silver_2x2_step = 120
f_gold_2x2_step = 400
f_vip_2x2_step = 4000

# f_base_2x2_step = 1.5
# f_bronze_2x2_step = 3
# f_silver_2x2_step = 10
# f_gold_2x2_step = 30
# f_vip_2x2_step = 300
#
# f_base_2x2_step = 1
# f_bronze_2x2_step = 2
# f_silver_2x2_step = 8
# f_gold_2x2_step = 20
# f_vip_2x2_step = 200

# 2x3
f_base_2x3_win = 150
f_bronze_2x3_win = 400
f_silver_2x3_win = 1250
f_gold_2x3_win = 4000
f_vip_2x3_win = 40000

f_base_2x3_loss = 90
f_bronze_2x3_loss = 240
f_silver_2x3_loss = 750
f_gold_2x3_loss = 2400
f_vip_2x3_loss = 24000

f_base_2x3_step = 30
f_bronze_2x3_step = 80
f_silver_2x3_step = 250
f_gold_2x3_step = 800
f_vip_2x3_step = 8000

# f_base_2x3_step = 2
# f_bronze_2x3_step = 7
# f_silver_2x3_step = 20
# f_gold_2x3_step = 70
# f_vip_2x3_step = 700
#
# f_base_2x3_step = 1
# f_bronze_2x3_step = 6
# f_silver_2x3_step = 15
# f_gold_2x3_step = 60
# f_vip_2x3_step = 600

# 3x3
f_base_3x3_win = 150
f_bronze_3x3_win = 400
f_silver_3x3_win = 1250
f_gold_3x3_win = 4000
f_vip_3x3_win = 40000

f_base_3x3_loss = 90
f_bronze_3x3_loss = 240
f_silver_3x3_loss = 750
f_gold_3x3_loss = 2400
f_vip_3x3_loss = 24000

f_base_3x3_lucky = 90
f_bronze_3x3_lucky = 240
f_silver_3x3_lucky = 750
f_gold_3x3_lucky = 2400
f_vip_3x3_lucky = 24000

f_base_3x3_step = 30
f_bronze_3x3_step = 80
f_silver_3x3_step = 250
f_gold_3x3_step = 800
f_vip_3x3_step = 8000

# f_base_3x3_step = 2
# f_bronze_3x3_step = 7
# f_silver_3x3_step = 20
# f_gold_3x3_step = 70
# f_vip_3x3_step = 700
#
# f_base_3x3_step = 1
# f_bronze_3x3_step = 6
# f_silver_3x3_step = 15
# f_gold_3x3_step = 60
# f_vip_3x3_step = 600

# 3x3 risk
f_base_four_win = 240
f_bronze_four_win = 640
f_silver_four_win = 2000
f_gold_four_win = 6400
f_vip_four_win = 64000

f_base_four_loss = 30
f_bronze_four_loss = 80
f_silver_four_loss = 250
f_gold_four_loss = 800
f_vip_four_loss = 8000

# 4x4
f_base_six_win = 450
f_bronze_six_win = 1200
f_silver_six_win = 3750
f_gold_six_win = 12000
f_vip_six_win = 120000

f_base_six_loss = 30
f_bronze_six_loss = 80
f_silver_six_loss = 250
f_gold_six_loss = 800
f_vip_six_loss = 8000

# 5x5
f_base_nine_win = 720
f_bronze_nine_win = 1920
f_silver_nine_win = 6000
f_gold_nine_win = 19200
f_vip_nine_win = 192000

f_base_nine_loss = 30
f_bronze_nine_loss = 80
f_silver_nine_loss = 250
f_gold_nine_loss = 800
f_vip_nine_loss = 8000

# -----------------------------------------------------------------------------------------------------

# ILS
s_base_2x2_win = 150
s_bronze_2x2_win = 450
s_silver_2x2_win = 1500
s_gold_2x2_win = 4500
s_vip_2x2_win = 45000

s_base_2x2_loss = 75
s_bronze_2x2_loss = 225
s_silver_2x2_loss = 750
s_gold_2x2_loss = 2250
s_vip_2x2_loss = 22500

s_base_2x2_stop = 25
s_bronze_2x2_stop = 75
s_silver_2x2_stop = 250
s_gold_2x2_stop = 750
s_vip_2x2_stop = 7500

s_base_2x2_step = 25
s_bronze_2x2_step = 75
s_silver_2x2_step = 250
s_gold_2x2_step = 750
s_vip_2x2_step = 7500

# s_base_2x2_step = 2
# s_bronze_2x2_step = 6
# s_silver_2x2_step = 20
# s_gold_2x2_step = 60
# s_vip_2x2_step = 600
#
# s_base_2x2_step = 1.5
# s_bronze_2x2_step = 4.5
# s_silver_2x2_step = 15
# s_gold_2x2_step = 45
# s_vip_2x2_step = 450

# 2x3
s_base_2x3_win = 250
s_bronze_2x3_win = 625
s_silver_2x3_win = 1875
s_gold_2x3_win = 6250
s_vip_2x3_win = 62500

s_base_2x3_loss = 150
s_bronze_2x3_loss = 375
s_silver_2x3_loss = 1125
s_gold_2x3_loss = 3750
s_vip_2x3_loss = 37500

s_base_2x3_step = 50
s_bronze_2x3_step = 125
s_silver_2x3_step = 375
s_gold_2x3_step = 1250
s_vip_2x3_step = 12500

# s_base_2x3_step = 4
# s_bronze_2x3_step = 10
# s_silver_2x3_step = 30
# s_gold_2x3_step = 100
# s_vip_2x3_step = 1000
#
# s_base_2x3_step = 3
# s_bronze_2x3_step = 7.5
# s_silver_2x3_step = 22.5
# s_gold_2x3_step = 75
# s_vip_2x3_step = 750

# 3x3
s_base_3x3_win = 250
s_bronze_3x3_win = 625
s_silver_3x3_win = 1875
s_gold_3x3_win = 6250
s_vip_3x3_win = 62500

s_base_3x3_loss = 150
s_bronze_3x3_loss = 375
s_silver_3x3_loss = 1125
s_gold_3x3_loss = 3750
s_vip_3x3_loss = 37500

s_base_3x3_lucky = 150
s_bronze_3x3_lucky = 375
s_silver_3x3_lucky = 1125
s_gold_3x3_lucky = 3750
s_vip_3x3_lucky = 37500

s_base_3x3_step = 50
s_bronze_3x3_step = 125
s_silver_3x3_step = 375
s_gold_3x3_step = 1250
s_vip_3x3_step = 12500

# s_base_3x3_step = 4
# s_bronze_3x3_step = 10
# s_silver_3x3_step = 30
# s_gold_3x3_step = 100
# s_vip_3x3_step = 1000
#
# s_base_3x3_step = 3
# s_bronze_3x3_step = 7.5
# s_silver_3x3_step = 22.5
# s_gold_3x3_step = 75
# s_vip_3x3_step = 750

# 3x3 risk
s_base_four_win = 400
s_bronze_four_win = 1000
s_silver_four_win = 3000
s_gold_four_win = 10000
s_vip_four_win = 100000

s_base_four_loss = 50
s_bronze_four_loss = 125
s_silver_four_loss = 375
s_gold_four_loss = 1250
s_vip_four_loss = 12500

# 4x4
s_base_six_win = 750
s_bronze_six_win = 1875
s_silver_six_win = 5625
s_gold_six_win = 18750
s_vip_six_win = 187500

s_base_six_loss = 50
s_bronze_six_loss = 125
s_silver_six_loss = 375
s_gold_six_loss = 1250
s_vip_six_loss = 12500

# 5x5
s_base_nine_win = 1200
s_bronze_nine_win = 3000
s_silver_nine_win = 9000
s_gold_nine_win = 30000
s_vip_nine_win = 300000

s_base_nine_loss = 50
s_bronze_nine_loss = 125
s_silver_nine_loss = 375
s_gold_nine_loss = 1250
s_vip_nine_loss = 12500

# -----------------------------------------------------------------------------------------------------

# EGP
t_base_2x2_win = 60
t_bronze_2x2_win = 90
t_silver_2x2_win = 300
t_gold_2x2_win = 900
t_vip_2x2_win = 9000

t_base_2x2_loss = 30
t_bronze_2x2_loss = 45
t_silver_2x2_loss = 150
t_gold_2x2_loss = 450
t_vip_2x2_loss = 4500

t_base_2x2_stop = 10
t_bronze_2x2_stop = 15
t_silver_2x2_stop = 50
t_gold_2x2_stop = 150
t_vip_2x2_stop = 1500

t_base_2x2_step = 10
t_bronze_2x2_step = 15
t_silver_2x2_step = 50
t_gold_2x2_step = 150
t_vip_2x2_step = 1500

# t_base_2x2_step = 1
# t_bronze_2x2_step = 1.2
# t_silver_2x2_step = 4
# t_gold_2x2_step = 12
# t_vip_2x2_step = 120
#
# t_base_2x2_step = 1
# t_bronze_2x2_step = 1
# t_silver_2x2_step = 3
# t_gold_2x2_step = 9
# t_vip_2x2_step = 90

# 2x3
t_base_2x3_win = 50
t_bronze_2x3_win = 125
t_silver_2x3_win = 375
t_gold_2x3_win = 1250
t_vip_2x3_win = 12500

t_base_2x3_loss = 30
t_bronze_2x3_loss = 75
t_silver_2x3_loss = 225
t_gold_2x3_loss = 750
t_vip_2x3_loss = 7500

t_base_2x3_step = 10
t_bronze_2x3_step = 25
t_silver_2x3_step = 75
t_gold_2x3_step = 250
t_vip_2x3_step = 2500

# t_base_2x3_step = 1
# t_bronze_2x3_step = 2
# t_silver_2x3_step = 6
# t_gold_2x3_step = 20
# t_vip_2x3_step = 200
#
# t_base_2x3_step = 1
# t_bronze_2x3_step = 1.5
# t_silver_2x3_step = 4.5
# t_gold_2x3_step = 15
# t_vip_2x3_step = 150

# 3x3
t_base_3x3_win = 50
t_bronze_3x3_win = 125
t_silver_3x3_win = 375
t_gold_3x3_win = 1250
t_vip_3x3_win = 12500

t_base_3x3_loss = 30
t_bronze_3x3_loss = 75
t_silver_3x3_loss = 225
t_gold_3x3_loss = 750
t_vip_3x3_loss = 7500

t_base_3x3_lucky = 30
t_bronze_3x3_lucky = 75
t_silver_3x3_lucky = 225
t_gold_3x3_lucky = 750
t_vip_3x3_lucky = 7500

t_base_3x3_step = 10
t_bronze_3x3_step = 25
t_silver_3x3_step = 75
t_gold_3x3_step = 250
t_vip_3x3_step = 2500

# t_base_3x3_step = 1
# t_bronze_3x3_step = 2
# t_silver_3x3_step = 6
# t_gold_3x3_step = 20
# t_vip_3x3_step = 200
#
# t_base_3x3_step = 1
# t_bronze_3x3_step = 1.5
# t_silver_3x3_step = 4.5
# t_gold_3x3_step = 15
# t_vip_3x3_step = 150

# 3x3 risk
t_base_four_win = 80
t_bronze_four_win = 200
t_silver_four_win = 600
t_gold_four_win = 2000
t_vip_four_win = 20000

t_base_four_loss = 10
t_bronze_four_loss = 25
t_silver_four_loss = 75
t_gold_four_loss = 250
t_vip_four_loss = 2500

# 4x4
t_base_six_win = 150
t_bronze_six_win = 375
t_silver_six_win = 1125
t_gold_six_win = 3750
t_vip_six_win = 37500

t_base_six_loss = 10
t_bronze_six_loss = 25
t_silver_six_loss = 75
t_gold_six_loss = 250
t_vip_six_loss = 2500

# 5x5
t_base_nine_win = 240
t_bronze_nine_win = 600
t_silver_nine_win = 1800
t_gold_nine_win = 6000
t_vip_nine_win = 60000

t_base_nine_loss = 10
t_bronze_nine_loss = 25
t_silver_nine_loss = 75
t_gold_nine_loss = 250
t_vip_nine_loss = 2500

# -----------------------------------------------------------------------------------------------------

# USD
fo_base_2x2_win = 300
fo_bronze_2x2_win = 900
fo_silver_2x2_win = 3000
fo_gold_2x2_win = 9000
fo_vip_2x2_win = 90000

fo_base_2x2_loss = 150
fo_bronze_2x2_loss = 450
fo_silver_2x2_loss = 1500
fo_gold_2x2_loss = 4500
fo_vip_2x2_loss = 45000

fo_base_2x2_stop = 50
fo_bronze_2x2_stop = 150
fo_silver_2x2_stop = 500
fo_gold_2x2_stop = 1500
fo_vip_2x2_stop = 15000

fo_base_2x2_step = 50
fo_bronze_2x2_step = 150
fo_silver_2x2_step = 500
fo_gold_2x2_step = 1500
fo_vip_2x2_step = 15000

# fo_base_2x2_step = 4
# fo_bronze_2x2_step = 12
# fo_silver_2x2_step = 40
# fo_gold_2x2_step = 120
# fo_vip_2x2_step = 1200
#
# fo_base_2x2_step = 3
# fo_bronze_2x2_step = 9
# fo_silver_2x2_step = 30
# fo_gold_2x2_step = 90
# fo_vip_2x2_step = 900

# 2x3
fo_base_2x3_win = 500
fo_bronze_2x3_win = 1250
fo_silver_2x3_win = 3750
fo_gold_2x3_win = 12500
fo_vip_2x3_win = 125000

fo_base_2x3_loss = 300
fo_bronze_2x3_loss = 750
fo_silver_2x3_loss = 2250
fo_gold_2x3_loss = 7500
fo_vip_2x3_loss = 75000

fo_base_2x3_step = 100
fo_bronze_2x3_step = 250
fo_silver_2x3_step = 750
fo_gold_2x3_step = 2500
fo_vip_2x3_step = 25000

# fo_base_2x3_step = 8
# fo_bronze_2x3_step = 20
# fo_silver_2x3_step = 60
# fo_gold_2x3_step = 200
# fo_vip_2x3_step = 2000
#
# fo_base_2x3_step = 6
# fo_bronze_2x3_step = 15
# fo_silver_2x3_step = 45
# fo_gold_2x3_step = 150
# fo_vip_2x3_step = 1500

# 3x3
fo_base_3x3_win = 500
fo_bronze_3x3_win = 1250
fo_silver_3x3_win = 3750
fo_gold_3x3_win = 12500
fo_vip_3x3_win = 125000

fo_base_3x3_loss = 300
fo_bronze_3x3_loss = 750
fo_silver_3x3_loss = 2250
fo_gold_3x3_loss = 7500
fo_vip_3x3_loss = 75000

fo_base_3x3_lucky = 300
fo_bronze_3x3_lucky = 750
fo_silver_3x3_lucky = 2250
fo_gold_3x3_lucky = 7500
fo_vip_3x3_lucky = 75000

fo_base_3x3_step = 100
fo_bronze_3x3_step = 250
fo_silver_3x3_step = 750
fo_gold_3x3_step = 2500
fo_vip_3x3_step = 25000

# fo_base_3x3_step = 8
# fo_bronze_3x3_step = 20
# fo_silver_3x3_step = 60
# fo_gold_3x3_step = 200
# fo_vip_3x3_step = 2000
#
# fo_base_3x3_step = 6
# fo_bronze_3x3_step = 15
# fo_silver_3x3_step = 45
# fo_gold_3x3_step = 150
# fo_vip_3x3_step = 1500

# 3x3 risk
fo_base_four_win = 800
fo_bronze_four_win = 2000
fo_silver_four_win = 6000
fo_gold_four_win = 20000
fo_vip_four_win = 200000

fo_base_four_loss = 100
fo_bronze_four_loss = 250
fo_silver_four_loss = 750
fo_gold_four_loss = 2500
fo_vip_four_loss = 25000

# 4x4
fo_base_six_win = 1500
fo_bronze_six_win = 3750
fo_silver_six_win = 11250
fo_gold_six_win = 37500
fo_vip_six_win = 375000

fo_base_six_loss = 100
fo_bronze_six_loss = 250
fo_silver_six_loss = 750
fo_gold_six_loss = 2500
fo_vip_six_loss = 25000

# 5x5
fo_base_nine_win = 2400
fo_bronze_nine_win = 6000
fo_silver_nine_win = 18000
fo_gold_nine_win = 60000
fo_vip_nine_win = 600000

fo_base_nine_loss = 100
fo_bronze_nine_loss = 250
fo_silver_nine_loss = 750
fo_gold_nine_loss = 2500
fo_vip_nine_loss = 25000


def norm_2x2_win(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_bronze_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_bronze_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_bronze_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_bronze_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_bronze_2x2_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_silver_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_silver_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_silver_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_silver_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_silver_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_silver_2x2_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_gold_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_gold_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_gold_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_gold_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_gold_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_gold_2x2_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_vip_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_vip_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_vip_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_vip_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_vip_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_vip_2x2_win
            balance = db.new_balance_plus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_base_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_base_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_base_2x2_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_base_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_base_2x2_win
            balance = db.new_balance_plus(user_id, ba)

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
    text = game_win(user_id, count)
    return text


def norm_2x2_loss(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_bronze_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_bronze_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_bronze_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_bronze_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_bronze_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_silver_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_silver_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_silver_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_silver_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_silver_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_silver_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_gold_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_gold_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_gold_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_gold_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_gold_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_gold_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_vip_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_vip_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_vip_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_vip_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_vip_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_vip_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_base_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_base_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_base_2x2_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_base_2x2_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_base_2x2_loss
            balance = db.new_balance_minus(user_id, ba)

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
    text = game_loss(user_id, count)
    return text


def norm_2x2_stop(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_bronze_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_silver_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_silver_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_gold_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_gold_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_vip_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_vip_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_2x2_stop
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_base_2x2_stop
            balance = db.new_balance_minus(user_id, ba)

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
    text = game_empty(user_id, count)
    return text


def norm_2x2_step(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_bronze_2x2_step
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_silver_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_silver_2x2_step
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_gold_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_gold_2x2_step
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_vip_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_vip_2x2_step
            balance = db.new_balance_minus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_2x2_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_base_2x2_step
            balance = db.new_balance_minus(user_id, ba)

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
    text = game_step(user_id, count)
    return text


def norm_2x3_win(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_bronze_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_bronze_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_bronze_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_bronze_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_bronze_2x3_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_silver_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_silver_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_silver_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_silver_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_silver_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_silver_2x3_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_gold_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_gold_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_gold_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_gold_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_gold_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_gold_2x3_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_vip_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_vip_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_vip_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_vip_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_vip_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_vip_2x3_win
            balance = db.new_balance_plus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_base_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_base_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_base_2x3_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_base_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_base_2x3_win
            balance = db.new_balance_plus(user_id, ba)

    if save == "game_base_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_2x3_step)
        else:
            count = int(balance // fo_base_2x3_step)
    elif save == "game_bronze_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_2x3_step)
        else:
            count = int(balance // fo_bronze_2x3_step)
    elif save == "game_silver_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_2x3_step)
        else:
            count = int(balance // fo_silver_2x3_step)
    elif save == "game_gold_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_2x3_step)
        else:
            count = int(balance // fo_gold_2x3_step)
    else:
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
    text = game_win(user_id, count)
    return text


def norm_2x3_loss(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_bronze_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_bronze_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_bronze_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_bronze_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_bronze_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_silver_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_silver_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_silver_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_silver_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_silver_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_silver_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_gold_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_gold_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_gold_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_gold_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_gold_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_gold_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_vip_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_vip_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_vip_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_vip_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_vip_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_vip_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_base_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_base_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_base_2x3_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_base_2x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_base_2x3_loss
            balance = db.new_balance_minus(user_id, ba)

    if save == "game_base_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_2x3_step)
        else:
            count = int(balance // fo_base_2x3_step)
    elif save == "game_bronze_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_2x3_step)
        else:
            count = int(balance // fo_bronze_2x3_step)
    elif save == "game_silver_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_2x3_step)
        else:
            count = int(balance // fo_silver_2x3_step)
    elif save == "game_gold_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_2x3_step)
        else:
            count = int(balance // fo_gold_2x3_step)
    else:
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
    text = game_loss(user_id, count)
    return text


def norm_2x3_step(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_bronze_2x3_step
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_silver_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_silver_2x3_step
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_gold_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_gold_2x3_step
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_vip_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_vip_2x3_step
            balance = db.new_balance_minus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_2x3_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_base_2x3_step
            balance = db.new_balance_minus(user_id, ba)

    if save == "game_base_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_2x3_step)
        else:
            count = int(balance // fo_base_2x3_step)
    elif save == "game_bronze_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_2x3_step)
        else:
            count = int(balance // fo_bronze_2x3_step)
    elif save == "game_silver_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_2x3_step)
        else:
            count = int(balance // fo_silver_2x3_step)
    elif save == "game_gold_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_2x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_2x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_2x3_step)
        else:
            count = int(balance // fo_gold_2x3_step)
    else:
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
    text = game_step(user_id, count)
    return text


def norm_3x3_win(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_bronze_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_bronze_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_bronze_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_bronze_3x3_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_silver_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_silver_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_silver_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_silver_3x3_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_gold_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_gold_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_gold_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_gold_3x3_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_vip_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_vip_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_vip_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_vip_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_vip_3x3_win
            balance = db.new_balance_plus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_base_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_base_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_base_3x3_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_base_3x3_win
            balance = db.new_balance_plus(user_id, ba)

    if save == "game_base_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_3x3_step)
        else:
            count = int(balance // fo_base_3x3_step)
    elif save == "game_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_3x3_step)
        else:
            count = int(balance // fo_bronze_3x3_step)
    elif save == "game_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_3x3_step)
        else:
            count = int(balance // fo_silver_3x3_step)
    elif save == "game_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_3x3_step)
        else:
            count = int(balance // fo_gold_3x3_step)
    else:
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
    text = game_win(user_id, count)
    return text


def norm_3x3_loss(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_bronze_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_bronze_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_bronze_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_bronze_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_silver_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_silver_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_silver_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_silver_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_gold_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_gold_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_gold_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_gold_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_vip_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_vip_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_vip_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_vip_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_vip_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_base_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_base_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_base_3x3_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_base_3x3_loss
            balance = db.new_balance_minus(user_id, ba)

    if save == "game_base_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_3x3_step)
        else:
            count = int(balance // fo_base_3x3_step)
    elif save == "game_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_3x3_step)
        else:
            count = int(balance // fo_bronze_3x3_step)
    elif save == "game_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_3x3_step)
        else:
            count = int(balance // fo_silver_3x3_step)
    elif save == "game_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_3x3_step)
        else:
            count = int(balance // fo_gold_3x3_step)
    else:
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
    text = game_loss(user_id, count)
    return text


def norm_3x3_lucky(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_bronze_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_bronze_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_bronze_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_bronze_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_silver_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_silver_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_silver_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_silver_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_gold_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_gold_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_gold_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_gold_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_vip_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_vip_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_vip_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_vip_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_vip_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = f_base_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = s_base_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = t_base_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_base_3x3_lucky
            balance = db.new_balance_plus(user_id, ba)

    if save == "game_base_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_3x3_step)
        else:
            count = int(balance // fo_base_3x3_step)
    elif save == "game_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_3x3_step)
        else:
            count = int(balance // fo_bronze_3x3_step)
    elif save == "game_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_3x3_step)
        else:
            count = int(balance // fo_silver_3x3_step)
    elif save == "game_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_3x3_step)
        else:
            count = int(balance // fo_gold_3x3_step)
    else:
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
    text = game_lucky(user_id, count)
    return text


def norm_3x3_step(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_bronze_3x3_step
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_silver_3x3_step
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_gold_3x3_step
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_vip_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_vip_3x3_step
            balance = db.new_balance_minus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_base_3x3_step
            balance = db.new_balance_minus(user_id, ba)

    if save == "game_base_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_base_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_base_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_base_3x3_step)
        else:
            count = int(balance // fo_base_3x3_step)
    elif save == "game_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_bronze_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_bronze_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_bronze_3x3_step)
        else:
            count = int(balance // fo_bronze_3x3_step)
    elif save == "game_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_silver_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_silver_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_silver_3x3_step)
        else:
            count = int(balance // fo_silver_3x3_step)
    elif save == "game_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            count = int(balance // f_gold_3x3_step)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            count = int(balance // s_gold_3x3_step)
        elif currency == "EGP" or currency == "INR":
            count = int(balance // t_gold_3x3_step)
        else:
            count = int(balance // fo_gold_3x3_step)
    else:
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
    text = game_step(user_id, count)
    return text

# -------------------------------------------------------------------------------------------------


def risk_3x3_win(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_risk_base_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_base_four_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_base_four_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_base_four_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_base_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_base_four_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_risk_bronze_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_bronze_four_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_bronze_four_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_bronze_four_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_bronze_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_bronze_four_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_risk_silver_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_silver_four_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_silver_four_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_silver_four_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_silver_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_silver_four_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_risk_gold_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_gold_four_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_gold_four_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_gold_four_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_gold_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_gold_four_win
            balance = db.new_balance_plus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_vip_four_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_vip_four_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_vip_four_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_vip_four_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_vip_four_win
            balance = db.new_balance_plus(user_id, ba)

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
    text = game_win(user_id, count)
    return text


def risk_3x3_loss(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_risk_base_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_four_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_four_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_four_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_base_four_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_risk_bronze_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_four_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_four_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_four_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_bronze_four_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_risk_silver_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_four_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_four_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_four_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_silver_four_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_risk_gold_four":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_four_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_four_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_four_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_gold_four_loss
            balance = db.new_balance_minus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_four_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_four_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_four_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_vip_four_loss
            balance = db.new_balance_minus(user_id, ba)

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
    text = game_step(user_id, count)
    return text


def risk_4x4_win(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_risk_base_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_base_six_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_base_six_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_base_six_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_base_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_base_six_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_risk_bronze_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_bronze_six_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_bronze_six_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_bronze_six_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_bronze_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_bronze_six_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_risk_silver_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_silver_six_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_silver_six_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_silver_six_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_silver_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_silver_six_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_risk_gold_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_gold_six_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_gold_six_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_gold_six_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_gold_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_gold_six_win
            balance = db.new_balance_plus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_vip_six_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_vip_six_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_vip_six_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_vip_six_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_vip_six_win
            balance = db.new_balance_plus(user_id, ba)

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
    text = game_win(user_id, count)
    return text


def risk_4x4_loss(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_risk_base_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_six_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_six_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_six_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_base_six_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_risk_bronze_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_six_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_six_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_six_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_bronze_six_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_risk_silver_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_six_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_six_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_six_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_silver_six_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_risk_gold_six":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_six_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_six_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_six_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_gold_six_loss
            balance = db.new_balance_minus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_six_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_six_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_six_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_vip_six_loss
            balance = db.new_balance_minus(user_id, ba)

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
    text = game_step(user_id, count)
    return text


def risk_5x5_win(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_risk_base_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_base_nine_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_base_nine_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_base_nine_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_base_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_base_nine_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_risk_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_bronze_nine_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_bronze_nine_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_bronze_nine_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_bronze_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_bronze_nine_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_risk_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_silver_nine_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_silver_nine_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_silver_nine_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_silver_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_silver_nine_win
            balance = db.new_balance_plus(user_id, ba)
    elif save == "game_risk_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_gold_nine_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_gold_nine_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_gold_nine_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_gold_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_gold_nine_win
            balance = db.new_balance_plus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = f_vip_nine_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = s_vip_nine_win
            balance = db.new_balance_plus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = t_vip_nine_win
            balance = db.new_balance_plus(user_id, ba)
        else:
            ba = fo_vip_nine_loss
            balance = db.new_balance_minus(user_id, ba)
            ba = fo_vip_nine_win
            balance = db.new_balance_plus(user_id, ba)

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
    text = game_win(user_id, count)
    return text


def risk_5x5_loss(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    save = db.get_save(user_id)
    if save == "game_risk_base_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_base_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_base_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_base_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_base_nine_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_risk_bronze_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_bronze_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_bronze_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_bronze_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_bronze_nine_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_risk_silver_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_silver_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_silver_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_silver_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_silver_nine_loss
            balance = db.new_balance_minus(user_id, ba)
    elif save == "game_risk_gold_nine":
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_gold_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_gold_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_gold_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_gold_nine_loss
            balance = db.new_balance_minus(user_id, ba)
    else:
        if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
            ba = f_vip_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
            ba = s_vip_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        elif currency == "EGP" or currency == "INR":
            ba = t_vip_nine_loss
            balance = db.new_balance_minus(user_id, ba)
        else:
            ba = fo_vip_nine_loss
            balance = db.new_balance_minus(user_id, ba)

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
    text = game_step(user_id, count)
    return text

# -----------------------------------------------------------------------------------------------------------------


def free_3x3_win(user_id):
    language = db.get_language(user_id)
    save = db.get_save(user_id)
    if save == "game_free":
        re = free_win
        res = db.new_res_plus(user_id, re)
        fre = 1
        free_game = db.new_free_game_minus(user_id, fre)
    else:
        ba = free_win
        balance = db.new_balance_plus(user_id, ba)
        re = free_skip
        res = db.new_res_minus(user_id, re)

    if save == "game_free":
        free_game = db.get_free_game(user_id)
        count = free_game
    else:
        res = db.get_res(user_id)
        count = int(res // free_skip)
    if count < 0:
        count = 0
    text = game_win(user_id, count)
    return text


def free_3x3_loss(user_id):
    language = db.get_language(user_id)
    save = db.get_save(user_id)
    if save == "game_free":
        # res -= free_loss
        fre = 1
        free_game = db.new_free_game_minus(user_id, fre)
    else:
        re = free_loss
        res = db.new_res_minus(user_id, re)
        re = free_skip
        res = db.new_res_minus(user_id, re)

    if save == "game_free":
        free_game = db.get_free_game(user_id)
        count = free_game
    else:
        res = db.get_res(user_id)
        count = int(res // free_skip)
    if count < 0:
        count = 0
    text = game_loss(user_id, count)
    return text


def free_3x3_lucky(user_id):
    language = db.get_language(user_id)
    save = db.get_save(user_id)
    if save == "game_free":
        fre = 1
        free_game = db.new_free_game_minus(user_id, fre)
    else:
        re = free_skip
        res = db.new_res_minus(user_id, re)
        re = free_lucky
        res = db.new_res_plus(user_id, re)

    if save == "game_free":
        free_game = db.get_free_game(user_id)
        count = free_game
    else:
        res = db.get_res(user_id)
        count = int(res // free_skip)
    if count < 0:
        count = 0
    text = game_lucky(user_id, count)
    return text


def free_3x3_step(user_id):
    language = db.get_language(user_id)
    save = db.get_save(user_id)
    if save == "game_free":
        pass
    else:
        re = free_skip
        res = db.new_res_minus(user_id, re)

    if save == "game_free":
        free_game = db.get_free_game(user_id)
        count = free_game
    else:
        res = db.get_res(user_id)
        count = int(res // free_skip)
    if count < 0:
        count = 0
    text = game_step(user_id, count)
    return text
