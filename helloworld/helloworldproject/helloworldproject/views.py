from django.http import HttpResponse
from django.views.generic import TemplateView


def helloworldfunction(request):
    return HttpResponse("Hello, world.")

class HelloworldView(TemplateView):
    #template_name は呼び出すファイル settings.pyの中で指定builds
    template_name = "hello.html"
