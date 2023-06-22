import random

'''
List of constants to provide some randomness in conversation.
'''
def get_random_item(lst):
    rand_idx = random.randint(0, len(lst)-1)

    return lst[rand_idx]

encouragement = [
    "Amazing job!", "Crushing it!", "Great work.", "You're getting the hang of this!"
]

question_reminders = [
    "Reply QUESTION: and then the text of your question if you're confused about anything!",
    "Don't forget you can always text me QUESTION: and then the text of your question if you're feeling confused.",
    "I'm happy to help out, just text me QUESTION: followed by any question you have!"
]

'''
Exercises: Can be modified depending on what is being practiced. In the future, can pull content from a centralized database rather than storing as constants

'''
EXERCISE_1 = f'''
Wonderful! Today we're focusing on friendship. And what I mean by that is *Adding and Editing Contacts.*\n
1. Let’s start with navigating to the “Contacts” app and hitting the little “+” sign on the top right corner. \n
2. Then go ahead and add my number as a contact.\n
3. Fill in my First Name "Tech", Last Name "Tutor" and my number (you'll see it at the top of these messages).\n 
4. For extra credit, give me a nice contact photo (remember you can "screenshot" anything from the internet like we learned last week!)

Reply DONE when you're finished!

{get_random_item(question_reminders)}
'''

EXERCISE_2 = f'''
{get_random_item(encouragement)} Now, repeat that again for two other people in your life.  Maybe even shoot them a text message or give them a call, just for kicks! \n

{get_random_item(question_reminders)}
'''

EXERCISE_3 = f'''
All done? Take a screenshot and text it back to me for credit. 

{get_random_item(question_reminders)}
'''

'''
Message templates for hello, goodbye, and abort
'''

HELLO_MESSAGE = '''
Hi there! I'd say this beautiful summer day is as good a day as any
 to brush up on our tech skills, what say you? Reply YES to start today's tutorial!
'''

GOODBYE_MESSAGE = '''
     Proud of you, you\'re one step closer to being a tech genius. See you tomorrow!
 '''

ABORT_MESSAGE = "No problem, I\'ll check in again later today!"

QUESTION_MESSGAE = "Check out the video tutorial I just emailed over!"


EXERCISES = [
    EXERCISE_1,
    EXERCISE_2,
    EXERCISE_3
]


