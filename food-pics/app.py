import os
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pprint import pprint   #makes payload look nicer to read
from twilio.rest import Client

#calls the other file
from clarifaiapp import get_relevant_tags

app = Flask(__name__)
TWILIO_ACCOUNT_SID =  os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN =  os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

food_pics = {}

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route('/webhook', methods=['POST'])
def reply():
    # pprint(request.values)
    sender = request.form.get('From')
    media_msg = request.form.get('NumMedia')    #0 if false, 1 if true
    pprint(media_msg)
    message = request.form.get('Body').lower()
    #check if user already sent in something. if they send something new, then update it
    if sender in food_pics or sender not in food_pics:
        if media_msg == '1':
            pic_url = request.form.get('MediaUrl0')  #URL of the person's media
            pprint(pic_url)
            relevant_tags = get_relevant_tags(pic_url)
            if 'food' in relevant_tags:
                #put picture URL into food_pics dictionary
                food_pics[sender] = pic_url
                return respond(f'Thanks for sending in a picture.')
        if message == 'What\'s cooking?' and food_pics.values():
            pprint(food_pics.values())
            for entry in food_pics:
                pprint(food_pics.get(entry))
                url_entry_pic = food_pics.get(entry)
                mms = client.messages.create(
                            body='Submitted by ' + entry,
                            from_='whatsapp:+14155238886',
                            media_url = food_pics.get(entry),
                            to=sender
                        )
            return respond(f'Bon appetit!')
        else:
            return respond(f'Please send a picture of food.')
