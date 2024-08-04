from telethon import TelegramClient, events, Button
import logging

# API ID və API Hash (Bu məlumatları Telegram Developer saytından əldə edə bilərsiniz)
API_ID = '20038971'
API_HASH = '19f2a0b0d4ca36631b9f3314b9ce8674'
TOKEN = '6874384795:AAHjxTi2SgTvZblnC_DLql3oeGf9oxdp_08'

# Məhsul məlumatlarını fayldan oxumaq
def load_products(filename='products.txt'):
    products = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    key, description = line.split('|', 1)
                    products[key] = description
    except FileNotFoundError:
        print(f"Xəta: {filename} faylı tapılmadı.")
    return products

# Məhsul məlumatları
products = load_products()

# Telegram müştəri obyektini yaradın
client = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=TOKEN)

# /start komandasına cavab
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    keyboard = [
        [Button.inline("Məhsul 1", b'product_1')],
        [Button.url("Sifariş 1", 'https://wa.me/0998666881?text=Sifari%C5%9F%201')]
    ]
    await event.respond('Məhsul seçin:', buttons=keyboard)

# Düyməyə klikləmə cavabı
@client.on(events.CallbackQuery)
async def button(event):
    product_key = event.data.decode('utf-8')

    if product_key in products:
        response_text = products[product_key]
    else:
        response_text = 'Məhsul tapılmadı.'

    await event.edit(response_text)

# Botu işə salın
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    client.run_until_disconnected()
