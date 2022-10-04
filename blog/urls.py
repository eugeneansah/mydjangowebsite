from . import views
from django.urls import path


urlpatterns = [

    path('<slug:slug>', views.Blogview.as_view(), name='blog_view')
]