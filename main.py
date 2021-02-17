#!/usr/bin/env python3

from telegram.ext import (
    Updater,
    CommandHandler,
    Dispatcher,
    InlineQueryHandler,
    CallbackQueryHandler,
)
from telegram import (
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
    InlineKeyboardButton,
    InputMediaPhoto,
)
import logging
import qrcode
import subprocess
from uuid import uuid4
from settings import TOKEN, CACHING_CHAT_ID, PLACEHOLDER_QR, SOURCE_URL

logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)
updater = None


def inline(update, context):
    answers = []
    query = str(update.inline_query.query)

    qr = qrcode.QRCode()
    qr.add_data(query)
    qr.make()
    img = qr.make_image()
    img_id = uuid4()
    img.save(f"/tmp/qrcode{img_id}.png")

    answers.append(
        InlineQueryResultPhoto(
            id=uuid4(),
            title=query,
            photo_url=PLACEHOLDER_QR,
            thumb_url=PLACEHOLDER_QR,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Show Image", callback_data=str(img_id))]]
            ),
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, answers, cache_time=0)


def show_image(update, context):
    query = update.callback_query
    img_id = query.data

    file = context.bot.send_photo(
        chat_id=CACHING_CHAT_ID, photo=open(f"/tmp/qrcode{img_id}.png", "rb")
    )["photo"][-1]["file_id"]

    subprocess.call(f"rm /tmp/qrcode{img_id}.png", shell=True)

    context.bot.edit_message_media(
        inline_message_id=query.inline_message_id,
        media=InputMediaPhoto(media=file),
    )


def start(update, context):
    update.message.reply_text(
        """
To use this bot start typing
@qrencodebot <content>
and click on the image.
When message will be sent click on the "Show Image" button to display generated QR code.
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Source Code", url=SOURCE_URL)]]
        ),
    )


def main():
    global updater
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler(["start", "help"], start))
    dispatcher.add_handler(InlineQueryHandler(inline))
    dispatcher.add_handler(CallbackQueryHandler(show_image))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
