from aiogram import types

import all_lang
import config
import db
# from exchange import usd1, eur1, rub1, gbp1, uah1, kzt1, byn1, krw1, ils1, idr1, aed1, gel1, twd1, try1, hkd1, inr1, cad1, amd1, aud1, pln1, cop1, brl1, chf1, mxn1, ars1, sgd1, sar1, mdl1, jpy1, ron1, sek1, azn1, rsd1, nok1, myr1, bgn1, egp1, gtq1, clp1, nzd1
import exchange
from exchange import fir1, sec1, thi1, fou1, fif1, six1, sev1, fir2, sec2, thi2, fou2, fif2, six2, sev2, fir3, sec3, thi3, fou3, fif3, six3, sev3, fir4, sec4, thi4, fou4, fif4, six4, sev4


def pay(user_id, key):
    currency = db.get_currency(user_id)
    name = 'PIXEL'
    lab = name
    description = all_lang.des(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        first_price = fir1
        second_price = sec1
        third_price = thi1
        fourth_price = fou1
        fifth_price = fif1
        sixth_price = six1
        seventh_price = sev1
        if key == "first_pay":
            title = "300.0 PIXEL"
        elif key == "second_pay":
            title = "600.0 PIXEL"
        elif key == "third_pay":
            title = "1200.0 PIXEL"
        elif key == "fourth_pay":
            title = "1800.0 PIXEL"
        elif key == "fifth_pay":
            title = "3000.0 PIXEL"
        elif key == "sixth_pay":
            title = "6000.0 PIXEL"
        else:
            title = "60000.0 PIXEL"
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BEN" or currency == "MXN":
        first_price = fir2
        second_price = sec2
        third_price = thi2
        fourth_price = fou2
        fifth_price = fif2
        sixth_price = six2
        seventh_price = sev2
        if key == "first_pay":
            title = "500.0 PIXEL"
        elif key == "second_pay":
            title = "1000.0 PIXEL"
        elif key == "third_pay":
            title = "2000.0 PIXEL"
        elif key == "fourth_pay":
            title = "3000.0 PIXEL"
        elif key == "fifth_pay":
            title = "5000.0 PIXEL"
        elif key == "sixth_pay":
            title = "10000.0 PIXEL"
        else:
            title = "100000.0 PIXEL"
    elif currency == "EGP" or currency == "INR":
        first_price = fir3
        second_price = sec3
        third_price = thi3
        fourth_price = fou3
        fifth_price = fif3
        sixth_price = six3
        seventh_price = sev3
        if key == "first_pay":
            title = "100.0 PIXEL"
        elif key == "second_pay":
            title = "200.0 PIXEL"
        elif key == "third_pay":
            title = "400.0 PIXEL"
        elif key == "fourth_pay":
            title = "600.0 PIXEL"
        elif key == "fifth_pay":
            title = "1000.0 PIXEL"
        elif key == "sixth_pay":
            title = "2000.0 PIXEL"
        else:
            title = "20000.0 PIXEL"
    else:
        first_price = fir4
        second_price = sec4
        third_price = thi4
        fourth_price = fou4
        fifth_price = fif4
        sixth_price = six4
        seventh_price = sev4
        if key == "first_pay":
            title = "1000.0 PIXEL"
        elif key == "second_pay":
            title = "2000.0 PIXEL"
        elif key == "third_pay":
            title = "4000.0 PIXEL"
        elif key == "fourth_pay":
            title = "6000.0 PIXEL"
        elif key == "fifth_pay":
            title = "10000.0 PIXEL"
        elif key == "sixth_pay":
            title = "20000.0 PIXEL"
        else:
            title = "200000.0 PIXEL"

    rate = exchange.get_price(user_id)
    if currency == "EUR":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # EUR
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # EUR
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # EUR
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # EUR
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # EUR
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # EUR
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # EUR
    elif currency == "RUB":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # RUB
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # RUB
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # RUB
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # RUB
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # RUB
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # RUB
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # RUB
    elif currency == "GBP":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # GBP
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # GBP
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # GBP
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # GBP
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # GBP
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # GBP
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # GBP
    elif currency == "UAH":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # UAH
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # UAH
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # UAH
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # UAH
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # UAH
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # UAH
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # UAH
    elif currency == "KZT":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # KZT
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # KZT
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # KZT
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # KZT
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # KZT
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # KZT
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # KZT
    elif currency == "BYN":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # BYN
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # BYN
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # BYN
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # BYN
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # BYN
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # BYN
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # BYN
    elif currency == "KRW":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price / 10))  # KRW
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price / 10))  # KRW
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price / 10))  # KRW
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price / 10))  # KRW
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price / 10))  # KRW
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price / 10))  # KRW
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price / 10))  # KRW
    elif currency == "ILS":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # ILS
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # ILS
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # ILS
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # ILS
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # ILS
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # ILS
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # ILS
    elif currency == "IDR":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # IDR
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # IDR
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # IDR
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # IDR
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # IDR
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # IDR
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # IDR
    elif currency == "AED":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # AED
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # AED
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # AED
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # AED
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # AED
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # AED
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # AED
    elif currency == "GEL":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # GEL
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # GEL
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # GEL
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # GEL
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # GEL
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # GEL
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # GEL
    elif currency == "TWD":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # TWD
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # TWD
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # TWD
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # TWD
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # TWD
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # TWD
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # TWD
    elif currency == "TRY":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # TRY
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # TRY
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # TRY
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # TRY
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # TRY
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # TRY
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # TRY
    elif currency == "HKD":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # HKD
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # HKD
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # HKD
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # HKD
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # HKD
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # HKD
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # HKD
    elif currency == "INR":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # INR
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # INR
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # INR
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # INR
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # INR
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # INR
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # INR
    elif currency == "CAD":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # CAD
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # CAD
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # CAD
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # CAD
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # CAD
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # CAD
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # CAD
    elif currency == "AMD":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # AMD
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # AMD
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # AMD
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # AMD
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # AMD
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # AMD
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # AMD
    elif currency == "AUD":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # AUD
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # AUD
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # AUD
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # AUD
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # AUD
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # AUD
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # AUD
    elif currency == "PLN":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # PLN
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # PLN
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # PLN
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # PLN
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # PLN
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # PLN
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # PLN
    elif currency == "COP":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # COP
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # COP
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # COP
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # COP
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # COP
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # COP
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # COP
    elif currency == "BRL":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # BRL
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # BRL
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # BRL
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # BRL
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # BRL
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # BRL
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # BRL
    elif currency == "CHF":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # CHF
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # CHF
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # CHF
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # CHF
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # CHF
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # CHF
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # CHF
    elif currency == "MXN":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # MXN
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # MXN
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # MXN
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # MXN
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # MXN
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # MXN
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # MXN
    elif currency == "ARS":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # ARS
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # ARS
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # ARS
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # ARS
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # ARS
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # ARS
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # ARS
    elif currency == "SGD":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # SGD
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # SGD
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # SGD
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # SGD
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # SGD
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # SGD
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # SGD
    elif currency == "SAR":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # SAR
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # SAR
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # SAR
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # SAR
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # SAR
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # SAR
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # SAR
    elif currency == "MDL":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # MDL
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # MDL
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # MDL
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # MDL
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # MDL
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # MDL
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # MDL
    elif currency == "JPY":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price / 10))  # JPY
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price / 10))  # JPY
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price / 10))  # JPY
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price / 10))  # JPY
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price / 10))  # JPY
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price / 10))  # JPY
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price / 10))  # JPY
    elif currency == "RON":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # RON
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # RON
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # RON
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # RON
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # RON
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # RON
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # RON
    elif currency == "SEK":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # SEK
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # SEK
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # SEK
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # SEK
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # SEK
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # SEK
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # SEK
    elif currency == "AZN":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # AZN
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # AZN
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # AZN
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # AZN
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # AZN
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # AZN
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # AZN
    elif currency == "RSD":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # RSD
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # RSD
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # RSD
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # RSD
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # RSD
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # RSD
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # RSD
    elif currency == "NOK":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # NOK
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # NOK
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # NOK
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # NOK
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # NOK
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # NOK
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # NOK
    elif currency == "MYR":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # MYR
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # MYR
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # MYR
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # MYR
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # MYR
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # MYR
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # MYR
    elif currency == "BGN":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # BGN
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # BGN
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # BGN
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # BGN
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # BGN
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # BGN
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # BGN
    elif currency == "EGP":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # EGP
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # EGP
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # EGP
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # EGP
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # EGP
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # EGP
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # EGP
    elif currency == "GTQ":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # GTQ
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # GTQ
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # GTQ
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # GTQ
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # GTQ
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # GTQ
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # GTQ
    elif currency == "CLP":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price / 10))  # CLP
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price / 10))  # CLP
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price / 10))  # CLP
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price / 10))  # CLP
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price / 10))  # CLP
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price / 10))  # CLP
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price / 10))  # CLP
    elif currency == "NZD":
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # NZD
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # NZD
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # NZD
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # NZD
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # NZD
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # NZD
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # NZD
    else:
        if key == "first_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * first_price * 10))  # USD
        elif key == "second_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * second_price * 10))  # USD
        elif key == "third_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * third_price * 10))  # USD
        elif key == "fourth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fourth_price * 10))  # USD
        elif key == "fifth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * fifth_price * 10))  # USD
        elif key == "sixth_pay":
            price = types.LabeledPrice(label=lab, amount=int(rate * sixth_price * 10))  # USD
        else:
            price = types.LabeledPrice(label=lab, amount=int(rate * seventh_price * 10))  # USD

    if currency == "EUR":
        currencies = "eur"
    elif currency == "RUB":
        currencies = "rub"
    elif currency == "GBP":
        currencies = "gbp"
    elif currency == "UAH":
        currencies = "uah"
    elif currency == "KZT":
        currencies = "kzt"
    elif currency == "BYN":
        currencies = "byn"
    elif currency == "KRW":
        currencies = "krw"
    elif currency == "ILS":
        currencies = "ils"
    elif currency == "IDR":
        currencies = "idr"
    elif currency == "AED":
        currencies = "aed"
    elif currency == "GEL":
        currencies = "gel"
    elif currency == "TWD":
        currencies = "twd"
    elif currency == "TRY":
        currencies = "try"
    elif currency == "HKD":
        currencies = "hkd"
    elif currency == "INR":
        currencies = "inr"
    elif currency == "CAD":
        currencies = "cad"
    elif currency == "AMD":
        currencies = "amd"
    elif currency == "AUD":
        currencies = "aud"
    elif currency == "PLN":
        currencies = "pln"
    elif currency == "COP":
        currencies = "cop"
    elif currency == "BRL":
        currencies = "brl"
    elif currency == "CHF":
        currencies = "chf"
    elif currency == "MXN":
        currencies = "mxn"
    elif currency == "ARS":
        currencies = "ars"
    elif currency == "SGD":
        currencies = "sgd"
    elif currency == "SAR":
        currencies = "sar"
    elif currency == "MDL":
        currencies = "mdl"
    elif currency == "JPY":
        currencies = "jpy"
    elif currency == "RON":
        currencies = "ron"
    elif currency == "SEK":
        currencies = "sek"
    elif currency == "AZN":
        currencies = "azn"
    elif currency == "RSD":
        currencies = "rsd"
    elif currency == "NOK":
        currencies = "nok"
    elif currency == "MYR":
        currencies = "myr"
    elif currency == "BGN":
        currencies = "bgn"
    elif currency == "EGP":
        currencies = "egp"
    elif currency == "GTQ":
        currencies = "gtq"
    elif currency == "CLP":
        currencies = "clp"
    elif currency == "NZD":
        currencies = "nzd"
    else:
        currencies = "usd"

    # currencies = "PIXEL"
    photo_url = 'https://ic.wampi.ru/2023/07/28/pixel_fon_no.png'
    # photo_url = 'https://cdn3d.iconscout.com/3d/premium/thumb/ton-coin-8914655-7237154.png'
    photo_width = 450
    photo_height = 450
    photo_size = 400
    is_flexible = False
    prices = [price]
    start_parameter = "pay"
    payload = "test-invoice-payload"
    if currency == "RUB":
        provider_token = config.PAYMENTS_TOKEN_RUB
    else:
        provider_token = config.PAYMENTS_TOKEN

    return price, title, description, provider_token, currencies, photo_url, photo_width, photo_height, photo_size, \
        is_flexible, prices, start_parameter, payload
