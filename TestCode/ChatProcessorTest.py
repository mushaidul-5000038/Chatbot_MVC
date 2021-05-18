import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(
    os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(
    'D:\My_chatbot_mvc_repos\Chatbot_MVC\MVC_STRUCTURE\MODEL\chat_processor.py', 'D:\My_chatbot_mvc_repos\Chatbot_MVC\MVC_STRUCTURE')))
# first parameter goes for the Script Directory path
# second parameter goes for the parent directory path
from MODEL.chat_processor import *

import pickle
import numpy as np
import json

intents = json.loads(open('MODEL\intents.json').read())
words = pickle.load(open('MODEL\words.pkl','rb'))
classes = pickle.load(open('MODEL\classes.pkl','rb'))



def Test_clean_up_sentence():
    assert clean_up_sentence('what are you') == ['what','are','you']

def Test_predict_class():
    assert predict_class('what are you?')[0]['intent'] == 'options'

def Test_get_response():
    response=getResponse('options',intents)

    assert ( response == 'I am here to help you navigate through the services offered by Life Hospital Ltd' or  response ==  'Offering support for your inquiries on the services provided by Life Hospital Ltd')
                                
def Test_send():
    response=send('What are you?')

    assert (response == 'I am here to help you navigate through the services offered by Life Hospital Ltd' or response == 'Offering support for your inquiries on the services provided by Life Hospital Ltd')



if __name__ == "__main__":
    Test_clean_up_sentence()
    Test_predict_class()
    Test_get_response()
    Test_send()
    print("Everything passed")

#bag_of_words
#chatbot_query