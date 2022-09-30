from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    # 예시 : blog/
    path('', views.PostLV.as_view(), name = 'index'),

    # 예시 : blog/post/
    path('post/', views.PostLV.as_view(), name='post_list'),
    
    # 예시 : blog/post/슬러그-슬러그-슬러그
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
    
    # 예시 : blog/archive/tag/
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    
    # 예시 : /blog/tag/tagname/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    
    # 예시 : /blog/Search/
    path('search/', views.SearchFV.as_view(), name='search'),
    
    
    path('add/', views.PostCreateView.as_view(), name = 'add'),
    path('change/', views.PostChangeLV.as_view(), name = 'change'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name = 'update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'delete'),

    path('list/', views.PostTownView.as_view(), name='town'),

    ]
