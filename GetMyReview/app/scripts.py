from __future__ import print_function
from .models import User, Review

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
import math

# sort users by how many reviews they've left
# returns a list of tuples, with 0 being the user and 1 being the number of reviews
def get_sorted_users_by_reviews():
    users = []
    # for each user
    for user in list(User.objects.all()):
        # count their reviews
        length = 0
        for r in user.review_set.all():
            length += 1
        # add those to a list of tuples
        users.append((user, length))

    #sort by the lengths
    users.sort(key=lambda x: x[1], reverse=True)
    #return only the list of users
    return [x[0] for x in users]


#create LDA categories for the dummy user


#Jaccard similarity between each LDA category for the user
# and each LDA category for each restaurant


#take the highest similarity scores and return these as the ranked results


# similarity between one category from user and one category from restaurant
# each category is provided as a list
#returns a single numeric score 0<=score<=1
def jac_cat_cat(user_cat, rest_cat):
    # intersection starts as 0
    inters_mag = 0
    # union starts as size of all terms in user_cat
    union_mag = len(user_cat)
    # for each term in rest_cat
    for j in range(0, len(rest_cat)):
        if (rest_cat[j] in user_cat):
            # not a new term
            union_mag += 1
        else:
            #new term
            inters_mag += 1

    if (union_mag == 0):
        #don't divide by 0
        return 0
    else:
        return (inters_mag / union_mag)

#similarity between the categories of a user and a restaurant
# each input provided as list of categories (each entry is a list
# containing the category's words
#output is a single score, the highest score between one of the user's
# categpries and one of the rest cats
def jac_user_rest(user_cats, rest_cats):
    max_jac = 0
    for i in range(0, len(user_cats)):
        for j in range(0, len(rest_cats)):
            temp_score = jac_cat_cat(user_cats[i], rest_cats[j])
            if temp_score > max_jac:
                temp_score = max_jac
    return max_jac

#find the best restaurants to recommend
#gives the best 10 based from Jaccard similarity between LDA categories
# of the user and all restaurants
#input: list of user cats, each entry is a list of words;
# list of restaurants, each entry is a list of
# cats, each entry is a list of words
#output: list of 10 indices (wrt rest input list) that are best
# restaurant matches (0=best)
def best_jacs(user_cats, all_rest_cats):
    rest_scores = []
    for r in range(0, len(all_rest_cats)):
        rest_scores.append(jac_user_rest(user_cats, all_rest_cats[r]))
    best = np.flip(np.argsort(rest_scores), axis=0)
    return best[:10]

#run the LDA algorithm to generate topics
#input: lump sum of text
#output: list of lists, each list element is a category of words
def LDA(text):
    print("Executing LDA")
    # running the comparison

    n_features = 1000
    n_topics = 10
    n_top_words = 3

##real LDA function
    # dataset = text.split(' ')
    #
    # tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
    #                                 max_features=n_features,
    #                                 stop_words='english')
    # print("Vectorized.")
    # # tf_vectorizer = CountVectorizer(max_features=n_features)
    #
    # tf = tf_vectorizer.fit_transform(dataset)
    #
    # print("Creating LDA... ", end="")
    # lda = LatentDirichletAllocation(n_components=n_topics, max_iter=20,
    #                                 learning_method='online',
    #                                 learning_offset=50.)
    # print("done. \nFitting. This could take awhile... ", end="")
    # lda.fit(tf)
    # print("done.")
    # tf_feature_names = tf_vectorizer.get_feature_names()
    cats = []

##also real LDA function
    # for topic_idx, topic in enumerate(lda.components_):
    #     cats.append([tf_feature_names[i]
    #                     for i in topic.argsort()[:-n_top_words - 1:-1]])

    text_split = text.split(' ')
    num_words = len(text_split)
    size = math.floor(num_words/n_topics)
    for i in range(0, n_topics):
        start = i*size
        cats.append(text_split[start:start+size])

    return (cats)
