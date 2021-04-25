from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.PostListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('profile/new-post/', views.create_post, name='new_post'),
    path('post/<int:post_id>/', views.comment, name='comment'),
]