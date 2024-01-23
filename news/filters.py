from django import forms
from django_filters import FilterSet, DateFilter

from .models import Post


# Создаем свой набор фильтров для модели Post.
class PostFilter(FilterSet):
    date = DateFilter(field_name='time_in',
                      widget=forms.DateInput(attrs={'type': 'date'}),
                      label='поиск по дате начиная с',
                      lookup_expr='date__gte')
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'title': ['icontains'],
            # поиск по имени автора
            'autor': ['exact'],
        }
