from requests import Session
import json
import config
import db
import decimal

url = config.API_URL

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': config.API_KEY
}


def get_price(user_id):
    currency = db.get_currency(user_id)
    rate = db.get_rate(currency)
    rate = round(rate, 2)
    return rate


fir1 = 30
sec1 = 60
thi1 = 120
fou1 = 180
fif1 = 300
six1 = 600
sev1 = 6000

fir2 = 50
sec2 = 100
thi2 = 200
fou2 = 300
fif2 = 500
six2 = 1000
sev2 = 10000

fir3 = 10
sec3 = 20
thi3 = 40
fou3 = 60
fif3 = 100
six3 = 200
sev3 = 2000

fir4 = 100
sec4 = 200
thi4 = 400
fou4 = 600
fif4 = 1000
six4 = 2000
sev4 = 20000
