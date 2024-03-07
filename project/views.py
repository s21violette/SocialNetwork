from django.http import HttpResponse
from django.http import HttpResponseNotFound


def home(request):
    return HttpResponse("<H1>This is home page</H1>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page is not found</h1>")
