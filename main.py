from telethon import TelegramClient, events, types


# Telethon ile MySQL bağlantısını kullanın



# API anahtarlarınızı ve diğer bilgilerinizi buraya ekleyin
#hedef_id = '-1001940513035'
hedef_id = ''
api_id = ''
api_hash = ''
user_id_to_watch = 
channel_username = ''  # Kanalın kullanıcı adı
admin_user_id = ''  # Admin olarak belirlediğiniz kullanıcının ID'si
phone_number = ''
TOKEN=""
# Telegram istemcisini oluşturun


client1 = TelegramClient('client_session', api_id, api_hash)

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=TOKEN)
# /start komutunu işleyen olayları tanımlayın
@client.on(events.NewMessage(pattern='/ok'))
async def start(event):
    await event.respond('Selam!')

# @client.on(events.NewMessage(chats=('AgaevX')))
# async def yeni_mesaj(event):
#     await event.forward_to(hedef_id)

# @client.on(events.NewMessage(chats=('Agaev6881x')))
# async def yeni_mesaj(event):
#     await event.forward_to(hedef_id)

@client.on(events.NewMessage)
async def yeni_mesaj(event):
	if isinstance(event.chat, types.User) or isinstance(event.chat, types.Channel):
	    await event.forward_to(hedef_id)

# İstemciyi başlatın
with client:
    client.run_until_disconnected()
