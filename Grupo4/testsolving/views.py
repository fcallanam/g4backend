from django.shortcuts import render
from testsolving.models import Perguntas, PerguntasTestes, Testes, Respostas
from testsolving.funcs import *

# Create your views here.

def getTestId(request):
    allTestsIds = Testes.objects.values('id')

    list = [i for i in allTestsIds.values()]

    context = {'tests': list}

    print("============\n")
    print(list)
    print("\n============\n")

    return render(request, "index.html", context)
    # return context

def getQuestionId(request, testId):
    allQuestionsId = PerguntasTestes.objects.get(id=testId)

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
    print("hi")

    return render(request, template_name="index.html", context=tests)
    # return render(request, template_name="testsolving.html", context=data)
