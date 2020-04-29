from django.conf.urls import (include, url)
from . import views

from django.conf import settings
from django.conf.urls.static import static

#app_name = "scienceproject"

urlpatterns = [
	url(r'^$', views.science_project.as_view()),
	url('form-test/', views.test_from)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
