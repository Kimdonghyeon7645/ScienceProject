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




class science_project(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'scienceproject/index.html'
        weather_header = Header.objects.all()

        gu = request.GET.get('gu', '')
        
        if gu == 0:
            weather_gu = Gu0.objects.all()
        elif gu == 1:
            weather_gu = Gu1.objects.all()
        elif gu == 2:
            weather_gu = Gu2.objects.all()
        elif gu == 3:
            weather_gu = Gu3.objects.all()
        elif gu == 4:
            weather_gu = Gu4.objects.all()
        else:
            weather_gu = Gu0.objects.all()

        return render(request, template_name, {"header": weather_header, "gu0": weather_gu})


def test_from(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        form = GuForm()
        return render(request, 'scienceproject/index.html', {'form':form})
