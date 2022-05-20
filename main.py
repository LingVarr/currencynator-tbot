# Импорт библиотек:
import requests
from bttns_kbrds import *
from aiogram import Bot, Dispatcher, executor, types
from pycoingecko import CoinGeckoAPI

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()  # < API с курсами фиатных валют.
cg = CoinGeckoAPI()  # < API с курсами криптовалют.
bot = Bot(token='5381141733:AAEFO27ho1UUk180LiREsk_O-cy17evahDU')  # < Токен Бота.
disp = Dispatcher(bot)


# Команда "/start":
@disp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Приветствую! Я Бот, который может подсказать '
                        'курс выбранной Фиатной валюты и Криптовалюты!', reply_markup=keyb_fiat)


# Клавиатура с Криптовалютой:
@disp.message_handler(text=['Криптовалюты (в $) >>>'])
async def next_keyboard(message: types.Message):
    await message.reply('Выбрана Криптовалюта', reply_markup=keyb_crypt)


# Клавиатура с Фиатной валютой:
@disp.message_handler(text=['<<< Фиатные валюты (в ₽)'])
async def next_keyboard(message: types.Message):
    await message.reply('Выбрана Фиатная валюта', reply_markup=keyb_fiat)


# Кнопки, показывающий курс выбранной Фиатной валюты при нажатии:
@disp.message_handler(text=['Доллар США ($) - USD'])
async def get_cur_usd(message: types.Message):
    usd_get = data['Valute']['USD']['Value']
    await message.reply(f'Курс Доллара: {usd_get}₽', reply_markup=keyb_fiat)


@disp.message_handler(text=['Евро (€) - EUR'])
async def get_cur_eur(message: types.Message):
    eur_get = data['Valute']['USD']['Value']
    await message.reply(f'Курс Евро: {eur_get}₽', reply_markup=keyb_fiat)


@disp.message_handler(text=['Швейцарский франк (₣) - CHF'])
async def get_cur_chf(message: types.Message):
    chf_get = data['Valute']['CHF']['Value']
    await message.reply(f'Курс Франка: {chf_get}₽', reply_markup=keyb_fiat)


@disp.message_handler(text=['Польский злотый (zł) - PLN'])
async def get_cur_pln(message: types.Message):
    pln_get = data['Valute']['PLN']['Value']
    await message.reply(f'Курс Злотого: {pln_get}₽', reply_markup=keyb_fiat)


@disp.message_handler(text=['Японская иена (¥) - JPY'])
async def get_cur_jpy(message: types.Message):
    jpy_get = data['Valute']['JPY']['Value']
    await message.reply(f'Курс Иена: {jpy_get}₽', reply_markup=keyb_fiat)


@disp.message_handler(text=['Китайский юань (¥) - CNY'])
async def get_cur_cny(message: types.Message):
    cny_get = round(data['Valute']['CNY']['Value'] * 0.1, 2)
    await message.reply(f'Курс Юаня: {cny_get}₽', reply_markup=keyb_fiat)


@disp.message_handler(text=['Белорусский рубль (Br) - BYN'])
async def get_cur_jpy(message: types.Message):
    bny_get = data['Valute']['BNY']['Value']
    await message.reply(f'Курс Бел. рубля: {bny_get}₽', reply_markup=keyb_fiat)


@disp.message_handler(text=['Украинская гривна (₴) - UAH'])
async def get_cur_uah(message: types.Message):
    uah_get = round(data['Valute']['UAH']['Value'] * 0.1, 2)
    await message.reply(f'Курс Гривны: {uah_get}₽', reply_markup=keyb_fiat)


@disp.message_handler(text=['Казахстанский тенге (₸) - KZT'])
async def get_cur_kzt(message: types.Message):
    kzt_get = round(data['Valute']['KZT']['Value'] * 0.01, 2)
    await message.reply(f'Курс Тенге: {kzt_get}₽', reply_markup=keyb_fiat)


@disp.message_handler(text=['Фунт стерлингов СК (£) - GBP'])
async def get_cur_gdp(message: types.Message):
    gdp_get = data['Valute']['GDP']['Value']
    await message.reply(f'Курс Фунта стерлингов: {gdp_get}₽', reply_markup=keyb_fiat)


# Кнопки, показывающий курс выбранной Криптовалюты при нажатии:
@disp.message_handler(text=['Bitcoin (₿) - BTC'])
async def btc_to_usd(message: types.Message):
    get_btc_to_usd = cg.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']
    await message.reply(f'Курс Bitcoin: {get_btc_to_usd}$', reply_markup=keyb_crypt)


@disp.message_handler(text=['Ethereum (Ξ) - ETH'])
async def eth_to_usd(message: types.Message):
    get_eth_to_usd = cg.get_price(ids='ethereum', vs_currencies='usd')['ethereum']['usd']
    await message.reply(f'Курс Ethereum: {get_eth_to_usd}$', reply_markup=keyb_crypt)


@disp.message_handler(text=['Bitcoin Cash (Ƀ) - BCH'])
async def bch_to_usd(message: types.Message):
    get_bch_to_usd = cg.get_price(ids='bitcoin-cash', vs_currencies='usd')['bitcoin-cash']['usd']
    await message.reply(f'Курс Bitcoin Cash: {get_bch_to_usd}$', reply_markup=keyb_crypt)


@disp.message_handler(text=['Monero (ɱ) - XMR'])
async def xmr_to_usd(message: types.Message):
    get_xmr_to_usd = cg.get_price(ids='monero', vs_currencies='usd')['monero']['usd']
    await message.reply(f'Курс Monero: {get_xmr_to_usd}$', reply_markup=keyb_crypt)


@disp.message_handler(text=['Tether (₮) - USDT'])
async def usdt_to_usd(message: types.Message):
    get_usdt_to_usd = cg.get_price(ids='tether', vs_currencies='usd')['tether']['usd']
    await message.reply(f'Курс Tether: {get_usdt_to_usd}$', reply_markup=keyb_crypt)


@disp.message_handler(text=['Solana (◎) - SOL'])
async def sol_to_usd(message: types.Message):
    get_sol_to_usd = cg.get_price(ids='solana', vs_currencies='usd')['solana']['usd']
    await message.reply(f'Курс Solana: {get_sol_to_usd}$', reply_markup=keyb_crypt)


@disp.message_handler(text=['Dogecoin (Ð) - DOGE'])
async def doge_to_usd(message: types.Message):
    get_doge_to_usd = cg.get_price(ids='dogecoin', vs_currencies='usd')['dogecoin']['usd']
    await message.reply(f'Курс Dogecoin: {get_doge_to_usd}$', reply_markup=keyb_crypt)


@disp.message_handler(text=['Litecoin (Ł) - LTC'])
async def ltc_to_usd(message: types.Message):
    get_ltc_to_usd = cg.get_price(ids='litecoin', vs_currencies='usd')['litecoin']['usd']
    await message.reply(f'Курс Litecoin: {get_ltc_to_usd}$', reply_markup=keyb_crypt)


if __name__ == '__main__':
    executor.start_polling(disp)
