#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#載入LineBot所需要的套件
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


# In[31]:


import pandas as pd


# In[32]:


test = pd.read_csv('test.csv')


# In[33]:


name = []
for i in test['品項']:
    for j in range(len(i)):
        if i[j] == '(':
            name.append(i[:j])
        elif i[j] == '（':
            name.append(i[:j])
kcal = []
for i in test['熱量(kcal)']:
    kcal.append(i)

category = []
for i in test['分類']:
    category.append(i)

menu = []
for i in range(len(name)):
    menu.append([name[i], int(kcal[i]), category[i]])


# In[34]:


category_lst = []
for i in category:
    if i not in category_lst:
        category_lst.append(i)


# In[ ]:

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
 # 訊息傳遞區塊
 # 基本上程式編輯都在這個function

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    

    # 開頭觸發文字
    if event.message.text == '我餓':
  
        try:
            inform_message = TextSendMessage(text='想吃哪類食物呢？')

            line_bot_api.push_message('Uc148f9785af67639ec3b4581f49bab47',FlexSendMessage(
                alt_text='主選單',
                contents={
                        "type": "bubble",
                        "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": [
                          {
                            "type": "text",
                            "text": "想吃哪一類食物呢?",
                            "weight": "bold",
                            "size": "lg",
                            "gravity": "center"
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                              {
                                "type": "button",
                                "action": {
                                  "type": "message",
                                  "label": "麵類",
                                  "text": "麵類"
                                },
                                "height": "sm",
                                "style": "secondary",
                                "gravity": "center",
                                "color": "#f1edff"
                              },
                             
                              {
                                "type": "button",
                                "action": {
                                  "type": "message",
                                  "label": "點心",
                                  "text": "點心"
                                },
                                "height": "sm",
                                "style": "secondary",
                                "gravity": "center",
                                "color": "#f1edff"
                              },
                             
                              {
                                "type": "button",
                                "action": {
                                  "type": "message",
                                  "label": "排餐",
                                  "text": "排餐"
                                },
                                "height": "sm",
                                "style": "secondary",
                                "gravity": "center",
                                "color": "#f1edff"
                              },
                             
                              {
                                "type": "button",
                                "action": {
                                  "type": "message",
                                  "label": "西式特餐",
                                  "text": "西式特餐"
                                },
                                "height": "sm",
                                "style": "secondary",
                                "gravity": "center",
                                "color": "#f1edff"
                              },
                              
                              {
                                "type": "button",
                                "action": {
                                  "type": "message",
                                  "label": "早餐",
                                  "text": "早餐"
                                },
                                "height": "sm",
                                "style": "secondary",
                                "gravity": "center",
                                "color": "#f1edff"
                              },
                              
                              {
                                "type": "button",
                                "action": {
                                  "type": "message",
                                  "label": "盤菜、自助餐",
                                  "text": "盤菜、自助餐"
                                },
                                "height": "sm",
                                "style": "secondary",
                                "gravity": "center",
                                "color": "#f1edff"
                              },
                             
                              {
                                "type": "button",
                                "action": {
                                  "type": "message",
                                  "label": "飯類",
                                  "text": "飯類"
                                },
                                "height": "sm",
                                "style": "secondary",
                                "gravity": "center",
                                "color": "#f1edff"
                              },
                                     {
                                "type": "button",
                                "action": {
                                  "type": "message",
                                  "label": "飲料",
                                  "text": "飲料"
                                },
                                "height": "sm",
                                "style": "secondary",
                                "gravity": "center",
                                "color": "#f1edff"
                              },   
                                {
                                "type": "button",
                                "action": {
                                  "type": "message",
                                  "label": "湯類",
                                  "text": "湯類"
                                },
                                "height": "sm",
                                "style": "secondary",
                                "gravity": "center",
                                "color": "#f1edff"
                              },
                             
                            ]
                          }
                        ]
                      }
                    }
            )
         
            #line_bot_api.reply_message(event.reply_token,[inform_message, mainMenu_flex_message])

        except ValueError:
            pass

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

