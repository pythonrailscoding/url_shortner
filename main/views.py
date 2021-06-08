from django.shortcuts import redirect, render
import uuid
from .models import UrlShortner
from django.http import HttpResponse

def index(request):
    return render(request, "index.html", {})

def create(request):
    if request.method == 'POST':
        url = request.POST["link"]
        uid = str(uuid.uuid4())[:5]

        new_url = UrlShortner(url=url, uuid=uid)
        new_url.save()

        return HttpResponse("https://dj-shorturls.herokuapp.com/"+uid)
    else:
        return HttpResponse("Submitted")

def go(request, pk):
    url_details = UrlShortner.objects.get(uuid=pk)
    return redirect(url_details.url)
