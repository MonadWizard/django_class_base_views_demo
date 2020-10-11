from django.shortcuts import render
from datetime import datetime  # for take date-time  
from django.views.generic import ListView, DetailView  # for handle listBase View
from django.core.exceptions import ImproperlyConfigured

from django.urls import reverse

from .models import Article


# create Mixin

class PageTitleMixin:
    page_title = ''

    def get_page_title(self):
        return self.page_title

    # optional for multiple data pass
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_title'] = self.get_page_title()
        return context


class PublicMixin:
    is_public_field = 'is_public'
    

    @property
    def get_is_public(self):
        return {self.is_public_field: True}

    def get_queryset(self):
        if self.model:
            return self.model._default_manager.filter(**self.get_is_public)
        elif self.queryset:
            return self.queryset.filter(**self.get_is_public)
        else:
            raise ImproperlyConfigured(
                '%(cls)s.model is missing. Define '
                'queryset.' % {'cls' : self.__class__.__name__}
        
        )





# with ListView

class ArticleListView(PageTitleMixin,PublicMixin, ListView):
    template_name = 'articles/list.html' # define template
    page_title = 'CBV using mixin'
    model = Article # define model name  or can be use  queryset = Article.objects.all()



class ArticleDetailView(PageTitleMixin, DetailView):
    model = Article
    template_name = 'articles/detail.html'
    # primary key with slug
    query_pk_and_slug = True

    # change page title by name
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        self.page_title = obj.title
        return obj



