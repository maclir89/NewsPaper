from django.urls import path
# Импортируем созданное нами представление
from .views import (NewsList, ArticlesList, NewsSearch, NewsDetail, NewsCreate, ArticlesDetail, ArticlesSearch, ArticlesCreate,
NewsUpdate, ArticlesUpdate, NewsDelete, ArticlesDelete)

urlpatterns = [
   path('news/', NewsList.as_view(), name='news_list'),
   path('news/<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('news/search/', NewsSearch.as_view(), name='news_search'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('articles/', ArticlesList.as_view(), name='articles_list'),
   path('articles/<int:pk>', ArticlesDetail.as_view(), name='articles_detail'),
   path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
   path('articles/search/', ArticlesSearch.as_view(), name='articles_search'),
   path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(), name='articles_edit'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
]

