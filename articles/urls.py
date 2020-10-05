from django.urls import path
from django.views.generic import TemplateView  # for templateView

from . import views

app_name = 'articles'  # use for get_success method


urlpatterns = [
    path('',TemplateView.as_view(template_name = 'articles/list.html'), name='list'),
    path('c/',views.ArticleFormView.as_view(), name='creat' ),    
]


