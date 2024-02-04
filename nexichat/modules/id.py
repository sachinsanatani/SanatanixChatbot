from pyrogram import filters
from pyrogram.enums import ParseMode

from nexichat import nexichat


@nexichat.on_cmd("id")
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[мєѕѕєgє ι∂:]({message.link})** `{message_id}`\n"
    text += f"**[уσυʀ ι∂:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[ᴜsᴇʀ ɪᴅ:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("ᴛʜɪs ᴜsᴇʀ ᴅᴏᴇsɴ'ᴛ ᴇxɪsᴛ.", quote=True)

    text += f"**[ᴄнαт ι∂:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[ʀєρℓιє∂ мєѕѕєgє ι∂:]({reply.link})** `{reply.id}`\n"
        text += f"**[ʀєρℓιє∂ υѕєʀ ι∂:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"тнє fσʀωαʀ∂є∂ ᴄнαииєℓ, {reply.forward_from_chat.title}, нαѕ αи ι∂ σf `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"ι∂ σf тнє ʀєρℓιє∂ ᴄнαт/ᴄнαииєℓ, ιѕ `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )
