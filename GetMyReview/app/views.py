from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User,Review

def index(request):
    user_list = User.objects.all()
    print(user_list)
    template = loader.get_template('app/index.html')
    context = {
        "user_list":user_list,
    }
    return render(request, 'app/index.html', context)

def user_profile(request, id):
    usr = User.objects.filter(user_id=id)[0]
    template = loader.get_template('app/profile.html')
    context = {
        "user": usr,
    }
    return render(request, 'app/profile.html', context)

def review_detail(request, review_id):
    return HttpResponse("You're looking at %s" % review_id)
