#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, StickerSendMessage
)

# from scraper file
from scraper import get_exchange_rate


def reply_exchange_rate(name):
    try:
        # {"美元":{"bids": 30,...}}
        exchange_rate = get_exchange_rate()
        # buy
        bids = exchange_rate[name]["bids"]
        # sell
        offers = exchange_rate[name]["offers"]
        reply_str = "{} Buy:{},Sell:{}".format(name, bids, offers)
        return reply_str
    except:
        return "Please enter a currency. Format : 美元"


app = Flask(__name__)
print("[程式開始運行]")

CHANNEL_ACCESS_TOKEN = 'HtlGlxurH7P2JLHkE/8KLmuEFs4Vo8VLo9fsTGyZxRA5/3O6Phex3UjKWPewa/utbY6joerh+8Xll94FZehuIJIZz4rsLW0Hdz0hJWPjGb0TvUIu+IS+vg0SSCldzOSGIpDbpxqQf3xAhcPmmu6/4gdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '19f681005805fe30d780464fd129eabc'


#  X-LINE-SIGNATURE

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    print('[REQUEST]')
    print(request)
    print('[SIGNATURE]')
    print(signature)

    body = request.get_data(as_text=True)
    print("[BODY]")
    print(body)
    app.logger.info("Request body: " + body)

    try:
        print('[try]')
        handler.handle(body, signature)
    except InvalidSignatureError:
        print('[except]')
        abort(400)

    return 'OK'

# message handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print('[使用者傳入文字訊息]')
    print(str(event))
    user_msg = event.message.text
    reply_msg = reply_exchange_rate(user_msg)
    reply = TextSendMessage(text=reply_msg)

    line_bot_api.reply_message(
        event.reply_token,
        reply)


# sticker message
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    print('[使用者傳入貼圖訊息]')
    print(str(event))
    
    reply = StickerSendMessage(package_id='2', sticker_id='149')

    line_bot_api.reply_message(
        event.reply_token,
        reply)


import os
if __name__ == "__main__":
    print('[伺服器開始運行]')
    port = int(os.environ.get('PORT', 8080))
    print('[預計運行於連接端口:{}]'.format(port))
    app.run(host='0.0.0.0', port=port)
