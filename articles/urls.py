from django.urls import path
from . import views

app_name = 'articles'  # use for get_success method


urlpatterns = [
    # path('',views.ArticleListView.as_view(), name='list'),
    path('t/',views.ArticleTemplateView.as_view(), name='list'),
    path('',views.ArticleListView.as_view(), name='list'),
]


