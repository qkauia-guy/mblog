from django.contrib import admin
from django.urls import path
from mysite.views import index, show_post, mqtt

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("post/<slug:slug>", show_post),
    path("mqtt/", mqtt),
]
