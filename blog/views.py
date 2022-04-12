from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
post = [ {'author':'varun',
               'content':'django_project',
               'date_added':'28-1-2018',
               'title':'blog 1'},
               {'author':'gopal',
               'content':'python_tutorial',
               'date_added':'29-1-2018',
               'title':'blog 2'},
              
]
def home(request):
    context = {'post':Post.objects.all()}
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})
