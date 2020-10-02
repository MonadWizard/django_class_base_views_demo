from django.urls import path

from . import views

app_name = 'articles'


urlpatterns = [

    path('',views.article_list_view ),
    path('cbv/',views.ArticleListView.as_view() ),
    path('cbv_t/',views.MyTemplateView.as_view() ),
    
]



# for static template we just only define it...
from django.views.generic import TemplateView  # for templateView

urlpatterns += [path('cbv_tt/',TemplateView.as_view(template_name = 'articles/list.html') )]
