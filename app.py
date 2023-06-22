from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
import random
from constants import *

app = Flask(__name__)
app.secret_key = 'top-secret'


def delete_session():
    del session['convo_tracker']
    del session['answers']

@app.route('/', methods=['POST'])
def survey():
    incoming_msg = request.values['Body']
    # Session used to track progress in conversation
    convo_tracker = session.get('convo_tracker', -1)

    # Nonexistent session returns -1, prompting hello message
    if convo_tracker == -1:
        response = HELLO_MESSAGE
        session['convo_tracker'] = 0
        session['answers'] = []

    # Conversation still in progress; provide next exercise
    elif convo_tracker < len(EXERCISES):
        if convo_tracker == 0 and 'yes' not in incoming_msg.lower():
            response = ABORT_MESSAGE
            delete_session()
        else:
        	# For now, return hardcoded question response
            if "question" in incoming_msg.lower():
                response = QUESTION_MESSAGE
            # If not a question, assume next exercise can be sent
            else:
                response = f'({EXERCISES[convo_tracker]}'
                session['convo_tracker'] += 1
            # Keep track of answers
            if convo_tracker > 0:
                session['answers'].append(incoming_msg)
    else:
        response = EXIT_MESSAGE
        answers = session['answers']
        answers.append(incoming_msg)
        delete_session()
        
        # In the future, store answers for record keeping by writing back to a centralized database
        print('Exercise answers:', answers)

    r = MessagingResponse()
    r.message(response)
    return str(r)
