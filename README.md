
from NewsPaper.models import *

1)
User1= User.objects.create_user('user1','user1@mail.ru','user1')
User2 = User.objects.create_user('user2','user2@mail.ru','user2')

2)
Author1 = Author.objects.create(user=User1)
Author2 = Author.objects.create(user=User2)

3)
Sport = Category.objects.create(name='Sport')
Game = Category.objects.create(name='Game')
History = Category.objects.create(name='History')
Party = Category.objects.create(name='Party')

4)
Post1 = Post.objects.create(author=Author1,post_type=post)
Post2 = Post.objects.create(author=Author1,post_type=post)
News1 = Post.objects.create(author=Author2,post_type=news)

5)
News1.category.add(Sport,Game)
Post1.category.add(History)
Post2.category.add(Party)

6)
Comment1 = Comment.objects.create(post=News1,user=User1)
Comment2 = Comment.objects.create(post=News1,user=User2)
Comment3 = Comment.objects.create(post=Post1,user=User2)
Comment4 = Comment.objects.create(post=Post2,user=User2)

7)
News1.like
News1.like
News1.like
News1.like
News1.dislike
News1.dislike

Post1.dislike
Post1.dislike
Post1.like
Post1.like
Post1.like

Post2.like
Post2.like
Post2.like
Post2.like
Post2.like
Post2.like
Post2.like

Comment1.like

Comment2.dislike
Comment2.dislike
Comment2.dislike
Comment2.dislike


Comment3.like
Comment3.like
Comment3.like

Comment4.dislike
Comment4.dislike
Comment4.dislike
Comment4.dislike
Comment4.dislike


8)
Author1.update_rating
Author2.update_rating

9)
Author.objects.all().order_by('-rating').values('user__username','rating')[0]

10)
Post.objects.all().order_by('-rating').values('created_time','author__user__username','rating','heading')[0]
Post.objects.all().order_by('-rating')[0].preview

11)
Post.objects.all().order_by('-rating')[0].comment_set.values('created_time','user__username','rating','text')
