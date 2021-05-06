from django.forms import ModelForm, BooleanField
from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author','post_type','heading','text','category',]