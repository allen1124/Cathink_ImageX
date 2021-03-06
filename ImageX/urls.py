"""ImageX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from ImageX.views import index
from images import views as images_view
from members import views as members_view
from images.views import ImageLikesAPIToggle


urlpatterns = [
	path('admin/', admin.site.urls, name='admin'),
	path('', index, name='index'),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
	url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		auth_views.password_reset_confirm, name='password_reset_confirm'),
	url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
	url(r'^images/$', images_view.image_search, name='images'),
	url(r'^images/upload/$', images_view.image_upload),
	url(r'^images/detail/(?P<id>\d+)/$', images_view.image_detail, name="image_detail"),
	url(r'^images/like/api/(?P<id>\d+)/$', ImageLikesAPIToggle.as_view(), name="like-api-toggle"),
	url(r'^images/edit/(?P<id>\d+)/$', images_view.image_edit),
	url(r'^images/delete/(?P<id>\d+)/$', images_view.image_delete),
	url(r'^images/download/(?P<id>\d+)/$', images_view.image_download),
	url(r'^profile/edit$', members_view.profile_edit),
	url(r'^profile/change-password$', members_view.change_password),
	url(r'^profile/detail/(?P<id>\d+)/$', members_view.profile_detail, name="profile_detail"),
	url(r'^profile/invitation/$', members_view.invitation, name="invitation"),
	url(r'^register/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/(?P<email>.*?)/$',
		members_view.register, name='register'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
