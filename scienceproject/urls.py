from django.conf.urls import (include, url)
from . import views

from django.conf import settings
from django.conf.urls.static import static

#app_name = "scienceproject"

urlpatterns = [
	url(r'^$', views.gu0.as_view()),
	url(r'0', views.gu0.as_view()),
	url(r'1', views.gu1.as_view()),
	url(r'2', views.gu2.as_view()),
	url(r'3', views.gu3.as_view()),
	url(r'4', views.gu4.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
