from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=300,unique=True)
    content = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

class BlogUser(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    blog_id = models.ForeignKey(to=Blog,on_delete=models.CASCADE)
    user_id = models.ForeignKey(to=BlogUser,on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.comment



