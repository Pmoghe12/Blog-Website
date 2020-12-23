from django.urls import path
from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *

from . import views

urlpatterns = [
    path('',views.Homepage.as_view(),name='home'),
 #   path('new',views.AddPost.as_view(),name='new'),
    path('detailView/<int:pk>',views.ViewDetail.as_view(),name='detailView'),
    path('blog_edit/<int:pk>',views.EditPost.as_view(),name='blog_edit'),
    path('blog_delete/<int:pk>',views.DeletePost.as_view(),name='blog_delete'),
    path('about',views.Aboutus.as_view(),name='about'),
    path('abt',views.Abt.as_view(),name='abt'),
    path('join',views.Join.as_view(),name='join'),
	path('new', hotel_image_view, name = 'new'), 
  #  path('success', success, name = 'success'), 
  



]

if settings.DEBUG: 
		urlpatterns += static(settings.MEDIA_URL, 
							document_root=settings.MEDIA_ROOT) 