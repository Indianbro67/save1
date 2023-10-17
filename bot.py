from pyrogram import Client, filters
from pyrogram.types import Message

api_id = '22860197'
api_hash = '577f362c70fe9bb911d7c876801c1ed5'
bot_token = '6570500718:AAEWO94h-xzWfnHhh3IPiU6Lc8PRzfrzbmE'

app = Client('m_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

async def check_bio_and_send_details(client, message, chat_id):
    user_id = message.from_user.id

    async def get_user_bio(user_id):
        try:
            chat = await client.get_chat(user_id)


            return chat.bio
        except Exception as e:
            return None

    bio = await get_user_bio(user_id)

    if bio and any(link in bio for link in ('http://', 'https://', 'www.', '/t.me', '@')):
        name = f"{message.from_user.first_name} {message.from_user.last_name or ''}"
        username = f"@{message.from_user.username or 'N/A'}"
        user_details = f"User Details:\nName: {name}\nUsername: {username}\nUser ID: {user_id}\nBio: {bio}"

        await client.send_message(chat_id, user_details)

@app.on_message(filters.text)
async def check_user_message(client, message: Message):
    chat_id = 5841005593
    await check_bio_and_send_details(client, message, chat_id)

app.run()
