from django.contrib.auth.models import User
from django.db import models

# posts model
class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def comment_count(self):
        return len(self.comment_set.all())
        


# comment model
class Comment(models.Model):
    msg = models.CharField(max_length=150)
    date_commented = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.msg

