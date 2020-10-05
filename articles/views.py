from django.shortcuts import render
from datetime import datetime  # for take date-time  
from django.views.generic import TemplateView, ListView  # for handle listBase View
from django.urls import reverse

from .models import Article

# without generic ListView
from django.views import View

class ArticleListView(View):

    def get(self,request):
        articles = Article.objects.all()
        context = {
            'articles': articles
        }
        return render(request,'articles/list.html', context)

# with TemplateView

class ArticleTemplateView(TemplateView):
    template_name = 'articles/list.html'
    

    def get_context_data(self,*args, **kwargs):
        articles = Article.objects.all()
        queryset = articles.filter(is_public= True)

        context = super().get_context_data(*args, **kwargs)
        context['articles'] = queryset # define articles to see all
        return context


# with ListView

class ArticleListView(ListView):
    template_name = 'articles/list.html' # define template
    # model = Article # define model name  or can be use  queryset = Article.objects.all()
    queryset = Article.objects.filter(is_public= True)
    # context_object_name = 'articles'  # it's use if we need override

    # optional for multiple data pass
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = 'CBV'
        context['articles'] = context.get('object_list')
        return context







