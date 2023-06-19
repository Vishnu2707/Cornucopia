from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
    path('<slug:slug>/increase-view-count/', views.increase_view_count, name="increase_view_count"),
    path('book.html', views.NavB.as_view(), name='book'),
    path('film.html', views.NavF.as_view(), name='film'),
    path('general.html', views.NavG.as_view(), name='general'),
    path('contact.html', views.NavContact.as_view(), name="contact"),
    path('ham.html', views.NavHam.as_view(), name="ham"),
    path('author.html', views.NavAut.as_view(), name="author"),
]