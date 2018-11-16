from app.models import User,Review
import json

current_user = User(user_id="default")
reviews = list()
filename = 'reviews.json'
i = 1
# build a list of users from all the reviews
for line in open(filename):
    print("Loading: " + str(i), end="\r")
    i+=1
    data = json.loads(line)

    if (not data['user_id'] == current_user.user_id):
        current_user = User(user_id=data['user_id'])
        current_user.save()
    # don't create duplicate users
    # if (data['user_id'] not in user_ids):
    # user_ids.append(data['user_id'])
    # u = User(user_id=data['user_id'])
    # users.append(u)
    r = Review(user=current_user, review_id=data['review_id'], business_id=data['business_id'], stars=data['stars'], review_text=data['text'])
    # print(r)
    r.save()
        # print(data['business_id'])
    # print(u)
    # print(data)
print("\nDone!")
