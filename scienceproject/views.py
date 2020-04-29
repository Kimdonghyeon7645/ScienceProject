from django.shortcuts import (render, redirect)
from .models import Header
from .models import Gu0
from .models import Gu1
from .models import Gu2
from .models import Gu3
from .models import Gu4

from .forms import GuForm


from django.views import View
from django.views import generic


class gu0(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'scienceproject/index.html'
        weather_header = Header.objects.all()
        weather_gu = Gu0.objects.all()

        return render(request, template_name, {"header": weather_header, "gu0": weather_gu})

class gu1(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'scienceproject/index.html'
        weather_header = Header.objects.all()
        weather_gu = Gu1.objects.all()

        return render(request, template_name, {"header": weather_header, "gu0": weather_gu})

class gu2(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'scienceproject/index.html'
        weather_header = Header.objects.all()
        weather_gu = Gu2.objects.all()

        return render(request, template_name, {"header": weather_header, "gu0": weather_gu})

class gu3(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'scienceproject/index.html'
        weather_header = Header.objects.all()
        weather_gu = Gu3.objects.all()

        return render(request, template_name, {"header": weather_header, "gu0": weather_gu})

class gu4(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'scienceproject/index.html'
        weather_header = Header.objects.all()
        weather_gu = Gu4.objects.all()

        return render(request, template_name, {"header": weather_header, "gu0": weather_gu})
