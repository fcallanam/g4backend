from django.shortcuts import render
from testsolving.models import Perguntas, PerguntasTestes, Testes, Respostas
from testsolving.funcs import *

# Create your views here.

def getTestId(request):
    tests_id = Testes.objects.values('id')

    # context = {'tests_id': [i for i in tests_id.values()]}

    context = {'tests_id': tests_id}

    # return render(request, "index.html", context)
    return context

def getQuestionId(request, testId):
    allQuestionsId = PerguntasTestes.objects.get(testes_id=testId)

    list = [i for i in allQuestionsId.values()]

    print("============\n")
    print(list)
    print("\n============\n")

    context = {
        'id': allQuestionsId,
    }

    return render(request, template_name="questionid.html", context=context)
    # return questionId

def testsolvingView(request):
    # data = Get Users (maybe), questions and answers
    tests = getTestId(request)

    # questions = getQuestionId(request, 101)

    return render(request, template_name="index.html", context=tests)
