import django_filters
from django_filters import FilterSet
from django import forms


class PostFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название статьи')
    author__user__username = django_filters.CharFilter(lookup_expr='icontains', label='Автор')
    time_create = django_filters.DateFilter(lookup_expr='gt',
                                            widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                            label='Статьи опубликованные позже указанной даты')
