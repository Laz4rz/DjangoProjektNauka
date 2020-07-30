from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.


#dummy data przed opanowaniem databazy
# posts = [
#     {
#         'author':'CoreyMS',
#         'title':'BlogPost1',
#         'content':'First post content',
#         'date_posted':'August 27, 2018'
#     },
#     {
#         'author':'JaneDoe',
#         'title':'BlogPost2',
#         'content':'Second post content',
#         'date_posted':'August 28, 2018'
#     }
# ]

#z uzyciem templatki
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#z uzyciem response
# def about(request):
#     return HttpResponse('<h1>BLOG ABOUT</h1>')

#z uzyciem render
def about(request):
    return render(request, 'blog/about.html', {'title':"About"})

