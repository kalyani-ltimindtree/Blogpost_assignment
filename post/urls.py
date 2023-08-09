from django.urls import path
from post import views
from post.views import PostList, PostDetail, CommentList

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('profile/', views.getProfile, name='profile'),
    path('profile/update/', views.updateProfile, name='update-profile'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('comments/', CommentList.as_view(), name='commets-list'),

]
