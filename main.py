from telethon import TelegramClient

# API_ID, API_HASH kiriting
api_id = 'API_ID_KIRITING'
api_hash = 'API_HASH_KIRITING'

session_name = 'account'

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()
    print("Muvaffaqiyatli!")
    print("Session ushbu faylga saqlandi:", session_name + '.session')


with client:
    client.loop.run_until_complete(main())
