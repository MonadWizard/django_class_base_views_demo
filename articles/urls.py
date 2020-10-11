from django.urls import path
from . import views

app_name = 'articles'  # use for get_success method


urlpatterns = [

    path('',views.ArticleListView.as_view(), name='list'),
    path('<int:pk>/<str:slug>/',views.ArticleDetailView.as_view(), name='detail'),


]


