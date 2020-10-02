from django.shortcuts import render
from django.views import View   # for classBaseView

from datetime import datetime  # for take date-time

# Create simple function base View
def article_list_view(request):

    return render(request,'articles/list.html',{'now': datetime.now()})
# we define POST or GET request by if-else condition 
# and use request.method == '' for only function base views.




# work same with class Base views
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

