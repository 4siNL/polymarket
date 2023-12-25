from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.AccountLoginView.as_view(), name='login'),
    path('logout', views.AccountLogoutView.as_view(), name='logout'),
    path('catalog', views.CatalogView.as_view(), name='catalog'),
    path('catalog/<pk>/delete/', views.DeleteServiceView.as_view(),
         name='delete_service'),
    path('catalog/create', views.CreateServiceView.as_view(),
         name='create_service'),
    path('catalog/<pk>/update/', views.UpdateServiceView.as_view(),
         name='update_service'),
    path('catalog/<pk>', views.ServiceView.as_view(), name='service')
]
