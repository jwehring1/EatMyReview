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
