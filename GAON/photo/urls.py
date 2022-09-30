from django.urls import path
from photo import views

app_name = 'photo'
urlpatterns = [
   
    # # /photo/album/99
    # path('album/<int:pk>', views.AlbumDV.as_view(), name = 'album_detail'),

    # /photo/
    path('', views.AlbumLV.as_view(), name = 'index'),
    # /photo/album/ same as /photo/
    path('photo/', views.AlbumLV.as_view(), name = 'photo_list'),
    
    path('photo/region/', views.RegionDV.as_view(), name = 'region_list'),
    
    # /photo/photo/99
    path('photo/<int:pk>', views.PhotoDV.as_view(), name = 'photo_detail'),
    
    path('photo/add/', views.PhotoCV.as_view(), name = 'photo_add'),
    path('photo/change/', views.PhotoChangeLV.as_view(), name = 'photo_change'),
    path('photo/<int:pk>/update/', views.PhotoUV.as_view(), name = 'photo_update'),
    path('photo/<int:pk>/delete/', views.PhotoDelV.as_view(), name = 'photo_delete'),
]