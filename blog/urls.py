from . import views
from django.urls import path


urlpatterns = [

    path('<slug:slug>', views.Blogview.as_view(), name='blog_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('', views.PostList.as_view(), name='home')
]