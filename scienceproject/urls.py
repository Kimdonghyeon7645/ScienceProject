from django.conf.urls import (include, url)
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "scienceproject"

urlpatterns = [
	url(r'^$', views.gu0.as_view()),
	url(r'idong', views.idong, name='idong')
	# url() 에서 name 을 views 의 함수 이름과 동일하게 하고, indew.html 의 form action 속성값도 동일하게 한다.
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
