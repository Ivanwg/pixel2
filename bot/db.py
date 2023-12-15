import random
import os

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    Boolean,
    String,
    Float,
    CheckConstraint,
    DateTime,
    BIGINT
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.exc import SQLAlchemyError


# from dotenv import load_dotenv
# load_dotenv()

db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DATABASE')}"
print(db_url)
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    telegram_id = Column(BIGINT, primary_key=True)
    balance = Column(Integer, CheckConstraint("balance >= 0"), default=0.0)
    ton = Column(Integer, CheckConstraint("ton >= 0"), default=0)
    res = Column(Integer, CheckConstraint("res >= 0"), default=0)
    free_game = Column(Integer, CheckConstraint("free_game >= 0"), default=0)
    god_mode = Column(Boolean, default=False)
    language = Column(String(3), default="eng")
    currency = Column(String(3), default="USD")
    save = Column(String(255), default="")
    registry = Column(Boolean, default=False)
    ticket = Column(Integer, default=0)
    my_promo = Column(String(255), default="")
    count_deposit = Column(Integer, default=0)
    sum_deposit = Column(Float, default=0)
    count_friend = Column(Integer, default=0)
    game_base = Column(Integer, default=0)
    game_bronze = Column(Integer, default=0)
    game_silver = Column(Integer, default=0)
    game_gold = Column(Integer, default=0)
    game_vip = Column(Integer, default=0)


class DBGame(Base):
    __tablename__ = "games"
    telegram_id = Column(BIGINT, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    game_type = Column(String(10), nullable=False)
    rows = Column(Integer, nullable=False)
    cols = Column(Integer, nullable=False)
    field = Column(String(255), nullable=False)
    bid = Column(Integer, nullable=False)
    ghost_number = Column(Integer, nullable=False, default=0)


class Currency(Base):
    __tablename__ = "currencies"
    currency = Column(String(3), primary_key=True)
    rate = Column(Float, nullable=False)


def update_currency(currency: str, rate: float):
    session = Session()
    cur = session.query(Currency).filter(Currency.currency == currency).first()
    if cur == None:
        cur = Currency(currency=currency, rate=rate)
        session.add(cur)
    else:
        cur.rate = rate
    session.commit()
    session.close()


def get_rate(currency: str):
    session = Session()

    cur = session.query(Currency).filter(Currency.currency == currency).first()
    session.close()
    return cur.rate
# ! Язык пользователя
language = 'en'


# ! Валюта пользователя
currency = 'USD'


# ! Промокод пользователя, который его использовал (нужно его сохранить в базе)
my_promo = ""


# ! Баланс пользователя
balance = 0


# ! Резервный баланс пользователя
res = 0


# ! Тон баланс пользователя
ton = 0


# ! Бесплатные игры пользователя
free_game = 0


# ! Количество приглашённых друзей
count_friend = 0


# ! Список билетов пользователя
ticket = []


# ! Количество пополнений
count_deposit = 0


# ! Количество выводов средств
count_withdraw = 0


# ! Общая сумма пополнений
sum_deposit = 0


# ! Общая сумма выводов средств
sum_withdraw = 0


# ! Количество сыгранных игр на базе
game_base = 0


# ! Количество сыгранных игр на бронзе
game_bronze = 0


# ! Количество сыгранных игр на серебре
game_silver = 0


# ! Количество сыгранных игр на золоте
game_gold = 0


# ! Количество сыгранных игр на випе
game_vip = 0


# ! Сохранение последних действий
save = ''


# ! Балансирование (один параметр для всех пользователей (изночально False))
god_mode = False


# ! Подтверждение регистрации
registry = False


# ! 2x2 список для рандома
string_four = [0, 1, 2, 3]


# ! 2x3 список для рандома
string_six = [0, 1, 2, 0, 1, 2]


# ! 3x3 список для рандома
string_nine = [0, 1, 2, 0, 1, 2, 0, 1, 2]


# ! 3x3 risk список для рандома
strings_four = [0, 1, 2, 3, 4, 5, 6, 7, 8]


# ! 4x4 risk список для рандома
strings_six = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# ! 5x5 risk список для рандома
strings_nine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


# ! string four
f1 = 0
f2 = 0
f3 = 0
f4 = 0

# ! string six
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0

# ! string nine
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0

# ! strings four
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0
q6 = 0
q7 = 0
q8 = 0
q9 = 0

# ! strings six
w1 = 0
w2 = 0
w3 = 0
w4 = 0
w5 = 0
w6 = 0
w7 = 0
w8 = 0
w9 = 0
w10 = 0
w11 = 0
w12 = 0
w13 = 0
w14 = 0
w15 = 0
w16 = 0

# ! strings nine
e1 = 0
e2 = 0
e3 = 0
e4 = 0
e5 = 0
e6 = 0
e7 = 0
e8 = 0
e9 = 0
e10 = 0
e11 = 0
e12 = 0
e13 = 0
e14 = 0
e15 = 0
e16 = 0
e17 = 0
e18 = 0
e19 = 0
e20 = 0
e21 = 0
e22 = 0
e23 = 0
e24 = 0
e25 = 0


# ---------------------------------------
def add_user(user: User) -> None:
    session = Session()
    db_user = session.query(User).filter_by(telegram_id=user.telegram_id).first()
    if db_user is None:
        session.add(user)
        session.commit()
        session.close()
    else:
        session.close()
        raise KeyError(f"User already exists. Telegram id: {user.telegram_id}")



def get_field(user_id, field_name):
    try:
        session = Session()
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if user:
            return getattr(user, field_name, None)
        else:
            user = User(telegram_id=user_id)
            session.add(user)
            session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        # Handle the error or log it
    finally:
        session.close()
    return 0

def set_field(user_id, field_name, value):
    try:
        session = Session()
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if not user:
            user = User(telegram_id=user_id)
            session.add(user)
        setattr(user, field_name, value)
        session.commit()
        return value
    except SQLAlchemyError as e:
        session.rollback()
        # Handle the error or log it
    finally:
        session.close()
    return None


def get_language(user_id):
    return get_field(user_id, "language")


def get_god_mode(user_id):
    return get_field(user_id, "god_mode")


def get_registry(user_id):
    return get_field(user_id, "registry")


def get_currency(user_id):
    return get_field(user_id, "currency")


def get_my_promo(user_id):
    return get_field(user_id, "my_promo")


def get_balance(user_id):
    return get_field(user_id, "balance")


def get_ton(user_id):
    return get_field(user_id, "ton")


def get_res(user_id):
    return get_field(user_id, "res")


def get_free_game(user_id):
    return get_field(user_id, "free_game")


def get_save(user_id):
    return get_field(user_id, "save")


def new_language(user_id, lang):
    set_field(user_id, "language", lang)


def new_currency(user_id, value):
    set_field(user_id, "currency", value)


def new_registry(user_id, reg):
    set_field(user_id, "registry", reg)


def new_user_yes(user_id):
    v = get_free_game(user_id) + 8
    set_field(user_id, "free_game", v)
    return v

def new_user_no(user_id):
    aa = get_free_game(user_id)
    v = get_free_game(user_id) + 5
    set_field(user_id, "free_game", v)
    return v

def ref_user(referrer_id):
    v = get_free_game(referrer_id) + 5
    set_field(referrer_id, "free_game", v)
    return v


def new_my_promo(user_id, referrer_id):
    set_field(user_id, "my_promo", referrer_id)


def new_balance_minus(user_id, ba):
    v = get_balance(user_id) - ba
    set_field(user_id, "balance", v)
    return v


def new_balance_plus(user_id, ba):
    v = get_balance(user_id) + ba
    set_field(user_id, "balance", v)
    return v


def new_ton_minus(user_id, to):
    v = get_ton(user_id) - to
    set_field(user_id, "ton", v)
    return v


def new_ton_plus(user_id, to):
    v = get_ton(user_id) + to
    set_field(user_id, "ton", v)
    return v


def new_res_minus(user_id, re):
    v = get_res(user_id) - re
    set_field(user_id, "res", v)
    return v


def new_res_plus(user_id, re):
    v = get_res(user_id) + re
    set_field(user_id, "res", v)
    return v


def new_free_game_minus(user_id, fre):
    v = get_free_game(user_id) - fre
    set_field(user_id, "free_game", v)
    return v


def new_free_game_plus(user_id, fre):
    v = get_free_game(user_id) + fre
    set_field(user_id, "free_game", v)
    return v


def new_save(user_id, msg):
    set_field(user_id, "save", msg)


def get_string_four(user_id):
    global string_four
    return string_four


def new_string_four(user_id):
    global string_four
    return random.shuffle(string_four)


def get_string_six(user_id):
    global string_six
    return string_six


def new_string_six(user_id):
    global string_six
    random.shuffle(string_six)
    return string_six


def get_string_nine(user_id):
    global string_nine
    return string_nine


def new_string_nine(user_id):
    global string_nine
    random.shuffle(string_nine)
    return string_nine


def get_strings_four(user_id):
    global strings_four
    return strings_four


def new_strings_four(user_id):
    global strings_four
    random.shuffle(strings_four)
    return strings_four


def get_strings_six(user_id):
    global strings_six
    return strings_six


def new_strings_six(user_id):
    global strings_six
    random.shuffle(strings_six)
    return strings_six


def get_strings_nine(user_id):
    global strings_nine
    return strings_nine


def new_strings_nine(user_id):
    global strings_nine
    random.shuffle(strings_nine)
    return strings_nine


def index_strings_four(user_id):
    global q1, q2, q3, q4, q5, q6, q7, q8, q9, strings_four
    strings_four = get_strings_four(user_id)
    q1 = strings_four[0]
    q2 = strings_four[1]
    q3 = strings_four[2]
    q4 = strings_four[3]
    q5 = strings_four[4]
    q6 = strings_four[5]
    q7 = strings_four[6]
    q8 = strings_four[7]
    q9 = strings_four[8]
    return q1, q2, q3, q4, q5, q6, q7, q8, q9


def index_strings_six(user_id):
    global w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, strings_six
    strings_six = get_strings_six(user_id)
    w1 = strings_six[0]
    w2 = strings_six[1]
    w3 = strings_six[2]
    w4 = strings_six[3]
    w5 = strings_six[4]
    w6 = strings_six[5]
    w7 = strings_six[6]
    w8 = strings_six[7]
    w9 = strings_six[8]
    w10 = strings_six[9]
    w11 = strings_six[10]
    w12 = strings_six[11]
    w13 = strings_six[12]
    w14 = strings_six[13]
    w15 = strings_six[14]
    w16 = strings_six[15]
    return w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16


def index_strings_nine(user_id):
    global e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25, strings_nine
    strings_nine = get_strings_nine(user_id)
    e1 = strings_nine[0]
    e2 = strings_nine[1]
    e3 = strings_nine[2]
    e4 = strings_nine[3]
    e5 = strings_nine[4]
    e6 = strings_nine[5]
    e7 = strings_nine[6]
    e8 = strings_nine[7]
    e9 = strings_nine[8]
    e10 = strings_nine[9]
    e11 = strings_nine[10]
    e12 = strings_nine[11]
    e13 = strings_nine[12]
    e14 = strings_nine[13]
    e15 = strings_nine[14]
    e16 = strings_nine[15]
    e17 = strings_nine[16]
    e18 = strings_nine[17]
    e19 = strings_nine[18]
    e20 = strings_nine[19]
    e21 = strings_nine[20]
    e22 = strings_nine[21]
    e23 = strings_nine[22]
    e24 = strings_nine[23]
    e25 = strings_nine[24]
    return e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25


def index_string_four(user_id):
    global f1, f2, f3, f4, string_four
    string_four = get_string_four(user_id)
    f1 = string_four[0]
    f2 = string_four[1]
    f3 = string_four[2]
    f4 = string_four[3]
    return f1, f2, f3, f4


def index_string_six(user_id):
    global i1, i2, i3, i4, i5, i6, string_six
    string_six = get_string_six(user_id)
    i1 = string_six[0]
    i2 = string_six[1]
    i3 = string_six[2]
    i4 = string_six[3]
    i5 = string_six[4]
    i6 = string_six[5]
    return i1, i2, i3, i4, i5, i6


def index_string_nine(user_id):
    global s1, s2, s3, s4, s5, s6, s7, s8, s9, string_nine
    string_nine = get_string_nine(user_id)
    s1 = string_nine[0]
    s2 = string_nine[1]
    s3 = string_nine[2]
    s4 = string_nine[3]
    s5 = string_nine[4]
    s6 = string_nine[5]
    s7 = string_nine[6]
    s8 = string_nine[7]
    s9 = string_nine[8]
    return s1, s2, s3, s4, s5, s6, s7, s8, s9

def get_count_friend(user_id):
    return get_field(user_id, "count_friend")

def new_count_friend(user_id):
    v = get_count_friend(user_id) + 1
    set_field(user_id, "count_friend", v)
    return v

def get_sum_deposit(user_id):
    return get_field(user_id, "sum_deposit")

def new_sum_deposit(user_id, ba):
    v = get_sum_deposit(user_id) + ba
    set_field(user_id, "sum_deposit", v)
    return v

def get_count_deposit(user_id):
    return get_field(user_id, "count_deposit")

def get_ticket(user_id):
    return get_field(user_id, "ticket")

def new_count_deposit(user_id):
    v = get_count_deposit(user_id)
    if v == 0:
        set_field(user_id, "ticket", get_ticket(user_id) + 1)
    v += 1
    return v


def new_game(user_id):
    save = get_save(user_id)
    if save == "game_risk_bronze_four":
        game_bronze = new_game_bronze(user_id)
        if game_bronze == 50:
            set_field(user_id, "game_bronze", 0)
            set_field(user_id, "ticket", get_ticket(user_id) + 1)
            # ! Выдача 1 билета и обнуление параметра game_bronze и по новой до 50 игр
    elif save == "game_risk_silver_four":
        game_silver = new_game_silver(user_id)
        if game_silver == 30:
            set_field(user_id, "game_silver", 0)
            set_field(user_id, "ticket", get_ticket(user_id) + 1)

            # ! Выдача 1 билета и обнуление параметра game_silver и по новой до 30 игр
    elif save == "game_risk_gold_four":
        game_gold = new_game_gold(user_id)
        if game_gold == 10:
            set_field(user_id, "game_gold", 0)
            set_field(user_id, "ticket", get_ticket(user_id) + 1)
            # ! Выдача 1 билета и обнуление параметра game_gold и по новой до 10 игр
    elif save == "game_risk_vip_four":
        game_vip = new_game_vip(user_id)
        if game_vip == 1:
            set_field(user_id, "game_vip", 0)
            set_field(user_id, "ticket", get_ticket(user_id) + 1)
            # ! Выдача 1 билета и обнуление параметра game_vip и по новой до 1 игры
    else:
        game_base = new_game_base(user_id)
        if game_base == 100:
            set_field(user_id, "game_base", 0)
            set_field(user_id, "ticket", get_ticket(user_id) + 1)
            # ! Выдача 1 билета и обнуление параметра game_base и по новой до 100 игр
    right = "."
    return right

def get_game_base(user_id):
    return get_field(user_id, "game_base")

def new_game_base(user_id):
    v = get_game_base(user_id) + 1
    set_field(user_id, "game_base", v)
    return v


def new_game_bronze(user_id):
    v = get_field(user_id, "game_bronze") + 1
    set_field(user_id, "game_bronze", v)
    return v


def new_game_silver(user_id):
    v = get_field(user_id, "game_silver") + 1
    set_field(user_id, "game_silver", v)
    return v


def new_game_gold(user_id):
    v = get_field(user_id, "game_gold") + 1
    set_field(user_id, "game_gold", v)
    return v


def new_game_vip(user_id):
    v = get_field(user_id, "game_vip") + 1
    set_field(user_id, "game_vip", v)
