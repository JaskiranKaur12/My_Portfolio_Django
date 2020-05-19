from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Blog

# Create your views here.

class Index(generic.ListView):
    template_name ='blogs/all_blogs.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.order_by('-date')

# def all_blogs(request):
#     blogs=Blog.objects.order_by('-date')
#     return render(request,'blogs/all_blogs.html',{'blogs':blogs})     

def detail(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html',{'blog':blog})

