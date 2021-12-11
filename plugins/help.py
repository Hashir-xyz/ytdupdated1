from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"CLICK DOWNLOAD OPTION -- Select Platform-- Enter Link -- Select Quality!!!"
    await message.reply_text(helptxt)
