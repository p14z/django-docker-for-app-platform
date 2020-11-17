from django.http import HttpResponse


def home(request):
    return HttpResponse("I'm a teapot", status=408)
