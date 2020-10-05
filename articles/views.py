from django.shortcuts import render
from datetime import datetime  # for take date-time
from django.views.generic import FormView  # for handle fromBase View
from django.urls import reverse

from .forms import ArticleForm

# work with form view

class ArticleFormView(FormView):
    form_class = ArticleForm
    template_name = 'articles/create_article.html' 

    # success_url = 'articles/' 

    def get_success_url(self):
        return reverse('articles:list')   #reverse('appname:urlpathname')

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)

        return super().form_valid(form)








