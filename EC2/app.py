'''

載入前面的圖文選單設定，

並要求line_bot_api將圖文選單上傳至Line
    

'''
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import RichMenu
import requests
import json
line_bot_api = LineBotApi(secretFileContentJson.get("channel_access_token"))
menuJson=json.loads(menuRawData)

lineRichMenuId = line_bot_api.create_rich_menu(rich_menu=RichMenu.new_from_json_dict(menuJson))
print(lineRichMenuId)