from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect("https://django-cloudrun-i7gftfbecq-uc.a.run.app/cms/")