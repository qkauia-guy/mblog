from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime


# Create your views here.
def index(request):
    posts = Post.objects.all()
    now = datetime.now()
    # return HttpResponse("HEllo, wwwwwwwwwww at posts index")
    # return HttpResponse(posts)
    return render(request, "index.html", locals())


def show_post(request, slug):
    post = Post.objects.get(slug=slug)
    now = datetime.now()
    return render(request, "show_post.html", locals())


def mqtt(request):
    return render(request, "mqtt-dashboard-temp-json.html", locals())
