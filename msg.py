import os
from dotenv import load_dotenv
from flask import Flask, request, url_for
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from datetime import datetime

load_dotenv()
app = Flask(__name__)
TWILIO_ACCOUNT_SID =  os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN =  os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')
RECIEPIENT_NUMBER = os.environ.get('RECIEPIENT_NUMBER')


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

filtered_message_history = client.messages.list(
                               date_sent=datetime(2020, 6, 9, 0, 0, 0),
                               from_=TWILIO_NUMBER,
                               to=RECIEPIENT_NUMBER,
                               limit=5
                           )
sender_history_csv = open('sender_message_history.csv','w')
for record in filtered_message_history:
    sender_history_csv.write(record.sid + ',' + record.body + '\n') 
    #prints the SID of the text message from twilio # -> you
sender_history_csv.close()

recipient_messages_csv = open('recipient_messages_history.csv','w')
recipient_messages = client.messages.list(
    date_sent=datetime(2020, 6, 12, 0, 0, 0),
    from_='+14086434472',
    to='+19145296977',
)
recipient_messages_csv.write(recipient_messages[0].from_ + ',')
for msg in recipient_messages:
    recipient_messages_csv.write(msg.body + ',')
recipient_messages_csv.close() 

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route('/webhook', methods=['POST'])
def webhook():
    recipient = request.form.get('From')
    # return respond(f'{recipient}')
    return respond(f'your message was received')

# @app.route('/recipientMessages', methods=['GET'])
# def getWebhook(): 
#     return respond(f'nothing at the moment')

