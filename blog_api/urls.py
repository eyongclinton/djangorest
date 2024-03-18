from django.urls import path
from .views import PostList, PostDetail

app_name = "blog_api"

urlpatterns = [
    # /api/posts - list of all
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
]
