from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=50)
    def __str__(self):
        return "USERID: " + str(self.user_id)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    review_id = models.CharField(max_length = 50)
    business_id=models.CharField(max_length=50, default='BUSINESS_ID')
    stars = models.IntegerField(default=0)
    review_text = models.CharField(max_length=500)
    def __str__(self):
        return str(self.stars) + "/5\n" + str(self.review_id) + " \n" + str(self.review_text)
