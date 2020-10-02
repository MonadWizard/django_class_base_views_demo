from django.urls import path

from . import views

app_name = 'articles'


urlpatterns = [

    path('',views.article_list_view ),
    path('cbv/',views.ArticleListView.as_view() ),
]
