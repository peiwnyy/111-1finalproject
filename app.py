from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('QdnxdzUpW3bG3IekkGkys2bKehjP46GR3pABHDgqz0oFVcIkVNYjYaadWnbI1vpyv+CzYjTGOavX2eFBXVCixm4TxrGVul2RZlVg0/m9hZZ5s2rqbZa+iq/nm9lMxyiYfu6NpLC4W8g7D2v+3FOFKAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('1d52764ed6d474557dd6b589adecddac')

line_bot_api.push_message('Uc148f9785af67639ec3b4581f49bab47', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 訊息傳遞區塊
# 基本上程式編輯都在這個function
 @handler.add(MessageEvent, message=TextMessage)
 def handle_message(event):
     message = text=event.message.text
     if re.match('告訴我秘密',message):
         buttons_template_message = TemplateSendMessage(
         alt_text='這個看不到',
         template=ButtonsTemplate(
             thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
             title='行銷搬進大程式',
             text='選單功能－TemplateSendMessage',
             actions=[
                 PostbackAction(
                     label='偷偷傳資料',
                     display_text='檯面上',
                     data='action=檯面下'
                 ),
                 MessageAction(
                     label='光明正大傳資料',
                     text='我就是資料'
                 ),
                 URIAction(
                     label='行銷搬進大程式',
                     uri='https://marketingliveincode.com/'
                 )
             ]
         )
     )
         line_bot_api.reply_message(event.reply_token, buttons_template_message)
     else:
         line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
# 主程式
import os
if __name__ == "__main__":
     port = int(os.environ.get('PORT', 5000))
     app.run(host='0.0.0.0', port=port)
