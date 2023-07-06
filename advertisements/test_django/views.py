from django.shortcuts import render
from django.http import HttpResponse

def test_1(request):
    return HttpResponse('test')