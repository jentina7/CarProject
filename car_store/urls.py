from django.urls import path
from .views import UserProfileViewSet, BrandViewSet, CarModelViewSet, \
    CarPhotosViewSet, CarListViewSet, CarDetailViewSet


urlpatterns = [
    path('', CarListViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_list'),
    path('<int:pk>/', CarDetailViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update', 'delete': 'destroy'}), name='car_detail'),


    path('marka/', BrandViewSet.as_view({'get': 'list', 'post': 'create'}), name='brand_list'),
    path('marka/<int:pk>/', BrandViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update', 'delete': 'destroy'}), name='brand_detail'),


    path('model/', CarModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='model_list'),
    path('model/<int:pk>/', CarModelViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update', 'delete': 'destroy'}), name='model_detail'),


    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update', 'delete': 'destroy'}), name='user_detail'),



]
