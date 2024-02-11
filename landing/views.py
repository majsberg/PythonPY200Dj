from django.shortcuts import render
from django.views import View
from .forms import TemplateForm
from django.http import JsonResponse, HttpResponse


# Create your views here.
# def index_view(request):
#     if request.method == "GET":
#         return render(request, 'landing/index.html')


class TemplView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

    def post(self, request):
        received_data = request.POST
        form = TemplateForm(received_data)
        if form.is_valid():
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')
            form.cleaned_data['ip'] = ip
            form.cleaned_data['user_agent'] = user_agent
            return JsonResponse(form.cleaned_data, json_dumps_params={'ensure_ascii': False,
                                                                                      'indent': 4})
        return render(request, 'landing/index.html', context={"form": form})