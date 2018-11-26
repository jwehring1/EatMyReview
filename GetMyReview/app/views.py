from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User,Review
from app.scripts import get_sorted_users_by_reviews,LDA,best_jacs
import pickle


def index(request):
    # user_list = User.objects.all()
    user_list = get_sorted_users_by_reviews()
    template = loader.get_template('app/index.html')
    context = {
        "user_list":user_list,
    }
    return render(request, 'app/index.html', context)

def database(request):
	context = {
        "user_list":user_list,
    }
	return(request, 'app/database.html', context)

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

def recommendations(request, id ):
    template = loader.get_template('app/recommendations.html')
    r = Review.objects.all()

    RUN_REST_LDA = True

    usr = User.objects.filter(user_id=id)[0]

    seperator = " "

    ### User LDA
    all_user_revs = []
    for rev in usr.review_set.all():
        if (rev.stars > 2.5):
            all_user_revs.append(rev.review_text)
    all_user_revs_str = seperator.join(all_user_revs)
    user_cats = LDA(all_user_revs_str)

    #make list of rest_IDs
    rest_ID_list = []
    for r in Review.objects.all():
        rid = r.business_id 
        if rid not in rest_ID_list:
            rest_ID_list.append(rid)

    rest_cats = []
    ### Restaurant LDA
    if (RUN_REST_LDA):
        #create strings combining all revs for each rest
        rest_rev_strs = []
        for rest in rest_ID_list:
            all_rest_revs = []
            for rev in Review.objects.filter(business_id=rest):
                if(rev.stars > 2.5):
                    all_rest_revs.append(rev.review_text)
            #combine revs with a space
            rest_str = seperator.join(all_user_revs)
            rest_rev_strs.append(rest_str)
        #run LDA on each combined string
        for r in rest_rev_strs:
            rest_cats.append(LDA(r))

        #store to file
        f = open('rest_cats.pckl', 'wb')
        pickle.dump(rest_cats, f)
        f.close()

    else:
        f = open('rest_cats.pckl', 'rb')
        rest_cats = pickle.load(f)
        f.close()


    #list of indices wrt rest_cats for 10 best restaurant matches
    #return this
    best_rests = best_jacs(user_cats, rest_cats)

    business_ids = [rest_ID_list[i] for i in best_rests]
    context = {
        "reviews": r,
        "business_ids" : business_ids,
    }
    return render(request, 'app/recommendations.html', context)
