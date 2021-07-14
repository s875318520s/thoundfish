from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from main.models import unit

class Index(TemplateView):
    template_name = "./Index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['db'] = unit.objects.all()

        return context

    def post(self, request):
        result = {}
        try:
            query_result = unit.objects.filter(pk=request.POST['index'])[0]
            if request.POST['type'] == '1':
                query_result.status_1 = True
                query_result.status_1_change = datetime.now()
                query_result.status_1_uesr = request.POST['name']
                result['change'] = '已開啟'
            elif request.POST['type'] == '2':
                query_result.status_2 = True
                query_result.status_2_change = datetime.now()
                query_result.status_2_uesr = request.POST['name']
                result['change'] = '已驗證'
            result['status'] = 'success'
            query_result.save()
        except IOError as error:
            result['status'] = 'fail'
            result['change'] = error
        except IndexError:
            result['status'] = 'fail'
            result['change'] = '錯誤PK'
        return JsonResponse(result)
class All(TemplateView):
    template_name = "./all.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['db'] = unit.objects.all()

        return context

class API_update_status(View):
    def get(self, request):
        all = unit.objects.all()
        contents = ''
        for items in all:
            button1, button2 = '', ''
            pk = str(items.pk)
            if items.status_1:
                button1 = '<button type="button" class="btn btn-success" disabled>完成</button>'
            else:
                button1 = '<button type="button" class="btn btn-secondary" onclick="send(' + pk + ',1)">未啟動</button>'
            if items.status_2:
                button2 = '<button type="button" class="btn btn-success" disabled>完成</button>'
            else:
                if items.status_1:
                    button2 = '<button type="button" class="btn btn-secondary" onclick="send(' + pk + ',2)">未啟動</button>'
                else:
                    button2 = '<button type="button" class="btn btn-secondary" disabled>未啟動</button>'

            contents += '<tr><th scope="row">' + pk + '</th><td>' + items.name + '</td><td>' + button1 + '</td><td>' + button2 + '</td></tr>'
        return JsonResponse({'data': contents})
