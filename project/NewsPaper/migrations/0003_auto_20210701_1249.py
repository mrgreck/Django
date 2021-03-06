# Generated by Django 3.1.7 on 2021-07-01 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPaper', '0002_auto_20210525_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.category')),
            ],
        ),
        migrations.CreateModel(
            name='PostWeekPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.post')),
                ('postweek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.postweek')),
            ],
        ),
        migrations.AddField(
            model_name='postweek',
            name='post',
            field=models.ManyToManyField(through='NewsPaper.PostWeekPost', to='NewsPaper.Post'),
        ),
    ]
