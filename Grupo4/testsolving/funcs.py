"""
from testsolving.models import Perguntas, PerguntasTestes, Testes, Respostas


def getTestId(request):
    allTestIds = Testes.objects.values('id')

    context = {
        'id': allTestIds,
    }

    return allTestIds


def getFullQuestion(request):
    tests = Testes.objects.values('id')

    # questions = PerguntasTestes.objects.get(id=)

    questionId = Perguntas.objects.values('id', 'descr')

    print(questionId)

    return questionId
"""