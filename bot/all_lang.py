import config
import db
import exchange
import lists
from aiogram.types import InlineKeyboardButton
from options import free_skip


# def text_start(user_id):
#     language = db.get_language(user_id)
#     if language == "ru":
#         text = f'Играйте, покупайте и обменивайте внутреигровую валюту быстро и надежно через TON прямо в Telegram!\n\n' \
#                f'Присоединяйтесь к <a href="{config.CHANNEL_URL}">нашему каналу</a> и будьте в курсе всех обновлений' \
#                f' и промоакций.\n\n' \
#                f'<b>📖 Полный FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     elif language == "id":
#         text = f'Mainkan, beli, dan tukar mata uang dalam game dengan cepat dan aman melalui TON langsung di Telegram!\n\n' \
#                f'Bergabunglah dengan <a href="{config.CHANNEL_URL}">saluran kami</a> untuk mendapatkan update dan promosi.\n\n' \
#                f'<b>📖 Penuh FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     elif language == "es":
#         text = f'¡Juega, compra e intercambia moneda del juego de forma rápida y segura a través de TON directamente en Telegram!\n\n' \
#                f'Únase a <a href="{config.CHANNEL_URL}">nuestro canal</a> para recibir noticias y promociones.\n\n' \
#                f'<b>📖 lleno FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     elif language == "ko":
#         text = f'텔레그램에서 바로 TON을 통해 게임 내 화폐를 빠르고 안전하게 플레이하고 구매하고 교환하세요!\n\n' \
#                f'업데이트 및 프로모션을 받으려면 <a href="{config.CHANNEL_URL}">저희 채널</a> 에 가입하세요.\n\n' \
#                f'<b>📖 가득한 FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     elif language == "it":
#         text = f'Gioca, acquista e scambia valuta di gioco in modo rapido e sicuro tramite PIXEL direttamente su Telegram!\n\n' \
#                f'Unisciti al <a href="{config.CHANNEL_URL}">nostro canale</a> per ricevere aggiornamenti e promozioni.\n\n' \
#                f'<b>📖 pieno FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     elif language == "ch":
#         text = f'直接在Telegram上通過TON快速安全地玩、購買和兌換遊戲內貨幣！\n\n' \
#                f'加入<a href="{config.CHANNEL_URL}">我们的频道</a>以接收更新和促销。\n\n' \
#                f'<b>📖 滿的 FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     elif language == "ta":
#         text = f'直接在Telegram上通过TON快速安全地玩、购买和兑换游戏内货币！\n\n' \
#                f'加入<a href="{config.CHANNEL_URL}">我們的頻道</a>以接收更新和促銷。\n\n' \
#                f'<b>📖 满的 FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     elif language == "fa":
#         text = f'بازی، خرید و تبادل ارز درون بازی به سرعت و ایمن از طریق TON مستقیماً در تلگرام!\n\n' \
#                f'برای دریافت آخرین به‌روزرسانی‌ها و پروموشن‌ها، به <a href="{config.CHANNEL_URL}">کانال ما</a> بپیوندید.\n\n' \
#                f'<b>📖 پر شده FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     elif language == "tr":
#         text = f"Doğrudan Telegram'da TON aracılığıyla oyun içi parayı hızlı ve güvenli bir şekilde oynayın, satın alın ve değiştirin!\n\n" \
#                f'Güncel gelişmeler ve promosyonlar hakkında bilgi almak için <a href="{config.CHANNEL_URL}">kanalımıza</a> katılın.\n\n' \
#                f'<b>📖 dolu FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     elif language == "uz":
#         text = f"To'g'ridan-to'g'ri Telegram'da TON orqali tez va xavfsiz o'yin ichidagi valyutani o'ynang, sotib oling va almashtiring!\n\n" \
#                f'Yangiliklar va aksiyalardan xabardor bo‘lish uchun <a href="{config.CHANNEL_URL}">kanalimizga</a> qo‘shiling.\n\n' \
#                f'<b>📖 to’la FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     elif language == "be":
#         text = f'টেলিগ্রামে TON-এর মাধ্যমে দ্রুত এবং নিরাপদে ইন-গেম মুদ্রা খেলুন, কিনুন এবং বিনিময় করুন!\n\n' \
#                f'আপডেট এবং প্রচার পেতে <a href="{config.CHANNEL_URL}">আমাদের চ্যানেলে</a> যোগ দিন।\n\n' \
#                f'<b>📖 সম্পূর্ণ FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     elif language == "hi":
#         text = f'सीधे टेलीग्राम पर TON के माध्यम से इन-गेम मुद्रा को जल्दी और सुरक्षित रूप से खेलें, खरीदें और एक्सचेंज करें!\n\n' \
#                f'अपडेट और प्रचार प्राप्त करने के लिए <a href="{config.CHANNEL_URL}">हमारे चैनल</a> से जुड़े।\n\n' \
#                f'<b>📖 भरा हुआ FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     else:
#         text = f'Play, buy and exchange in-game currency quickly and securely through TON right on Telegram!\n\n' \
#                f'Join <a href="{config.CHANNEL_URL}">our channel</a> to receive updates' \
#                f' and promotions.\n\n' \
#                f'<b>📖 Full FAQ:</b> <a href="{config.PIXEL_FAQ}">PIXEL FAQ – Telegraph</a>'
#     return text


def text_start(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = f'Играйте, покупайте и обменивайте внутреигровую валюту быстро и надежно через TON прямо в Telegram!\n\n' \
               f'Присоединяйтесь к <a href="{config.CHANNEL_URL}">нашему каналу</a> и будьте в курсе всех обновлений' \
               f' и промоакций.'
    elif language == "id":
        text = f'Mainkan, beli, dan tukar mata uang dalam game dengan cepat dan aman melalui TON langsung di Telegram!\n\n' \
               f'Bergabunglah dengan <a href="{config.CHANNEL_URL}">saluran kami</a> untuk mendapatkan update dan promosi.'
    elif language == "es":
        text = f'¡Juega, compra e intercambia moneda del juego de forma rápida y segura a través de TON directamente en Telegram!\n\n' \
               f'Únase a <a href="{config.CHANNEL_URL}">nuestro canal</a> para recibir noticias y promociones.'
    elif language == "ko":
        text = f'텔레그램에서 바로 TON을 통해 게임 내 화폐를 빠르고 안전하게 플레이하고 구매하고 교환하세요!\n\n' \
               f'업데이트 및 프로모션을 받으려면 <a href="{config.CHANNEL_URL}">저희 채널</a> 에 가입하세요.'
    elif language == "it":
        text = f'Gioca, acquista e scambia valuta di gioco in modo rapido e sicuro tramite PIXEL direttamente su Telegram!\n\n' \
               f'Unisciti al <a href="{config.CHANNEL_URL}">nostro canale</a> per ricevere aggiornamenti e promozioni.'
    elif language == "ch":
        text = f'直接在Telegram上通過TON快速安全地玩、購買和兌換遊戲內貨幣！\n\n' \
               f'加入<a href="{config.CHANNEL_URL}">我们的频道</a>以接收更新和促销。'
    elif language == "ta":
        text = f'直接在Telegram上通过TON快速安全地玩、购买和兑换游戏内货币！\n\n' \
               f'加入<a href="{config.CHANNEL_URL}">我們的頻道</a>以接收更新和促銷。'
    elif language == "fa":
        text = f'بازی، خرید و تبادل ارز درون بازی به سرعت و ایمن از طریق TON مستقیماً در تلگرام!\n\n' \
               f'برای دریافت آخرین به‌روزرسانی‌ها و پروموشن‌ها، به <a href="{config.CHANNEL_URL}">کانال ما</a> بپیوندید.\n\n'
    elif language == "tr":
        text = f"Doğrudan Telegram'da TON aracılığıyla oyun içi parayı hızlı ve güvenli bir şekilde oynayın, satın alın ve değiştirin!\n\n" \
               f'Güncel gelişmeler ve promosyonlar hakkında bilgi almak için <a href="{config.CHANNEL_URL}">kanalımıza</a> katılın.'
    elif language == "uz":
        text = f"To'g'ridan-to'g'ri Telegram'da TON orqali tez va xavfsiz o'yin ichidagi valyutani o'ynang, sotib oling va almashtiring!\n\n" \
               f'Yangiliklar va aksiyalardan xabardor bo‘lish uchun <a href="{config.CHANNEL_URL}">kanalimizga</a> qo‘shiling.'
    elif language == "be":
        text = f'টেলিগ্রামে TON-এর মাধ্যমে দ্রুত এবং নিরাপদে ইন-গেম মুদ্রা খেলুন, কিনুন এবং বিনিময় করুন!\n\n' \
               f'আপডেট এবং প্রচার পেতে <a href="{config.CHANNEL_URL}">আমাদের চ্যানেলে</a> যোগ দিন।'
    elif language == "hi":
        text = f'सीधे टेलीग्राम पर TON के माध्यम से इन-गेम मुद्रा को जल्दी और सुरक्षित रूप से खेलें, खरीदें और एक्सचेंज करें!\n\n' \
               f'अपडेट और प्रचार प्राप्त करने के लिए <a href="{config.CHANNEL_URL}">हमारे चैनल</a> से जुड़े।'
    else:
        text = f'Play, buy and exchange in-game currency quickly and securely through TON right on Telegram!\n\n' \
               f'Join <a href="{config.CHANNEL_URL}">our channel</a> to receive updates' \
               f' and promotions.'
    return text


def button_start(user_id):
    language = db.get_language(user_id)
    webs = lists.webapp()
    if language == "ru":
        wal = InlineKeyboardButton(text='💰 Мой кошелек', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 Супер Приз', web_app=webs)
        instruction = InlineKeyboardButton(text='🎁 Пригласить друга', callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ Настройки', callback_data='settings')
        game = InlineKeyboardButton(text='💎 Открыть игру', callback_data='tg_mode')
    elif language == "id":
        wal = InlineKeyboardButton(text='💰 Dompet saya', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 Hadiah Super', web_app=webs)
        instruction = InlineKeyboardButton(text='🎁 Undang teman', callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ Pengaturan', callback_data='settings')
        game = InlineKeyboardButton(text='💎 Buka Permainan', callback_data='tg_mode')
    elif language == "es":
        wal = InlineKeyboardButton(text='💰 Mi monedero', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 Súper premio', web_app=webs)
        instruction = InlineKeyboardButton(text='🎁 Invitar a amigo', callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ Ajustes', callback_data='settings')
        game = InlineKeyboardButton(text='💎 Juego abierto', callback_data='tg_mode')
    elif language == "ko":
        wal = InlineKeyboardButton(text='💰 내 월렛', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 슈퍼상', web_app=webs)
        instruction = InlineKeyboardButton(text='🎁 친구를 초대하다', callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ 설정', callback_data='settings')
        game = InlineKeyboardButton(text='💎 오픈 게임', callback_data='tg_mode')
    elif language == "it":
        wal = InlineKeyboardButton(text='💰 Il mio wallet', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 Superpremio', web_app=webs)
        instruction = InlineKeyboardButton(text='🎁 Invita un amico', callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ Impostazioni', callback_data='settings')
        game = InlineKeyboardButton(text='💎 Apri il gioco', callback_data='tg_mode')
    elif language == "ch":
        wal = InlineKeyboardButton(text='💰 我的钱包', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 超級獎', web_app=webs)
        instruction = InlineKeyboardButton(text='🎁 邀請朋友', callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ 设置', callback_data='settings')
        game = InlineKeyboardButton(text='💎 開放遊戲', callback_data='tg_mode')
    elif language == "ta":
        wal = InlineKeyboardButton(text='💰 我的錢包', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 超级奖', web_app=webs)
        instruction = InlineKeyboardButton(text='🎁 邀请朋友', callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ 設置', callback_data='settings')
        game = InlineKeyboardButton(text='💎 开放游戏', callback_data='tg_mode')
    elif language == "fa":
        wal = InlineKeyboardButton(text='💰 کیف پول من', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 جایزه فوق العاده', web_app=webs)
        instruction = InlineKeyboardButton(text='🎁 دعوت از دوست', callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ تنظیمات', callback_data='settings')
        game = InlineKeyboardButton(text='💎 بازی را باز کنید', callback_data='tg_mode')
    elif language == "tr":
        wal = InlineKeyboardButton(text='💰 Cüzdanım', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 Süper Ödül', web_app=webs)
        instruction = InlineKeyboardButton(text='🎁 Arkadaş davet et', callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ Ayarlar', callback_data='settings')
        game = InlineKeyboardButton(text='💎 Oyunu aç', callback_data='tg_mode')
    elif language == "uz":
        wal = InlineKeyboardButton(text='💰 Hamyonim', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 Super mukofot', web_app=webs)
        instruction = InlineKeyboardButton(text="🎁 do'stni taklif", callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ Sozlamalar', callback_data='settings')
        game = InlineKeyboardButton(text="💎 Ochiq o'yin", callback_data='tg_mode')
    elif language == "be":
        wal = InlineKeyboardButton(text='💰 আমার ওয়ালেট', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 সুপার প্রাইজ', web_app=webs)
        instruction = InlineKeyboardButton(text='🎁 বন্ধু আমন্ত্রণ', callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ সেটিংস', callback_data='settings')
        game = InlineKeyboardButton(text='💎 ওপেন গেম', callback_data='tg_mode')
    elif language == "hi":
        wal = InlineKeyboardButton(text='💰 मेरा वैलेट', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 सुपर पुरस्कार', web_app=webs)
        instruction = InlineKeyboardButton(text='🎁 मित्र को न्योता', callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ सेटिंग्स', callback_data='settings')
        game = InlineKeyboardButton(text='💎 खुला खेल', callback_data='tg_mode')
    else:
        wal = InlineKeyboardButton(text='💰 My Wallet', callback_data='wallet')
        jac = InlineKeyboardButton(text='💸 Super Prize', web_app=webs)
        instruction = InlineKeyboardButton(text='🎁 Invite friend', callback_data='promo_code')
        sett = InlineKeyboardButton(text='⚙️ Settings', callback_data='settings')
        game = InlineKeyboardButton(text='💎 Open Game', callback_data='tg_mode')
    return wal, jac, instruction, sett, game


def text_wallet(user_id):
    language = db.get_language(user_id)
    balance = db.get_balance(user_id)
    ton = db.get_ton(user_id)
    res = db.get_res(user_id)
    free_game = db.get_free_game(user_id)
    if balance >= 0:
        bal = balance
    else:
        bal = 0
    if ton >= 0:
        to = ton
    else:
        to = 0
    if res >= 0:
        re = res
    else:
        re = 0
    if free_game >= 0:
        fr = free_game
    else:
        fr = 0
    if language == "ru":
        text = f"💰 <b>Мой кошелек</b>\n\n<b>Баланс:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Резерв:</b> {re} PIXEL\n\n<b>Бесплатные игры:</b> {fr}"
    elif language == "id":
        text = f"💰 <b>Dompet saya</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Reserve:</b> {re} PIXEL\n\n<b>Free games:</b> {fr}"
    elif language == "es":
        text = f"💰 <b>Mi monedero</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Reserve:</b> {re} PIXEL\n\n<b>Free games:</b> {fr}"
    elif language == "ko":
        text = f"💰 <b>내 월렛</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Reserve:</b> {re} PIXEL\n\n<b>Free games:</b> {fr}"
    elif language == "it":
        text = f"💰 <b>Il mio wallet</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Reserve:</b> {re} PIXEL\n\n<b>Free games:</b> {fr}"
    elif language == "ch":
        text = f"💰 <b>我的钱包</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Reserve:</b> {re} PIXEL\n\n<b>Free games:</b> {fr}"
    elif language == "ta":
        text = f"💰 <b>我的錢包</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Reserve:</b> {re} PIXEL\n\n<b>Free games:</b> {fr}"
    elif language == "fa":
        text = f"💰 <b>کیف پول من</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Reserve:</b> {re} PIXEL\n\n<b>Free games:</b> {fr}"
    elif language == "tr":
        text = f"💰 <b>Cüzdanım</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Reserve:</b> {re} PIXEL\n\n<b>Free games:</b> {fr}"
    elif language == "uz":
        text = f"💰 <b>Hamyonim</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Reserve:</b> {re} PIXEL\n\n<b>Free games:</b> {fr}"
    elif language == "be":
        text = f"💰 <b>আমার ওয়ালেট</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Reserve:</b> {re} PIXEL\n\n<b>Free games:</b> {fr}"
    elif language == "hi":
        text = f"💰 <b>मेरा वैलेट</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Reserve:</b> {re} PIXEL\n\n<b>Free games:</b> {fr}"
    else:
        text = f"💰 <b>My Wallet</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n<b>Toncoin:</b> {to} " \
               f"TON\n\n<b>Reserve:</b> {re} PIXEL\n\n<b>Free games:</b> {fr}"
    return text


def button_wallet(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        top = InlineKeyboardButton(text='➕ Пополнить', callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ Вывести', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 Купить криптовалюту', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 Обменять', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='< Назад', callback_data='back')
    elif language == "id":
        top = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ Tarik', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 Beli kripto', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 Tukar', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='< Kembali', callback_data='back')
    elif language == "es":
        top = InlineKeyboardButton(text='➕ Recibir', callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ Enviar', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 Comprar cripto', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 Cambiar', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='< Volver', callback_data='back')
    elif language == "ko":
        top = InlineKeyboardButton(text='➕ 예치', callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ 철회하다', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 암호화폐 구매', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 환전', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='< 뒤로', callback_data='back')
    elif language == "it":
        top = InlineKeyboardButton(text='➕ Deposita', callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ Preleva', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 Compra le criptovalute', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 Scambia', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='< Indietro', callback_data='back')
    elif language == "ch":
        top = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ 提取', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 購買加密貨幣', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 交易', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='<返回', callback_data='back')
    elif language == "ta":
        top = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ 提取', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 购买加密货币', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 兌據', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='<返回', callback_data='back')
    elif language == "fa":
        top = InlineKeyboardButton(text='➕ واریز کردن', callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ کنار کشیدن', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 کریپتو بخر', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 مبادله کردن', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='< برگشت', callback_data='back')
    elif language == "tr":
        top = InlineKeyboardButton(text='➕ Yatırma', callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ Para çekme', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 Kripto satın alın', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 Takas', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='< Geri', callback_data='back')
    elif language == "uz":
        top = InlineKeyboardButton(text="➕ To'ldirish", callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ Yechib olish', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 Kripto sotib olish', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 Almashtirish', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='< Ortga', callback_data='back')
    elif language == "be":
        top = InlineKeyboardButton(text='➕ জমা', callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ প্রত্যাহার', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 ক্রিপ্টো ক্রয়', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 বিনিময়', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='< পিছনে', callback_data='back')
    elif language == "hi":
        top = InlineKeyboardButton(text='➕ जमा', callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ निकालना', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 क्रिप्टो खरीदें', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 एक्सचेंज', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='<वापस', callback_data='back')
    else:
        top = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        wit = InlineKeyboardButton(text='➡️ Withdraw', callback_data='withdraw')
        buy_ton = InlineKeyboardButton(text='💳 Buy crypto with bank card', url=config.WALLET_URL)
        ch = InlineKeyboardButton(text='🔁 Exchange', callback_data='change')
        faq = InlineKeyboardButton(text='📖 FAQ', url=config.PIXEL_FAQ)
        back = InlineKeyboardButton(text='< Back', callback_data='back')
    return top, wit, buy_ton, ch, faq, back


def text_change(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = "<b>🔁 Обменять</b>\n\nВыберите валюту, которую хотите отправить"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = "<b>🔁 Tukar</b>\n\nPilih mata uang yang ingin Anda kirim"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = "<b>🔁 Cambiar</b>\n\nSeleccione la moneda que desea enviar"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = "<b>🔁 환전</b>\n\n송금하려는 통화를 선택하세요"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = "<b>🔁 Scambia</b>\n\nSeleziona la valuta che vuoi inviare"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = "<b>🔁 交易</b>\n\n选择您想要发送的货币"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = "<b>🔁 兌據</b>\n\n選擇您想要發送的貨幣"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = "<b>🔁 مبادله کردن</b>\n\nارز مورد نظر برای ارسال را انتخاب کنید"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = "<b>🔁 Takas</b>\n\nGöndermek istediğiniz para birimini seçin"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = "<b>🔁 Almashtirish</b>\n\nYubormoqchi bo'lgan valyutangizni tanlang"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = "<b>🔁 বিনিময়</b>\n\nআপনি যে মুদ্রা পাঠাতে চান তা নির্বাচন করুন"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = "<b>🔁 एक्सचेंज</b>\n\nवह मुद्रा चुनें जिसे आप भेजना चाहते हैं"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = "<b>🔁 Exchange</b>\n\nSelect currency you want to send"
        pixel = InlineKeyboardButton(text='PIXEL', callback_data='ton_change')
        ton = InlineKeyboardButton(text='TON', callback_data='pixel_change')
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text, pixel, ton, back


def text_pixel_change(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    ton = db.get_ton(user_id)
    rate = exchange.get_price(user_id)
    a, b, c, d, e, f, g, first, last = button_pixel_change(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>Обменный курс:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Мин. сумма: {first}.0 TON</i>\n<i>Макс. сумма: {last}.0 TON</i>\n\n" \
               f"Выберите в сообщении сумму TON, которую вы хотите обменять."
        back = InlineKeyboardButton(text='< Назад', callback_data='change')
    elif language == "id":
        text = f"<b>🔁 Tukar: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>Kurs:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Min: {first}.0 TON</i>\n<i>Maks: {last}.0 TON</i>\n\n" \
               f"Pilih jumlah TON yang ingin Anda tukarkan di pesan."
        back = InlineKeyboardButton(text='< Kembali', callback_data='change')
    elif language == "es":
        text = f"<b>🔁 Cambiar: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>Tipo de cambio:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Mín.: {first}.0 TON</i>\n<i>Máx.: {last}.0 TON</i>\n\n" \
               f"Selecciona la cantidad de TON que deseas intercambiar en el mensaje."
        back = InlineKeyboardButton(text='< Volver', callback_data='change')
    elif language == "ko":
        text = f"<b>🔁 환전: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>환율:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>최소: {first}.0 TON</i>\n<i>최대: {last}.0 TON</i>\n\n" \
               f"메시지에서 교환하고 싶은 TON 수량을 선택하세요."
        back = InlineKeyboardButton(text='< 뒤로', callback_data='change')
    elif language == "it":
        text = f"<b>🔁 Scambia: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>Tasso di cambio:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Minimo: {first}.0 TON</i>\n<i>Massimo: {last}.0 TON</i>\n\n" \
               f"Seleziona nel messaggio la quantità di TON che desideri scambiare."
        back = InlineKeyboardButton(text='< Indietro', callback_data='change')
    elif language == "ch":
        text = f"<b>🔁 交易: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>匯率：</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>分鐘：{first}.0 TON</i>\n<i>最大限度：{last}.0 TON</i>\n\n" \
               f"在消息中選擇您要交換的 TON 數量。"
        back = InlineKeyboardButton(text='< 返回', callback_data='change')
    elif language == "ta":
        text = f"<b>🔁 兌據: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>汇率：</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>分钟：{first}.0 TON</i>\n<i>最大限度：{last}.0 TON</i>\n\n" \
               f"在消息中选择您要交换的 TON 数量。"
        back = InlineKeyboardButton(text='< 返回', callback_data='change')
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>قیمت ارز:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>حداقل: {first}.0 TON</i>\n<i>حداکثر: {last}.0 TON</i>\n\n" \
               f"مقدار TON مورد نظر برای تبادل را در پیام انتخاب کنید."
        back = InlineKeyboardButton(text='< برگشت', callback_data='change')
    elif language == "tr":
        text = f"<b>🔁 Takas: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>Döviz kuru:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Min: {first}.0 TON</i>\n<i>Maks: {last}.0 TON</i>\n\n" \
               f"Mesajda takas etmek istediğiniz TON miktarını seçin."
        back = InlineKeyboardButton(text='< Geri', callback_data='change')
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>Valyuta kursi:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Eng kam: {first}.0 TON</i>\n<i>Eng ko'p: {last}.0 TON</i>\n\n" \
               f"Xabarda almashtirmoqchi bo'lgan TON miqdorini tanlang."
        back = InlineKeyboardButton(text='< Ortga', callback_data='change')
    elif language == "be":
        text = f"<b>🔁 বিনিময়: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>বিনিময় হার:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>ন্যূনতম: {first}.0 TON</i>\n<i>সর্বোচ্চ: {last}.0 TON</i>\n\n" \
               f"বার্তায় আপনি যে পরিমাণ TON বিনিময় করতে চান তা নির্বাচন করুন।"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='change')
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>विनिमय दर:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>न्यूनतम: {first}.0 TON</i>\n<i>अधिकतम: {last}.0 TON</i>\n\n" \
               f"संदेश में TON की वह मात्रा चुनें जिसे आप एक्सचेंज करना चाहते हैं।"
        back = InlineKeyboardButton(text='<वापस', callback_data='change')
    else:
        text = f"<b>🔁 Exchange: TON → PIXEL</b>\n\n<b>Toncoin:</b> {ton} TON\n\n" \
               f"<b>Exchange rate:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Min: {first}.0 TON</i>\n<i>Max: {last}.0 TON</i>\n\n" \
               f"Select the amount of TON you want to exchange in the message."
        back = InlineKeyboardButton(text='< Back', callback_data='change')
    return text, back, a, b, c, d, e, f, g


def button_pixel_change(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='3 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='12 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='18 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='600 TON', callback_data='pixel_change_seventh')
        first = "3"
        last = "600"
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='5 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='50 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='1000 TON', callback_data='pixel_change_seventh')
        first = "5"
        last = "1000"
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='1 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='2 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='4 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_seventh')
        first = "1"
        last = "200"
    else:
        a = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='40 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='2000 TON', callback_data='pixel_change_seventh')
        first = "10"
        last = "2000"
    return a, b, c, d, e, f, g, first, last


def text_pixel_change_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = "<b>🔁 Обменять: TON → PIXEL</b>\n\nPIXEL поступят на ваш кошелёк в боте"
        back = InlineKeyboardButton(text='< Назад', callback_data='pixel_change')
    elif language == "id":
        text = "<b>🔁 Tukar: TON → PIXEL</b>\n\nPIXEL akan masuk ke dompet Anda di bot"
        back = InlineKeyboardButton(text='< Back', callback_data='pixel_change')
    elif language == "es":
        text = "<b>🔁 Cambiar: TON → PIXEL</b>\n\nPIXEL irá a tu billetera en el bot"
        back = InlineKeyboardButton(text='< Volver', callback_data='pixel_change')
    elif language == "ko":
        text = "<b>🔁 환전: TON → PIXEL</b>\n\nPIXEL이 봇의 지갑으로 이동합니다."
        back = InlineKeyboardButton(text='< 뒤로', callback_data='pixel_change')
    elif language == "it":
        text = "<b>🔁 Scambia: TON → PIXEL</b>\n\nPIXEL andrà nel tuo portafoglio nel bot"
        back = InlineKeyboardButton(text='< Indietro', callback_data='pixel_change')
    elif language == "ch":
        text = "<b>🔁 交易: TON → PIXEL</b>\n\nPIXEL 將進入您在機器人中的錢包"
        back = InlineKeyboardButton(text='< 返回', callback_data='pixel_change')
    elif language == "ta":
        text = "<b>🔁 兌據: TON → PIXEL</b>\n\nPIXEL 将进入您在机器人中的钱包"
        back = InlineKeyboardButton(text='< 返回', callback_data='pixel_change')
    elif language == "fa":
        text = "<b>🔁 مبادله کردن: TON → PIXEL</b>\n\nPIXEL در ربات به کیف پول شما می رود"
        back = InlineKeyboardButton(text='< برگشت', callback_data='pixel_change')
    elif language == "tr":
        text = "<b>🔁 Takas: TON → PIXEL</b>\n\nPIXEL bottaki cüzdanınıza gidecek"
        back = InlineKeyboardButton(text='< Geri', callback_data='pixel_change')
    elif language == "uz":
        text = "<b>🔁 Almashtirish: TON → PIXEL</b>\n\nPIXEL botdagi hamyoningizga o‘tadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='pixel_change')
    elif language == "be":
        text = "<b>🔁 বিনিময়: TON → PIXEL</b>\n\nPIXEL বটে আপনার ওয়ালেটে যাবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='pixel_change')
    elif language == "hi":
        text = "<b>🔁 एक्सचेंज: TON → PIXEL</b>\n\nPIXEL बॉट में आपके वॉलेट में जाएगा"
        back = InlineKeyboardButton(text='<वापस', callback_data='pixel_change')
    else:
        text = "<b>🔁 Exchange: TON → PIXEL</b>\n\nPIXEL will go to your wallet in the bot"
        back = InlineKeyboardButton(text='< Back', callback_data='pixel_change')
    return text, back


def text_pixel_change_first(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_pixel_change_first(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: TON → PIXEL</b>\n\n<b>Покупка:</b> {argument * 100}.0 PIXEL за {argument} TON"
    elif language == "id":
        text = f"<b>🔁 Tukar: TON → PIXEL</b>\n\n<b>Pembelian:</b> {argument * 100}.0 PIXEL untuk {argument} TON"
    elif language == "es":
        text = f"<b>🔁 Cambiar: TON → PIXEL</b>\n\n<b>Compra:</b> {argument * 100}.0 PIXEL por {argument} TON"
    elif language == "ko":
        text = f"<b>🔁 환전: TON → PIXEL</b>\n\n<b>구입:</b> {argument * 100}.0 PIXEL 위한 {argument} TON"
    elif language == "it":
        text = f"<b>🔁 Scambia: TON → PIXEL</b>\n\n<b>Acquistare:</b> {argument * 100}.0 PIXEL per {argument} TON"
    elif language == "ch":
        text = f"<b>🔁 交易: TON → PIXEL</b>\n\n<b>購買：</b> {argument * 100}.0 PIXEL 為了 {argument} TON"
    elif language == "ta":
        text = f"<b>🔁 兌據: TON → PIXEL</b>\n\n<b>购买：</b> {argument * 100}.0 PIXEL 为了 {argument} TON"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: TON → PIXEL</b>\n\n<b>خرید:</b> {argument * 100}.0 PIXEL برای {argument} TON"
    elif language == "tr":
        text = f"<b>🔁 Takas: TON → PIXEL</b>\n\n<b>Satın almak:</b> {argument * 100}.0 PIXEL için {argument} TON"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: TON → PIXEL</b>\n\n<b>Sotib olish:</b> {argument * 100}.0 PIXEL uchun {argument} TON"
    elif language == "be":
        text = f"<b>🔁 বিনিময়: TON → PIXEL</b>\n\n<b>ক্রয়:</b> {argument * 100}.0 PIXEL জন্য {argument} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: TON → PIXEL</b>\n\n<b>खरीदना:</b> {argument * 100}.0 PIXEL के लिए {argument} TON"
    else:
        text = f"<b>🔁 Exchange: TON → PIXEL</b>\n\n<b>Purchase:</b> {argument * 100}.0 PIXEL for {argument} TON"
    return text


def text_pixel_change_second(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_pixel_change_second(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: TON → PIXEL</b>\n\n<b>Покупка:</b> {argument * 100}.0 PIXEL за {argument} TON"
    elif language == "id":
        text = f"<b>🔁 Tukar: TON → PIXEL</b>\n\n<b>Pembelian:</b> {argument * 100}.0 PIXEL untuk {argument} TON"
    elif language == "es":
        text = f"<b>🔁 Cambiar: TON → PIXEL</b>\n\n<b>Compra:</b> {argument * 100}.0 PIXEL por {argument} TON"
    elif language == "ko":
        text = f"<b>🔁 환전: TON → PIXEL</b>\n\n<b>구입:</b> {argument * 100}.0 PIXEL 위한 {argument} TON"
    elif language == "it":
        text = f"<b>🔁 Scambia: TON → PIXEL</b>\n\n<b>Acquistare:</b> {argument * 100}.0 PIXEL per {argument} TON"
    elif language == "ch":
        text = f"<b>🔁 交易: TON → PIXEL</b>\n\n<b>購買：</b> {argument * 100}.0 PIXEL 為了 {argument} TON"
    elif language == "ta":
        text = f"<b>🔁 兌據: TON → PIXEL</b>\n\n<b>购买：</b> {argument * 100}.0 PIXEL 为了 {argument} TON"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: TON → PIXEL</b>\n\n<b>خرید:</b> {argument * 100}.0 PIXEL برای {argument} TON"
    elif language == "tr":
        text = f"<b>🔁 Takas: TON → PIXEL</b>\n\n<b>Satın almak:</b> {argument * 100}.0 PIXEL için {argument} TON"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: TON → PIXEL</b>\n\n<b>Sotib olish:</b> {argument * 100}.0 PIXEL uchun {argument} TON"
    elif language == "be":
        text = f"<b>🔁 বিনিময়: TON → PIXEL</b>\n\n<b>ক্রয়:</b> {argument * 100}.0 PIXEL জন্য {argument} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: TON → PIXEL</b>\n\n<b>खरीदना:</b> {argument * 100}.0 PIXEL के लिए {argument} TON"
    else:
        text = f"<b>🔁 Exchange: TON → PIXEL</b>\n\n<b>Purchase:</b> {argument * 100}.0 PIXEL for {argument} TON"
    return text


def text_pixel_change_third(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_pixel_change_third(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: TON → PIXEL</b>\n\n<b>Покупка:</b> {argument * 100}.0 PIXEL за {argument} TON"
    elif language == "id":
        text = f"<b>🔁 Tukar: TON → PIXEL</b>\n\n<b>Pembelian:</b> {argument * 100}.0 PIXEL untuk {argument} TON"
    elif language == "es":
        text = f"<b>🔁 Cambiar: TON → PIXEL</b>\n\n<b>Compra:</b> {argument * 100}.0 PIXEL por {argument} TON"
    elif language == "ko":
        text = f"<b>🔁 환전: TON → PIXEL</b>\n\n<b>구입:</b> {argument * 100}.0 PIXEL 위한 {argument} TON"
    elif language == "it":
        text = f"<b>🔁 Scambia: TON → PIXEL</b>\n\n<b>Acquistare:</b> {argument * 100}.0 PIXEL per {argument} TON"
    elif language == "ch":
        text = f"<b>🔁 交易: TON → PIXEL</b>\n\n<b>購買：</b> {argument * 100}.0 PIXEL 為了 {argument} TON"
    elif language == "ta":
        text = f"<b>🔁 兌據: TON → PIXEL</b>\n\n<b>购买：</b> {argument * 100}.0 PIXEL 为了 {argument} TON"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: TON → PIXEL</b>\n\n<b>خرید:</b> {argument * 100}.0 PIXEL برای {argument} TON"
    elif language == "tr":
        text = f"<b>🔁 Takas: TON → PIXEL</b>\n\n<b>Satın almak:</b> {argument * 100}.0 PIXEL için {argument} TON"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: TON → PIXEL</b>\n\n<b>Sotib olish:</b> {argument * 100}.0 PIXEL uchun {argument} TON"
    elif language == "be":
        text = f"<b>🔁 বিনিময়: TON → PIXEL</b>\n\n<b>ক্রয়:</b> {argument * 100}.0 PIXEL জন্য {argument} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: TON → PIXEL</b>\n\n<b>खरीदना:</b> {argument * 100}.0 PIXEL के लिए {argument} TON"
    else:
        text = f"<b>🔁 Exchange: TON → PIXEL</b>\n\n<b>Purchase:</b> {argument * 100}.0 PIXEL for {argument} TON"
    return text


def text_pixel_change_fourth(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_pixel_change_fourth(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: TON → PIXEL</b>\n\n<b>Покупка:</b> {argument * 100}.0 PIXEL за {argument} TON"
    elif language == "id":
        text = f"<b>🔁 Tukar: TON → PIXEL</b>\n\n<b>Pembelian:</b> {argument * 100}.0 PIXEL untuk {argument} TON"
    elif language == "es":
        text = f"<b>🔁 Cambiar: TON → PIXEL</b>\n\n<b>Compra:</b> {argument * 100}.0 PIXEL por {argument} TON"
    elif language == "ko":
        text = f"<b>🔁 환전: TON → PIXEL</b>\n\n<b>구입:</b> {argument * 100}.0 PIXEL 위한 {argument} TON"
    elif language == "it":
        text = f"<b>🔁 Scambia: TON → PIXEL</b>\n\n<b>Acquistare:</b> {argument * 100}.0 PIXEL per {argument} TON"
    elif language == "ch":
        text = f"<b>🔁 交易: TON → PIXEL</b>\n\n<b>購買：</b> {argument * 100}.0 PIXEL 為了 {argument} TON"
    elif language == "ta":
        text = f"<b>🔁 兌據: TON → PIXEL</b>\n\n<b>购买：</b> {argument * 100}.0 PIXEL 为了 {argument} TON"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: TON → PIXEL</b>\n\n<b>خرید:</b> {argument * 100}.0 PIXEL برای {argument} TON"
    elif language == "tr":
        text = f"<b>🔁 Takas: TON → PIXEL</b>\n\n<b>Satın almak:</b> {argument * 100}.0 PIXEL için {argument} TON"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: TON → PIXEL</b>\n\n<b>Sotib olish:</b> {argument * 100}.0 PIXEL uchun {argument} TON"
    elif language == "be":
        text = f"<b>🔁 বিনিময়: TON → PIXEL</b>\n\n<b>ক্রয়:</b> {argument * 100}.0 PIXEL জন্য {argument} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: TON → PIXEL</b>\n\n<b>खरीदना:</b> {argument * 100}.0 PIXEL के लिए {argument} TON"
    else:
        text = f"<b>🔁 Exchange: TON → PIXEL</b>\n\n<b>Purchase:</b> {argument * 100}.0 PIXEL for {argument} TON"
    return text


def text_pixel_change_fifth(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_pixel_change_fifth(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: TON → PIXEL</b>\n\n<b>Покупка:</b> {argument * 100}.0 PIXEL за {argument} TON"
    elif language == "id":
        text = f"<b>🔁 Tukar: TON → PIXEL</b>\n\n<b>Pembelian:</b> {argument * 100}.0 PIXEL untuk {argument} TON"
    elif language == "es":
        text = f"<b>🔁 Cambiar: TON → PIXEL</b>\n\n<b>Compra:</b> {argument * 100}.0 PIXEL por {argument} TON"
    elif language == "ko":
        text = f"<b>🔁 환전: TON → PIXEL</b>\n\n<b>구입:</b> {argument * 100}.0 PIXEL 위한 {argument} TON"
    elif language == "it":
        text = f"<b>🔁 Scambia: TON → PIXEL</b>\n\n<b>Acquistare:</b> {argument * 100}.0 PIXEL per {argument} TON"
    elif language == "ch":
        text = f"<b>🔁 交易: TON → PIXEL</b>\n\n<b>購買：</b> {argument * 100}.0 PIXEL 為了 {argument} TON"
    elif language == "ta":
        text = f"<b>🔁 兌據: TON → PIXEL</b>\n\n<b>购买：</b> {argument * 100}.0 PIXEL 为了 {argument} TON"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: TON → PIXEL</b>\n\n<b>خرید:</b> {argument * 100}.0 PIXEL برای {argument} TON"
    elif language == "tr":
        text = f"<b>🔁 Takas: TON → PIXEL</b>\n\n<b>Satın almak:</b> {argument * 100}.0 PIXEL için {argument} TON"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: TON → PIXEL</b>\n\n<b>Sotib olish:</b> {argument * 100}.0 PIXEL uchun {argument} TON"
    elif language == "be":
        text = f"<b>🔁 বিনিময়: TON → PIXEL</b>\n\n<b>ক্রয়:</b> {argument * 100}.0 PIXEL জন্য {argument} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: TON → PIXEL</b>\n\n<b>खरीदना:</b> {argument * 100}.0 PIXEL के लिए {argument} TON"
    else:
        text = f"<b>🔁 Exchange: TON → PIXEL</b>\n\n<b>Purchase:</b> {argument * 100}.0 PIXEL for {argument} TON"
    return text


def text_pixel_change_sixth(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_pixel_change_sixth(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: TON → PIXEL</b>\n\n<b>Покупка:</b> {argument * 100}.0 PIXEL за {argument} TON"
    elif language == "id":
        text = f"<b>🔁 Tukar: TON → PIXEL</b>\n\n<b>Pembelian:</b> {argument * 100}.0 PIXEL untuk {argument} TON"
    elif language == "es":
        text = f"<b>🔁 Cambiar: TON → PIXEL</b>\n\n<b>Compra:</b> {argument * 100}.0 PIXEL por {argument} TON"
    elif language == "ko":
        text = f"<b>🔁 환전: TON → PIXEL</b>\n\n<b>구입:</b> {argument * 100}.0 PIXEL 위한 {argument} TON"
    elif language == "it":
        text = f"<b>🔁 Scambia: TON → PIXEL</b>\n\n<b>Acquistare:</b> {argument * 100}.0 PIXEL per {argument} TON"
    elif language == "ch":
        text = f"<b>🔁 交易: TON → PIXEL</b>\n\n<b>購買：</b> {argument * 100}.0 PIXEL 為了 {argument} TON"
    elif language == "ta":
        text = f"<b>🔁 兌據: TON → PIXEL</b>\n\n<b>购买：</b> {argument * 100}.0 PIXEL 为了 {argument} TON"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: TON → PIXEL</b>\n\n<b>خرید:</b> {argument * 100}.0 PIXEL برای {argument} TON"
    elif language == "tr":
        text = f"<b>🔁 Takas: TON → PIXEL</b>\n\n<b>Satın almak:</b> {argument * 100}.0 PIXEL için {argument} TON"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: TON → PIXEL</b>\n\n<b>Sotib olish:</b> {argument * 100}.0 PIXEL uchun {argument} TON"
    elif language == "be":
        text = f"<b>🔁 বিনিময়: TON → PIXEL</b>\n\n<b>ক্রয়:</b> {argument * 100}.0 PIXEL জন্য {argument} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: TON → PIXEL</b>\n\n<b>खरीदना:</b> {argument * 100}.0 PIXEL के लिए {argument} TON"
    else:
        text = f"<b>🔁 Exchange: TON → PIXEL</b>\n\n<b>Purchase:</b> {argument * 100}.0 PIXEL for {argument} TON"
    return text


def text_pixel_change_seventh(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_pixel_change_seventh(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: TON → PIXEL</b>\n\n<b>Покупка:</b> {argument * 100}.0 PIXEL за {argument} TON"
    elif language == "id":
        text = f"<b>🔁 Tukar: TON → PIXEL</b>\n\n<b>Pembelian:</b> {argument * 100}.0 PIXEL untuk {argument} TON"
    elif language == "es":
        text = f"<b>🔁 Cambiar: TON → PIXEL</b>\n\n<b>Compra:</b> {argument * 100}.0 PIXEL por {argument} TON"
    elif language == "ko":
        text = f"<b>🔁 환전: TON → PIXEL</b>\n\n<b>구입:</b> {argument * 100}.0 PIXEL 위한 {argument} TON"
    elif language == "it":
        text = f"<b>🔁 Scambia: TON → PIXEL</b>\n\n<b>Acquistare:</b> {argument * 100}.0 PIXEL per {argument} TON"
    elif language == "ch":
        text = f"<b>🔁 交易: TON → PIXEL</b>\n\n<b>購買：</b> {argument * 100}.0 PIXEL 為了 {argument} TON"
    elif language == "ta":
        text = f"<b>🔁 兌據: TON → PIXEL</b>\n\n<b>购买：</b> {argument * 100}.0 PIXEL 为了 {argument} TON"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: TON → PIXEL</b>\n\n<b>خرید:</b> {argument * 100}.0 PIXEL برای {argument} TON"
    elif language == "tr":
        text = f"<b>🔁 Takas: TON → PIXEL</b>\n\n<b>Satın almak:</b> {argument * 100}.0 PIXEL için {argument} TON"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: TON → PIXEL</b>\n\n<b>Sotib olish:</b> {argument * 100}.0 PIXEL uchun {argument} TON"
    elif language == "be":
        text = f"<b>🔁 বিনিময়: TON → PIXEL</b>\n\n<b>ক্রয়:</b> {argument * 100}.0 PIXEL জন্য {argument} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: TON → PIXEL</b>\n\n<b>खरीदना:</b> {argument * 100}.0 PIXEL के लिए {argument} TON"
    else:
        text = f"<b>🔁 Exchange: TON → PIXEL</b>\n\n<b>Purchase:</b> {argument * 100}.0 PIXEL for {argument} TON"
    return text


def button_pixel_first_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='pixel_change_first_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='pixel_change_first_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='pixel_change_first_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='pixel_change_first_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='pixel_change_first_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='pixel_change_first_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='pixel_change_first_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='pixel_change_first_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='pixel_change_first_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='pixel_change_first_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='pixel_change_first_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='pixel_change_first_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='pixel_change_first_finish')
    return done


def button_pixel_second_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='pixel_change_second_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='pixel_change_second_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='pixel_change_second_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='pixel_change_second_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='pixel_change_second_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='pixel_change_second_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='pixel_change_second_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='pixel_change_second_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='pixel_change_second_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='pixel_change_second_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='pixel_change_second_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='pixel_change_second_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='pixel_change_second_finish')
    return done


def button_pixel_third_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='pixel_change_third_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='pixel_change_third_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='pixel_change_third_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='pixel_change_third_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='pixel_change_third_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='pixel_change_third_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='pixel_change_third_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='pixel_change_third_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='pixel_change_third_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='pixel_change_third_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='pixel_change_third_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='pixel_change_third_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='pixel_change_third_finish')
    return done


def button_pixel_fourth_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='pixel_change_fourth_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='pixel_change_fourth_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='pixel_change_fourth_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='pixel_change_fourth_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='pixel_change_fourth_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='pixel_change_fourth_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='pixel_change_fourth_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='pixel_change_fourth_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='pixel_change_fourth_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='pixel_change_fourth_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='pixel_change_fourth_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='pixel_change_fourth_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='pixel_change_fourth_finish')
    return done


def button_pixel_fifth_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='pixel_change_fifth_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='pixel_change_fifth_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='pixel_change_fifth_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='pixel_change_fifth_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='pixel_change_fifth_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='pixel_change_fifth_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='pixel_change_fifth_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='pixel_change_fifth_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='pixel_change_fifth_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='pixel_change_fifth_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='pixel_change_fifth_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='pixel_change_fifth_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='pixel_change_fifth_finish')
    return done


def button_pixel_sixth_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='pixel_change_sixth_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='pixel_change_sixth_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='pixel_change_sixth_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='pixel_change_sixth_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='pixel_change_sixth_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='pixel_change_sixth_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='pixel_change_sixth_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='pixel_change_sixth_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='pixel_change_sixth_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='pixel_change_sixth_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='pixel_change_sixth_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='pixel_change_sixth_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='pixel_change_sixth_finish')
    return done


def button_pixel_seventh_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='pixel_change_seventh_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='pixel_change_seventh_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='pixel_change_seventh_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='pixel_change_seventh_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='pixel_change_seventh_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='pixel_change_seventh_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='pixel_change_seventh_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='pixel_change_seventh_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='pixel_change_seventh_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='pixel_change_seventh_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='pixel_change_seventh_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='pixel_change_seventh_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='pixel_change_seventh_finish')
    return done


def back_pixel_change(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = "На вашем балансе недостаточно средств. Пожалуйста, пополните свой кошелек."
        dep = InlineKeyboardButton(text='➕ Пополнить', callback_data='deposit')
        back = InlineKeyboardButton(text='< Назад', callback_data='pixel_change')
    elif language == "id":
        text = "Saldo Anda tidak cukup. Silakan depositkan uang kripto ke dompet Anda."
        dep = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        back = InlineKeyboardButton(text='< Kembali', callback_data='pixel_change')
    elif language == "es":
        text = "Su saldo es insuficiente. Por favor, deposite criptomonedas en su monedero."
        dep = InlineKeyboardButton(text='➕ Recibir', callback_data='deposit')
        back = InlineKeyboardButton(text='< Volver', callback_data='pixel_change')
    elif language == "ko":
        text = "잔액이 부족합니다. 월렛에 암호화폐를 충전하세요."
        dep = InlineKeyboardButton(text='➕ 예치', callback_data='deposit')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='pixel_change')
    elif language == "it":
        text = "Il tuo saldo è insufficiente. Per favore deposita le criptovalute nel tuo wallet."
        dep = InlineKeyboardButton(text='➕ Deposita', callback_data='deposit')
        back = InlineKeyboardButton(text='< Indietro', callback_data='pixel_change')
    elif language == "ch":
        text = "您的余额不足。请向您的钱包里存入加密货币。"
        dep = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        back = InlineKeyboardButton(text='< 返回', callback_data='pixel_change')
    elif language == "ta":
        text = "您的餘額不足。請向您的錢包裡存入加密貨幣。"
        dep = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        back = InlineKeyboardButton(text='< 返回', callback_data='pixel_change')
    elif language == "fa":
        text = "موجودی حساب شما ناکافی است. لطفا به کیف پول خود کریپتو واریز کنید."
        dep = InlineKeyboardButton(text='➕ واریز کردن', callback_data='deposit')
        back = InlineKeyboardButton(text='< برگشت', callback_data='pixel_change')
    elif language == "tr":
        text = "Bakiyeniz yetersiz. Lütfen cüzdanınıza kripto para yatırın."
        dep = InlineKeyboardButton(text='➕ Yatırma', callback_data='deposit')
        back = InlineKeyboardButton(text='< Geri', callback_data='pixel_change')
    elif language == "uz":
        text = "Hisobingizda mablag’ yetarli emas. Iltimos, hamyoningizga kriptovalyuta kiriting."
        dep = InlineKeyboardButton(text="'➕ To'ldirish", callback_data='deposit')
        back = InlineKeyboardButton(text='< Ortga', callback_data='pixel_change')
    elif language == "be":
        text = "আপনার ব্যালেন্স অপর্যাপ্ত। অনুগ্রহ করে, আপনার ওয়ালেটে ক্রিপ্টো জমা করুন।"
        dep = InlineKeyboardButton(text='➕ জমা', callback_data='deposit')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='pixel_change')
    elif language == "hi":
        text = "आपका बैलेंस अपर्याप्त है। कृपया, क्रिप्टो को अपने वैलेट में जमा करें।"
        dep = InlineKeyboardButton(text='➕ जमा', callback_data='deposit')
        back = InlineKeyboardButton(text='<वापस', callback_data='pixel_change')
    else:
        text = "Your balance is insufficient. Please, deposit crypto into your wallet."
        dep = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        back = InlineKeyboardButton(text='< Back', callback_data='pixel_change')
    return text, dep, back


def back_to_pixel(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        back = InlineKeyboardButton(text='< Назад', callback_data='pixel_change')
    elif language == "id":
        back = InlineKeyboardButton(text='< Kembali', callback_data='pixel_change')
    elif language == "es":
        back = InlineKeyboardButton(text='< Volver', callback_data='pixel_change')
    elif language == "ko":
        back = InlineKeyboardButton(text='< 뒤로', callback_data='pixel_change')
    elif language == "it":
        back = InlineKeyboardButton(text='< Indietro', callback_data='pixel_change')
    elif language == "ch":
        back = InlineKeyboardButton(text='< 返回', callback_data='pixel_change')
    elif language == "ta":
        back = InlineKeyboardButton(text='< 返回', callback_data='pixel_change')
    elif language == "fa":
        back = InlineKeyboardButton(text='< برگشت', callback_data='pixel_change')
    elif language == "tr":
        back = InlineKeyboardButton(text='< Geri', callback_data='pixel_change')
    elif language == "uz":
        back = InlineKeyboardButton(text='< Ortga', callback_data='pixel_change')
    elif language == "be":
        back = InlineKeyboardButton(text='< পিছনে', callback_data='pixel_change')
    elif language == "hi":
        back = InlineKeyboardButton(text='<वापस', callback_data='pixel_change')
    else:
        back = InlineKeyboardButton(text='< Back', callback_data='pixel_change')
    return back


def button_pixel_change_first(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_first_done')
        b = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='12 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='18 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='600 TON', callback_data='pixel_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_first_done')
        b = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='50 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='1000 TON', callback_data='pixel_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_first_done')
        b = InlineKeyboardButton(text='2 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='4 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_seventh')
    else:
        a = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_first_done')
        b = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='40 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='2000 TON', callback_data='pixel_change_seventh')
    return a, b, c, d, e, f, g


def button_pixel_change_second(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='3 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_second_done')
        c = InlineKeyboardButton(text='12 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='18 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='600 TON', callback_data='pixel_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='5 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_second_done')
        c = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='50 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='1000 TON', callback_data='pixel_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='1 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_second_done')
        c = InlineKeyboardButton(text='4 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_seventh')
    else:
        a = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_second_done')
        c = InlineKeyboardButton(text='40 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='2000 TON', callback_data='pixel_change_seventh')
    return a, b, c, d, e, f, g


def button_pixel_change_third(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='3 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_third_done')
        d = InlineKeyboardButton(text='18 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='600 TON', callback_data='pixel_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='5 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_third_done')
        d = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='50 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='1000 TON', callback_data='pixel_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='1 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='2 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_third_done')
        d = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_seventh')
    else:
        a = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_third_done')
        d = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='2000 TON', callback_data='pixel_change_seventh')
    return a, b, c, d, e, f, g


def button_ton_change(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='300 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='1200 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='1800 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='60000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='500 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='5000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='100000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='100 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='200 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='400 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_seventh')
    else:
        a = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='4000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='200000 PIXEL', callback_data='ton_change_seventh')
    return a, b, c, d, e, f, g


def text_ton_change(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    balance = db.get_balance(user_id)
    minimum, maximum = lists.min_max_pixel(user_id)
    # rate = exchange.get_price(user_id)
    rate = exchange.get_price(user_id)
    bal = balance
    if bal < 0:
        bal = 0
    if language == "ru":
        text = f"<b>🔁 Обменять: PIXEL → TON</b>\n\n<b>Баланс:</b> {bal} PIXEL\n\n" \
               f"<b>Обменный курс:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Мин. сумма: {minimum}.0 PIXEL</i>\n" \
               f"<i>Макс. сумма: {maximum}.0 PIXEL</i>\n\nВыберите в сообщении сумму TON, которую вы хотите обменять."
    elif language == "id":
        text = f"<b>🔁 Tukar: PIXEL → TON</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n" \
               f"<b>Kurs:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Min: {minimum}.0 PIXEL</i>\n" \
               f"<i>Maks: {maximum}.0 PIXEL</i>\n\nPilih jumlah TON yang ingin Anda tukarkan di pesan."
    elif language == "es":
        text = f"<b>🔁 Cambiar: PIXEL → TON</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n" \
               f"<b>Tipo de cambio:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Mín.: {minimum}.0 PIXEL</i>\n" \
               f"<i>Máx.: {maximum}.0 PIXEL</i>\n\nSelect the amount of TON you want to exchange in the message."
    elif language == "ko":
        text = f"<b>🔁 환전: PIXEL → TON</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n" \
               f"<b>환율:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>최소: {minimum}.0 PIXEL</i>\n" \
               f"<i>최대: {maximum}.0 PIXEL</i>\n\n메시지에서 교환하고 싶은 TON 수량을 선택하세요."
    elif language == "it":
        text = f"<b>🔁 Scambia: PIXEL → TON</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n" \
               f"<b>Tasso di cambio:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Minimo: {minimum}.0 PIXEL</i>\n" \
               f"<i>Massimo: {maximum}.0 PIXEL</i>\n\nSeleziona nel messaggio la quantità di TON che desideri scambiare."
    elif language == "ch":
        text = f"<b>🔁 交易: PIXEL → TON</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n" \
               f"<b>匯率：</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>分鐘：{minimum}.0 PIXEL</i>\n" \
               f"<i>最大限度：{maximum}.0 PIXEL</i>\n\n在消息中選擇您要交換的 TON 數量。"
    elif language == "ta":
        text = f"<b>🔁 兌據: PIXEL → TON</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n" \
               f"<b>汇率：</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>分钟：{minimum}.0 PIXEL</i>\n" \
               f"<i>最大限度：{maximum}.0 PIXEL</i>\n\n在消息中选择您要交换的 TON 数量。"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: PIXEL → TON</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n" \
               f"<b>قیمت ارز:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>حداقل: {minimum}.0 PIXEL</i>\n" \
               f"<i>حداکثر: {maximum}.0 PIXEL</i>\n\nمقدار TON مورد نظر برای تبادل را در پیام انتخاب کنید."
    elif language == "tr":
        text = f"<b>🔁 Takas: PIXEL → TON</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n" \
               f"<b>Döviz kuru:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Min: {minimum}.0 PIXEL</i>\n" \
               f"<i>Maks: {maximum}.0 PIXEL</i>\n\nMesajda takas etmek istediğiniz TON miktarını seçin."
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: PIXEL → TON</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n" \
               f"<b>Valyuta kursi:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Eng kam: {minimum}.0 PIXEL</i>\n" \
               f"<i>Eng ko'p: {maximum}.0 PIXEL</i>\n\nXabarda almashtirmoqchi bo'lgan TON miqdorini tanlang."
    elif language == "be":
        text = f"<b>🔁 বিনিময়: PIXEL → TON</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n" \
               f"<b>বিনিময় হার:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>ন্যূনতম: {minimum}.0 PIXEL</i>\n" \
               f"<i>সর্বোচ্চ: {maximum}.0 PIXEL</i>\n\nবার্তায় আপনি যে পরিমাণ TON বিনিময় করতে চান তা নির্বাচন করুন।"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: PIXEL → TON</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n" \
               f"<b>विनिमय दर:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>न्यूनतम: {minimum}.0 PIXEL</i>\n" \
               f"<i>अधिकतम: {maximum}.0 PIXEL</i>\n\nसंदेश में TON की वह मात्रा चुनें जिसे आप एक्सचेंज करना चाहते हैं।"
    else:
        text = f"<b>🔁 Exchange: PIXEL → TON</b>\n\n<b>Balance:</b> {bal} PIXEL\n\n" \
               f"<b>Exchange rate:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n<i>Min: {minimum}.0 PIXEL</i>\n" \
               f"<i>Max: {maximum}.0 PIXEL</i>\n\nSelect the amount of TON you want to exchange in the message."
    return text


def button_ton_change_first(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_first_done')
        b = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='1200 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='1800 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='60000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_first_done')
        b = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='5000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='100000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_first_done')
        b = InlineKeyboardButton(text='200 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='400 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_seventh')
    else:
        a = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_first_done')
        b = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='4000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='200000 PIXEL', callback_data='ton_change_seventh')
    return a, b, c, d, e, f, g


def back_to_ton_change(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_change')
    elif language == "id":
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_change')
    elif language == "es":
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_change')
    elif language == "ko":
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_change')
    elif language == "it":
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_change')
    elif language == "ch":
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_change')
    elif language == "ta":
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_change')
    elif language == "fa":
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_change')
    elif language == "tr":
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_change')
    elif language == "uz":
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_change')
    elif language == "be":
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_change')
    elif language == "hi":
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_change')
    else:
        back = InlineKeyboardButton(text='< Back', callback_data='ton_change')
    return back


def back_ton_change(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = "На вашем балансе недостаточно средств. Пожалуйста, пополните свой кошелек."
        dep = InlineKeyboardButton(text='➕ Пополнить', callback_data='deposit')
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_change')
    elif language == "id":
        text = "Saldo Anda tidak cukup. Silakan depositkan uang kripto ke dompet Anda."
        dep = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_change')
    elif language == "es":
        text = "Su saldo es insuficiente. Por favor, deposite criptomonedas en su monedero."
        dep = InlineKeyboardButton(text='➕ Recibir', callback_data='deposit')
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_change')
    elif language == "ko":
        text = "잔액이 부족합니다. 월렛에 암호화폐를 충전하세요."
        dep = InlineKeyboardButton(text='➕ 예치', callback_data='deposit')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_change')
    elif language == "it":
        text = "Il tuo saldo è insufficiente. Per favore deposita le criptovalute nel tuo wallet."
        dep = InlineKeyboardButton(text='➕ Deposita', callback_data='deposit')
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_change')
    elif language == "ch":
        text = "您的余额不足。请向您的钱包里存入加密货币。"
        dep = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_change')
    elif language == "ta":
        text = "您的餘額不足。請向您的錢包裡存入加密貨幣。"
        dep = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_change')
    elif language == "fa":
        text = "موجودی حساب شما ناکافی است. لطفا به کیف پول خود کریپتو واریز کنید."
        dep = InlineKeyboardButton(text='➕ واریز کردن', callback_data='deposit')
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_change')
    elif language == "tr":
        text = "Bakiyeniz yetersiz. Lütfen cüzdanınıza kripto para yatırın."
        dep = InlineKeyboardButton(text='➕ Yatırma', callback_data='deposit')
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_change')
    elif language == "uz":
        text = "Hisobingizda mablag’ yetarli emas. Iltimos, hamyoningizga kriptovalyuta kiriting."
        dep = InlineKeyboardButton(text="'➕ To'ldirish", callback_data='deposit')
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_change')
    elif language == "be":
        text = "আপনার ব্যালেন্স অপর্যাপ্ত। অনুগ্রহ করে, আপনার ওয়ালেটে ক্রিপ্টো জমা করুন।"
        dep = InlineKeyboardButton(text='➕ জমা', callback_data='deposit')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_change')
    elif language == "hi":
        text = "आपका बैलेंस अपर्याप्त है। कृपया, क्रिप्टो को अपने वैलेट में जमा करें।"
        dep = InlineKeyboardButton(text='➕ जमा', callback_data='deposit')
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_change')
    else:
        text = "Your balance is insufficient. Please, deposit crypto into your wallet."
        dep = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        back = InlineKeyboardButton(text='< Back', callback_data='ton_change')
    return text, dep, back


def text_ton_change_all_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = "<b>🔁 Обменять: PIXEL → TON</b>\n\nTON поступят на ваш кошелек в боте"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_change')
    elif language == "id":
        text = "<b>🔁 Tukar: PIXEL → TON</b>\n\nTON akan dikirim ke dompet Anda"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_change')
    elif language == "es":
        text = "<b>🔁 Cambiar: PIXEL → TON</b>\n\nTON se enviará a tu billetera"
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_change')
    elif language == "ko":
        text = "<b>🔁 환전: PIXEL → TON</b>\n\nTON이 지갑으로 전송됩니다."
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_change')
    elif language == "it":
        text = "<b>🔁 Scambia: PIXEL → TON</b>\n\nTON verrà inviato al tuo portafoglio"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_change')
    elif language == "ch":
        text = "<b>🔁 交易: PIXEL → TON</b>\n\nTON 將發送至您的錢包"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_change')
    elif language == "ta":
        text = "<b>🔁 兌據: PIXEL → TON</b>\n\nTON 将发送至您的钱包"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_change')
    elif language == "fa":
        text = "<b>🔁 مبادله کردن: PIXEL → TON</b>\n\nTON به کیف پول شما ارسال می شود"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_change')
    elif language == "tr":
        text = "<b>🔁 Tukar: PIXEL → TON</b>\n\nTON cüzdanınıza gönderilecek"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_change')
    elif language == "uz":
        text = "<b>🔁 Almashtirish: PIXEL → TON</b>\n\nTON hamyoningizga yuboriladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='ton_change')
    elif language == "be":
        text = "<b>🔁 বিনিময়: PIXEL → TON</b>\n\nTON আপনার ওয়ালেটে পাঠানো হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_change')
    elif language == "hi":
        text = "<b>🔁 एक्सचेंज: PIXEL → TON</b>\n\nTON आपके वॉलेट में भेज दिया जाएगा"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_change')
    else:
        text = "<b>🔁 Exchange: PIXEL → TON</b>\n\nTON will be sent to your wallet"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_change')
    return text, back


def button_ton_change_first_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='ton_change_first_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='ton_change_first_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='ton_change_first_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='ton_change_first_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='ton_change_first_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='ton_change_first_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='ton_change_first_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='ton_change_first_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='ton_change_first_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='ton_change_first_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='ton_change_first_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='ton_change_first_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='ton_change_first_finish')
    return done


def button_ton_change_second_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='ton_change_second_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='ton_change_second_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='ton_change_second_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='ton_change_second_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='ton_change_second_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='ton_change_second_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='ton_change_second_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='ton_change_second_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='ton_change_second_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='ton_change_second_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='ton_change_second_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='ton_change_second_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='ton_change_second_finish')
    return done


def button_ton_change_third_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='ton_change_third_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='ton_change_third_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='ton_change_third_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='ton_change_third_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='ton_change_third_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='ton_change_third_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='ton_change_third_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='ton_change_third_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='ton_change_third_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='ton_change_third_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='ton_change_third_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='ton_change_third_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='ton_change_third_finish')
    return done


def button_ton_change_fourth_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='ton_change_fourth_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='ton_change_fourth_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='ton_change_fourth_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='ton_change_fourth_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='ton_change_fourth_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='ton_change_fourth_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='ton_change_fourth_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='ton_change_fourth_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='ton_change_fourth_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='ton_change_fourth_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='ton_change_fourth_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='ton_change_fourth_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='ton_change_fourth_finish')
    return done


def button_ton_change_fifth_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='ton_change_fifth_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='ton_change_fifth_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='ton_change_fifth_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='ton_change_fifth_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='ton_change_fifth_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='ton_change_fifth_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='ton_change_fifth_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='ton_change_fifth_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='ton_change_fifth_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='ton_change_fifth_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='ton_change_fifth_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='ton_change_fifth_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='ton_change_fifth_finish')
    return done


def button_ton_change_sixth_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='ton_change_sixth_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='ton_change_sixth_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='ton_change_sixth_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='ton_change_sixth_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='ton_change_sixth_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='ton_change_sixth_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='ton_change_sixth_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='ton_change_sixth_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='ton_change_sixth_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='ton_change_sixth_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='ton_change_sixth_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='ton_change_sixth_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='ton_change_sixth_finish')
    return done


def button_ton_change_seventh_done(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        done = InlineKeyboardButton(text='✅ Использовать кошелек бота', callback_data='ton_change_seventh_finish')
    elif language == "id":
        done = InlineKeyboardButton(text='✅ Gunakan bot dompet', callback_data='ton_change_seventh_finish')
    elif language == "es":
        done = InlineKeyboardButton(text='✅ Usar monedero bot', callback_data='ton_change_seventh_finish')
    elif language == "ko":
        done = InlineKeyboardButton(text='✅ 봇 지갑 사용', callback_data='ton_change_seventh_finish')
    elif language == "it":
        done = InlineKeyboardButton(text='✅ Usa il bot wallet', callback_data='ton_change_seventh_finish')
    elif language == "ch":
        done = InlineKeyboardButton(text='✅ 使用機器人錢包', callback_data='ton_change_seventh_finish')
    elif language == "ta":
        done = InlineKeyboardButton(text='✅ 使用机器人钱包', callback_data='ton_change_seventh_finish')
    elif language == "fa":
        done = InlineKeyboardButton(text='✅ از کیف پول ربات استفاده کنید', callback_data='ton_change_seventh_finish')
    elif language == "tr":
        done = InlineKeyboardButton(text='✅ Bot cüzdanını kullan', callback_data='ton_change_seventh_finish')
    elif language == "uz":
        done = InlineKeyboardButton(text='✅ Bot hamyonidan foydalaning', callback_data='ton_change_seventh_finish')
    elif language == "be":
        done = InlineKeyboardButton(text='✅ বট ওয়ালেট ব্যবহার করুন', callback_data='ton_change_seventh_finish')
    elif language == "hi":
        done = InlineKeyboardButton(text='✅ बॉट वॉलेट का प्रयोग करें', callback_data='ton_change_seventh_finish')
    else:
        done = InlineKeyboardButton(text='✅ Use bot wallet', callback_data='ton_change_seventh_finish')
    return done


def text_no_res(user_id):
    language = db.get_language(user_id)
    res = db.get_res(user_id)
    if res < 0:
        res = 0
    bal = free_skip - res
    if language == "ru":
        text = f"На вашем резерве недостаёт {bal} PIXEL. Пожалуйста, пополните свой кошелек."
        dep = InlineKeyboardButton(text='➕ Пополнить', callback_data='deposit')
        back = InlineKeyboardButton(text='< Назад', callback_data='tg_mode')
    elif language == "id":
        text = f"Cadangan Anda hilang {bal} PIXEL. Silakan depositkan uang kripto ke dompet Anda."
        dep = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        back = InlineKeyboardButton(text='< Kembali', callback_data='tg_mode')
    elif language == "es":
        text = f"Falta tu reserva {bal} PIXEL. Por favor, deposite criptomonedas en su monedero."
        dep = InlineKeyboardButton(text='➕ Recibir', callback_data='deposit')
        back = InlineKeyboardButton(text='< Volver', callback_data='tg_mode')
    elif language == "ko":
        text = f"귀하의 예금이 누락되었습니다 {bal} PIXEL. 월렛에 암호화폐를 충전하세요."
        dep = InlineKeyboardButton(text='➕ 예치', callback_data='deposit')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='tg_mode')
    elif language == "it":
        text = f"Manca la tua riserva {bal} PIXEL. Per favore deposita le criptovalute nel tuo wallet."
        dep = InlineKeyboardButton(text='➕ Deposita', callback_data='deposit')
        back = InlineKeyboardButton(text='< Indietro', callback_data='tg_mode')
    elif language == "ch":
        text = f"您的儲備缺失 {bal} PIXEL. 请向您的钱包里存入加密货币。"
        dep = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        back = InlineKeyboardButton(text='< 返回', callback_data='tg_mode')
    elif language == "ta":
        text = f"您的储备缺失 {bal} PIXEL. 請向您的錢包裡存入加密貨幣。"
        dep = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        back = InlineKeyboardButton(text='< 返回', callback_data='tg_mode')
    elif language == "fa":
        text = f"ذخیره شما گم شده است {bal} PIXEL. لطفا به کیف پول خود کریپتو واریز کنید."
        dep = InlineKeyboardButton(text='➕ واریز کردن', callback_data='deposit')
        back = InlineKeyboardButton(text='< برگشت', callback_data='tg_mode')
    elif language == "tr":
        text = f"Rezerviniz eksik {bal} PIXEL. Lütfen cüzdanınıza kripto para yatırın."
        dep = InlineKeyboardButton(text='➕ Yatırma', callback_data='deposit')
        back = InlineKeyboardButton(text='< Geri', callback_data='tg_mode')
    elif language == "uz":
        text = f"Sizning zaxirangiz yo'q {bal} PIXEL. Iltimos, hamyoningizga kriptovalyuta kiriting."
        dep = InlineKeyboardButton(text="'➕ To'ldirish", callback_data='deposit')
        back = InlineKeyboardButton(text='< Ortga', callback_data='tg_mode')
    elif language == "be":
        text = f"আপনার রিজার্ভ অনুপস্থিত {bal} PIXEL. অনুগ্রহ করে, আপনার ওয়ালেটে ক্রিপ্টো জমা করুন।"
        dep = InlineKeyboardButton(text='➕ জমা', callback_data='deposit')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='tg_mode')
    elif language == "hi":
        text = f"आपका रिज़र्व गायब है {bal} PIXEL. कृपया, क्रिप्टो को अपने वैलेट में जमा करें।"
        dep = InlineKeyboardButton(text='➕ जमा', callback_data='deposit')
        back = InlineKeyboardButton(text='<वापस', callback_data='tg_mode')
    else:
        text = f"Your reserve is missing {bal} PIXEL. Please, deposit crypto into your wallet."
        dep = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        back = InlineKeyboardButton(text='< Back', callback_data='tg_mode')
    return text, dep, back


def text_no_bal(user_id, strike):
    language = db.get_language(user_id)
    balance = db.get_balance(user_id)
    if balance < 0:
        balance = 0
    bal = strike - balance
    if language == "ru":
        text = f"На вашем балансе недостаёт {bal} PIXEL. Пожалуйста, пополните свой кошелек."
        dep = InlineKeyboardButton(text='➕ Пополнить', callback_data='deposit')
        back = InlineKeyboardButton(text='< Назад', callback_data='tg_mode')
    elif language == "id":
        text = f"Saldo Anda hilang {bal} PIXEL. Silakan depositkan uang kripto ke dompet Anda."
        dep = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        back = InlineKeyboardButton(text='< Kembali', callback_data='tg_mode')
    elif language == "es":
        text = f"Falta tu saldo {bal} PIXEL. Por favor, deposite criptomonedas en su monedero."
        dep = InlineKeyboardButton(text='➕ Recibir', callback_data='deposit')
        back = InlineKeyboardButton(text='< Volver', callback_data='tg_mode')
    elif language == "ko":
        text = f"잔액이 없습니다 {bal} PIXEL. 월렛에 암호화폐를 충전하세요."
        dep = InlineKeyboardButton(text='➕ 예치', callback_data='deposit')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='tg_mode')
    elif language == "it":
        text = f"Manca il tuo saldo {bal} PIXEL. Per favore deposita le criptovalute nel tuo wallet."
        dep = InlineKeyboardButton(text='➕ Deposita', callback_data='deposit')
        back = InlineKeyboardButton(text='< Indietro', callback_data='tg_mode')
    elif language == "ch":
        text = f"您的餘額缺失 {bal} PIXEL. 请向您的钱包里存入加密货币。"
        dep = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        back = InlineKeyboardButton(text='< 返回', callback_data='tg_mode')
    elif language == "ta":
        text = f"您的余额缺失 {bal} PIXEL. 請向您的錢包裡存入加密貨幣。"
        dep = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        back = InlineKeyboardButton(text='< 返回', callback_data='tg_mode')
    elif language == "fa":
        text = f"موجودی شما از دست رفته است {bal} PIXEL. لطفا به کیف پول خود کریپتو واریز کنید."
        dep = InlineKeyboardButton(text='➕ واریز کردن', callback_data='deposit')
        back = InlineKeyboardButton(text='< برگشت', callback_data='tg_mode')
    elif language == "tr":
        text = f"Bakiyeniz eksik {bal} PIXEL. Lütfen cüzdanınıza kripto para yatırın."
        dep = InlineKeyboardButton(text='➕ Yatırma', callback_data='deposit')
        back = InlineKeyboardButton(text='< Geri', callback_data='tg_mode')
    elif language == "uz":
        text = f"Balansingiz yetishmayapti {bal} PIXEL. Iltimos, hamyoningizga kriptovalyuta kiriting."
        dep = InlineKeyboardButton(text="'➕ To'ldirish", callback_data='deposit')
        back = InlineKeyboardButton(text='< Ortga', callback_data='tg_mode')
    elif language == "be":
        text = f"আপনার ব্যালেন্স অনুপস্থিত {bal} PIXEL. অনুগ্রহ করে, আপনার ওয়ালেটে ক্রিপ্টো জমা করুন।"
        dep = InlineKeyboardButton(text='➕ জমা', callback_data='deposit')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='tg_mode')
    elif language == "hi":
        text = f"आपका बैलेंस गायब है {bal} PIXEL. कृपया, क्रिप्टो को अपने वैलेट में जमा करें।"
        dep = InlineKeyboardButton(text='➕ जमा', callback_data='deposit')
        back = InlineKeyboardButton(text='<वापस', callback_data='tg_mode')
    else:
        text = f"Your balance is missing {bal} PIXEL. Please, deposit crypto into your wallet."
        dep = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        back = InlineKeyboardButton(text='< Back', callback_data='tg_mode')
    return text, dep, back


def text_no_balance(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = "На вашем балансе недостаточно средств. Пожалуйста, пополните свой кошелек."
        dep = InlineKeyboardButton(text='➕ Пополнить', callback_data='deposit')
        back = InlineKeyboardButton(text='< Назад', callback_data='tg_mode')
    elif language == "id":
        text = "Saldo Anda tidak cukup. Silakan depositkan uang kripto ke dompet Anda."
        dep = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        back = InlineKeyboardButton(text='< Kembali', callback_data='tg_mode')
    elif language == "es":
        text = "Su saldo es insuficiente. Por favor, deposite criptomonedas en su monedero."
        dep = InlineKeyboardButton(text='➕ Recibir', callback_data='deposit')
        back = InlineKeyboardButton(text='< Volver', callback_data='tg_mode')
    elif language == "ko":
        text = "잔액이 부족합니다. 월렛에 암호화폐를 충전하세요."
        dep = InlineKeyboardButton(text='➕ 예치', callback_data='deposit')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='tg_mode')
    elif language == "it":
        text = "Il tuo saldo è insufficiente. Per favore deposita le criptovalute nel tuo wallet."
        dep = InlineKeyboardButton(text='➕ Deposita', callback_data='deposit')
        back = InlineKeyboardButton(text='< Indietro', callback_data='tg_mode')
    elif language == "ch":
        text = "您的余额不足。请向您的钱包里存入加密货币。"
        dep = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        back = InlineKeyboardButton(text='< 返回', callback_data='tg_mode')
    elif language == "ta":
        text = "您的餘額不足。請向您的錢包裡存入加密貨幣。"
        dep = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        back = InlineKeyboardButton(text='< 返回', callback_data='tg_mode')
    elif language == "fa":
        text = "موجودی حساب شما ناکافی است. لطفا به کیف پول خود کریپتو واریز کنید."
        dep = InlineKeyboardButton(text='➕ واریز کردن', callback_data='deposit')
        back = InlineKeyboardButton(text='< برگشت', callback_data='tg_mode')
    elif language == "tr":
        text = "Bakiyeniz yetersiz. Lütfen cüzdanınıza kripto para yatırın."
        dep = InlineKeyboardButton(text='➕ Yatırma', callback_data='deposit')
        back = InlineKeyboardButton(text='< Geri', callback_data='tg_mode')
    elif language == "uz":
        text = "Hisobingizda mablag’ yetarli emas. Iltimos, hamyoningizga kriptovalyuta kiriting."
        dep = InlineKeyboardButton(text="'➕ To'ldirish", callback_data='deposit')
        back = InlineKeyboardButton(text='< Ortga', callback_data='tg_mode')
    elif language == "be":
        text = "আপনার ব্যালেন্স অপর্যাপ্ত। অনুগ্রহ করে, আপনার ওয়ালেটে ক্রিপ্টো জমা করুন।"
        dep = InlineKeyboardButton(text='➕ জমা', callback_data='deposit')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='tg_mode')
    elif language == "hi":
        text = "आपका बैलेंस अपर्याप्त है। कृपया, क्रिप्टो को अपने वैलेट में जमा करें।"
        dep = InlineKeyboardButton(text='➕ जमा', callback_data='deposit')
        back = InlineKeyboardButton(text='<वापस', callback_data='tg_mode')
    else:
        text = "Your balance is insufficient. Please, deposit crypto into your wallet."
        dep = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        back = InlineKeyboardButton(text='< Back', callback_data='tg_mode')
    return text, dep, back


def text_withdraw_sixth_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    argument = lists.argument_withdraw_sixth(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Вывод средств:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Tarik: TON</b>\n\n" \
               f"<b>Penarikan:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Retiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>철수:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Ritiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>برداشت از حساب:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Fonların çekilmesi:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Olib tashlash:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>উত্তোলন:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>निकासी:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Withdrawal:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text


def button_withdraw_sixth_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Вывести через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Penarikan melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Retirar a través de Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 출금',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Preleva tramite Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包提現',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包提现',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 برداشت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan aracılığıyla para çekme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Wallet orqali yechib oling',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে প্রত্যাহার করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से निकासी',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        pay = InlineKeyboardButton(text='👛 Withdraw via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return pay, back


def text_withdraw_sixth(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    argument = lists.argument_withdraw_sixth(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Вывод средств:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Tarik: TON</b>\n\n" \
               f"<b>Penarikan:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Retiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>철수:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Ritiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>برداشت از حساب:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Fonların çekilmesi:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Olib tashlash:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>উত্তোলন:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>निकासी:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Withdrawal:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text, back


def button_withdraw_sixth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        b1 = InlineKeyboardButton(text='6 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='12 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='18 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='30 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='60 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_sixth_ok')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        b1 = InlineKeyboardButton(text='10 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='30 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='50 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='100 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_sixth_ok')
    elif currency == "EGP" or currency == "INR":
        b1 = InlineKeyboardButton(text='6 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='8 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='10 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='15 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_sixth_ok')
    else:
        b1 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='40 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='60 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='100 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='200 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_sixth_ok')
    return b1, b2, b3, b4, b5, b6


def text_withdraw_fifth_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    argument = lists.argument_withdraw_fifth(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Вывод средств:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Tarik: TON</b>\n\n" \
               f"<b>Penarikan:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Retiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>철수:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Ritiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>برداشت از حساب:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Fonların çekilmesi:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Olib tashlash:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>উত্তোলন:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>निकासी:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Withdrawal:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text


def button_withdraw_fifth_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Вывести через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Penarikan melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Retirar a través de Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 출금',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Preleva tramite Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包提現',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包提现',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 برداشت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan aracılığıyla para çekme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Wallet orqali yechib oling',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে প্রত্যাহার করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से निकासी',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        pay = InlineKeyboardButton(text='👛 Withdraw via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return pay, back


def text_withdraw_fifth(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    argument = lists.argument_withdraw_fifth(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Вывод средств:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Tarik: TON</b>\n\n" \
               f"<b>Penarikan:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Retiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>철수:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Ritiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>برداشت از حساب:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Fonların çekilmesi:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Olib tashlash:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>উত্তোলন:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>निकासी:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Withdrawal:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text, back


def button_withdraw_fifth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        b1 = InlineKeyboardButton(text='6 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='12 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='18 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='30 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_fifth_ok')
        b6 = InlineKeyboardButton(text='600 TON', callback_data='withdraw_sixth')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        b1 = InlineKeyboardButton(text='10 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='30 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='50 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_fifth_ok')
        b6 = InlineKeyboardButton(text='1000 TON', callback_data='withdraw_sixth')
    elif currency == "EGP" or currency == "INR":
        b1 = InlineKeyboardButton(text='6 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='8 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='10 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='15 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_fifth_ok')
        b6 = InlineKeyboardButton(text='200 TON', callback_data='withdraw_sixth')
    else:
        b1 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='40 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='60 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='100 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_fifth_ok')
        b6 = InlineKeyboardButton(text='2000 TON', callback_data='withdraw_sixth')
    return b1, b2, b3, b4, b5, b6


def text_withdraw_fourth_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    argument = lists.argument_withdraw_fourth(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Вывод средств:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Tarik: TON</b>\n\n" \
               f"<b>Penarikan:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Retiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>철수:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Ritiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>برداشت از حساب:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Fonların çekilmesi:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Olib tashlash:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>উত্তোলন:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>निकासी:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Withdrawal:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text


def button_withdraw_fourth_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Вывести через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Penarikan melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Retirar a través de Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 출금',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Preleva tramite Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包提現',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包提现',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 برداشت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan aracılığıyla para çekme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Wallet orqali yechib oling',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে প্রত্যাহার করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से निकासी',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        pay = InlineKeyboardButton(text='👛 Withdraw via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return pay, back


def text_withdraw_fourth(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    argument = lists.argument_withdraw_fourth(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Вывод средств:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Tarik: TON</b>\n\n" \
               f"<b>Penarikan:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Retiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>철수:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Ritiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>برداشت از حساب:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Fonların çekilmesi:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Olib tashlash:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>উত্তোলন:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>निकासी:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Withdrawal:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text, back


def button_withdraw_fourth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        b1 = InlineKeyboardButton(text='6 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='12 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='18 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_fourth_ok')
        b5 = InlineKeyboardButton(text='60 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='600 TON', callback_data='withdraw_sixth')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        b1 = InlineKeyboardButton(text='10 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='30 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_fourth_ok')
        b5 = InlineKeyboardButton(text='100 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='1000 TON', callback_data='withdraw_sixth')
    elif currency == "EGP" or currency == "INR":
        b1 = InlineKeyboardButton(text='6 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='8 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='10 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_fourth_ok')
        b5 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='200 TON', callback_data='withdraw_sixth')
    else:
        b1 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='40 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='60 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_fourth_ok')
        b5 = InlineKeyboardButton(text='200 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='2000 TON', callback_data='withdraw_sixth')
    return b1, b2, b3, b4, b5, b6


def text_withdraw_third_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    argument = lists.argument_withdraw_third(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Вывод средств:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Tarik: TON</b>\n\n" \
               f"<b>Penarikan:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Retiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>철수:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Ritiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>برداشت از حساب:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Fonların çekilmesi:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Olib tashlash:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>উত্তোলন:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>निकासी:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Withdrawal:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text


def button_withdraw_third_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Вывести через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Penarikan melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Retirar a través de Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 출금',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Preleva tramite Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包提現',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包提现',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 برداشت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan aracılığıyla para çekme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Wallet orqali yechib oling',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে প্রত্যাহার করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से निकासी',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        pay = InlineKeyboardButton(text='👛 Withdraw via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return pay, back


def text_withdraw_third(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    argument = lists.argument_withdraw_third(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Вывод средств:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Tarik: TON</b>\n\n" \
               f"<b>Penarikan:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Retiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>철수:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Ritiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>برداشت از حساب:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Fonların çekilmesi:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Olib tashlash:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>উত্তোলন:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>निकासी:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Withdrawal:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text, back


def button_withdraw_third(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        b1 = InlineKeyboardButton(text='6 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='12 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_third_ok')
        b4 = InlineKeyboardButton(text='30 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='60 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='600 TON', callback_data='withdraw_sixth')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        b1 = InlineKeyboardButton(text='10 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_third_ok')
        b4 = InlineKeyboardButton(text='50 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='100 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='1000 TON', callback_data='withdraw_sixth')
    elif currency == "EGP" or currency == "INR":
        b1 = InlineKeyboardButton(text='6 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='8 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_third_ok')
        b4 = InlineKeyboardButton(text='15 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='200 TON', callback_data='withdraw_sixth')
    else:
        b1 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='40 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_third_ok')
        b4 = InlineKeyboardButton(text='100 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='200 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='2000 TON', callback_data='withdraw_sixth')
    return b1, b2, b3, b4, b5, b6


def text_withdraw_second_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    argument = lists.argument_withdraw_second(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Вывод средств:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Tarik: TON</b>\n\n" \
               f"<b>Penarikan:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Retiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>철수:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Ritiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>برداشت از حساب:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Fonların çekilmesi:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Olib tashlash:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>উত্তোলন:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>निकासी:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Withdrawal:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text


def button_withdraw_second_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Вывести через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Penarikan melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Retirar a través de Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 출금',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Preleva tramite Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包提現',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包提现',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 برداشت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan aracılığıyla para çekme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Wallet orqali yechib oling',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে প্রত্যাহার করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से निकासी',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        pay = InlineKeyboardButton(text='👛 Withdraw via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return pay, back


def text_withdraw_second(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    argument = lists.argument_withdraw_second(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Вывод средств:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Tarik: TON</b>\n\n" \
               f"<b>Penarikan:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Retiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>철수:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Ritiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>برداشت از حساب:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Fonların çekilmesi:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Olib tashlash:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>উত্তোলন:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>निकासी:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Withdrawal:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text, back


def button_withdraw_second(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        b1 = InlineKeyboardButton(text='6 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_second_ok')
        b3 = InlineKeyboardButton(text='18 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='30 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='60 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='600 TON', callback_data='withdraw_sixth')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        b1 = InlineKeyboardButton(text='10 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_second_ok')
        b3 = InlineKeyboardButton(text='30 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='50 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='100 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='1000 TON', callback_data='withdraw_sixth')
    elif currency == "EGP" or currency == "INR":
        b1 = InlineKeyboardButton(text='6 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_second_ok')
        b3 = InlineKeyboardButton(text='10 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='15 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='200 TON', callback_data='withdraw_sixth')
    else:
        b1 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_second_ok')
        b3 = InlineKeyboardButton(text='60 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='100 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='200 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='2000 TON', callback_data='withdraw_sixth')
    return b1, b2, b3, b4, b5, b6


def text_withdraw_first_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    argument = lists.argument_withdraw_first(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Вывод средств:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Tarik: TON</b>\n\n" \
               f"<b>Penarikan:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Retiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>철수:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Ritiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>برداشت از حساب:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Fonların çekilmesi:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Olib tashlash:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>উত্তোলন:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>निकासी:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Withdrawal:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text


def button_withdraw_first_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Вывести через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Penarikan melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Retirar a través de Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 출금',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Preleva tramite Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包提現',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包提现',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 برداشت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan aracılığıyla para çekme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Wallet orqali yechib oling',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে প্রত্যাহার করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से निकासी',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        pay = InlineKeyboardButton(text='👛 Withdraw via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return pay, back


def text_withdraw_first(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    argument = lists.argument_withdraw_first(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Вывод средств:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Tarik: TON</b>\n\n" \
               f"<b>Penarikan:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Retiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>철수:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Ritiro:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>退出：</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>برداشت از حساب:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Fonların çekilmesi:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Olib tashlash:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>উত্তোলন:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>निकासी:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Withdrawal:</b> {argument}.0 TON ~{round(argument * rate, 2)} {currency}\n\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text, back


def button_withdraw_first(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        b1 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_first_ok')
        b2 = InlineKeyboardButton(text='12 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='18 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='30 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='60 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='600 TON', callback_data='withdraw_sixth')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        b1 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_first_ok')
        b2 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='30 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='50 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='100 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='1000 TON', callback_data='withdraw_sixth')
    elif currency == "EGP" or currency == "INR":
        b1 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_first_ok')
        b2 = InlineKeyboardButton(text='8 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='10 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='15 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='200 TON', callback_data='withdraw_sixth')
    else:
        b1 = InlineKeyboardButton(text='✅ Ok', callback_data='withdraw_first_ok')
        b2 = InlineKeyboardButton(text='40 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='60 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='100 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='200 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='2000 TON', callback_data='withdraw_sixth')
    return b1, b2, b3, b4, b5, b6


def back_no_wallet(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = "На вашем балансе недостаточно средств. Пожалуйста, пополните свой кошелек."
        top = InlineKeyboardButton(text='➕ Пополнить', callback_data='deposit')
        back = InlineKeyboardButton(text='< Назад', callback_data='wallet')
    elif language == "id":
        text = "Saldo Anda tidak cukup. Silakan depositkan uang kripto ke dompet Anda."
        top = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        back = InlineKeyboardButton(text='< Kembali', callback_data='wallet')
    elif language == "es":
        text = "Su saldo es insuficiente. Por favor, deposite criptomonedas en su monedero."
        top = InlineKeyboardButton(text='➕ Recibir', callback_data='deposit')
        back = InlineKeyboardButton(text='< Volver', callback_data='wallet')
    elif language == "ko":
        text = "잔액이 부족합니다. 월렛에 암호화폐를 충전하세요."
        top = InlineKeyboardButton(text='➕ 예치', callback_data='deposit')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='wallet')
    elif language == "it":
        text = "Il tuo saldo è insufficiente. Per favore deposita le criptovalute nel tuo wallet."
        top = InlineKeyboardButton(text='➕ Deposita', callback_data='deposit')
        back = InlineKeyboardButton(text='< Indietro', callback_data='wallet')
    elif language == "ch":
        text = "您的余额不足。请向您的钱包里存入加密货币。"
        top = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        back = InlineKeyboardButton(text='< 返回', callback_data='wallet')
    elif language == "ta":
        text = "您的餘額不足。請向您的錢包裡存入加密貨幣。"
        top = InlineKeyboardButton(text='➕ 存款', callback_data='deposit')
        back = InlineKeyboardButton(text='< 返回', callback_data='wallet')
    elif language == "fa":
        text = "موجودی حساب شما ناکافی است. لطفا به کیف پول خود کریپتو واریز کنید."
        top = InlineKeyboardButton(text='➕ واریز کردن', callback_data='deposit')
        back = InlineKeyboardButton(text='< برگشت', callback_data='wallet')
    elif language == "tr":
        text = "Bakiyeniz yetersiz. Lütfen cüzdanınıza kripto para yatırın."
        top = InlineKeyboardButton(text='➕ Yatırma', callback_data='deposit')
        back = InlineKeyboardButton(text='< Geri', callback_data='wallet')
    elif language == "uz":
        text = "Hisobingizda mablag’ yetarli emas. Iltimos, hamyoningizga kriptovalyuta kiriting."
        top = InlineKeyboardButton(text="'➕ To'ldirish", callback_data='deposit')
        back = InlineKeyboardButton(text='< Ortga', callback_data='wallet')
    elif language == "be":
        text = "আপনার ব্যালেন্স অপর্যাপ্ত। অনুগ্রহ করে, আপনার ওয়ালেটে ক্রিপ্টো জমা করুন।"
        top = InlineKeyboardButton(text='➕ জমা', callback_data='deposit')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='wallet')
    elif language == "hi":
        text = "आपका बैलेंस अपर्याप्त है। कृपया, क्रिप्टो को अपने वैलेट में जमा करें।"
        top = InlineKeyboardButton(text='➕ जमा', callback_data='deposit')
        back = InlineKeyboardButton(text='<वापस', callback_data='wallet')
    else:
        text = "Your balance is insufficient. Please, deposit crypto into your wallet."
        top = InlineKeyboardButton(text='➕ Deposit', callback_data='deposit')
        back = InlineKeyboardButton(text='< Back', callback_data='wallet')
    return text, top, back


def text_withdraw(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    ton = db.get_ton(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➡️ Вывести: TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"Используйте суммы ниже для перевода TON на кошелек Wallet.\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены в течение 2 минут"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"Gunakan jumlah di bawah ini untuk mentransfer TON ke Wallet.\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan dikreditkan dalam waktu 2 menit"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➡️ Enviar: TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"Utilice las cantidades siguientes para transferir TON a Wallet.\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán en 2 minutos."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➡️ 철회하다: TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"아래 금액을 사용하여 TON을 월렛으로 이체하세요.\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"2분 이내에 자금이 입금됩니다."
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➡️ Preleva: TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"Utilizza gli importi seguenti per trasferire TON su Wallet.\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati entro 2 minuti"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"使用以下金額將 TON 轉入錢包。\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將在2分鐘內到賬"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➡️ 提取：TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"使用以下金额将 TON 转入钱包。\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将在2分钟内到账"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➡️ کنار کشیدن: TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"از مبالغ زیر برای انتقال TON به کیف پول استفاده کنید.\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه در عرض 2 دقیقه واریز می شود"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➡️ Para çekme: TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"TON'u Cüzdan'a aktarmak için aşağıdaki tutarları kullanın.\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar 2 dakika içinde aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➡️ Yechib olish: TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"TONni Wallet’ga o‘tkazish uchun quyidagi miqdorlardan foydalaning.\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar 2 daqiqa ichida o'tkaziladi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➡️ প্রত্যাহার: TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"ওয়ালেটে TON স্থানান্তর করতে নীচের পরিমাণগুলি ব্যবহার করুন৷\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"2 মিনিটের মধ্যে তহবিল জমা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➡️ निकालना: TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"TON को वॉलेट में स्थानांतरित करने के लिए नीचे दी गई राशि का उपयोग करें।\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"2 मिनट के भीतर धनराशि जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➡️ Withdraw: TON</b>\n\n" \
               f"<b>Toncoin:</b> {ton} TON ~{round(ton * rate, 2)} {currency}\n\n" \
               f"Use the amounts below to transfer TON to Wallet.\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited within 2 minutes"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text, back


def button_withdraw(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        b1 = InlineKeyboardButton(text='6 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='12 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='18 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='30 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='60 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='600 TON', callback_data='withdraw_sixth')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        b1 = InlineKeyboardButton(text='10 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='30 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='50 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='100 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='1000 TON', callback_data='withdraw_sixth')
    elif currency == "EGP" or currency == "INR":
        b1 = InlineKeyboardButton(text='6 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='8 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='10 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='15 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='200 TON', callback_data='withdraw_sixth')
    else:
        b1 = InlineKeyboardButton(text='20 TON', callback_data='withdraw_first')
        b2 = InlineKeyboardButton(text='40 TON', callback_data='withdraw_second')
        b3 = InlineKeyboardButton(text='60 TON', callback_data='withdraw_third')
        b4 = InlineKeyboardButton(text='100 TON', callback_data='withdraw_fourth')
        b5 = InlineKeyboardButton(text='200 TON', callback_data='withdraw_fifth')
        b6 = InlineKeyboardButton(text='2000 TON', callback_data='withdraw_sixth')
    return b1, b2, b3, b4, b5, b6


def text_seventh_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 200000
    s = 2000
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text


def button_seventh_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Оплатить через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Bayar melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Pagar mediante billetera',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 결제',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Paga tramite Portafoglio',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 پرداخت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan ile ödeme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Hamyon orqali toʻlash',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে অর্থপ্রদান করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से भुगतान करें',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        pay = InlineKeyboardButton(text='👛 Pay via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return pay, back


def text_seventh_buy_ton(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 200000
    s = 2000
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text, back


def button_seventh_buy_ton(user_id):
    language = db.get_language(user_id)
    b1 = InlineKeyboardButton(text='1000 PIXEL', callback_data='first_buy_ton')
    b2 = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_buy_ton')
    b3 = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_buy_ton')
    b4 = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_buy_ton')
    b5 = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_buy_ton')
    b6 = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_buy_ton')
    b7 = InlineKeyboardButton(text='✅ Ok', callback_data='seventh_buy_ton_ok')
    return b1, b2, b3, b4, b5, b6, b7


def text_sixth_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 20000
    s = 200
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text


def button_sixth_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Оплатить через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Bayar melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Pagar mediante billetera',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 결제',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Paga tramite Portafoglio',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 پرداخت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan ile ödeme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Hamyon orqali toʻlash',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে অর্থপ্রদান করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से भुगतान करें',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        pay = InlineKeyboardButton(text='👛 Pay via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return pay, back


def text_sixth_buy_ton(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 20000
    s = 200
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text, back


def button_sixth_buy_ton(user_id):
    language = db.get_language(user_id)
    b1 = InlineKeyboardButton(text='1000 PIXEL', callback_data='first_buy_ton')
    b2 = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_buy_ton')
    b3 = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_buy_ton')
    b4 = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_buy_ton')
    b5 = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_buy_ton')
    b6 = InlineKeyboardButton(text='✅ Ok', callback_data='sixth_buy_ton_ok')
    b7 = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_buy_ton')
    return b1, b2, b3, b4, b5, b6, b7


def text_fifth_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 10000
    s = 100
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text


def button_fifth_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Оплатить через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Bayar melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Pagar mediante billetera',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 결제',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Paga tramite Portafoglio',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 پرداخت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan ile ödeme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Hamyon orqali toʻlash',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে অর্থপ্রদান করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से भुगतान करें',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        pay = InlineKeyboardButton(text='👛 Pay via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return pay, back


def text_fifth_buy_ton(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 10000
    s = 100
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text, back


def button_fifth_buy_ton(user_id):
    b1 = InlineKeyboardButton(text='1000 PIXEL', callback_data='first_buy_ton')
    b2 = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_buy_ton')
    b3 = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_buy_ton')
    b4 = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_buy_ton')
    b5 = InlineKeyboardButton(text='✅ Ok', callback_data='fifth_buy_ton_ok')
    b6 = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_buy_ton')
    b7 = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_buy_ton')
    return b1, b2, b3, b4, b5, b6, b7


def text_fourth_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 6000
    s = 60
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text


def button_fourth_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Оплатить через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Bayar melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Pagar mediante billetera',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 결제',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Paga tramite Portafoglio',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 پرداخت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan ile ödeme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Hamyon orqali toʻlash',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে অর্থপ্রদান করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से भुगतान करें',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        pay = InlineKeyboardButton(text='👛 Pay via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return pay, back


def text_fourth_buy_ton(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 6000
    s = 60
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text, back


def button_fourth_buy_ton(user_id):
    language = db.get_language(user_id)
    b1 = InlineKeyboardButton(text='1000 PIXEL', callback_data='first_buy_ton')
    b2 = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_buy_ton')
    b3 = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_buy_ton')
    b4 = InlineKeyboardButton(text='✅ Ok', callback_data='fourth_buy_ton_ok')
    b5 = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_buy_ton')
    b6 = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_buy_ton')
    b7 = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_buy_ton')
    return b1, b2, b3, b4, b5, b6, b7


def text_third_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 4000
    s = 40
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text


def button_third_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Оплатить через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Bayar melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Pagar mediante billetera',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 결제',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Paga tramite Portafoglio',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 پرداخت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan ile ödeme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Hamyon orqali toʻlash',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে অর্থপ্রদান করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से भुगतान करें',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        pay = InlineKeyboardButton(text='👛 Pay via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return pay, back


def text_third_buy_ton(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 4000
    s = 40
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text, back


def button_third_buy_ton(user_id):
    b1 = InlineKeyboardButton(text='1000 PIXEL', callback_data='first_buy_ton')
    b2 = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_buy_ton')
    b3 = InlineKeyboardButton(text='✅ Ok', callback_data='third_buy_ton_ok')
    b4 = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_buy_ton')
    b5 = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_buy_ton')
    b6 = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_buy_ton')
    b7 = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_buy_ton')
    return b1, b2, b3, b4, b5, b6, b7


def text_second_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 2000
    s = 20
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text


def button_second_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Оплатить через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Bayar melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Pagar mediante billetera',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 결제',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Paga tramite Portafoglio',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 پرداخت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan ile ödeme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Hamyon orqali toʻlash',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে অর্থপ্রদান করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से भुगतान करें',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        pay = InlineKeyboardButton(text='👛 Pay via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return pay, back


def text_second_buy_ton(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 2000
    s = 20
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text, back


def button_second_buy_ton(user_id):
    b1 = InlineKeyboardButton(text='1000 PIXEL', callback_data='first_buy_ton')
    b2 = InlineKeyboardButton(text='✅ Ok', callback_data='second_buy_ton_ok')
    b3 = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_buy_ton')
    b4 = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_buy_ton')
    b5 = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_buy_ton')
    b6 = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_buy_ton')
    b7 = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_buy_ton')
    return b1, b2, b3, b4, b5, b6, b7


def text_first_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 1000
    s = 10
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text


def button_first_buy_ton_ok(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        pay = InlineKeyboardButton(text='👛 Оплатить через Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        pay = InlineKeyboardButton(text='👛 Bayar melalui Dompet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        pay = InlineKeyboardButton(text='👛 Pagar mediante billetera',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        pay = InlineKeyboardButton(text='👛 지갑을 통해 결제',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        pay = InlineKeyboardButton(text='👛 Paga tramite Portafoglio',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        pay = InlineKeyboardButton(text='👛 通過錢包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        pay = InlineKeyboardButton(text='👛 通过钱包支付',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        pay = InlineKeyboardButton(text='👛 پرداخت از طریق کیف پول',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        pay = InlineKeyboardButton(text='👛 Cüzdan ile ödeme',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        pay = InlineKeyboardButton(text='👛 Hamyon orqali toʻlash',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        pay = InlineKeyboardButton(text='👛 ওয়ালেটের মাধ্যমে অর্থপ্রদান করুন',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        pay = InlineKeyboardButton(text='👛 वॉलेट के माध्यम से भुगतान करें',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        pay = InlineKeyboardButton(text='👛 Pay via Wallet',
                                   url='https://t.me/wallet?startattach=wpay_order-orderId__9623182631763970')
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return pay, back


def button_first_buy_ton(user_id):
    b1 = InlineKeyboardButton(text='✅ Ok', callback_data='first_buy_ton_ok')
    b2 = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_buy_ton')
    b3 = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_buy_ton')
    b4 = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_buy_ton')
    b5 = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_buy_ton')
    b6 = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_buy_ton')
    b7 = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_buy_ton')
    return b1, b2, b3, b4, b5, b6, b7


def text_first_buy_ton(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    f = 1000
    s = 10
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n<b>Покупка:</b> {f} PIXEL за {s} TON ~{round(s * rate, 2)} {currency}\n\nСеть: <b>The Open Network - TON.</b>\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад', callback_data='ton_coin')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Pembelian:</b> {f} PIXEL untuk {s} TON ~{round(s * rate, 2)} {currency}\n\nJaringan: <b>The Open Network - TON.</b>\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali', callback_data='ton_coin')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n<b>Compra:</b> {f} PIXEL por {s} TON ~{round(s * rate, 2)} {currency}\n\nRed: <b>The Open Network - TON.</b>\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver', callback_data='ton_coin')
    elif language == "ko":
        text = f"➕ <b>내 월렛: TON</b>\n\n<b>구입:</b> {f} PIXEL 위한 {s} TON ~{round(s * rate, 2)} {currency}\n\n네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='ton_coin')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n<b>Acquistare:</b> {f} PIXEL per {s} TON ~{round(s * rate, 2)} {currency}\n\nRete: <b>The Open Network - TON.</b>\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Indietro', callback_data='ton_coin')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n<b>購買:</b> {f} PIXEL 為了 {s} TON ~{round(s * rate, 2)} {currency}\n\n网络：<b>The Open Network - TON.</b>\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n<b>购买:</b> {f} PIXEL 为了 {s} TON ~{round(s * rate, 2)} {currency}\n\n網絡：<b>The Open Network - TON.</b>\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回', callback_data='ton_coin')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n<b>خرید:</b> {f} PIXEL برای {s} TON ~{round(s * rate, 2)} {currency}\n\nشبکه: <b>The Open Network - TON.</b>\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< برگشت', callback_data='ton_coin')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n<b>Satın almak:</b> {f} PIXEL için {s} TON ~{round(s * rate, 2)} {currency}\n\nAğ: <b>The Open Network - TON.</b>\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Geri', callback_data='ton_coin')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n<b>Xarid:</b> {f} PIXEL uchun {s} TON ~{round(s * rate, 2)} {currency}\n\nTarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Ortga', callback_data='ton_coin')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n<b>ক্রয়:</b> {s} TON এর বদলে {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nঅন্তর্জাল: <b>The Open Network - TON.</b>\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='ton_coin')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n<b>खरीद:</b> {s} TON से {f} PIXEL ~{round(s * rate, 2)} {currency}\n\nनेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वापस', callback_data='ton_coin')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n<b>Purchase:</b> {f} PIXEL for {s} TON ~{round(s * rate, 2)} {currency}\n\nNetwork: <b>The Open Network - TON.</b>\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back', callback_data='ton_coin')
    return text, back


def button_ton_coin(user_id):
    b1 = InlineKeyboardButton(text='1000 PIXEL', callback_data='first_buy_ton')
    b2 = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_buy_ton')
    b3 = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_buy_ton')
    b4 = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_buy_ton')
    b5 = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_buy_ton')
    b6 = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_buy_ton')
    b7 = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_buy_ton')
    return b1, b2, b3, b4, b5, b6, b7


def text_ton_coin(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"➕ <b>Пополнить: TON</b>\n\n" \
               f"Используйте суммы ниже для покупки PIXEL за TON.\n" \
               f"Сеть: <b>The Open Network - TON.</b>\n\n" \
               f"<b>Обменный курс:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"Средства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"➕ <b>Deposit: TON</b>\n\n" \
               f"Gunakan jumlah di bawah untuk membeli PIXEL dengan TON.\n" \
               f"Jaringan: <b>The Open Network - TON.</b>\n\n" \
               f"<b>Kurs:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"Dana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"➕ <b>Recibir: TON</b>\n\n" \
               f"Utilice las cantidades siguientes para comprar PIXEL con TON.\n" \
               f"Red: <b>The Open Network - TON.</b>\n\n" \
               f"<b>Tipo de cambio:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"Los fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"➕ <b>예치: TON</b>\n\n" \
               f"TON으로 PIXEL을 구매하려면 아래 금액을 사용하세요.\n" \
               f"네트워크: <b>The Open Network - TON.</b>\n\n" \
               f"<b>환율:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"➕ <b>Deposita: TON</b>\n\n" \
               f"Utilizza gli importi seguenti per acquistare PIXEL con TON.\n" \
               f"Rete: <b>The Open Network - TON.</b>\n\n" \
               f"<b>Tasso di cambio:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"I fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"➕ <b>存款: TON</b>\n\n" \
               f"使用以下金額通過 TON 購買 PIXEL。\n" \
               f"网络：<b>The Open Network - TON.</b>\n\n" \
               f"<b>匯率：</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"資金將立即存入"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"➕ <b>存款: TON</b>\n\n" \
               f"使用以下金额通过 TON 购买 PIXEL。\n" \
               f"網絡：<b>The Open Network - TON.</b>\n\n" \
               f"<b>汇率：</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"资金将立即存入"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"➕ <b>واریز کردن: TON</b>\n\n" \
               f"برای خرید PIXEL با TON از مبالغ زیر استفاده کنید.\n" \
               f"شبکه: <b>The Open Network - TON.</b>\n\n" \
               f"<b>قیمت ارز:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"وجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"➕ <b>Yatırma: TON</b>\n\n" \
               f"TON ile PIXEL satın almak için aşağıdaki miktarları kullanın.\n" \
               f"Ağ: <b>The Open Network - TON.</b>\n\n" \
               f"<b>Döviz kuru:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"Fonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"➕ <b>To'ldirish: TON</b>\n\n" \
               f"TON bilan PIXEL sotib olish uchun quyidagi miqdorlardan foydalaning.\n" \
               f"Tarmoq: <b>The Open Network - TON.</b>\n\n" \
               f"<b>Valyuta kursi:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"Mablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"➕ <b>জমা: TON</b>\n\n" \
               f"TON দিয়ে PIXEL কিনতে নিচের পরিমাণ ব্যবহার করুন।\n" \
               f"নেটওয়ার্ক: <b>The Open Network - TON.</b>\n\n" \
               f"<b>বিনিময় হার:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"তহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"➕ <b>जमा: TON</b>\n\n" \
               f"PIXEL को TON के साथ खरीदने के लिए नीचे दी गई राशि का उपयोग करें।\n" \
               f"नेटवर्क: <b>The Open Network - TON.</b>\n\n" \
               f"<b>विनिमय दर:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"धनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"➕ <b>Deposit: TON</b>\n\n" \
               f"Use the amounts below to buy PIXEL with TON.\n" \
               f"Network: <b>The Open Network - TON.</b>\n\n" \
               f"<b>Exchange rate:</b> 1 TON = 100 PIXEL ~{rate} {currency}\n\n" \
               f"Funds will be credited immediately"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text, back


def button_seventh_card(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        first = InlineKeyboardButton(text='300 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='600 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='1200 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='1800 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='6000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='✅ Ok', callback_data='seventh_pay')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        first = InlineKeyboardButton(text='500 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='1000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='2000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='5000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='10000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='✅ Ok', callback_data='seventh_pay')
    elif currency == "EGP" or currency == "INR":
        first = InlineKeyboardButton(text='100 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='200 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='400 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='600 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='1000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='2000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='✅ Ok', callback_data='seventh_pay')
    else:
        first = InlineKeyboardButton(text=f'1000 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='✅ Ok', callback_data='seventh_pay')
    return first, second, third, fourth, fifth, sixth, seventh


def button_sixth_card(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        first = InlineKeyboardButton(text='300 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='600 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='1200 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='1800 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='✅ Ok', callback_data='sixth_pay')
        seventh = InlineKeyboardButton(text='60000 PIXEL', callback_data='seventh_card')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        first = InlineKeyboardButton(text='500 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='1000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='2000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='5000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='✅ Ok', callback_data='sixth_pay')
        seventh = InlineKeyboardButton(text='100000 PIXEL', callback_data='seventh_card')
    elif currency == "EGP" or currency == "INR":
        first = InlineKeyboardButton(text='100 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='200 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='400 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='600 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='1000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='✅ Ok', callback_data='sixth_pay')
        seventh = InlineKeyboardButton(text='20000 PIXEL', callback_data='seventh_card')
    else:
        first = InlineKeyboardButton(text=f'1000 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='✅ Ok', callback_data='sixth_pay')
        seventh = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_card')
    return first, second, third, fourth, fifth, sixth, seventh


def button_fifth_card(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        first = InlineKeyboardButton(text='300 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='600 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='1200 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='1800 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='✅ Ok', callback_data='fifth_pay')
        sixth = InlineKeyboardButton(text='6000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='60000 PIXEL', callback_data='seventh_card')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        first = InlineKeyboardButton(text='500 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='1000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='2000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='✅ Ok', callback_data='fifth_pay')
        sixth = InlineKeyboardButton(text='10000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='100000 PIXEL', callback_data='seventh_card')
    elif currency == "EGP" or currency == "INR":
        first = InlineKeyboardButton(text='100 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='200 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='400 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='600 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='✅ Ok', callback_data='fifth_pay')
        sixth = InlineKeyboardButton(text='2000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='20000 PIXEL', callback_data='seventh_card')
    else:
        first = InlineKeyboardButton(text=f'1000 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='✅ Ok', callback_data='fifth_pay')
        sixth = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_card')
    return first, second, third, fourth, fifth, sixth, seventh


def button_fourth_card(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        first = InlineKeyboardButton(text='300 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='600 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='1200 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='✅ Ok', callback_data='fourth_pay')
        fifth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='6000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='60000 PIXEL', callback_data='seventh_card')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        first = InlineKeyboardButton(text='500 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='1000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='2000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='✅ Ok', callback_data='fourth_pay')
        fifth = InlineKeyboardButton(text='5000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='10000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='100000 PIXEL', callback_data='seventh_card')
    elif currency == "EGP" or currency == "INR":
        first = InlineKeyboardButton(text='100 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='200 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='400 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='✅ Ok', callback_data='fourth_pay')
        fifth = InlineKeyboardButton(text='1000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='2000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='20000 PIXEL', callback_data='seventh_card')
    else:
        first = InlineKeyboardButton(text=f'1000 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='✅ Ok', callback_data='fourth_pay')
        fifth = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_card')
    return first, second, third, fourth, fifth, sixth, seventh


def button_third_card(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        first = InlineKeyboardButton(text='300 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='600 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='✅ Ok', callback_data='third_pay')
        fourth = InlineKeyboardButton(text='1800 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='6000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='60000 PIXEL', callback_data='seventh_card')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        first = InlineKeyboardButton(text='500 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='1000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='✅ Ok', callback_data='third_pay')
        fourth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='5000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='10000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='100000 PIXEL', callback_data='seventh_card')
    elif currency == "EGP" or currency == "INR":
        first = InlineKeyboardButton(text='100 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='200 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='✅ Ok', callback_data='third_pay')
        fourth = InlineKeyboardButton(text='600 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='1000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='2000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='20000 PIXEL', callback_data='seventh_card')
    else:
        first = InlineKeyboardButton(text=f'1000 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='✅ Ok', callback_data='third_pay')
        fourth = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_card')
    return first, second, third, fourth, fifth, sixth, seventh


def button_second_card(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        first = InlineKeyboardButton(text='300 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='✅ Ok', callback_data='second_pay')
        third = InlineKeyboardButton(text='1200 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='1800 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='6000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='60000 PIXEL', callback_data='seventh_card')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        first = InlineKeyboardButton(text='500 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='✅ Ok', callback_data='second_pay')
        third = InlineKeyboardButton(text='2000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='5000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='10000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='100000 PIXEL', callback_data='seventh_card')
    elif currency == "EGP" or currency == "INR":
        first = InlineKeyboardButton(text='100 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='✅ Ok', callback_data='second_pay')
        third = InlineKeyboardButton(text='400 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='600 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='1000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='2000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='20000 PIXEL', callback_data='seventh_card')
    else:
        first = InlineKeyboardButton(text=f'1000 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='✅ Ok', callback_data='second_pay')
        third = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_card')
    return first, second, third, fourth, fifth, sixth, seventh


def back_to_card(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        back = InlineKeyboardButton(text='< Назад', callback_data='card')
    elif language == "id":
        back = InlineKeyboardButton(text='< Kembali', callback_data='card')
    elif language == "es":
        back = InlineKeyboardButton(text='< Volver', callback_data='card')
    elif language == "ko":
        back = InlineKeyboardButton(text='< 뒤로', callback_data='card')
    elif language == "it":
        back = InlineKeyboardButton(text='< Indietro', callback_data='card')
    elif language == "ch":
        back = InlineKeyboardButton(text='< 返回', callback_data='card')
    elif language == "ta":
        back = InlineKeyboardButton(text='< 返回', callback_data='card')
    elif language == "fa":
        back = InlineKeyboardButton(text='< برگشت', callback_data='card')
    elif language == "tr":
        back = InlineKeyboardButton(text='< Geri', callback_data='card')
    elif language == "uz":
        back = InlineKeyboardButton(text='< Ortga', callback_data='card')
    elif language == "be":
        back = InlineKeyboardButton(text='< পিছনে', callback_data='card')
    elif language == "hi":
        back = InlineKeyboardButton(text='<वापस', callback_data='card')
    else:
        back = InlineKeyboardButton(text='< Back', callback_data='card')
    return back


def button_first_card(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        first = InlineKeyboardButton(text='✅ Ok', callback_data='first_pay')
        second = InlineKeyboardButton(text='600 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='1200 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='1800 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='6000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='60000 PIXEL', callback_data='seventh_card')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        first = InlineKeyboardButton(text='✅ Ok', callback_data='first_pay')
        second = InlineKeyboardButton(text='1000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='2000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='5000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='10000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='100000 PIXEL', callback_data='seventh_card')
    elif currency == "EGP" or currency == "INR":
        first = InlineKeyboardButton(text='✅ Ok', callback_data='first_pay')
        second = InlineKeyboardButton(text='200 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='400 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='600 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='1000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='2000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='20000 PIXEL', callback_data='seventh_card')
    else:
        first = InlineKeyboardButton(text=f'✅ Ok', callback_data='first_pay')
        second = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_card')
    return first, second, third, fourth, fifth, sixth, seventh


def text_first_card(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    net = lists.network_currency(user_id)
    ex = lists.exchange_first(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➕ Пополнить: {currency}</b>\n\n<b>Покупка:</b> {ex}0.0 PIXEL за {round(rate / 10 * ex, 2)} {currency}\n\nСеть: " \
               f"<b>{net}.</b>\n\nСредства будут зачислены сразу"
    elif language == "id":
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Pembelian:</b> {ex}0.0 PIXEL untuk {round(rate / 10 * ex, 2)} {currency}\n\nJaringan: " \
               f"<b>{net}.</b>\n\nDana akan segera dikreditkan"
    elif language == "es":
        text = f"<b>➕ Recibir: {currency}</b>\n\n<b>Compra:</b> {ex}0.0 PIXEL por {round(rate / 10 * ex, 2)} {currency}\n\nRed: " \
               f"<b>{net}.</b>\n\nLos fondos se acreditarán inmediatamente."
    elif language == "ko":
        text = f"<b>➕ 예치: {currency}</b>\n\n<b>구입:</b> {ex}0.0 PIXEL 위한 {round(rate / 10 * ex, 2)} {currency}\n\n네트워크: " \
               f"<b>{net}.</b>\n\n자금은 즉시 적립됩니다"
    elif language == "it":
        text = f"<b>➕ Deposita: {currency}</b>\n\n<b>Acquistare:</b> {ex}0.0 PIXEL per {round(rate / 10 * ex, 2)} {currency}\n\nRete: " \
               f"<b>{net}.</b>\n\nI fondi verranno accreditati immediatamente"
    elif language == "ch":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>購買：</b> {ex}0.0 PIXEL 為了 {round(rate / 10 * ex, 2)} {currency}\n\n网络：" \
               f"<b>{net}.</b>\n\n資金將立即存入"
    elif language == "ta":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>购买：</b> {ex}0.0 PIXEL 为了 {round(rate / 10 * ex, 2)} {currency}\n\n網絡：" \
               f"<b>{net}.</b>\n\n资金将立即存入"
    elif language == "fa":
        text = f"<b>➕ واریز کردن: {currency}</b>\n\n<b>خرید:</b> {ex}0.0 PIXEL برای {round(rate / 10 * ex, 2)} {currency}\n\nشبکه: " \
               f"<b>{net}.</b>\n\nوجوه بلافاصله واریز خواهد شد"
    elif language == "tr":
        text = f"<b>➕ Yatırma: {currency}</b>\n\n<b>Satın almak:</b> {ex}0.0 PIXEL için {round(rate / 10 * ex, 2)} {currency}\n\nAğ: " \
               f"<b>{net}.</b>\n\nFonlar hemen aktarılacak"
    elif language == "uz":
        text = f"<b>➕ To'ldirish: {currency}</b>\n\n<b>Sotib olish:</b> {ex}0.0 PIXEL uchun {round(rate / 10 * ex, 2)} {currency}\n\nTarmoq: " \
               f"<b>{net}.</b>\n\nMablag'lar darhol hisobga olinadi"
    elif language == "be":
        text = f"<b>➕ জমা: {currency}</b>\n\n<b>ক্রয়:</b> {ex}0.0 PIXEL জন্য {round(rate / 10 * ex, 2)} {currency}\n\nনেটওয়ার্ক: " \
               f"<b>{net}.</b>\n\nতহবিল অবিলম্বে জমা করা হবে"
    elif language == "hi":
        text = f"<b>➕ जमा: {currency}</b>\n\n<b>खरीदना:</b> {ex}0.0 PIXEL के लिए {round(rate / 10 * ex, 2)} {currency}\n\nनेटवर्क: " \
               f"<b>{net}.</b>\n\nधनराशि तुरंत जमा कर दी जाएगी"
    else:
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Purchase:</b> {ex}0.0 PIXEL for {round(rate / 10 * ex, 2)} {currency}\n\nNetwork: " \
               f"<b>{net}.</b>\n\nFunds will be credited immediately"
    return text


def text_second_card(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    net = lists.network_currency(user_id)
    ex = lists.exchange_second(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➕ Пополнить: {currency}</b>\n\n<b>Покупка:</b> {ex}0.0 PIXEL за {round(rate / 10 * ex, 2)} {currency}\n\nСеть: " \
               f"<b>{net}.</b>\n\nСредства будут зачислены сразу"
    elif language == "id":
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Pembelian:</b> {ex}0.0 PIXEL untuk {round(rate / 10 * ex, 2)} {currency}\n\nJaringan: " \
               f"<b>{net}.</b>\n\nDana akan segera dikreditkan"
    elif language == "es":
        text = f"<b>➕ Recibir: {currency}</b>\n\n<b>Compra:</b> {ex}0.0 PIXEL por {round(rate / 10 * ex, 2)} {currency}\n\nRed: " \
               f"<b>{net}.</b>\n\nLos fondos se acreditarán inmediatamente."
    elif language == "ko":
        text = f"<b>➕ 예치: {currency}</b>\n\n<b>구입:</b> {ex}0.0 PIXEL 위한 {round(rate / 10 * ex, 2)} {currency}\n\n네트워크: " \
               f"<b>{net}.</b>\n\n자금은 즉시 적립됩니다"
    elif language == "it":
        text = f"<b>➕ Deposita: {currency}</b>\n\n<b>Acquistare:</b> {ex}0.0 PIXEL per {round(rate / 10 * ex, 2)} {currency}\n\nRete: " \
               f"<b>{net}.</b>\n\nI fondi verranno accreditati immediatamente"
    elif language == "ch":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>購買：</b> {ex}0.0 PIXEL 為了 {round(rate / 10 * ex, 2)} {currency}\n\n网络：" \
               f"<b>{net}.</b>\n\n資金將立即存入"
    elif language == "ta":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>购买：</b> {ex}0.0 PIXEL 为了 {round(rate / 10 * ex, 2)} {currency}\n\n網絡：" \
               f"<b>{net}.</b>\n\n资金将立即存入"
    elif language == "fa":
        text = f"<b>➕ واریز کردن: {currency}</b>\n\n<b>خرید:</b> {ex}0.0 PIXEL برای {round(rate / 10 * ex, 2)} {currency}\n\nشبکه: " \
               f"<b>{net}.</b>\n\nوجوه بلافاصله واریز خواهد شد"
    elif language == "tr":
        text = f"<b>➕ Yatırma: {currency}</b>\n\n<b>Satın almak:</b> {ex}0.0 PIXEL için {round(rate / 10 * ex, 2)} {currency}\n\nAğ: " \
               f"<b>{net}.</b>\n\nFonlar hemen aktarılacak"
    elif language == "uz":
        text = f"<b>➕ To'ldirish: {currency}</b>\n\n<b>Sotib olish:</b> {ex}0.0 PIXEL uchun {round(rate / 10 * ex, 2)} {currency}\n\nTarmoq: " \
               f"<b>{net}.</b>\n\nMablag'lar darhol hisobga olinadi"
    elif language == "be":
        text = f"<b>➕ জমা: {currency}</b>\n\n<b>ক্রয়:</b> {ex}0.0 PIXEL জন্য {round(rate / 10 * ex, 2)} {currency}\n\nনেটওয়ার্ক: " \
               f"<b>{net}.</b>\n\nতহবিল অবিলম্বে জমা করা হবে"
    elif language == "hi":
        text = f"<b>➕ जमा: {currency}</b>\n\n<b>खरीदना:</b> {ex}0.0 PIXEL के लिए {round(rate / 10 * ex, 2)} {currency}\n\nनेटवर्क: " \
               f"<b>{net}.</b>\n\nधनराशि तुरंत जमा कर दी जाएगी"
    else:
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Purchase:</b> {ex}0.0 PIXEL for {round(rate / 10 * ex, 2)} {currency}\n\nNetwork: " \
               f"<b>{net}.</b>\n\nFunds will be credited immediately"
    return text


def text_third_card(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    net = lists.network_currency(user_id)
    ex = lists.exchange_third(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➕ Пополнить: {currency}</b>\n\n<b>Покупка:</b> {ex}0.0 PIXEL за {round(rate / 10 * ex, 2)} {currency}\n\nСеть: " \
               f"<b>{net}.</b>\n\nСредства будут зачислены сразу"
    elif language == "id":
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Pembelian:</b> {ex}0.0 PIXEL untuk {round(rate / 10 * ex, 2)} {currency}\n\nJaringan: " \
               f"<b>{net}.</b>\n\nDana akan segera dikreditkan"
    elif language == "es":
        text = f"<b>➕ Recibir: {currency}</b>\n\n<b>Compra:</b> {ex}0.0 PIXEL por {round(rate / 10 * ex, 2)} {currency}\n\nRed: " \
               f"<b>{net}.</b>\n\nLos fondos se acreditarán inmediatamente."
    elif language == "ko":
        text = f"<b>➕ 예치: {currency}</b>\n\n<b>구입:</b> {ex}0.0 PIXEL 위한 {round(rate / 10 * ex, 2)} {currency}\n\n네트워크: " \
               f"<b>{net}.</b>\n\n자금은 즉시 적립됩니다"
    elif language == "it":
        text = f"<b>➕ Deposita: {currency}</b>\n\n<b>Acquistare:</b> {ex}0.0 PIXEL per {round(rate / 10 * ex, 2)} {currency}\n\nRete: " \
               f"<b>{net}.</b>\n\nI fondi verranno accreditati immediatamente"
    elif language == "ch":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>購買：</b> {ex}0.0 PIXEL 為了 {round(rate / 10 * ex, 2)} {currency}\n\n网络：" \
               f"<b>{net}.</b>\n\n資金將立即存入"
    elif language == "ta":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>购买：</b> {ex}0.0 PIXEL 为了 {round(rate / 10 * ex, 2)} {currency}\n\n網絡：" \
               f"<b>{net}.</b>\n\n资金将立即存入"
    elif language == "fa":
        text = f"<b>➕ واریز کردن: {currency}</b>\n\n<b>خرید:</b> {ex}0.0 PIXEL برای {round(rate / 10 * ex, 2)} {currency}\n\nشبکه: " \
               f"<b>{net}.</b>\n\nوجوه بلافاصله واریز خواهد شد"
    elif language == "tr":
        text = f"<b>➕ Yatırma: {currency}</b>\n\n<b>Satın almak:</b> {ex}0.0 PIXEL için {round(rate / 10 * ex, 2)} {currency}\n\nAğ: " \
               f"<b>{net}.</b>\n\nFonlar hemen aktarılacak"
    elif language == "uz":
        text = f"<b>➕ To'ldirish: {currency}</b>\n\n<b>Sotib olish:</b> {ex}0.0 PIXEL uchun {round(rate / 10 * ex, 2)} {currency}\n\nTarmoq: " \
               f"<b>{net}.</b>\n\nMablag'lar darhol hisobga olinadi"
    elif language == "be":
        text = f"<b>➕ জমা: {currency}</b>\n\n<b>ক্রয়:</b> {ex}0.0 PIXEL জন্য {round(rate / 10 * ex, 2)} {currency}\n\nনেটওয়ার্ক: " \
               f"<b>{net}.</b>\n\nতহবিল অবিলম্বে জমা করা হবে"
    elif language == "hi":
        text = f"<b>➕ जमा: {currency}</b>\n\n<b>खरीदना:</b> {ex}0.0 PIXEL के लिए {round(rate / 10 * ex, 2)} {currency}\n\nनेटवर्क: " \
               f"<b>{net}.</b>\n\nधनराशि तुरंत जमा कर दी जाएगी"
    else:
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Purchase:</b> {ex}0.0 PIXEL for {round(rate / 10 * ex, 2)} {currency}\n\nNetwork: " \
               f"<b>{net}.</b>\n\nFunds will be credited immediately"
    return text


def text_fourth_card(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    net = lists.network_currency(user_id)
    ex = lists.exchange_fourth(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➕ Пополнить: {currency}</b>\n\n<b>Покупка:</b> {ex}0.0 PIXEL за {round(rate / 10 * ex, 2)} {currency}\n\nСеть: " \
               f"<b>{net}.</b>\n\nСредства будут зачислены сразу"
    elif language == "id":
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Pembelian:</b> {ex}0.0 PIXEL untuk {round(rate / 10 * ex, 2)} {currency}\n\nJaringan: " \
               f"<b>{net}.</b>\n\nDana akan segera dikreditkan"
    elif language == "es":
        text = f"<b>➕ Recibir: {currency}</b>\n\n<b>Compra:</b> {ex}0.0 PIXEL por {round(rate / 10 * ex, 2)} {currency}\n\nRed: " \
               f"<b>{net}.</b>\n\nLos fondos se acreditarán inmediatamente."
    elif language == "ko":
        text = f"<b>➕ 예치: {currency}</b>\n\n<b>구입:</b> {ex}0.0 PIXEL 위한 {round(rate / 10 * ex, 2)} {currency}\n\n네트워크: " \
               f"<b>{net}.</b>\n\n자금은 즉시 적립됩니다"
    elif language == "it":
        text = f"<b>➕ Deposita: {currency}</b>\n\n<b>Acquistare:</b> {ex}0.0 PIXEL per {round(rate / 10 * ex, 2)} {currency}\n\nRete: " \
               f"<b>{net}.</b>\n\nI fondi verranno accreditati immediatamente"
    elif language == "ch":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>購買：</b> {ex}0.0 PIXEL 為了 {round(rate / 10 * ex, 2)} {currency}\n\n网络：" \
               f"<b>{net}.</b>\n\n資金將立即存入"
    elif language == "ta":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>购买：</b> {ex}0.0 PIXEL 为了 {round(rate / 10 * ex, 2)} {currency}\n\n網絡：" \
               f"<b>{net}.</b>\n\n资金将立即存入"
    elif language == "fa":
        text = f"<b>➕ واریز کردن: {currency}</b>\n\n<b>خرید:</b> {ex}0.0 PIXEL برای {round(rate / 10 * ex, 2)} {currency}\n\nشبکه: " \
               f"<b>{net}.</b>\n\nوجوه بلافاصله واریز خواهد شد"
    elif language == "tr":
        text = f"<b>➕ Yatırma: {currency}</b>\n\n<b>Satın almak:</b> {ex}0.0 PIXEL için {round(rate / 10 * ex, 2)} {currency}\n\nAğ: " \
               f"<b>{net}.</b>\n\nFonlar hemen aktarılacak"
    elif language == "uz":
        text = f"<b>➕ To'ldirish: {currency}</b>\n\n<b>Sotib olish:</b> {ex}0.0 PIXEL uchun {round(rate / 10 * ex, 2)} {currency}\n\nTarmoq: " \
               f"<b>{net}.</b>\n\nMablag'lar darhol hisobga olinadi"
    elif language == "be":
        text = f"<b>➕ জমা: {currency}</b>\n\n<b>ক্রয়:</b> {ex}0.0 PIXEL জন্য {round(rate / 10 * ex, 2)} {currency}\n\nনেটওয়ার্ক: " \
               f"<b>{net}.</b>\n\nতহবিল অবিলম্বে জমা করা হবে"
    elif language == "hi":
        text = f"<b>➕ जमा: {currency}</b>\n\n<b>खरीदना:</b> {ex}0.0 PIXEL के लिए {round(rate / 10 * ex, 2)} {currency}\n\nनेटवर्क: " \
               f"<b>{net}.</b>\n\nधनराशि तुरंत जमा कर दी जाएगी"
    else:
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Purchase:</b> {ex}0.0 PIXEL for {round(rate / 10 * ex, 2)} {currency}\n\nNetwork: " \
               f"<b>{net}.</b>\n\nFunds will be credited immediately"
    return text


def text_fifth_card(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    net = lists.network_currency(user_id)
    ex = lists.exchange_fifth(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➕ Пополнить: {currency}</b>\n\n<b>Покупка:</b> {ex}0.0 PIXEL за {round(rate / 10 * ex, 2)} {currency}\n\nСеть: " \
               f"<b>{net}.</b>\n\nСредства будут зачислены сразу"
    elif language == "id":
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Pembelian:</b> {ex}0.0 PIXEL untuk {round(rate / 10 * ex, 2)} {currency}\n\nJaringan: " \
               f"<b>{net}.</b>\n\nDana akan segera dikreditkan"
    elif language == "es":
        text = f"<b>➕ Recibir: {currency}</b>\n\n<b>Compra:</b> {ex}0.0 PIXEL por {round(rate / 10 * ex, 2)} {currency}\n\nRed: " \
               f"<b>{net}.</b>\n\nLos fondos se acreditarán inmediatamente."
    elif language == "ko":
        text = f"<b>➕ 예치: {currency}</b>\n\n<b>구입:</b> {ex}0.0 PIXEL 위한 {round(rate / 10 * ex, 2)} {currency}\n\n네트워크: " \
               f"<b>{net}.</b>\n\n자금은 즉시 적립됩니다"
    elif language == "it":
        text = f"<b>➕ Deposita: {currency}</b>\n\n<b>Acquistare:</b> {ex}0.0 PIXEL per {round(rate / 10 * ex, 2)} {currency}\n\nRete: " \
               f"<b>{net}.</b>\n\nI fondi verranno accreditati immediatamente"
    elif language == "ch":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>購買：</b> {ex}0.0 PIXEL 為了 {round(rate / 10 * ex, 2)} {currency}\n\n网络：" \
               f"<b>{net}.</b>\n\n資金將立即存入"
    elif language == "ta":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>购买：</b> {ex}0.0 PIXEL 为了 {round(rate / 10 * ex, 2)} {currency}\n\n網絡：" \
               f"<b>{net}.</b>\n\n资金将立即存入"
    elif language == "fa":
        text = f"<b>➕ واریز کردن: {currency}</b>\n\n<b>خرید:</b> {ex}0.0 PIXEL برای {round(rate / 10 * ex, 2)} {currency}\n\nشبکه: " \
               f"<b>{net}.</b>\n\nوجوه بلافاصله واریز خواهد شد"
    elif language == "tr":
        text = f"<b>➕ Yatırma: {currency}</b>\n\n<b>Satın almak:</b> {ex}0.0 PIXEL için {round(rate / 10 * ex, 2)} {currency}\n\nAğ: " \
               f"<b>{net}.</b>\n\nFonlar hemen aktarılacak"
    elif language == "uz":
        text = f"<b>➕ To'ldirish: {currency}</b>\n\n<b>Sotib olish:</b> {ex}0.0 PIXEL uchun {round(rate / 10 * ex, 2)} {currency}\n\nTarmoq: " \
               f"<b>{net}.</b>\n\nMablag'lar darhol hisobga olinadi"
    elif language == "be":
        text = f"<b>➕ জমা: {currency}</b>\n\n<b>ক্রয়:</b> {ex}0.0 PIXEL জন্য {round(rate / 10 * ex, 2)} {currency}\n\nনেটওয়ার্ক: " \
               f"<b>{net}.</b>\n\nতহবিল অবিলম্বে জমা করা হবে"
    elif language == "hi":
        text = f"<b>➕ जमा: {currency}</b>\n\n<b>खरीदना:</b> {ex}0.0 PIXEL के लिए {round(rate / 10 * ex, 2)} {currency}\n\nनेटवर्क: " \
               f"<b>{net}.</b>\n\nधनराशि तुरंत जमा कर दी जाएगी"
    else:
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Purchase:</b> {ex}0.0 PIXEL for {round(rate / 10 * ex, 2)} {currency}\n\nNetwork: " \
               f"<b>{net}.</b>\n\nFunds will be credited immediately"
    return text


def text_sixth_card(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    net = lists.network_currency(user_id)
    ex = lists.exchange_sixth(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➕ Пополнить: {currency}</b>\n\n<b>Покупка:</b> {ex}0.0 PIXEL за {round(rate / 10 * ex, 2)} {currency}\n\nСеть: " \
               f"<b>{net}.</b>\n\nСредства будут зачислены сразу"
    elif language == "id":
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Pembelian:</b> {ex}0.0 PIXEL untuk {round(rate / 10 * ex, 2)} {currency}\n\nJaringan: " \
               f"<b>{net}.</b>\n\nDana akan segera dikreditkan"
    elif language == "es":
        text = f"<b>➕ Recibir: {currency}</b>\n\n<b>Compra:</b> {ex}0.0 PIXEL por {round(rate / 10 * ex, 2)} {currency}\n\nRed: " \
               f"<b>{net}.</b>\n\nLos fondos se acreditarán inmediatamente."
    elif language == "ko":
        text = f"<b>➕ 예치: {currency}</b>\n\n<b>구입:</b> {ex}0.0 PIXEL 위한 {round(rate / 10 * ex, 2)} {currency}\n\n네트워크: " \
               f"<b>{net}.</b>\n\n자금은 즉시 적립됩니다"
    elif language == "it":
        text = f"<b>➕ Deposita: {currency}</b>\n\n<b>Acquistare:</b> {ex}0.0 PIXEL per {round(rate / 10 * ex, 2)} {currency}\n\nRete: " \
               f"<b>{net}.</b>\n\nI fondi verranno accreditati immediatamente"
    elif language == "ch":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>購買：</b> {ex}0.0 PIXEL 為了 {round(rate / 10 * ex, 2)} {currency}\n\n网络：" \
               f"<b>{net}.</b>\n\n資金將立即存入"
    elif language == "ta":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>购买：</b> {ex}0.0 PIXEL 为了 {round(rate / 10 * ex, 2)} {currency}\n\n網絡：" \
               f"<b>{net}.</b>\n\n资金将立即存入"
    elif language == "fa":
        text = f"<b>➕ واریز کردن: {currency}</b>\n\n<b>خرید:</b> {ex}0.0 PIXEL برای {round(rate / 10 * ex, 2)} {currency}\n\nشبکه: " \
               f"<b>{net}.</b>\n\nوجوه بلافاصله واریز خواهد شد"
    elif language == "tr":
        text = f"<b>➕ Yatırma: {currency}</b>\n\n<b>Satın almak:</b> {ex}0.0 PIXEL için {round(rate / 10 * ex, 2)} {currency}\n\nAğ: " \
               f"<b>{net}.</b>\n\nFonlar hemen aktarılacak"
    elif language == "uz":
        text = f"<b>➕ To'ldirish: {currency}</b>\n\n<b>Sotib olish:</b> {ex}0.0 PIXEL uchun {round(rate / 10 * ex, 2)} {currency}\n\nTarmoq: " \
               f"<b>{net}.</b>\n\nMablag'lar darhol hisobga olinadi"
    elif language == "be":
        text = f"<b>➕ জমা: {currency}</b>\n\n<b>ক্রয়:</b> {ex}0.0 PIXEL জন্য {round(rate / 10 * ex, 2)} {currency}\n\nনেটওয়ার্ক: " \
               f"<b>{net}.</b>\n\nতহবিল অবিলম্বে জমা করা হবে"
    elif language == "hi":
        text = f"<b>➕ जमा: {currency}</b>\n\n<b>खरीदना:</b> {ex}0.0 PIXEL के लिए {round(rate / 10 * ex, 2)} {currency}\n\nनेटवर्क: " \
               f"<b>{net}.</b>\n\nधनराशि तुरंत जमा कर दी जाएगी"
    else:
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Purchase:</b> {ex}0.0 PIXEL for {round(rate / 10 * ex, 2)} {currency}\n\nNetwork: " \
               f"<b>{net}.</b>\n\nFunds will be credited immediately"
    return text


def text_seventh_card(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    net = lists.network_currency(user_id)
    ex = lists.exchange_seventh(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➕ Пополнить: {currency}</b>\n\n<b>Покупка:</b> {ex}0.0 PIXEL за {round(rate / 10 * ex, 2)} {currency}\n\nСеть: " \
               f"<b>{net}.</b>\n\nСредства будут зачислены сразу"
    elif language == "id":
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Pembelian:</b> {ex}0.0 PIXEL untuk {round(rate / 10 * ex, 2)} {currency}\n\nJaringan: " \
               f"<b>{net}.</b>\n\nDana akan segera dikreditkan"
    elif language == "es":
        text = f"<b>➕ Recibir: {currency}</b>\n\n<b>Compra:</b> {ex}0.0 PIXEL por {round(rate / 10 * ex, 2)} {currency}\n\nRed: " \
               f"<b>{net}.</b>\n\nLos fondos se acreditarán inmediatamente."
    elif language == "ko":
        text = f"<b>➕ 예치: {currency}</b>\n\n<b>구입:</b> {ex}0.0 PIXEL 위한 {round(rate / 10 * ex, 2)} {currency}\n\n네트워크: " \
               f"<b>{net}.</b>\n\n자금은 즉시 적립됩니다"
    elif language == "it":
        text = f"<b>➕ Deposita: {currency}</b>\n\n<b>Acquistare:</b> {ex}0.0 PIXEL per {round(rate / 10 * ex, 2)} {currency}\n\nRete: " \
               f"<b>{net}.</b>\n\nI fondi verranno accreditati immediatamente"
    elif language == "ch":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>購買：</b> {ex}0.0 PIXEL 為了 {round(rate / 10 * ex, 2)} {currency}\n\n网络：" \
               f"<b>{net}.</b>\n\n資金將立即存入"
    elif language == "ta":
        text = f"<b>➕ 存款: {currency}</b>\n\n<b>购买：</b> {ex}0.0 PIXEL 为了 {round(rate / 10 * ex, 2)} {currency}\n\n網絡：" \
               f"<b>{net}.</b>\n\n资金将立即存入"
    elif language == "fa":
        text = f"<b>➕ واریز کردن: {currency}</b>\n\n<b>خرید:</b> {ex}0.0 PIXEL برای {round(rate / 10 * ex, 2)} {currency}\n\nشبکه: " \
               f"<b>{net}.</b>\n\nوجوه بلافاصله واریز خواهد شد"
    elif language == "tr":
        text = f"<b>➕ Yatırma: {currency}</b>\n\n<b>Satın almak:</b> {ex}0.0 PIXEL için {round(rate / 10 * ex, 2)} {currency}\n\nAğ: " \
               f"<b>{net}.</b>\n\nFonlar hemen aktarılacak"
    elif language == "uz":
        text = f"<b>➕ To'ldirish: {currency}</b>\n\n<b>Sotib olish:</b> {ex}0.0 PIXEL uchun {round(rate / 10 * ex, 2)} {currency}\n\nTarmoq: " \
               f"<b>{net}.</b>\n\nMablag'lar darhol hisobga olinadi"
    elif language == "be":
        text = f"<b>➕ জমা: {currency}</b>\n\n<b>ক্রয়:</b> {ex}0.0 PIXEL জন্য {round(rate / 10 * ex, 2)} {currency}\n\nনেটওয়ার্ক: " \
               f"<b>{net}.</b>\n\nতহবিল অবিলম্বে জমা করা হবে"
    elif language == "hi":
        text = f"<b>➕ जमा: {currency}</b>\n\n<b>खरीदना:</b> {ex}0.0 PIXEL के लिए {round(rate / 10 * ex, 2)} {currency}\n\nनेटवर्क: " \
               f"<b>{net}.</b>\n\nधनराशि तुरंत जमा कर दी जाएगी"
    else:
        text = f"<b>➕ Deposit: {currency}</b>\n\n<b>Purchase:</b> {ex}0.0 PIXEL for {round(rate / 10 * ex, 2)} {currency}\n\nNetwork: " \
               f"<b>{net}.</b>\n\nFunds will be credited immediately"
    return text


def button_card(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        first = InlineKeyboardButton(text='300 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='600 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='1200 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='1800 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='6000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='60000 PIXEL', callback_data='seventh_card')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        first = InlineKeyboardButton(text='500 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='1000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='2000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='3000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='5000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='10000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='100000 PIXEL', callback_data='seventh_card')
    elif currency == "EGP" or currency == "INR":
        first = InlineKeyboardButton(text='100 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='200 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='400 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='600 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='1000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='2000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='20000 PIXEL', callback_data='seventh_card')
    else:
        first = InlineKeyboardButton(text=f'1000 PIXEL', callback_data='first_card')
        second = InlineKeyboardButton(text='2000 PIXEL', callback_data='second_card')
        third = InlineKeyboardButton(text='4000 PIXEL', callback_data='third_card')
        fourth = InlineKeyboardButton(text='6000 PIXEL', callback_data='fourth_card')
        fifth = InlineKeyboardButton(text='10000 PIXEL', callback_data='fifth_card')
        sixth = InlineKeyboardButton(text='20000 PIXEL', callback_data='sixth_card')
        seventh = InlineKeyboardButton(text='200000 PIXEL', callback_data='seventh_card')
    return first, second, third, fourth, fifth, sixth, seventh


def text_card(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    net = lists.network_currency(user_id)
    rate = exchange.get_price(user_id)
    if language == "ru":
        text = f"<b>➕ Пополнить: {currency}</b>\n\nИспользуйте суммы ниже для покупки PIXEL за {currency}.\nСеть: " \
               f"<b>{net}.</b>\n\n<b>Обменный курс:</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\nСредства будут зачислены сразу"
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = f"<b>➕ Deposit: {currency}</b>\n\nGunakan jumlah di bawah untuk membeli PIXEL untuk {currency}.\nJaringan: " \
               f"<b>{net}.</b>\n\n<b>Kurs:</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\nDana akan segera dikreditkan"
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = f"<b>➕ Recibir: {currency}</b>\n\nUtilice las cantidades siguientes para comprar PIXEL por {currency}.\nRed: " \
               f"<b>{net}.</b>\n\n<b>Tipo de cambio:</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\nLos fondos se acreditarán inmediatamente."
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = f"<b>➕ 예치: {currency}</b>\n\nPIXEL을 구매하려면 아래 금액을 사용하세요 위한 {currency}.\n네트워크: " \
               f"<b>{net}.</b>\n\n<b>환율:</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\n자금은 즉시 적립됩니다"
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = f"<b>➕ Deposita: {currency}</b>\n\nUtilizza gli importi seguenti per acquistare PIXEL per {currency}.\nRete: " \
               f"<b>{net}.</b>\n\n<b>Tasso di cambio:</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\nI fondi verranno accreditati immediatamente"
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = f"<b>➕ 存款: {currency}</b>\n\n使用以下金額購買 PIXEL 為了 {currency}.\n网络：" \
               f"<b>{net}.</b>\n\n<b>匯率：</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\n資金將立即存入"
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = f"<b>➕ 存款: {currency}</b>\n\n使用以下金额购买 PIXEL 为了 {currency}.\n網絡：" \
               f"<b>{net}.</b>\n\n<b>汇率：</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\n资金将立即存入"
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = f"<b>➕ واریز کردن: {currency}</b>\n\nبرای خرید PIXEL از مبالغ زیر استفاده کنید {currency}.\nشبکه: " \
               f"<b>{net}.</b>\n\n<b>قیمت ارز:</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\nوجوه بلافاصله واریز خواهد شد"
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = f"<b>➕ Yatırma: {currency}</b>\n\nPIXEL satın almak için aşağıdaki tutarları kullanın için {currency}.\nAğ: " \
               f"<b>{net}.</b>\n\n<b>Döviz kuru:</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\nFonlar hemen aktarılacak"
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = f"<b>➕ To'ldirish: {currency}</b>\n\nPIXEL sotib olish uchun quyidagi miqdorlardan foydalaning {currency}.\nTarmoq: " \
               f"<b>{net}.</b>\n\n<b>Valyuta kursi:</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\nMablag'lar darhol hisobga olinadi"
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = f"<b>➕ জমা: {currency}</b>\n\nPIXEL কেনার জন্য নিচের পরিমাণ ব্যবহার করুন {currency}.\nনেটওয়ার্ক: " \
               f"<b>{net}.</b>\n\n<b>বিনিময় হার:</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\nতহবিল অবিলম্বে জমা করা হবে"
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = f"<b>➕ जमा: {currency}</b>\n\nPIXEL खरीदने के लिए नीचे दी गई राशि का उपयोग करें {currency}.\nनेटवर्क: " \
               f"<b>{net}.</b>\n\n<b>विनिमय दर:</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\nधनराशि तुरंत जमा कर दी जाएगी"
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = f"<b>➕ Deposit: {currency}</b>\n\nUse the amounts below to purchase PIXEL for {currency}.\nNetwork: " \
               f"<b>{net}.</b>\n\n<b>Exchange rate:</b> 1 PIXEL ≈ {round(rate / 100, 4)} {currency}\n\nFunds will be credited immediately"
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text, back


def text_deposit(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    if language == "ru":
        text = "<b>➕ Пополнить</b>\n\nКаким способом вы хотите пополнить кошелек?"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='< Назад в кошелек', callback_data='wallet')
    elif language == "id":
        text = "<b>➕ Deposit</b>\n\nBagaimana Anda ingin menyetor dompet Anda?"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='< Kembali ke dompet', callback_data='wallet')
    elif language == "es":
        text = "<b>➕ Recibir</b>\n\n¿Cómo quieres depositar tu billetera?"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='< Volver a monedero', callback_data='wallet')
    elif language == "ko":
        text = "<b>➕ 예치</b>\n\n지갑을 어떻게 입금하시겠습니까?"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='< 지갑으로 돌아가기', callback_data='wallet')
    elif language == "it":
        text = "<b>➕ Deposita</b>\n\nCome vuoi depositare il tuo portafoglio?"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='< Ritorna al wallet', callback_data='wallet')
    elif language == "ch":
        text = "<b>➕ 存款</b>\n\n您想如何存入錢包？"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='< 返回錢包', callback_data='wallet')
    elif language == "ta":
        text = "<b>➕ 存款</b>\n\n您想如何存入钱包？"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='< 返回钱包', callback_data='wallet')
    elif language == "fa":
        text = "<b>➕ واریز کردن</b>\n\nچگونه می خواهید کیف پول خود را واریز کنید؟"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='< بازگشت به کیف پول', callback_data='wallet')
    elif language == "tr":
        text = "<b>➕ Yatırma</b>\n\nCüzdanınızı nasıl yatırmak istiyorsunuz?"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='< Cüzdana geri dön', callback_data='wallet')
    elif language == "uz":
        text = "<b>➕ To'ldirish</b>\n\nHamyoningizni qanday qilib depozitga qo'ymoqchisiz?"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='< Hamyonga qaytish', callback_data='wallet')
    elif language == "be":
        text = "<b>➕ জমা</b>\n\nআপনি কিভাবে আপনার ওয়ালেট জমা করতে চান?"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='< ওয়ালেটে ফিরে যান', callback_data='wallet')
    elif language == "hi":
        text = "<b>➕ जमा</b>\n\nआप अपना बटुआ कैसे जमा करना चाहते हैं?"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='<वॉलेट पर वापस जाएँ', callback_data='wallet')
    else:
        text = "<b>➕ Deposit</b>\n\nHow do you want to deposit your wallet?"
        cards = InlineKeyboardButton(text=f'💳 {currency}', callback_data='card')
        ton_c = InlineKeyboardButton(text='💎 TON', callback_data='ton_coin')
        back = InlineKeyboardButton(text='< Back to wallet', callback_data='wallet')
    return text, cards, ton_c, back


def button_promo_code(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        invite = InlineKeyboardButton(text='✉️ Отправить реферальную ссылку',
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='< Назад', callback_data='back')
    elif language == "id":
        invite = InlineKeyboardButton(text='✉️ Kirim tautan rujukan',
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='< Kembali', callback_data='back')
    elif language == "es":
        invite = InlineKeyboardButton(text='✉️ Enviar enlace de referencia',
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='< Volver', callback_data='back')
    elif language == "ko":
        invite = InlineKeyboardButton(text='✉️ 추천 링크 보내기',
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='back')
    elif language == "it":
        invite = InlineKeyboardButton(text='✉️ Invia collegamento di riferimento',
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='< Indietro', callback_data='back')
    elif language == "ch":
        invite = InlineKeyboardButton(text='✉️ 發送推薦鏈接',
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='< 返回', callback_data='back')
    elif language == "ta":
        invite = InlineKeyboardButton(text='✉️ 发送推荐链接',
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='< 返回', callback_data='back')
    elif language == "fa":
        invite = InlineKeyboardButton(text='✉️ ارسال لینک ارجاع',
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='< برگشت', callback_data='back')
    elif language == "tr":
        invite = InlineKeyboardButton(text='✉️ Yönlendirme bağlantısını gönder',
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='< Geri', callback_data='back')
    elif language == "uz":
        invite = InlineKeyboardButton(text="✉️ Yo'naltiruvchi havolani yuboring",
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='< Ortga', callback_data='back')
    elif language == "be":
        invite = InlineKeyboardButton(text='✉️ রেফারেল লিঙ্ক পাঠান',
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='back')
    elif language == "hi":
        invite = InlineKeyboardButton(text='✉️ रेफरल लिंक भेजें',
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='<वापस', callback_data='back')
    else:
        invite = InlineKeyboardButton(text='✉️ Send referral link',
                                      switch_inline_query=f'\n\nhttps://t.me/PlXELBOT?start={user_id}')
        back = InlineKeyboardButton(text='< Back', callback_data='back')
    return invite, back


def text_promo_code(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = f"🎁 <b>Пригласить друга</b>\n\n<b>Ваша ссылка:</b> https://t.me/PlXELBOT?start={user_id}\n\nДля получения 5 бесплатных игр, вам нужен друг, который не зарегистрирован в PIXEL. Ему просто нужно использовать вашу реферальную ссылку и вы получите бесплатные игры. Количество друзей неограничено."
    elif language == "id":
        text = f"🎁 <b>Undang teman</b>\n\n<b>Tautan Anda:</b> https://t.me/PlXELBOT?start={user_id}\n\nUntuk mendapatkan 5 game gratis Anda memerlukan teman yang tidak terdaftar di PIXEL. Dia hanya perlu menggunakan link referral Anda dan Anda akan mendapatkan game gratis. Jumlah teman tidak terbatas."
    elif language == "es":
        text = f"🎁 <b>Invitar a amigo</b>\n\n<b>Su enlace:</b> https://t.me/PlXELBOT?start={user_id}\n\nPara obtener 5 juegos gratis necesitas un amigo que no esté registrado en PIXEL. Sólo necesita usar tu enlace de referencia y obtendrás juegos gratis. El número de amigos es ilimitado."
    elif language == "ko":
        text = f"🎁 <b>친구를 초대하다</b>\n\n<b>귀하의 링크:</b> https://t.me/PlXELBOT?start={user_id}\n\n5개의 무료 게임을 받으려면 PIXEL에 등록되지 않은 친구가 필요합니다. 그는 귀하의 추천 링크를 사용하기만 하면 귀하는 무료 게임을 받을 수 있습니다. 친구 수는 무제한입니다."
    elif language == "it":
        text = f"🎁 <b>Invita un amico</b>\n\n<b>Il tuo collegamento:</b> https://t.me/PlXELBOT?start={user_id}\n\nPer ottenere 5 giochi gratuiti è necessario un amico che non sia registrato su PIXEL. Deve solo usare il tuo link di riferimento e otterrai giochi gratuiti. Il numero di amici è illimitato."
    elif language == "ch":
        text = f"🎁 <b>邀請朋友</b>\n\n<b>您的鏈接：</b> https://t.me/PlXELBOT?start={user_id}\n\n要獲得 5 個免費遊戲，您需要一個未註冊 PIXEL 的朋友。 他只需要使用您的推薦鏈接，您就可以獲得免費遊戲。 好友數量沒有限制。"
    elif language == "ta":
        text = f"🎁 <b>邀请朋友</b>\n\n<b>您的链接：</b> https://t.me/PlXELBOT?start={user_id}\n\n要获得 5 个免费游戏，您需要一个未注册 PIXEL 的朋友。 他只需要使用您的推荐链接，您就可以获得免费游戏。 好友数量没有限制。"
    elif language == "fa":
        text = f"🎁 <b>دعوت از دوست</b>\n\n<b>لینک شما:</b> https://t.me/PlXELBOT?start={user_id}\n\nبرای دریافت 5 بازی رایگان به دوستی نیاز دارید که در PIXEL ثبت نام نکرده باشد. او فقط باید از لینک ارجاع شما استفاده کند و شما بازی های رایگان دریافت خواهید کرد. تعداد دوستان نامحدود است."
    elif language == "tr":
        text = f"🎁 <b>Arkadaş davet et</b>\n\n<b>Senin linkin:</b> https://t.me/PlXELBOT?start={user_id}\n\n5 ücretsiz oyuna sahip olmak için PIXEL'e kayıtlı olmayan bir arkadaşınıza ihtiyacınız var. Sadece yönlendirme bağlantınızı kullanması gerekiyor ve ücretsiz oyunlar alacaksınız. Arkadaş sayısı sınırsızdır."
    elif language == "uz":
        text = f"🎁 <b>do'stni taklif</b>\n\n<b>Sizning havolangiz:</b> https://t.me/PlXELBOT?start={user_id}\n\n5 ta bepul o'yinni olish uchun sizga PIXEL-da ro'yxatdan o'tmagan do'st kerak. U faqat sizning havola havolasidan foydalanishi kerak va siz bepul o'yinlarga ega bo'lasiz. Do'stlar soni cheksiz."
    elif language == "be":
        text = f"🎁 <b>বন্ধু আমন্ত্রণ</b>\n\n<b>আপনার লিঙ্ক:</b> https://t.me/PlXELBOT?start={user_id}\n\n5টি বিনামূল্যের গেম পেতে আপনার একজন বন্ধুর প্রয়োজন যিনি PIXEL-এ নিবন্ধিত নন৷ তাকে শুধু আপনার রেফারেল লিঙ্ক ব্যবহার করতে হবে এবং আপনি বিনামূল্যে গেম পাবেন। বন্ধুর সংখ্যা সীমাহীন।"
    elif language == "hi":
        text = f"🎁 <b>मित्र को न्योता</b>\n\n<b>आपका लिंक:</b> https://t.me/PlXELBOT?start={user_id}\n\n5 निःशुल्क गेम प्राप्त करने के लिए आपको एक ऐसे मित्र की आवश्यकता है जो PIXEL के साथ पंजीकृत न हो। उसे बस आपके रेफरल लिंक का उपयोग करना होगा और आपको मुफ्त गेम मिलेंगे। मित्रों की संख्या असीमित है."
    else:
        text = f"🎁 <b>Invite friend</b>\n\n<b>Your link:</b> https://t.me/PlXELBOT?start={user_id}\n\nTo get 5 free games you need a friend who is not registered with PIXEL. He just needs to use your referral link and you will get free games. The number of friends is unlimited."
    webs = lists.webapp()
    if language == "ru":
        play = InlineKeyboardButton(text='💎 Открыть игру', web_app=webs)
    elif language == "id":
        play = InlineKeyboardButton(text='💎 Buka Permainan', web_app=webs)
    elif language == "es":
        play = InlineKeyboardButton(text='💎 Juego abierto', web_app=webs)
    elif language == "ko":
        play = InlineKeyboardButton(text='💎 오픈 게임', web_app=webs)
    elif language == "it":
        play = InlineKeyboardButton(text='💎 Apri il gioco', web_app=webs)
    elif language == "ch":
        play = InlineKeyboardButton(text='💎 開放遊戲', web_app=webs)
    elif language == "ta":
        play = InlineKeyboardButton(text='💎 开放游戏', web_app=webs)
    elif language == "fa":
        play = InlineKeyboardButton(text='💎 بازی را باز کنید', web_app=webs)
    elif language == "tr":
        play = InlineKeyboardButton(text='💎 Oyunu aç', web_app=webs)
    elif language == "uz":
        play = InlineKeyboardButton(text="💎 Ochiq o'yin", web_app=webs)
    elif language == "be":
        play = InlineKeyboardButton(text='💎 ওপেন গেম', web_app=webs)
    elif language == "hi":
        play = InlineKeyboardButton(text='💎 खुला खेल', web_app=webs)
    else:
        play = InlineKeyboardButton(text='💎 Open Game', web_app=webs)
    invite, back = button_promo_code(user_id)
    return text, invite, play, back


def text_change_currency(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = "<b>Локальная валюта</b>\n\nПожалуйста, выберите локальную валюту"
        back = InlineKeyboardButton(text='< Назад', callback_data='settings')
    elif language == "id":
        text = "<b>Mata uang lokal</b>\n\nSilakan pilih mata uang lokal"
        back = InlineKeyboardButton(text='< Kembali', callback_data='settings')
    elif language == "es":
        text = "<b>Moneda local</b>\n\nPor favor, seleccione la moneda local"
        back = InlineKeyboardButton(text='< Volver', callback_data='settings')
    elif language == "ko":
        text = "<b>현지 통화</b>\n\n현지 통화를 선택하세요"
        back = InlineKeyboardButton(text='< 뒤로', callback_data='settings')
    elif language == "it":
        text = "<b>Valuta locale</b>\n\nPer favore seleziona la valuta locale"
        back = InlineKeyboardButton(text='< Indietro', callback_data='settings')
    elif language == "ch":
        text = "<b>本地货币</b>\n\n请选择当地货币"
        back = InlineKeyboardButton(text='< 返回', callback_data='settings')
    elif language == "ta":
        text = "<b>本地貨幣</b>\n\n請選擇本地貨幣"
        back = InlineKeyboardButton(text='< 返回', callback_data='settings')
    elif language == "fa":
        text = "<b>واحد پول محلی</b>\n\nلطفا واحد پول محلی را انتخاب کنید"
        back = InlineKeyboardButton(text='< برگشت', callback_data='settings')
    elif language == "tr":
        text = "<b>Yerel para birimi</b>\n\nLütfen yerel parabirimi seçin"
        back = InlineKeyboardButton(text='< Geri', callback_data='settings')
    elif language == "uz":
        text = "<b>Mahalliy valyuta</b>\n\nIltimos, mahalliy valyutani tanlang"
        back = InlineKeyboardButton(text='< Ortga', callback_data='settings')
    elif language == "be":
        text = "<b>স্থানীয় মুদ্রা</b>\n\nঅনুগ্রহ করে স্থানীয় মুদ্রা নির্বাচন করুনy"
        back = InlineKeyboardButton(text='< পিছনে', callback_data='settings')
    elif language == "hi":
        text = "<b>स्थानीय मुद्रा</b>\n\nकृपया स्थानीय मुद्रा का चयन करें"
        back = InlineKeyboardButton(text='<वापस', callback_data='settings')
    else:
        text = "<b>Local currency</b>\n\nPlease select the local currency"
        back = InlineKeyboardButton(text='< Back', callback_data='settings')
    return text, back


def text_change_lang(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = "Пожалуйста, выберите язык"
    elif language == "id":
        text = "Silakan pilih bahasa yang ingin digunakan"
    elif language == "es":
        text = "Por favor, seleccione un idioma"
    elif language == "ko":
        text = "언어를 선택하세요"
    elif language == "it":
        text = "Per favore seleziona una lingua"
    elif language == "ch":
        text = "请选择语言"
    elif language == "ta":
        text = "請選擇語言"
    elif language == "fa":
        text = "لطفا زبان خود را انتخاب کنید"
    elif language == "tr":
        text = "Lütfen, bir dil seçin"
    elif language == "uz":
        text = "Iltimos tilni tanlang"
    elif language == "be":
        text = "অনুগ্রহ করে, ভাষা নির্বাচন করুন"
    elif language == "hi":
        text = "कृपया, एक भाषा चुनें"
    else:
        text = "Please, select a language"
    return text


def text_settings(user_id):
    language = db.get_language(user_id)
    currency = db.get_currency(user_id)
    if language == "ru":
        lang = "🇷🇺 Русский"
    elif language == "id":
        lang = "🇮🇩 Bahasa Indonesia"
    elif language == "es":
        lang = "🇪🇸 Español"
    elif language == "ko":
        lang = "🇰🇷 한국어"
    elif language == "it":
        lang = "🇮🇹 Italiano"
    elif language == "ch":
        lang = "🇨🇳 中文（简体）"
    elif language == "ta":
        lang = "🇹🇼 中文（繁體）"
    elif language == "fa":
        lang = "🇮🇷 فارسی"
    elif language == "tr":
        lang = "🇹🇷 Türkçe"
    elif language == "uz":
        lang = "🇺🇿 Oʻzbekcha"
    elif language == "be":
        lang = "🇮🇳 বাংলা"
    elif language == "hi":
        lang = "🇮🇳 हिंदी"
    else:
        lang = "🇬🇧 English"
    if language == "ru":
        text = f"⚙️ <b>Настройки</b>\n\nЯзык: {lang}\nЛокальная валюта: {currency}"
    elif language == "id":
        text = f"⚙️ <b>Pengaturan</b>\n\nBahasa: {lang}\nMata uang lokal: {currency}"
    elif language == "es":
        text = f"⚙️ <b>Ajustes</b>\n\nIdioma: {lang}\nMoneda local: {currency}"
    elif language == "ko":
        text = f"⚙️ <b>설정</b>\n\n언어: {lang}\n현지 통화: {currency}"
    elif language == "it":
        text = f"⚙️ <b>Impostazioni</b>\n\nLingua: {lang}\nValuta locale: {currency}"
    elif language == "ch":
        text = f"⚙️ <b>设置</b>\n\n语言：{lang}\n本地货币：{currency}"
    elif language == "ta":
        text = f"⚙️ <b>設置</b>\n\n語言：{lang}\n本地貨幣：{currency}"
    elif language == "fa":
        text = f"⚙️ <b>تنظیمات</b>\n\nزبان: {lang}\nواحد پول محلی: {currency}"
    elif language == "tr":
        text = f"⚙️ <b>Ayarlar</b>\n\nDil: {lang}\nYerel para birimi: {currency}"
    elif language == "uz":
        text = f"⚙️ <b>Sozlamalar</b>\n\nTil: {lang}\nMahalliy valyuta: {currency}"
    elif language == "be":
        text = f"⚙️ <b>সেটিংস</b>\n\nভাষা: {lang}\nস্থানীয় মুদ্রা: {currency}"
    elif language == "hi":
        text = f"⚙️ <b>सेटिंग्स</b>\n\nभाषा: {lang}\nस्थानीय मुद्रा: {currency}"
    else:
        text = f"⚙️ <b>Settings</b>\n\nLanguage: {lang}\nLocal currency: {currency}"
    return text


def button_settings(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        lang = InlineKeyboardButton(text='Изменить язык', callback_data='change_lang')
        value = InlineKeyboardButton(text='Изменить локальную валюту', callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 Открыть Wallet', web_app=webs)
        back = InlineKeyboardButton(text='< Назад', callback_data='back')
    elif language == "id":
        lang = InlineKeyboardButton(text='Ganti Bahasa', callback_data='change_lang')
        value = InlineKeyboardButton(text='Ganti mata uang lokal', callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 Buka Wallet', web_app=webs)
        back = InlineKeyboardButton(text='< Kembali', callback_data='back')
    elif language == "es":
        lang = InlineKeyboardButton(text='Cambiar idioma', callback_data='change_lang')
        value = InlineKeyboardButton(text='Cambiar moneda local', callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 Abrir Wallet', web_app=webs)
        back = InlineKeyboardButton(text='< Volver', callback_data='back')
    elif language == "ko":
        lang = InlineKeyboardButton(text='언어 변경', callback_data='change_lang')
        value = InlineKeyboardButton(text='현지 통화 변경', callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 월렛 열기', web_app=webs)
        back = InlineKeyboardButton(text='< 뒤로', callback_data='back')
    elif language == "it":
        lang = InlineKeyboardButton(text='Cambia la lingua', callback_data='change_lang')
        value = InlineKeyboardButton(text='Cambia la valuta locale', callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 Apri il Wallet', web_app=webs)
        back = InlineKeyboardButton(text='< Indietro', callback_data='back')
    elif language == "ch":
        lang = InlineKeyboardButton(text='改變語言', callback_data='change_lang')
        value = InlineKeyboardButton(text='更改當地貨幣', callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 打開錢包', web_app=webs)
        back = InlineKeyboardButton(text='< 返回', callback_data='back')
    elif language == "ta":
        lang = InlineKeyboardButton(text='改变语言', callback_data='change_lang')
        value = InlineKeyboardButton(text='更改当地货币', callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 打开钱包', web_app=webs)
        back = InlineKeyboardButton(text='< 返回', callback_data='back')
    elif language == "fa":
        lang = InlineKeyboardButton(text='تغییر زبان', callback_data='change_lang')
        value = InlineKeyboardButton(text='واحد پول محلی را تغییر دهید', callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 باز کردن Wallet', web_app=webs)
        back = InlineKeyboardButton(text='< برگشت', callback_data='back')
    elif language == "tr":
        lang = InlineKeyboardButton(text='Dili değiştir', callback_data='change_lang')
        value = InlineKeyboardButton(text='Yerel para birimini değiştir', callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 Wallet aç', web_app=webs)
        back = InlineKeyboardButton(text='< Geri', callback_data='back')
    elif language == "uz":
        lang = InlineKeyboardButton(text="Tilni o'zgartirish", callback_data='change_lang')
        value = InlineKeyboardButton(text="Mahalliy valyutani o'zgartirish", callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 Wallet ochish', web_app=webs)
        back = InlineKeyboardButton(text='< Ortga', callback_data='back')
    elif language == "be":
        lang = InlineKeyboardButton(text='ভাষা পরিবর্তন করুন', callback_data='change_lang')
        value = InlineKeyboardButton(text='স্থানীয় মুদ্রা পরিবর্তন করুন', callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 Wallet খুলুন', web_app=webs)
        back = InlineKeyboardButton(text='< পিছনে', callback_data='back')
    elif language == "hi":
        lang = InlineKeyboardButton(text='भाषा बदलें', callback_data='change_lang')
        value = InlineKeyboardButton(text='स्थानीय मुद्रा बदलें', callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 Wallet खोलें', web_app=webs)
        back = InlineKeyboardButton(text='<वापस', callback_data='back')
    else:
        lang = InlineKeyboardButton(text='Change language', callback_data='change_lang')
        value = InlineKeyboardButton(text='Change local currency', callback_data='change_currency')
        webs = lists.webapp()
        ow = InlineKeyboardButton(text='👛 Open Wallet', web_app=webs)
        back = InlineKeyboardButton(text='< Back', callback_data='back')
    return lang, value, ow, back


def text_tg_mode(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = f"💎 Попадите в «алмаз» и выиграйте от x5 от выстрела\n\n<a href='{config.MODE_URL}'>Выберите режим игры</a>:"
    elif language == "id":
        text = f"💎 Tekan «berlian» dan menangkan x5 dari tembakan\n\n<a href='{config.MODE_URL}'>Pilih mode permainan</a>:"
    elif language == "es":
        text = f"💎 Golpea el «diamante» y gana x5 desde el tiro\n\n<a href='{config.MODE_URL}'>Selecciona el modo de juego</a>:"
    elif language == "ko":
        text = f"💎 «다이아몬드»를 치고 샷에서 x5를 얻으세요\n\n<a href='{config.MODE_URL}'>게임 모드 선택</a>:"
    elif language == "it":
        text = f"💎 Colpisci il «diamante» e vinci x5 dal tiro\n\n<a href='{config.MODE_URL}'>Seleziona la modalità di gioco</a>:"
    elif language == "ch":
        text = f"💎 擊中“鑽石”並通過射擊贏得 x5\n\n<a href='{config.MODE_URL}'>選擇遊戲模式</a>："
    elif language == "ta":
        text = f"💎 击中“钻石”并通过射击赢得 x5\n\n<a href='{config.MODE_URL}'>选择游戏模式</a>："
    elif language == "fa":
        text = f'💎 "الماس" را بزنید و x5 را از ضربه برنده شوید\n\n<a href="{config.MODE_URL}">حالت بازی را انتخاب کنید</a>:'
    elif language == "tr":
        text = f'💎 "Elmas"a basın ve atıştan x5 kazanın\n\n<a href="{config.MODE_URL}">Oyun modunu seçin</a>:'
    elif language == "uz":
        text = f"💎 «Olmos» ni bosing va zarbadan x5 yutib oling\n\n<a href='{config.MODE_URL}'>O'yin rejimini tanlang</a>:"
    elif language == "be":
        text = f"💎 «হীরা» আঘাত করুন এবং শট থেকে x5 জিতুন\n\n<a href='{config.MODE_URL}'>গেম মোড নির্বাচন করুন</a>:"
    elif language == "hi":
        text = f"💎 «हीरा» मारो और शॉट से x5 जीतो\n\n<a href='{config.MODE_URL}'>गेम मोड चुनें</a>:"
    else:
        text = f"💎 Hit the «diamond» and win x5 from the shot\n\n<a href='{config.MODE_URL}'>Select game mode</a>:"
    return text


def button_tg_mode(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        game_norm = InlineKeyboardButton(text='Обычная игра', callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text='Быстрая игра', callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text='Бесплатная игра', callback_data='game_free')
        back = InlineKeyboardButton(text='< Назад', callback_data='back')
        rul = InlineKeyboardButton(text='Правила', url=config.RULES_URL)
    elif language == "id":
        game_norm = InlineKeyboardButton(text='Permainan biasa', callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text='Permainan cepat', callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text='Game gratis', callback_data='game_free')
        back = InlineKeyboardButton(text='< Kembali', callback_data='back')
        rul = InlineKeyboardButton(text='Aturan', url=config.RULES_URL)
    elif language == "es":
        game_norm = InlineKeyboardButton(text='juego normal', callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text='Juego rápido', callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text='Juego gratis', callback_data='game_free')
        back = InlineKeyboardButton(text='< Volver', callback_data='back')
        rul = InlineKeyboardButton(text='Normas', url=config.RULES_URL)
    elif language == "ko":
        game_norm = InlineKeyboardButton(text='정규 경기', callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text='빠른 게임', callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text='무료 게임', callback_data='game_free')
        back = InlineKeyboardButton(text='< 뒤로', callback_data='back')
        rul = InlineKeyboardButton(text='규칙', url=config.RULES_URL)
    elif language == "it":
        game_norm = InlineKeyboardButton(text='Gioco regolare', callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text='Gioco veloce', callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text='Gioco gratis', callback_data='game_free')
        back = InlineKeyboardButton(text='< Indietro', callback_data='back')
        rul = InlineKeyboardButton(text='Regole', url=config.RULES_URL)
    elif language == "ch":
        game_norm = InlineKeyboardButton(text='常規比賽', callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text='快速遊戲', callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text='免費遊戲', callback_data='game_free')
        back = InlineKeyboardButton(text='< 返回', callback_data='back')
        rul = InlineKeyboardButton(text='規則', url=config.RULES_URL)
    elif language == "ta":
        game_norm = InlineKeyboardButton(text='常规比赛', callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text='快速游戏', callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text='免费游戏', callback_data='game_free')
        back = InlineKeyboardButton(text='< 返回', callback_data='back')
        rul = InlineKeyboardButton(text='规则', url=config.RULES_URL)
    elif language == "fa":
        game_norm = InlineKeyboardButton(text='بازی معمولی', callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text='بازی سریع', callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text='بازی آزاد', callback_data='game_free')
        back = InlineKeyboardButton(text='< برگشت', callback_data='back')
        rul = InlineKeyboardButton(text='قوانین', url=config.RULES_URL)
    elif language == "tr":
        game_norm = InlineKeyboardButton(text='Normal oyun', callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text='Hızlı oyun', callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text='Bedava oyun', callback_data='game_free')
        back = InlineKeyboardButton(text='< Geri', callback_data='back')
        rul = InlineKeyboardButton(text='Tüzük', url=config.RULES_URL)
    elif language == "uz":
        game_norm = InlineKeyboardButton(text="muntazam o'yin", callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text="Tez o'yin", callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text="Bepul o'yin", callback_data='game_free')
        back = InlineKeyboardButton(text='< Ortga', callback_data='back')
        rul = InlineKeyboardButton(text='Qoidalar', url=config.RULES_URL)
    elif language == "be":
        game_norm = InlineKeyboardButton(text='নিয়মিত খেলা', callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text='দ্রুত খেলা', callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text='বিনামূল্যে খেলা', callback_data='game_free')
        back = InlineKeyboardButton(text='< পিছনে', callback_data='back')
        rul = InlineKeyboardButton(text='নিয়ম', url=config.RULES_URL)
    elif language == "hi":
        game_norm = InlineKeyboardButton(text='नियमित खेल', callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text='जल्दी से खेलने वाली गेम', callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text='मुफ्त खेल', callback_data='game_free')
        back = InlineKeyboardButton(text='<वापस', callback_data='back')
        rul = InlineKeyboardButton(text='नियम', url=config.RULES_URL)
    else:
        game_norm = InlineKeyboardButton(text='Classic Game', callback_data='norm_base_four')
        game_risk = InlineKeyboardButton(text='Quick Game', callback_data='risk_base_four')
        game_free = InlineKeyboardButton(text='Free Game', callback_data='game_free')
        back = InlineKeyboardButton(text='< Back', callback_data='back')
        rul = InlineKeyboardButton(text='Rules', url=config.RULES_URL)
    return game_norm, game_risk, game_free, back, rul


def button_ton_change_seventh(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='300 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='1200 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='1800 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_seventh_done')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='500 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='5000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_seventh_done')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='100 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='200 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='400 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_seventh_done')
    else:
        a = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='4000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_seventh_done')
    return a, b, c, d, e, f, g


def text_ton_change_seventh(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_ton_change_seventh(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: PIXEL → TON</b>\n\n<b>Покупка:</b> {argument / 100} TON за {argument} PIXEL"
    elif language == "id":
        text = f"<b>🔁 Tukar: PIXEL → TON</b>\n\n<b>Beli:</b> {argument / 100} TON menggunakan {argument} PIXEL"
    elif language == "es":
        text = f"<b>🔁 Cambiar: PIXEL → TON</b>\n\n<b>Compra:</b> {argument / 100} TON por {argument} PIXEL"
    elif language == "ko":
        text = f"<b>🔁 환전: PIXEL → TON</b>\n\n<b>구입:</b> {argument / 100} TON 위한 {argument} PIXEL"
    elif language == "it":
        text = f"<b>🔁 Scambia: PIXEL → TON</b>\n\n<b>Acquista:</b> {argument / 100} TON per {argument} PIXEL"
    elif language == "ch":
        text = f"<b>🔁 交易: PIXEL → TON</b>\n\n<b>購買:</b> {argument / 100} TON 為了 {argument} PIXEL"
    elif language == "ta":
        text = f"<b>🔁 兌據: PIXEL → TON</b>\n\n<b>购买:</b> {argument / 100} TON 为了 {argument} PIXEL"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: PIXEL → TON</b>\n\n<b>خرید:</b> {argument / 100} TON برای {argument} PIXEL"
    elif language == "tr":
        text = f"<b>🔁 Takas: PIXEL → TON</b>\n\n<b>Satın alma:</b> {argument / 100} TON için {argument} PIXEL"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: PIXEL → TON</b>\n\n<b>Xarid:</b> {argument / 100} TON uchun {argument} PIXEL"
    elif language == "be":
        text = f"<b>🔁 ক্রয়: PIXEL → TON</b>\n\n<b>ক্রয়:</b> {argument} PIXEL এর বদলে {argument / 100} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: PIXEL → TON</b>\n\n<b>खरीद:</b> {argument} PIXEL से {argument / 100} TON"
    else:
        text = f"<b>🔁 Exchange: PIXEL → TON</b>\n\n<b>Purchase:</b> {argument / 100} TON for {argument} PIXEL"
    return text


def button_ton_change_sixth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='300 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='1200 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='1800 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_sixth_done')
        g = InlineKeyboardButton(text='60000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='500 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='5000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_sixth_done')
        g = InlineKeyboardButton(text='100000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='100 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='200 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='400 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_sixth_done')
        g = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_seventh')
    else:
        a = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='4000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_sixth_done')
        g = InlineKeyboardButton(text='200000 PIXEL', callback_data='ton_change_seventh')
    return a, b, c, d, e, f, g


def text_ton_change_sixth(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_ton_change_sixth(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: PIXEL → TON</b>\n\n<b>Покупка:</b> {argument / 100} TON за {argument} PIXEL"
    elif language == "id":
        text = f"<b>🔁 Tukar: PIXEL → TON</b>\n\n<b>Beli:</b> {argument / 100} TON menggunakan {argument} PIXEL"
    elif language == "es":
        text = f"<b>🔁 Cambiar: PIXEL → TON</b>\n\n<b>Compra:</b> {argument / 100} TON por {argument} PIXEL"
    elif language == "ko":
        text = f"<b>🔁 환전: PIXEL → TON</b>\n\n<b>구입:</b> {argument / 100} TON 위한 {argument} PIXEL"
    elif language == "it":
        text = f"<b>🔁 Scambia: PIXEL → TON</b>\n\n<b>Acquista:</b> {argument / 100} TON per {argument} PIXEL"
    elif language == "ch":
        text = f"<b>🔁 交易: PIXEL → TON</b>\n\n<b>購買:</b> {argument / 100} TON 為了 {argument} PIXEL"
    elif language == "ta":
        text = f"<b>🔁 兌據: PIXEL → TON</b>\n\n<b>购买:</b> {argument / 100} TON 为了 {argument} PIXEL"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: PIXEL → TON</b>\n\n<b>خرید:</b> {argument / 100} TON برای {argument} PIXEL"
    elif language == "tr":
        text = f"<b>🔁 Takas: PIXEL → TON</b>\n\n<b>Satın alma:</b> {argument / 100} TON için {argument} PIXEL"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: PIXEL → TON</b>\n\n<b>Xarid:</b> {argument / 100} TON uchun {argument} PIXEL"
    elif language == "be":
        text = f"<b>🔁 ক্রয়: PIXEL → TON</b>\n\n<b>ক্রয়:</b> {argument} PIXEL এর বদলে {argument / 100} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: PIXEL → TON</b>\n\n<b>खरीद:</b> {argument} PIXEL से {argument / 100} TON"
    else:
        text = f"<b>🔁 Exchange: PIXEL → TON</b>\n\n<b>Purchase:</b> {argument / 100} TON for {argument} PIXEL"
    return text


def button_ton_change_fifth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='300 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='1200 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='1800 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_fifth_done')
        f = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='60000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='500 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_fifth_done')
        f = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='100000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='100 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='200 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='400 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_fifth_done')
        f = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_seventh')
    else:
        a = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='4000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_fifth_done')
        f = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='200000 PIXEL', callback_data='ton_change_seventh')
    return a, b, c, d, e, f, g


def text_ton_change_fifth(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_ton_change_fifth(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: PIXEL → TON</b>\n\n<b>Покупка:</b> {argument / 100} TON за {argument} PIXEL"
    elif language == "id":
        text = f"<b>🔁 Tukar: PIXEL → TON</b>\n\n<b>Beli:</b> {argument / 100} TON menggunakan {argument} PIXEL"
    elif language == "es":
        text = f"<b>🔁 Cambiar: PIXEL → TON</b>\n\n<b>Compra:</b> {argument / 100} TON por {argument} PIXEL"
    elif language == "ko":
        text = f"<b>🔁 환전: PIXEL → TON</b>\n\n<b>구입:</b> {argument / 100} TON 위한 {argument} PIXEL"
    elif language == "it":
        text = f"<b>🔁 Scambia: PIXEL → TON</b>\n\n<b>Acquista:</b> {argument / 100} TON per {argument} PIXEL"
    elif language == "ch":
        text = f"<b>🔁 交易: PIXEL → TON</b>\n\n<b>購買:</b> {argument / 100} TON 為了 {argument} PIXEL"
    elif language == "ta":
        text = f"<b>🔁 兌據: PIXEL → TON</b>\n\n<b>购买:</b> {argument / 100} TON 为了 {argument} PIXEL"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: PIXEL → TON</b>\n\n<b>خرید:</b> {argument / 100} TON برای {argument} PIXEL"
    elif language == "tr":
        text = f"<b>🔁 Takas: PIXEL → TON</b>\n\n<b>Satın alma:</b> {argument / 100} TON için {argument} PIXEL"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: PIXEL → TON</b>\n\n<b>Xarid:</b> {argument / 100} TON uchun {argument} PIXEL"
    elif language == "be":
        text = f"<b>🔁 ক্রয়: PIXEL → TON</b>\n\n<b>ক্রয়:</b> {argument} PIXEL এর বদলে {argument / 100} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: PIXEL → TON</b>\n\n<b>खरीद:</b> {argument} PIXEL से {argument / 100} TON"
    else:
        text = f"<b>🔁 Exchange: PIXEL → TON</b>\n\n<b>Purchase:</b> {argument / 100} TON for {argument} PIXEL"
    return text


def button_ton_change_fourth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='300 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='1200 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_fourth_done')
        e = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='60000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='500 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_fourth_done')
        e = InlineKeyboardButton(text='5000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='100000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='100 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='200 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='400 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_fourth_done')
        e = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_seventh')
    else:
        a = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='4000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_fourth_done')
        e = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='200000 PIXEL', callback_data='ton_change_seventh')
    return a, b, c, d, e, f, g


def text_ton_change_fourth(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_ton_change_fourth(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: PIXEL → TON</b>\n\n<b>Покупка:</b> {argument / 100} TON за {argument} PIXEL"
    elif language == "id":
        text = f"<b>🔁 Tukar: PIXEL → TON</b>\n\n<b>Beli:</b> {argument / 100} TON menggunakan {argument} PIXEL"
    elif language == "es":
        text = f"<b>🔁 Cambiar: PIXEL → TON</b>\n\n<b>Compra:</b> {argument / 100} TON por {argument} PIXEL"
    elif language == "ko":
        text = f"<b>🔁 환전: PIXEL → TON</b>\n\n<b>구입:</b> {argument / 100} TON 위한 {argument} PIXEL"
    elif language == "it":
        text = f"<b>🔁 Scambia: PIXEL → TON</b>\n\n<b>Acquista:</b> {argument / 100} TON per {argument} PIXEL"
    elif language == "ch":
        text = f"<b>🔁 交易: PIXEL → TON</b>\n\n<b>購買:</b> {argument / 100} TON 為了 {argument} PIXEL"
    elif language == "ta":
        text = f"<b>🔁 兌據: PIXEL → TON</b>\n\n<b>购买:</b> {argument / 100} TON 为了 {argument} PIXEL"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: PIXEL → TON</b>\n\n<b>خرید:</b> {argument / 100} TON برای {argument} PIXEL"
    elif language == "tr":
        text = f"<b>🔁 Takas: PIXEL → TON</b>\n\n<b>Satın alma:</b> {argument / 100} TON için {argument} PIXEL"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: PIXEL → TON</b>\n\n<b>Xarid:</b> {argument / 100} TON uchun {argument} PIXEL"
    elif language == "be":
        text = f"<b>🔁 ক্রয়: PIXEL → TON</b>\n\n<b>ক্রয়:</b> {argument} PIXEL এর বদলে {argument / 100} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: PIXEL → TON</b>\n\n<b>खरीद:</b> {argument} PIXEL से {argument / 100} TON"
    else:
        text = f"<b>🔁 Exchange: PIXEL → TON</b>\n\n<b>Purchase:</b> {argument / 100} TON for {argument} PIXEL"
    return text


def button_ton_change_third(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='300 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_third_done')
        d = InlineKeyboardButton(text='1800 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='60000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='500 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_third_done')
        d = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='5000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='100000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='100 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='200 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_third_done')
        d = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_seventh')
    else:
        a = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_second')
        c = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_third_done')
        d = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='200000 PIXEL', callback_data='ton_change_seventh')
    return a, b, c, d, e, f, g


def text_ton_change_third(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_ton_change_third(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: PIXEL → TON</b>\n\n<b>Покупка:</b> {argument / 100} TON за {argument} PIXEL"
    elif language == "id":
        text = f"<b>🔁 Tukar: PIXEL → TON</b>\n\n<b>Beli:</b> {argument / 100} TON menggunakan {argument} PIXEL"
    elif language == "es":
        text = f"<b>🔁 Cambiar: PIXEL → TON</b>\n\n<b>Compra:</b> {argument / 100} TON por {argument} PIXEL"
    elif language == "ko":
        text = f"<b>🔁 환전: PIXEL → TON</b>\n\n<b>구입:</b> {argument / 100} TON 위한 {argument} PIXEL"
    elif language == "it":
        text = f"<b>🔁 Scambia: PIXEL → TON</b>\n\n<b>Acquista:</b> {argument / 100} TON per {argument} PIXEL"
    elif language == "ch":
        text = f"<b>🔁 交易: PIXEL → TON</b>\n\n<b>購買:</b> {argument / 100} TON 為了 {argument} PIXEL"
    elif language == "ta":
        text = f"<b>🔁 兌據: PIXEL → TON</b>\n\n<b>购买:</b> {argument / 100} TON 为了 {argument} PIXEL"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: PIXEL → TON</b>\n\n<b>خرید:</b> {argument / 100} TON برای {argument} PIXEL"
    elif language == "tr":
        text = f"<b>🔁 Takas: PIXEL → TON</b>\n\n<b>Satın alma:</b> {argument / 100} TON için {argument} PIXEL"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: PIXEL → TON</b>\n\n<b>Xarid:</b> {argument / 100} TON uchun {argument} PIXEL"
    elif language == "be":
        text = f"<b>🔁 ক্রয়: PIXEL → TON</b>\n\n<b>ক্রয়:</b> {argument} PIXEL এর বদলে {argument / 100} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: PIXEL → TON</b>\n\n<b>खरीद:</b> {argument} PIXEL से {argument / 100} TON"
    else:
        text = f"<b>🔁 Exchange: PIXEL → TON</b>\n\n<b>Purchase:</b> {argument / 100} TON for {argument} PIXEL"
    return text


def button_ton_change_second(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='300 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_second_done')
        c = InlineKeyboardButton(text='1200 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='1800 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='60000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='500 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_second_done')
        c = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='3000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='5000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='100000 PIXEL', callback_data='ton_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='100 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_second_done')
        c = InlineKeyboardButton(text='400 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='600 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='2000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_seventh')
    else:
        a = InlineKeyboardButton(text='1000 PIXEL', callback_data='ton_change_first')
        b = InlineKeyboardButton(text='✅ Ok', callback_data='ton_change_second_done')
        c = InlineKeyboardButton(text='4000 PIXEL', callback_data='ton_change_third')
        d = InlineKeyboardButton(text='6000 PIXEL', callback_data='ton_change_fourth')
        e = InlineKeyboardButton(text='10000 PIXEL', callback_data='ton_change_fifth')
        f = InlineKeyboardButton(text='20000 PIXEL', callback_data='ton_change_sixth')
        g = InlineKeyboardButton(text='200000 PIXEL', callback_data='ton_change_seventh')
    return a, b, c, d, e, f, g


def text_ton_change_second(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_ton_change_second(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: PIXEL → TON</b>\n\n<b>Покупка:</b> {argument / 100} TON за {argument} PIXEL"
    elif language == "id":
        text = f"<b>🔁 Tukar: PIXEL → TON</b>\n\n<b>Beli:</b> {argument / 100} TON menggunakan {argument} PIXEL"
    elif language == "es":
        text = f"<b>🔁 Cambiar: PIXEL → TON</b>\n\n<b>Compra:</b> {argument / 100} TON por {argument} PIXEL"
    elif language == "ko":
        text = f"<b>🔁 환전: PIXEL → TON</b>\n\n<b>구입:</b> {argument / 100} TON 위한 {argument} PIXEL"
    elif language == "it":
        text = f"<b>🔁 Scambia: PIXEL → TON</b>\n\n<b>Acquista:</b> {argument / 100} TON per {argument} PIXEL"
    elif language == "ch":
        text = f"<b>🔁 交易: PIXEL → TON</b>\n\n<b>購買:</b> {argument / 100} TON 為了 {argument} PIXEL"
    elif language == "ta":
        text = f"<b>🔁 兌據: PIXEL → TON</b>\n\n<b>购买:</b> {argument / 100} TON 为了 {argument} PIXEL"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: PIXEL → TON</b>\n\n<b>خرید:</b> {argument / 100} TON برای {argument} PIXEL"
    elif language == "tr":
        text = f"<b>🔁 Takas: PIXEL → TON</b>\n\n<b>Satın alma:</b> {argument / 100} TON için {argument} PIXEL"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: PIXEL → TON</b>\n\n<b>Xarid:</b> {argument / 100} TON uchun {argument} PIXEL"
    elif language == "be":
        text = f"<b>🔁 ক্রয়: PIXEL → TON</b>\n\n<b>ক্রয়:</b> {argument} PIXEL এর বদলে {argument / 100} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: PIXEL → TON</b>\n\n<b>खरीद:</b> {argument} PIXEL से {argument / 100} TON"
    else:
        text = f"<b>🔁 Exchange: PIXEL → TON</b>\n\n<b>Purchase:</b> {argument / 100} TON for {argument} PIXEL"
    return text


def text_ton_change_first(user_id):
    language = db.get_language(user_id)
    argument = lists.argument_ton_change_first(user_id)
    if language == "ru":
        text = f"<b>🔁 Обменять: PIXEL → TON</b>\n\n<b>Покупка:</b> {argument / 100} TON за {argument} PIXEL"
    elif language == "id":
        text = f"<b>🔁 Tukar: PIXEL → TON</b>\n\n<b>Beli:</b> {argument / 100} TON menggunakan {argument} PIXEL"
    elif language == "es":
        text = f"<b>🔁 Cambiar: PIXEL → TON</b>\n\n<b>Compra:</b> {argument / 100} TON por {argument} PIXEL"
    elif language == "ko":
        text = f"<b>🔁 환전: PIXEL → TON</b>\n\n<b>구입:</b> {argument / 100} TON 위한 {argument} PIXEL"
    elif language == "it":
        text = f"<b>🔁 Scambia: PIXEL → TON</b>\n\n<b>Acquista:</b> {argument / 100} TON per {argument} PIXEL"
    elif language == "ch":
        text = f"<b>🔁 交易: PIXEL → TON</b>\n\n<b>購買:</b> {argument / 100} TON 為了 {argument} PIXEL"
    elif language == "ta":
        text = f"<b>🔁 兌據: PIXEL → TON</b>\n\n<b>购买:</b> {argument / 100} TON 为了 {argument} PIXEL"
    elif language == "fa":
        text = f"<b>🔁 مبادله کردن: PIXEL → TON</b>\n\n<b>خرید:</b> {argument / 100} TON برای {argument} PIXEL"
    elif language == "tr":
        text = f"<b>🔁 Takas: PIXEL → TON</b>\n\n<b>Satın alma:</b> {argument / 100} TON için {argument} PIXEL"
    elif language == "uz":
        text = f"<b>🔁 Almashtirish: PIXEL → TON</b>\n\n<b>Xarid:</b> {argument / 100} TON uchun {argument} PIXEL"
    elif language == "be":
        text = f"<b>🔁 ক্রয়: PIXEL → TON</b>\n\n<b>ক্রয়:</b> {argument} PIXEL এর বদলে {argument / 100} TON"
    elif language == "hi":
        text = f"<b>🔁 एक्सचेंज: PIXEL → TON</b>\n\n<b>खरीद:</b> {argument} PIXEL से {argument / 100} TON"
    else:
        text = f"<b>🔁 Exchange: PIXEL → TON</b>\n\n<b>Purchase:</b> {argument / 100} TON for {argument} PIXEL"
    return text


def button_pixel_change_fourth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='3 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='12 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_fourth_done')
        e = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='600 TON', callback_data='pixel_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='5 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_fourth_done')
        e = InlineKeyboardButton(text='50 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='1000 TON', callback_data='pixel_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='1 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='2 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='4 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_fourth_done')
        e = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_seventh')
    else:
        a = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='40 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_fourth_done')
        e = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='2000 TON', callback_data='pixel_change_seventh')
    return a, b, c, d, e, f, g


def button_pixel_change_fifth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='3 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='12 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='18 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_fifth_done')
        f = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='600 TON', callback_data='pixel_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='5 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_fifth_done')
        f = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='1000 TON', callback_data='pixel_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='1 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='2 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='4 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_fifth_done')
        f = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_seventh')
    else:
        a = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='40 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_fifth_done')
        f = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='2000 TON', callback_data='pixel_change_seventh')
    return a, b, c, d, e, f, g


def button_pixel_change_sixth(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='3 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='12 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='18 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_sixth_done')
        g = InlineKeyboardButton(text='600 TON', callback_data='pixel_change_seventh')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='5 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='50 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_sixth_done')
        g = InlineKeyboardButton(text='1000 TON', callback_data='pixel_change_seventh')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='1 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='2 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='4 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_sixth_done')
        g = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_seventh')
    else:
        a = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='40 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_sixth_done')
        g = InlineKeyboardButton(text='2000 TON', callback_data='pixel_change_seventh')
    return a, b, c, d, e, f, g


def button_pixel_change_seventh(user_id):
    currency = db.get_currency(user_id)
    if currency == "RUB" or currency == "RSD" or currency == "BYN" or currency == "UAH" or currency == "KZT" or currency == "MDL" or currency == "BRL" or currency == "COP" or currency == "ARS" or currency == "MYR" or currency == "GTQ" or currency == "CLP" or currency == "IDR":
        a = InlineKeyboardButton(text='3 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='12 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='18 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_seventh_done')
    elif currency == "ILS" or currency == "TWD" or currency == "TRY" or currency == "PLN" or currency == "RON" or currency == "AZN" or currency == "GEL" or currency == "AMD" or currency == "BGN" or currency == "MXN":
        a = InlineKeyboardButton(text='5 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='30 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='50 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_seventh_done')
    elif currency == "EGP" or currency == "INR":
        a = InlineKeyboardButton(text='1 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='2 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='4 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='6 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_seventh_done')
    else:
        a = InlineKeyboardButton(text='10 TON', callback_data='pixel_change_first')
        b = InlineKeyboardButton(text='20 TON', callback_data='pixel_change_second')
        c = InlineKeyboardButton(text='40 TON', callback_data='pixel_change_third')
        d = InlineKeyboardButton(text='60 TON', callback_data='pixel_change_fourth')
        e = InlineKeyboardButton(text='100 TON', callback_data='pixel_change_fifth')
        f = InlineKeyboardButton(text='200 TON', callback_data='pixel_change_sixth')
        g = InlineKeyboardButton(text='✅ Ok', callback_data='pixel_change_seventh_done')
    return a, b, c, d, e, f, g


def back_to_ton(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        back = InlineKeyboardButton(text='< Назад', callback_data='change')
    elif language == "id":
        back = InlineKeyboardButton(text='< Kembali', callback_data='change')
    elif language == "es":
        back = InlineKeyboardButton(text='< Volver', callback_data='change')
    elif language == "ko":
        back = InlineKeyboardButton(text='< 뒤로', callback_data='change')
    elif language == "it":
        back = InlineKeyboardButton(text='< Indietro', callback_data='change')
    elif language == "ch":
        back = InlineKeyboardButton(text='< 返回', callback_data='change')
    elif language == "ta":
        back = InlineKeyboardButton(text='< 返回', callback_data='change')
    elif language == "fa":
        back = InlineKeyboardButton(text='< برگشت', callback_data='change')
    elif language == "tr":
        back = InlineKeyboardButton(text='< Geri', callback_data='change')
    elif language == "uz":
        back = InlineKeyboardButton(text='< Ortga', callback_data='change')
    elif language == "be":
        back = InlineKeyboardButton(text='< পিছনে', callback_data='change')
    elif language == "hi":
        back = InlineKeyboardButton(text='<वापस', callback_data='change')
    else:
        back = InlineKeyboardButton(text='< Back', callback_data='change')
    return back


def des(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        description = "Игровая валюта будет зачислена на ваш кошелек сразу после оплаты"
    elif language == "id":
        description = "Mata uang game akan dikreditkan ke dompet Anda segera setelah pembayaran"
    elif language == "es":
        description = "La moneda del juego se acreditará en tu billetera inmediatamente después del pago."
    elif language == "ko":
        description = "결제 후 즉시 게임 화폐가 지갑에 적립됩니다."
    elif language == "it":
        description = "La valuta del gioco verrà accreditata sul tuo portafoglio immediatamente dopo il pagamento"
    elif language == "ch":
        description = "付款後遊戲幣將立即存入您的錢包"
    elif language == "ta":
        description = "付款后游戏币将立即存入您的钱包"
    elif language == "fa":
        description = "ارز بازی بلافاصله پس از پرداخت به کیف پول شما واریز می شود"
    elif language == "tr":
        description = "Oyun para birimi, ödeme yapıldıktan hemen sonra cüzdanınıza aktarılacaktır"
    elif language == "uz":
        description = "O'yin valyutasi to'lovdan so'ng darhol hamyoningizga o'tkaziladi"
    elif language == "be":
        description = "পেমেন্টের পরপরই আপনার ওয়ালেটে গেমের মুদ্রা জমা হবে"
    elif language == "hi":
        description = "भुगतान के तुरंत बाद गेम मुद्रा आपके वॉलेट में जमा कर दी जाएगी"
    else:
        description = "Game currency will be credited to your wallet immediately after payment"
    return description


# --------------------------------------------------------------------------------------------------------------------

def text_count(user_id, count):
    language = db.get_language(user_id)
    if language == "ru":
        text = f"Игры: <b>{count}</b>\n\nПожалуйста, выберите нужный <a href='{config.LEVEL_URL}'>уровень</a> и <a href='{config.SIZE_URL}'>размер поля</a>:"
    elif language == "id":
        text = f"Permainan: <b>{count}</b>\n\nSilakan pilih <a href='{config.LEVEL_URL}'>level</a> dan <a href='{config.SIZE_URL}'>ukuran bidang</a> yang diperlukan:"
    elif language == "es":
        text = f"Juegos: <b>{count}</b>\n\nSeleccione el <a href='{config.LEVEL_URL}'>nivel</a> requerido y el <a href='{config.SIZE_URL}'>tamaño del campo</a>:"
    elif language == "ko":
        text = f"계략: <b>{count}</b>\n\n필요한 <a href='{config.LEVEL_URL}'>수준</a>과 <a href='{config.SIZE_URL}'>필드 크기를</a> 선택하십시오."
    elif language == "it":
        text = f"Giochi: <b>{count}</b>\n\nSeleziona il <a href='{config.LEVEL_URL}'>livello</a> richiesto e la <a href='{config.SIZE_URL}'>dimensione del campo</a>:"
    elif language == "ch":
        text = f"遊戲：<b>{count}</b>\n\n請選擇所需<a href='{config.LEVEL_URL}'>的級別</a>和<a href='{config.SIZE_URL}'>字段大小</a>："
    elif language == "ta":
        text = f"游戏：<b>{count}</b>\n\n请选择所需<a href='{config.LEVEL_URL}'>的级别</a>和<a href='{config.SIZE_URL}'>字段大小</a>："
    elif language == "fa":
        text = f"بازی ها: <b>{count}</b>\n\nلطفا سطح و اندازه فیلد مورد نیاز را انتخاب کنید:"
    elif language == "tr":
        text = f"Oyunlar: <b>{count}</b>\n\nLütfen gerekli <a href='{config.LEVEL_URL}'>seviyeyi</a> ve <a href='{config.SIZE_URL}'>alan boyutunu</a> seçin:"
    elif language == "uz":
        text = f"Oʻyinlar: <b>{count}</b>\n\nIltimos, kerakli <a href='{config.LEVEL_URL}'>daraja</a> va <a href='{config.SIZE_URL}'>maydon hajmini</a> tanlang:"
    elif language == "be":
        text = f"গেম: <b>{count}</b>\n\nঅনুগ্রহ করে প্রয়োজনীয় <a href='{config.LEVEL_URL}'>স্তর</a> এবং <a href='{config.SIZE_URL}'>ক্ষেত্রের আকার</b> নির্বাচন করুন:"
    elif language == "hi":
        text = f"खेल: <b>{count}</b>\n\nकृपया आवश्यक <a href='{config.LEVEL_URL}'>स्तर</a> और <a href='{config.SIZE_URL}'>फ़ील्ड आकार</a> का चयन करें:"
    else:
        text = f"Games: <b>{count}</b>\n\nPlease select the required <a href='{config.LEVEL_URL}'>level</a> and <a href='{config.SIZE_URL}'>field size</a>:"
    return text


def button_level(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        level = InlineKeyboardButton(text='Уровень', url=config.LEVEL_URL)
    elif language == "id":
        level = InlineKeyboardButton(text='Tingkat', url=config.LEVEL_URL)
    elif language == "es":
        level = InlineKeyboardButton(text='Nivel', url=config.LEVEL_URL)
    elif language == "ko":
        level = InlineKeyboardButton(text='수준', url=config.LEVEL_URL)
    elif language == "it":
        level = InlineKeyboardButton(text='Livello', url=config.LEVEL_URL)
    elif language == "ch":
        level = InlineKeyboardButton(text='等級', url=config.LEVEL_URL)
    elif language == "ta":
        level = InlineKeyboardButton(text='等级', url=config.LEVEL_URL)
    elif language == "fa":
        level = InlineKeyboardButton(text='مرحله', url=config.LEVEL_URL)
    elif language == "tr":
        level = InlineKeyboardButton(text='Seviye', url=config.LEVEL_URL)
    elif language == "uz":
        level = InlineKeyboardButton(text='Daraja', url=config.LEVEL_URL)
    elif language == "be":
        level = InlineKeyboardButton(text='স্তর', url=config.LEVEL_URL)
    elif language == "hi":
        level = InlineKeyboardButton(text='स्तर', url=config.LEVEL_URL)
    else:
        level = InlineKeyboardButton(text='Level', url=config.LEVEL_URL)
    return level


def button_field_size(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        size = InlineKeyboardButton(text='Размер поля', url=config.SIZE_URL)
    elif language == "id":
        size = InlineKeyboardButton(text='Ukuran lapangan', url=config.SIZE_URL)
    elif language == "es":
        size = InlineKeyboardButton(text='Tamaño del campo', url=config.SIZE_URL)
    elif language == "ko":
        size = InlineKeyboardButton(text='필드 크기', url=config.SIZE_URL)
    elif language == "it":
        size = InlineKeyboardButton(text='Dimensione del campo', url=config.SIZE_URL)
    elif language == "ch":
        size = InlineKeyboardButton(text='場地大小', url=config.SIZE_URL)
    elif language == "ta":
        size = InlineKeyboardButton(text='场地大小', url=config.SIZE_URL)
    elif language == "fa":
        size = InlineKeyboardButton(text='اندازه میدان', url=config.SIZE_URL)
    elif language == "tr":
        size = InlineKeyboardButton(text='Alan boyutu', url=config.SIZE_URL)
    elif language == "uz":
        size = InlineKeyboardButton(text='Maydon hajmi', url=config.SIZE_URL)
    elif language == "be":
        size = InlineKeyboardButton(text='মাঠ আকৃতি', url=config.SIZE_URL)
    elif language == "hi":
        size = InlineKeyboardButton(text='मैदान की माप', url=config.SIZE_URL)
    else:
        size = InlineKeyboardButton(text='Field size', url=config.SIZE_URL)
    return size


def button_name_level(user_id, nl):
    language = db.get_language(user_id)
    if language == "ru":
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='Бронза', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='Серебро', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='Золото', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='VIP', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='База', callback_data='false')
    elif language == "id":
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='Perunggu', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='Perak', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='Emas', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='VIP', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='Basis', callback_data='false')
    elif language == "es":
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='Bronce', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='Plata', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='Oro', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='VIP', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='Base', callback_data='false')
    elif language == "ko":
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='청동', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='은', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='금', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='VIP', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='베이스', callback_data='false')
    elif language == "it":
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='Bronzo', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='Argento', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='Oro', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='VIP', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='Base', callback_data='false')
    elif language == "ch":
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='青銅', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='銀', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='金子', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='貴賓', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='根據', callback_data='false')
    elif language == "ta":
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='青铜', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='银', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='金子', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='贵宾', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='根据', callback_data='false')
    elif language == "fa":
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='برنز', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='نقره', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='طلا', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='VIP', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='پایگاه', callback_data='false')
    elif language == "tr":
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='Bronz', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='Gümüş', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='Altın', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='VIP', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='Temel', callback_data='false')
    elif language == "uz":
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='Bronza', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='Kumush', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='Oltin', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='VIP', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='Baza', callback_data='false')
    elif language == "be":
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='ব্রোঞ্জ', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='সিলভার', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='সোনা', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='ভিআইপি', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='বেস', callback_data='false')
    elif language == "hi":
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='पीतल', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='चाँदी', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='सोना', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='वीआईपी', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='आधार', callback_data='false')
    else:
        if nl == "bronze":
            name_level = InlineKeyboardButton(text='Bronze', callback_data='false')
        elif nl == "silver":
            name_level = InlineKeyboardButton(text='Silver', callback_data='false')
        elif nl == "gold":
            name_level = InlineKeyboardButton(text='Gold', callback_data='false')
        elif nl == "vip":
            name_level = InlineKeyboardButton(text='VIP', callback_data='false')
        else:
            name_level = InlineKeyboardButton(text='Base', callback_data='false')
    return name_level


def button_back(user_id, cb):
    language = db.get_language(user_id)
    if language == "ru":
        back = InlineKeyboardButton(text='< Назад', callback_data=cb)
    elif language == "id":
        back = InlineKeyboardButton(text='< Kembali', callback_data=cb)
    elif language == "es":
        back = InlineKeyboardButton(text='< Volver', callback_data=cb)
    elif language == "ko":
        back = InlineKeyboardButton(text='< 뒤로', callback_data=cb)
    elif language == "it":
        back = InlineKeyboardButton(text='< Indietro', callback_data=cb)
    elif language == "ch":
        back = InlineKeyboardButton(text='< 返回', callback_data=cb)
    elif language == "ta":
        back = InlineKeyboardButton(text='< 返回', callback_data=cb)
    elif language == "fa":
        back = InlineKeyboardButton(text='< برگشت', callback_data=cb)
    elif language == "tr":
        back = InlineKeyboardButton(text='< Geri', callback_data=cb)
    elif language == "uz":
        back = InlineKeyboardButton(text='< Ortga', callback_data=cb)
    elif language == "be":
        back = InlineKeyboardButton(text='< পিছনে', callback_data=cb)
    elif language == "hi":
        back = InlineKeyboardButton(text='<वापस', callback_data=cb)
    else:
        back = InlineKeyboardButton(text='< Back', callback_data=cb)
    return back


def button_new_game(user_id, cn):
    language = db.get_language(user_id)
    if language == "ru":
        new_game = InlineKeyboardButton(text='Новая игра', callback_data=cn)
    elif language == "id":
        new_game = InlineKeyboardButton(text='Permainan baru', callback_data=cn)
    elif language == "es":
        new_game = InlineKeyboardButton(text='Nuevo juego', callback_data=cn)
    elif language == "ko":
        new_game = InlineKeyboardButton(text='새로운 게임', callback_data=cn)
    elif language == "it":
        new_game = InlineKeyboardButton(text='Nuovo gioco', callback_data=cn)
    elif language == "ch":
        new_game = InlineKeyboardButton(text='新遊戲', callback_data=cn)
    elif language == "ta":
        new_game = InlineKeyboardButton(text='新游戏', callback_data=cn)
    elif language == "fa":
        new_game = InlineKeyboardButton(text='بازی جدید', callback_data=cn)
    elif language == "tr":
        new_game = InlineKeyboardButton(text='Yeni oyun', callback_data=cn)
    elif language == "uz":
        new_game = InlineKeyboardButton(text="Yangi o'yin", callback_data=cn)
    elif language == "be":
        new_game = InlineKeyboardButton(text='নতুন খেলা', callback_data=cn)
    elif language == "hi":
        new_game = InlineKeyboardButton(text='नया खेल', callback_data=cn)
    else:
        new_game = InlineKeyboardButton(text='New game', callback_data=cn)
    return new_game


def button_play(user_id, cp):
    language = db.get_language(user_id)
    if language == "ru":
        play = InlineKeyboardButton(text='💎 Играть', callback_data=cp)
    elif language == "id":
        play = InlineKeyboardButton(text='💎 Bermain', callback_data=cp)
    elif language == "es":
        play = InlineKeyboardButton(text='💎 Jugar', callback_data=cp)
    elif language == "ko":
        play = InlineKeyboardButton(text='💎 놀다', callback_data=cp)
    elif language == "it":
        play = InlineKeyboardButton(text='💎 Giocare', callback_data=cp)
    elif language == "ch":
        play = InlineKeyboardButton(text='💎 玩', callback_data=cp)
    elif language == "ta":
        play = InlineKeyboardButton(text='💎 玩', callback_data=cp)
    elif language == "fa":
        play = InlineKeyboardButton(text='💎 بازی', callback_data=cp)
    elif language == "tr":
        play = InlineKeyboardButton(text='💎 Oynamak', callback_data=cp)
    elif language == "uz":
        play = InlineKeyboardButton(text="💎 O'ynang", callback_data=cp)
    elif language == "be":
        play = InlineKeyboardButton(text='💎 খেলা', callback_data=cp)
    elif language == "hi":
        play = InlineKeyboardButton(text='💎 खेल', callback_data=cp)
    else:
        play = InlineKeyboardButton(text='💎 Play', callback_data=cp)
    return play


def button_go_friend(user_id):
    language = db.get_language(user_id)
    webs = lists.webapp()
    if language == "ru":
        play = InlineKeyboardButton(text='💎 Открыть игру', web_app=webs)
        back = InlineKeyboardButton(text="< Назад в меню", callback_data="back")
    elif language == "id":
        play = InlineKeyboardButton(text='💎 Buka Permainan', web_app=webs)
        back = InlineKeyboardButton(text="< Kembali ke menu", callback_data="back")
    elif language == "es":
        play = InlineKeyboardButton(text='💎 Juego abierto', web_app=webs)
        back = InlineKeyboardButton(text="< Volver al menú", callback_data="back")
    elif language == "ko":
        play = InlineKeyboardButton(text='💎 오픈 게임', web_app=webs)
        back = InlineKeyboardButton(text="< 메뉴로 돌아가기", callback_data="back")
    elif language == "it":
        play = InlineKeyboardButton(text='💎 Apri il gioco', web_app=webs)
        back = InlineKeyboardButton(text="< Torna al menu", callback_data="back")
    elif language == "ch":
        play = InlineKeyboardButton(text='💎 開放遊戲', web_app=webs)
        back = InlineKeyboardButton(text="< 返回菜單", callback_data="back")
    elif language == "ta":
        play = InlineKeyboardButton(text='💎 开放游戏', web_app=webs)
        back = InlineKeyboardButton(text="< 返回菜单", callback_data="back")
    elif language == "fa":
        play = InlineKeyboardButton(text='💎 بازی را باز کنید', web_app=webs)
        back = InlineKeyboardButton(text="< بازگشت به منو", callback_data="back")
    elif language == "tr":
        play = InlineKeyboardButton(text='💎 Oyunu aç', web_app=webs)
        back = InlineKeyboardButton(text="< Menüye geri dön", callback_data="back")
    elif language == "uz":
        play = InlineKeyboardButton(text="💎 Ochiq o'yin", web_app=webs)
        back = InlineKeyboardButton(text="< Menyuga qaytish", callback_data="back")
    elif language == "be":
        play = InlineKeyboardButton(text='💎 ওপেন গেম', web_app=webs)
        back = InlineKeyboardButton(text="< মেনুতে ফিরে যান", callback_data="back")
    elif language == "hi":
        play = InlineKeyboardButton(text='💎 खुला खेल', web_app=webs)
        back = InlineKeyboardButton(text="<मेनू पर वापस जाएँ", callback_data="back")
    else:
        play = InlineKeyboardButton(text='💎 Open Game', web_app=webs)
        back = InlineKeyboardButton(text="< Back to menu", callback_data="back")
    return play, back


def text_go_friend(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = "🎉 Друг использовал вашу реферальную ссылку.\n🎁 Бесплатные игры уже ждут вас!"
    elif language == "id":
        text = "🎉 Seorang teman menggunakan tautan referensi Anda.\n🎁 Game gratis sudah menunggu Anda!"
    elif language == "es":
        text = "🎉 Un amigo usó tu enlace de referencia.\n🎁 ¡Los juegos gratis ya te están esperando!"
    elif language == "ko":
        text = "🎉 친구가 귀하의 추천 링크를 사용했습니다.\n🎁 무료 게임이 이미 여러분을 기다리고 있습니다!"
    elif language == "it":
        text = "🎉 Un amico ha utilizzato il tuo link di riferimento.\n🎁 I giochi gratuiti ti stanno già aspettando!"
    elif language == "ch":
        text = "🎉 位朋友使用了您的推薦鏈接。\n🎁 免費遊戲已經在等你了！"
    elif language == "ta":
        text = "🎉 位朋友使用了您的推荐链接。\n🎁 免费游戏已经在等你了！"
    elif language == "fa":
        text = "🎉 یکی از دوستان از لینک ارجاع شما استفاده کرده است.\n🎁 بازی های رایگان در حال حاضر در انتظار شما هستند!"
    elif language == "tr":
        text = "🎉 Bir arkadaşınız yönlendirme bağlantınızı kullandı.\n🎁 Ücretsiz oyunlar zaten sizi bekliyor!"
    elif language == "uz":
        text = "🎉 Do'stingiz havolangizdan foydalangan.\n🎁 Bepul o'yinlar allaqachon sizni kutmoqda!"
    elif language == "be":
        text = "🎉 একজন বন্ধু আপনার রেফারেল লিঙ্ক ব্যবহার করেছে।\n🎁 বিনামূল্যে গেম ইতিমধ্যে আপনার জন্য অপেক্ষা করছে!"
    elif language == "hi":
        text = "🎉 एक मित्र ने आपके रेफरल लिंक का उपयोग किया।\n🎁 मुफ़्त गेम पहले से ही आपका इंतज़ार कर रहे हैं!"
    else:
        text = "🎉 A friend used your referral link.\n🎁 Free games are already waiting for you!"
    return text


def text_no_use(user_id):
    language = db.get_language(user_id)
    if language == "ru":
        text = "⚠️ Нельзя использовать свою реферальную ссылку!\n\nЧтобы запустить бота нажмите кнопку ниже или используйте команду /start"
        again = InlineKeyboardButton(text="Приступим!", url=config.START_URL)
    elif language == "id":
        text = "⚠️ Anda tidak dapat menggunakan link referral Anda!\n\nUntuk memulai bot, klik tombol di bawah atau gunakan perintah /start"
        again = InlineKeyboardButton(text="Mari kita mulai!", url=config.START_URL)
    elif language == "es":
        text = "⚠️ ¡No puedes usar tu enlace de referencia!\n\nPara iniciar el bot, haga clic en el botón a continuación o use el comando /start"
        again = InlineKeyboardButton(text="¡Empecemos!", url=config.START_URL)
    elif language == "ko":
        text = "⚠️ 추천 링크를 사용할 수 없습니다!\n\n봇을 시작하려면 아래 버튼을 클릭하거나 /start 명령을 사용하세요."
        again = InlineKeyboardButton(text="시작하자!", url=config.START_URL)
    elif language == "it":
        text = "⚠️ Non puoi utilizzare il tuo link di riferimento!\n\nPer avviare il bot, fai clic sul pulsante in basso o utilizza il comando /start"
        again = InlineKeyboardButton(text="Iniziamo!", url=config.START_URL)
    elif language == "ch":
        text = "⚠️ 您無法使用您的推薦鏈接！\n\n要啟動機器人，請單擊下面的按鈕或使用 /start 命令"
        again = InlineKeyboardButton(text="讓我們開始吧！", url=config.START_URL)
    elif language == "ta":
        text = "⚠️ 您无法使用您的推荐链接！\n\n要启动机器人，请单击下面的按钮或使用 /start 命令"
        again = InlineKeyboardButton(text="让我们开始吧！", url=config.START_URL)
    elif language == "fa":
        text = "⚠️ شما نمی توانید از لینک ارجاع خود استفاده کنید!\n\nبرای راه اندازی ربات، روی دکمه زیر کلیک کنید یا از دستور start / استفاده کنید"
        again = InlineKeyboardButton(text="بیا شروع کنیم!", url=config.START_URL)
    elif language == "tr":
        text = "⚠️ Yönlendirme bağlantınızı kullanamazsınız!\n\nBotu başlatmak için aşağıdaki butona tıklayın veya /start komutunu kullanın."
        again = InlineKeyboardButton(text="Başlayalım!", url=config.START_URL)
    elif language == "uz":
        text = "⚠️ Siz tavsiya havolasidan foydalana olmaysiz!\n\nBotni ishga tushirish uchun quyidagi tugmani bosing yoki /start buyrug'idan foydalaning"
        again = InlineKeyboardButton(text="Qani boshladik!", url=config.START_URL)
    elif language == "be":
        text = "⚠️ আপনি আপনার রেফারেল লিঙ্ক ব্যবহার করতে পারবেন না!\n\nবট শুরু করতে, নীচের বোতামে ক্লিক করুন বা /start কমান্ডটি ব্যবহার করুন"
        again = InlineKeyboardButton(text="চল শুরু করি!", url=config.START_URL)
    elif language == "hi":
        text = "⚠️ आप अपने रेफरल लिंक का उपयोग नहीं कर सकते!\n\nबॉट शुरू करने के लिए, नीचे दिए गए बटन पर क्लिक करें या /स्टार्ट कमांड का उपयोग करें"
        again = InlineKeyboardButton(text="आएँ शुरू करें!", url=config.START_URL)
    else:
        text = "⚠️ You can't use your referral link!\n\nTo start the bot, click the button below or use the /start command"
        again = InlineKeyboardButton(text="Let's get started!", url=config.START_URL)
    return text, again


