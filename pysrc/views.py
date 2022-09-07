

from http.client import HTTPResponse
from django.http import HttpResponse

def home(request):
    return HttpResponse('Teste de apresentação da página')