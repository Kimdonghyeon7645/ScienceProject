from django.shortcuts import (render, redirect)
from .models import Header
from .models import Gu0
from .models import Gu1
from .models import Gu2
from .models import Gu3
from .models import Gu4


from django.views import View
from django.views import generic

class science_project(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'scienceproject/index.html'
        weather_header = Header.objects.all()
        weather_gu0 = Gu0.objects.all()
        weather_gu1 = Gu1.objects.all()
        weather_gu2 = Gu2.objects.all()
        weather_gu3 = Gu3.objects.all()
        weather_gu4 = Gu4.objects.all()
        return render(request, template_name,
                      {"header": weather_header, "gu0": weather_gu0, "gu1": weather_gu1,
                       "gu2": weather_gu2, "gu3": weather_gu3, "gu4": weather_gu4})