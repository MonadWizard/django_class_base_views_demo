from django.shortcuts import render
from django.views import View   # for classBaseView
from django.views.generic import TemplateView  # for templateView

from datetime import datetime  # for take date-time

# Create simple function base View
def article_list_view(request):

    return render(request,'articles/list.html',{'now': datetime.now()})
# we define POST or GET request by if-else condition 
# and use request.method == '' for only function base views.




# work same with basic class base views
class ArticleListView(View):

    # for handel get request
    def get(self, request):
        #code to process get request
        return render(request, 'articles/list.html', {'now': datetime.now()})

    # for handel post request
    def post(self, request):
        #code to process post request
        pass 
# right now we have nothing to handel as POST request so, we just pass it.


# work with template base views 
class MyTemplateView(TemplateView):
    template_name = 'articles/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        context['message'] = 'any kind of message you can be passed...'
        return context
# if we have static template & we don't need to pass any aditional data then 
# we jusy diclar template on urls.py  no need any class or function