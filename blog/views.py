from django.shortcuts import render
from django.http import HttpResponse

#chetterbot models in here#

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Chetterbot Objects in here.#

bot = ChatBot('chatbot', read_only=False,logic_adapters=['chatterbot.logic.BestMatch'])

# Chetterbot & Training & Teaching. #
list_to_train = [

    "hi",
    "hi, there",
    "what's your name",
    "I'm just a chatbot",
    "What is your favorite food?",
    "I like cheese"
    
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)



# Create your views here.

def index(request):
  return render(request, 'blog/index.html')

def specific(request):
  return HttpResponse(list1)

def getResponse(request):
  userMessage = request.GET.get('userMessage')
  return HttpResponse(userMessage)