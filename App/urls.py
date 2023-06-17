from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
    path('book.html', views.NavB.as_view(), name='book'),
    path('film.html', views.NavF.as_view(), name='book'),
    path('general.html', views.NavG.as_view(), name='book'),
]