from email import message
from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse
from dic import dic1,dic2, oracion
import pandas as pd
import numpy as np

app = Flask(__name__)
@app.route('/bot', methods=['POST'])
def reply():
    incoming_msg = request.values.get('Body', '').lower()
    response=MessagingResponse()
    message=response.message()
    responded = False
    words = incoming_msg.split()
    if dic1.keys().__contains__(incoming_msg) and len(words) ==1:
        reply = dic1[incoming_msg]
        message.body(reply)
        responded = True
    elif dic2.keys().__contains__(words[0]) and len(words) >1:  
        selected=words[0]
        int_selected=int(selected)
        id=int(words[1])
        reply = dic2[selected]+oracion
        data=[]
        with open('data.json',"r") as fp:
            data = json.load(fp)
        data.append({
            'id': id,
            'selected': int_selected
        })
        with open('data.json', 'w') as fp:
            json.dump(data, fp)
        message.body(reply)
        responded = True
    return str(response)
if __name__ == '__main__':
    app.run(port=4000)

