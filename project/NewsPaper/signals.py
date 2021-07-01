from django.core.mail import mail_managers
from django.core.mail import send_mail

from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.db.models.signals import m2m_changed

from .models import Post, PostWeek, Category


@receiver(m2m_changed, sender=Post.category.through )
def notify_managers_post(sender, instance, action, **kwargs):

    mmm = instance.category.values('followers__email')


    if action == "post_add":
        print(instance.category.values('id')[0]['id'])
        print(instance.category.values('followers__email'))

        for m in mmm:
            print(1)
            m = m['followers__email']
            if not m == '':

                send_mail(

                    subject=f'здравствуйте {m}',
                    # имя клиента и дата записи будут в теме для удобства
                    message=f'Вышел новый пост по интересной вам категории '
                            f'\n'
                            f'\n Кракое содержание поста: {instance.preview}'
                            f'\n'
                            f'\n ссылка на данный пост: http://127.0.0.1:8000/{instance.id}'
                            f'\n это письмо адресованно {m}',  # сообщение с кратким описанием проблемы
                    from_email='MrGreck135@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
                    recipient_list=[m]  # здесь список получателей. Например, секретарь, сам врач и т. д.
                )
                print(2)
            print(3)
        category_id = instance.category.values('id')[0]['id']
        if PostWeek.objects.filter(category=category_id).exists():
            PostWeek.objects.get(category=category_id).post.add(instance)
            print('пост добавил')

        else:
            ct = Category.objects.get(id=category_id)
            print('почти создал обект')
            pw = PostWeek.objects.create(category=ct)
            print('создал обект')
            pw.post.add(instance)
            print('добавил пост')





