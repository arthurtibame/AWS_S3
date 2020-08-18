import configparser
import json
from flask import Flask, request, abort
import logging
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)

from linebot.models import ImageMessage

# AWS S3
from S3_demo import AwsS3

app = Flask(__name__)

config = configparser.ConfigParser()
config.read("config.ini")
token: str = config.get("LINE", "CHANNEL_ACCESS_TOKEN")
secret: str = config.get("LINE", "CHANNEL_SECRET")

line_bot_api = LineBotApi(token)
handler = WebhookHandler(secret)


@staticmethod
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.setLevel(logging.INFO)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=ImageMessage)
def handler_image_message(event):
    """[summary]

    Args:
        event ([type]): [line bot event-> pass img]        
    Func 1.
        get img msg and reply msg    
    Func 2.
        upload iamge to AWS S3 client
    Func 3. (optional)
        udpate image detail(uploader id, image_path) to db         
    """
    # Step 1. Get message_id
    message_content = line_bot_api.get_message_content(event.message.id)
    file_name = f"{event.message.id }.jpg"

    # write iamge by message content (from user sent)
    with open(file_name, "wb") as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
    # upload file to S3
    AwsS3.upload_file(file_name, "iii-tutorial-v2", f"student14/{file_name}")

    # reply message
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text=f"Image saved ! {file_name}"),
            TextSendMessage(text=f"Image {file_name}  is uploader to AWS S3 !"),
        ],
    )


if __name__ == "__main__":
    app.run(port="8080", debug=True)

