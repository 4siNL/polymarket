from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.AccountLoginView.as_view(), name='login'),
    path('catalog', views.CatalogView.as_view(), name='catalog'),
    path('catalog/<pk>/delete/', views.DeleteServiceView.as_view(),
         name='delete_service')
]
