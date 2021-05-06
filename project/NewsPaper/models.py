from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


news = 'N'
post = 'P'

Post_type = [
    (news, 'Новости'),
    (post, 'Статья')
]

class Author(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE )
    rating = models.IntegerField(default=0)

    @property
    def update_rating(self):
        post_rating = Author.objects.get(user=self.user).post_set.all()
        comment_rating = self.user.comment_set.all()

        def Sum_rating(arg):
            result = 0
            for i in arg.values('rating'):
                result += i['rating']
            return result

        result = Sum_rating(post_rating)*3
        result += Sum_rating(comment_rating)
        self.rating = result
        print(f'Рейтинг автора:{result}')
        return self.save()




class Category(models.Model):
    name = models.CharField(max_length=255, unique = True)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    post_type = models.CharField(max_length=255, choices=Post_type, default=post)

    heading = models.CharField(max_length=255, default='heading')
    text = models.TextField(default='Text')

    category = models.ManyToManyField(Category, through='PostCategory')

    created_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    @property
    def preview(self):
        result = self.text[0:123] + '...'
        return result

    @property
    def like(self):
        self.rating += 1
        self.save()
        return f'Рейтинг: {self.rating}'


    @property
    def dislike(self):
        self.rating -= 1
        self.save()
        return f'Рейтинг: {self.rating}'

    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    text = models.TextField(default='comment')

    created_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)


    @property
    def like(self):
        self.rating += 1
        self.save()
        return f'Рейтинг: {self.rating}'

    @property
    def dislike(self):
        self.rating -= 1
        self.save()
        return f'Рейтинг: {self.rating}'




# on_delete = models.CASCADE

