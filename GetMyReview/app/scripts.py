from .models import User, Review

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
def jac_sim(user_cat, rest_cat):
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
