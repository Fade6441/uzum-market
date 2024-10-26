from django.forms import ModelForm, CharField
# from .models import Comments

# class CommentForm(ModelForm):
#     class Meta:
#         model = Comments
#         fields = ['text']

class SearchForm(ModelForm):
    query = CharField(label='Поиск', max_length=255)