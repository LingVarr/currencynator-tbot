from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

usd_cur = KeyboardButton('Доллар США ($) - USD')
eur_cur = KeyboardButton('Евро (€) - EUR')
chf_cur = KeyboardButton('Швейцарский франк (₣) - CHF')
pln_cur = KeyboardButton('Польский злотый (zł) - PLN')
jpy_cur = KeyboardButton('Японская иена (¥) - JPY')
cny_cur = KeyboardButton('Китайский юань (¥) - CNY')
byn_cur = KeyboardButton('Белорусский рубль (Br) - BYN')
uah_cur = KeyboardButton('Украинская гривна (₴) - UAH')
kzt_cur = KeyboardButton('Казахстанский тенге (₸) - KZT')
gbp_cur = KeyboardButton('Фунт стерлингов СК (£) - GBP')
next_but = KeyboardButton('Криптовалюты (в $) >>>')

keyb_fiat = ReplyKeyboardMarkup(row_width=1).add(usd_cur, eur_cur, cny_cur, kzt_cur, pln_cur,
                                                 uah_cur, byn_cur, gbp_cur, chf_cur, jpy_cur, next_but)

btc_cur = KeyboardButton('Bitcoin (₿) - BTC')
eth_cur = KeyboardButton('Ethereum (Ξ) - ETH')
bch_cur = KeyboardButton('Bitcoin Cash (Ƀ) - BCH')
xmr_cur = KeyboardButton('Monero (ɱ) - XMR')
usdt_cur = KeyboardButton('Tether (₮) - USDT')
sol_cur = KeyboardButton('Solana (◎) - SOL')
doge_cur = KeyboardButton('Dogecoin (Ð) - DOGE')
ltc_cur = KeyboardButton('Litecoin (Ł) - LTC')
back_but = KeyboardButton('<<< Фиатные валюты (в ₽)')

keyb_crypt = ReplyKeyboardMarkup(row_width=1).add(btc_cur, eth_cur, bch_cur, xmr_cur, usdt_cur,
                                                  sol_cur, doge_cur, ltc_cur, back_but)
