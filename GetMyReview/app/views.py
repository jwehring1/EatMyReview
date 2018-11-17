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
    r = Review.objects.filter(review_id=review_id)[0]
    template = loader.get_template('app/review.html')
    context = {
        "review": r,
    }
    return render(request, 'app/review.html', context)

def business_detail(request, business_id):
    template = loader.get_template('app/business.html')
    reviews = Review.objects.filter(business_id=business_id)
    context = {
        "business_id": business_id,
        "reviews": reviews,
    }
    return render(request, 'app/business.html', context)
