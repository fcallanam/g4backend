def index(request):
    latest_survey_list = Survey.objects.order_by('survey_id')[:5]

    context = {
        'latest_survey_list': latest_survey_list
    }
    return render(request, 'fragen/index.html', context)

def detail(request, survey_id):

    question = Survey.objects.get(pk=survey_id).question.all().values()
    question_dict = {
        'question': question
    }

    return render(request, 'fragen/detail.html', question_dict)