from django.shortcuts import render
from django.http import HttpResponse

#chetterbot models in here#

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


# Chetterbot Objects in here.#

bot = ChatBot('chatbot', read_only=False,
              logic_adapters=[
                {
                  'import_path':'chatterbot.logic.BestMatch',
                  #'default_response': 'Sorry, I dont know what you means',
                  #'maximum_similarity_threshold':0.90
                  
                }
                ])

# Chetterbot & Training & Teaching. #
list_to_train = [

    "hi",
    "hi, there",
    "what's your name",
    "I'm just a chatbot",
    "What is your favorite food?",
    "I like cheese",
    "what's your favorite sports?",
    "swimming",
    "Do you have Children?",
    "No",
    "Where Do you Live?",
    "Busan",
    "Where Do you live?",
    "Seoul",
    "What is your job?",
    "Maketor"
    
]


chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)


#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)

chatterbotCorpusTrainer.train('chatterbot.corpus.english')


# Create your views here.

def index(request):
  return render(request, 'blog/index.html')


def specific(request):
  return HttpResponse("list1")


def getResponse(request):
  userMessage = request.GET.get('userMessage')
  chatResponse = str(bot.get_response(userMessage))
  return HttpResponse(chatResponse)