# EatMyReview
<b>How to run</b>  
The website can be run in the folder GetMyReview just type the following commands.

python manage.py migrate


python manage.py shell

exec(open('dbLoad.py').read())

ctrl+Z


python manage.py runserver

Then the website should be up on localhost:8000/app

MORE INFORMATION FOUND ON THE WIKI!!!

<b>Description</b></n>
Eat My Review is Yelp recommender system that recommends restaurants based on a user's past reviews. Latent Dirichlet Allocation (or LDA) was the algorithm used to find a sample of the user's recommended restaurants. The application is written in python using the Django framework.
