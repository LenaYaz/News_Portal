from django.urls import path
from .views import PostList, PostDetail, create_post, PostUpdate, PostDelete
from django.contrib.auth.views import LoginView, LogoutView
from .forms import upgrade_me


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', create_post, name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('upgrade/', upgrade_me, name='upgrade')
]
