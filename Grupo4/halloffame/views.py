from django.shortcuts import render
from django.shortcuts import redirect
from halloffame.funcs import *


def halloffameView(request):

    if request.user.is_authenticated:

        #Function that returns a dictionary with the top 10 users and the logged user place
        top_users = get_top_users(request)

        return render(request, template_name="halloffame.html",context = top_users)
    else:
        return redirect("login")