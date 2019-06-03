from django.http import HttpResponse

def index(request):
    retun HttpResponse("Hello, you're at the home screen")
