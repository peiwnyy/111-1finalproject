#!/usr/bin/env python
# coding: utf-8

# In[14]:


@handler.add(MessageEvent, message=TextMessage)
 def handle_message(event):
        message = text=event.message.text
        if re.match('告訴我秘密',message):
            buttons_template_message = TemplateSendMessage(
            alt_text='這個看不到',
            template=ButtonsTemplate(
             thumbnail_image_url='https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2022/04/21/0/16706436.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600&w=930&nt=1',
             title='你想幹嘛',
             text='選單功能－TemplateSendMessage',
             actions=[
                 URIAction(
                     label='看學餐',
                     uri='https://meals.ntu.edu.tw/restaurant'
                 ),
                 MessageAction(
                     label='吃飯',
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
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(message))


# In[15]:


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
                            
                           ]
                         }
                       ]
                     }
                   }
           )
        
           #line_bot_api.reply_message(event.reply_token,[inform_message, mainMenu_flex_message])

       except ValueError:
           pass
                                     
handle_message()


# In[ ]:


# 主程式
import os
if name == "main":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


# In[ ]:





# In[ ]:




