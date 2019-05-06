from django.http import HttpResponse

def index(request):
    return HttpResponse('海胜天成！')