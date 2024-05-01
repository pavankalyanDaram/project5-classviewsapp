from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request,template_name='input.html')

class Add(View):
    def get(self, request):
        x = int(request.GET.get('t1'))
        y = int(request.GET.get('t2'))
        z = x+y
        con_dict = {'res': z}
        return render(request, template_name='result.html', context=con_dict)
    def post(self, request):
        x = int(request.POST.get('t1'))
        y = int(request.POST.get('t2'))
        z = x+y
        con_dict = {'res': z}
        return render(request, template_name='result.html', context=con_dict)