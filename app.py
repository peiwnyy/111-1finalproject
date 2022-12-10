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
# In[14]:


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('小幫手在嗎',message):
        buttons_template_message = TemplateSendMessage(
            alt_text='這個看不到',
            template=ButtonsTemplate(
            thumbnail_image_url='https://www.lib.ntu.edu.tw/img/cm_room_img1.jpg',
            title='在！你想幹嘛呢',
            text='有一些功能',
            actions=[
                 URIAction(
                     label='看學餐',
                     uri='https://meals.ntu.edu.tw/restaurant'
                 ),
                 MessageAction(
                     label='我餓',
                     text='我餓'
                 ),
                 URIAction(
                     label='每日卡路里',
                     uri='https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=544&pid=726'
                        )
                   ]
               )
             )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
'''           
         elif re.match('我餓',message):
         # Flex Message Simulator網頁：https://developers.line.biz/console/fx/
             flex_message = FlexSendMessage(
                 alt_text='行銷搬進大程式',
                 contents={
  "type": "bubble",
  "body": {
    "type": "box",        
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "想吃什麼？",
        "size": "lg"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "麵類",
          "text": "麵類"
        },
        "style": "secondary",
        "color": "#FFFFE0",
        "height": "sm",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "backgroundColor": "#FFFFFF",
        "margin": "lg"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "點心",
          "text": "點心"
        },
        "style": "secondary",
        "color": "#FFFFE0",
        "height": "sm",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "backgroundColor": "#FFFFFF",
        "margin": "lg"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "text": "排餐",
          "label": "排餐"
        },
        "style": "secondary",
        "color": "#FFFFE0",
        "height": "sm",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "backgroundColor": "#FFFFFF",
        "margin": "lg"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "西式特餐",
          "text": "西式特餐"
        },
        "style": "secondary",
        "color": "#FFFFE0",
        "height": "sm",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "backgroundColor": "#FFFFFF",
        "margin": "lg"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "早餐",
          "text": "早餐"
        },
        "style": "secondary",
        "color": "#FFFFE0",
        "height": "sm",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "backgroundColor": "#FFFFFF",
        "margin": "lg"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "盤菜、自助餐",
          "text": "盤菜、自助餐"
        },
        "style": "secondary",
        "color": "#FFFFE0",
        "height": "sm",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "backgroundColor": "#FFFFFF",
        "margin": "lg"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "飯類",
          "text": "飯類"
        },
        "style": "secondary",
        "color": "#FFFFE0",
        "height": "sm",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "backgroundColor": "#FFFFFF",
        "margin": "lg"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "飲料",
          "text": "飲料"
        },
        "style": "secondary",
        "color": "#FFFFE0",
        "height": "sm",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "backgroundColor": "#FFFFFF",
        "margin": "lg"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "湯類",
          "text": "湯類"
        },
        "style": "secondary",
        "color": "#FFFFE0",
        "height": "sm",
        "gravity": "center"
      }
    ]
  }
}
         )
             line_bot_api.reply_message(evented.reply_token, flex_message)
'''         
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你在叫我嗎:]'))
            
            
          
 
 # 主程式
import os
if __name__ == "__main__":
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)



