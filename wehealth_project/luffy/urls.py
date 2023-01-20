from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('adminsite/', views.adminSite, name='adminSite'),
    path('adminsite/<int:auth_id>', views.approveUser, name='approveUser'),
    path('adminsite/logout/', views.logOut, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)