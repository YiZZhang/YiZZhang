from flask import Flask,request
import requests,threading
from darkflow.net.build import TFNet
application = Flask(__name__)

replyToken=0
imageID=0

def postRequest():
    a=requests.post(
            url='https://api.line.me/v2/bot/message/reply',
            headers={'Content-Type':'application/json','Authorization':'Bearer {zRXlAg6abdYCV5UuZNytayQy+hl/ZZsu/phZ0IeqwMuGmieyNza2rxBEvIp9UyWlwvCXgnNh3TXuCf2KDfJAVS1PGgl0U93rVpbgu9XxosZDulsjNhOVsDAYd83jRyQDznhrjmk5bLQJXE6oTmapDwdB04t89/1O/w1cDnyilFU=}'},
            json={
                    "replyToken":str(replyToken),
                    "messages":[
                            {
                                "type":"text",
                                "text":str(imageID)
                            },
                            {
                                "type":"text",
                                "text":"May I help you?"
                            }
                    ]
            }
    )
    print(a)


@application.route('/', methods=['POST'])
def result():
    #receive request from line
    global replyToken
    global imageID
    
    requestBody=request.get_json()#use thie POST reply message
    try:
        replyToken=requestBody['events'][0]['replyToken']
    except Exception as e:
        pass
    try:
        imageID=requestBody['events'][0]['message']['id']
    except Exception as e:
        pass
        
    
    post=threading.Thread(target=postRequest)
    post.daemon=True
    post.start()
    
    #
    
    return '{result:success (200)}',200
    
if __name__ == '__main__':
    application.run()

