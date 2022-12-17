from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
import pandas as pd


app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('QdnxdzUpW3bG3IekkGkys2bKehjP46GR3pABHDgqz0oFVcIkVNYjYaadWnbI1vpyv+CzYjTGOavX2eFBXVCixm4TxrGVul2RZlVg0/m9hZZ5s2rqbZa+iq/nm9lMxyiYfu6NpLC4W8g7D2v+3FOFKAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('1d52764ed6d474557dd6b589adecddac')

line_bot_api.push_message('Uc148f9785af67639ec3b4581f49bab47', TextSendMessage(text='你可以開始了'))


test = pd.read_csv('test.csv')########(檔案路徑要換)

name = []
for i in test['品項']:
    for j in range(len(i)):
        if i[j] == '(':
            a = i[:j]
            name.append(a)
            break
        elif i[j] == '（':
            a = i[:j]
            name.append(a)
            break
        elif i[j] == ' ':
            if i[j+1] == '/' or i[j+1] == '1':
                pass
            else:
                a = i[:j]
                name.append(a)
                break

kcal = []
for i in test['熱量(kcal)']:
    kcal.append(int(i))

category = []
for i in test['分類']:
    category.append(i)

dict = {}
for i in range(len(name)):
    dict[name[i]] = kcal[i]

type = ['麵類', '點心', '排餐', '西式特餐', '早餐', '盤菜、自助餐', '飯類', '飲料', '湯類']

noodel = []
for i in range(len(category)):
    if category[i] == '麵類':
        noodel.append(name[i])

snack = []
for i in range(len(category)):
    if category[i] == '點心':
        snack.append(name[i])

meal = []
for i in range(len(category)):
    if category[i] == '排餐':
        meal.append(name[i])

western_meal = []
for i in range(len(category)):
    if category[i] == '西式特餐':
        western_meal.append(name[i])

breakfast = []
for i in range(len(category)):
    if category[i] == '早餐':
        breakfast.append(name[i])

buffet = []
for i in range(len(category)):
    if category[i] == '盤菜、自助餐':
        buffet.append(name[i])

rice = []
for i in range(len(category)):
    if category[i] == '飯類':
        rice.append(name[i])

beverage = []
for i in range(len(category)):
    if category[i] == '飲料':
        beverage.append(name[i])

soup = []
for i in range(len(category)):
    if category[i] == '湯類':
        soup.append(name[i])

namestr = ''.join(name)＝

stored_list = []

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


#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    
    #這裡是發小幫手在嗎以後會出現的選單(有總圖圖片的)
    if re.match('小幫手在嗎',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='叫出選單了',
        template=ButtonsTemplate(
            thumbnail_image_url='https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2022/04/21/0/16706436.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600&w=930&nt=1',
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
                    label='每日卡路里建議',
                    uri='https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=544&pid=726'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        
    #這裡是上一個選單選我餓以後會出現的選單(亮黃色的)    
    elif re.match('我餓',message):
        flex_message = FlexSendMessage(
            alt_text='選什麼',
            contents=
    {
        
    "type": "bubble",
    "body": 
        {
            "type": "box",
            "layout": "vertical",
            "contents": 
            [
                {
                "type": "text",
                "text": "想吃什麼？",
                "size": "lg"
                }
            ]
            +
            [
                {
                "type": "button",
                "action":
                    {
                    "type": "message",
                    "label": i,
                    "text": i
                    }
                ,
                "style": "secondary",
                "color": "#FFFFE0",
                "height": "sm",
                "gravity": "center"
                } 
            for i in type
            ]
        }
    }
)
        line_bot_api.reply_message(event.reply_token, flex_message)

                
    elif re.match('麵類',message):
        flex_message2 = FlexSendMessage(
            alt_text='行銷搬進大程式',
            contents=
{
  "type": "bubble",
  "body":
    {
    "type": "box",
    "layout": "vertical",
    "contents":
        [
        {
        "type": "text",
        "text": "麵類",
        "size": "lg",
        "margin": "none",
        "gravity": "center"
        }
        ]
    +
        [
        {
        "type": "button",
        "action":
            {
            "type": "message",
            "text": i,
            "label": i
            }
            ,
        "height": "sm",
        "style": "secondary",
        "color": "#E3E2B4"
        }
        for i in noodel
            ]
        }
    }
)
        line_bot_api.reply_message(event.reply_token, flex_message2)        
        
        
    elif re.match('點心',message):
        flex_message3 = FlexSendMessage(
            alt_text='行銷搬進大程式',
            contents=
{
  "type": "bubble",
  "body":
    {
    "type": "box",
    "layout": "vertical",
    "contents":
        [
        {
        "type": "text",
        "text": "點心",
        "size": "lg",
        "margin": "none",
        "gravity": "center"
        }
        ]
    +
        [
        {
        "type": "button",
        "action":
            {
            "type": "message",
            "text": i,
            "label": i
            }
            ,
        "height": "sm",
        "style": "secondary",
        "color": "#E3E2B4"
        }
        for i in snack
            ]
        }
    }
)
        line_bot_api.reply_message(event.reply_token, flex_message3)
        
    
    #湯類
    elif re.match('湯類',message):
        flex_message4 = FlexSendMessage(
            alt_text='行銷搬進大程式',
            contents=
{
  "type": "bubble",
  "body":
    {
    "type": "box",
    "layout": "vertical",
    "contents":
        [
        {
        "type": "text",
        "text": "湯類",
        "size": "lg",
        "margin": "none",
        "gravity": "center"
        }
        ]
    +
        [
        {
        "type": "button",
        "action":
            {
            "type": "message",
            "text": i,
            "label": i
            }
            ,
        "height": "sm",
        "style": "secondary",
        "color": "#E3E2B4"
        }
        for i in soup
            ]
        }
    }
)
        line_bot_api.reply_message(event.reply_token, flex_message4)           


    #排餐   
    elif re.match('排餐',message):
        flex_message5 = FlexSendMessage(
            alt_text='行銷搬進大程式',
            contents=
{
  "type": "bubble",
  "body":
    {
    "type": "box",
    "layout": "vertical",
    "contents":
        [
        {
        "type": "text",
        "text": "排餐",
        "size": "lg",
        "margin": "none",
        "gravity": "center"
        }
        ]
    +
        [
        {
        "type": "button",
        "action":
            {
            "type": "message",
            "text": i,
            "label": i
            }
            ,
        "height": "sm",
        "style": "secondary",
        "color": "#E3E2B4"
        }
        for i in meal
            ]
        }
    }
)
        line_bot_api.reply_message(event.reply_token, flex_message5)
    
    
    #西式特餐  
    elif re.match('西式特餐',message):
        flex_message6 = FlexSendMessage(
            alt_text='行銷搬進大程式',
            contents=
{
  "type": "bubble",
  "body":
    {
    "type": "box",
    "layout": "vertical",
    "contents":
        [
        {
        "type": "text",
        "text": "西式特餐",
        "size": "lg",
        "margin": "none",
        "gravity": "center"
        }
        ]
    +
        [
        {
        "type": "button",
        "action":
            {
            "type": "message",
            "text": i,
            "label": i
            }
            ,
        "height": "sm",
        "style": "secondary",
        "color": "#E3E2B4"
        }
        for i in western_meal
            ]
        }
    }
)
        line_bot_api.reply_message(event.reply_token, flex_message6)
    
    
    #早餐  
    elif re.match('早餐',message):
        flex_message7 = FlexSendMessage(
            alt_text='行銷搬進大程式',
            contents=
{
  "type": "bubble",
  "body":
    {
    "type": "box",
    "layout": "vertical",
    "contents":
        [
        {
        "type": "text",
        "text": "早餐",
        "size": "lg",
        "margin": "none",
        "gravity": "center"
        }
        ]
    +
        [
        {
        "type": "button",
        "action":
            {
            "type": "message",
            "text": i,
            "label": i
            }
            ,
        "height": "sm",
        "style": "secondary",
        "color": "#E3E2B4"
        }
        for i in breakfast
            ]
        }
    }
)
        line_bot_api.reply_message(event.reply_token, flex_message7)
    
    
    #盤菜、自助餐 
    elif re.match('盤菜、自助餐',message):
        flex_message8 = FlexSendMessage(
            alt_text='行銷搬進大程式',
            contents=
{
  "type": "bubble",
  "body":
    {
    "type": "box",
    "layout": "vertical",
    "contents":
        [
        {
        "type": "text",
        "text": "盤菜、自助餐",
        "size": "lg",
        "margin": "none",
        "gravity": "center"
        }
        ]
    +
        [
        {
        "type": "button",
        "action":
            {
            "type": "message",
            "text": i,
            "label": i
            }
            ,
        "height": "sm",
        "style": "secondary",
        "color": "#E3E2B4"
        }
        for i in buffet
            ]
        }
    }
)
        line_bot_api.reply_message(event.reply_token, flex_message8)
    
    
    #飯類 
    elif re.match('飯類',message):
        flex_message9 = FlexSendMessage(
            alt_text='行銷搬進大程式',
            contents=
{
  "type": "bubble",
  "body":
    {
    "type": "box",
    "layout": "vertical",
    "contents":
        [
        {
        "type": "text",
        "text": "飯類",
        "size": "lg",
        "margin": "none",
        "gravity": "center"
        }
        ]
    +
        [
        {
        "type": "button",
        "action":
            {
            "type": "message",
            "text": i,
            "label": i
            }
            ,
        "height": "sm",
        "style": "secondary",
        "color": "#E3E2B4"
        }
        for i in rice
            ]
        }
    }
)
        line_bot_api.reply_message(event.reply_token, flex_message9)
        
    
    #飲料
    elif re.match('飲料',message):
        flex_message10 = FlexSendMessage(
            alt_text='行銷搬進大程式',
            contents=
{
  "type": "bubble",
  "body":
    {
    "type": "box",
    "layout": "vertical",
    "contents":
        [
        {
        "type": "text",
        "text": "飲料",
        "size": "lg",
        "margin": "none",
        "gravity": "center"
        }
        ]
    +
        [
        {
        "type": "button",
        "action":
            {
            "type": "message",
            "text": i,
            "label": i
            }
            ,
        "height": "sm",
        "style": "secondary",
        "color": "#E3E2B4"
        }
        for i in beverage
            ]
        }
    }
)
        line_bot_api.reply_message(event.reply_token, flex_message10)
    
    
    elif re.search(message, namestr):
        try:
            stored_list.append(message)
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="你點了 {} 熱量為 {} 大卡".format(message, dict[message])))
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Sorry, 菜單上沒有呦'))  
    
    elif re.search(message, "點完了"):
        n = 0
        for i in range(len(stored_list)):
            n += dict[stored_list[i]]
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="你點了 {} 熱量為 {} 大卡".format(stored_list, dict[message])))
        stored_list = []  
    
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你在叫我嗎:]'))  
      
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)