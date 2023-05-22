from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def update_rating(self):
        posts_rating = self.post_set.aggregate(result=Sum('rating')).get('result')
        comments_rating = self.user.comment_set.aggregate(result=Sum('rating')).get('result')
        comment_post = Post.objects.filter(author=self).values('rating')
        a = 0
        for i in range(len(comment_post)): a = a + comment_post[i]['rating']
        self.rating = 3 * posts_rating + comments_rating + a
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    news = 'NW'
    arcticle = 'AR'

    TYPE = [
        (news, 'Новость'),
        (arcticle, 'Статья')
    ]

    post_type = models.CharField(max_length=2,
                                 choices=TYPE,
                                 default=arcticle)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self, length=124):
        return f"{self.text[:length]}..." if len(self.text) > length else self.text


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()