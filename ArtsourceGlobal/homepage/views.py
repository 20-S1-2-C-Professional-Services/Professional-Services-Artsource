from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse
from artworkpage.models import Artwork
from artworkpage.models import TagsNames

# Create your views here.
def index(request):
    artworks = Artwork.objects.all()
    tags = TagsNames.objects.values_list("tag_names")
    return render(request, 'homepage/index.html', {'artworks': artworks, 'tags': tags})


def successView(request):
    return render(request, 'success.html')


def artwork_detail(request, pk):
    artid = Artwork.objects.get(id=pk)
    return render(request, './artworkpage/index.html', {'artid': artid})


def booking_detail(request, pk):
    artid = Artwork.objects.get(id=pk)
    return render(request, './booking/bookart.html', {'artid': artid})

def search(request):
    art_list = Artwork.objects.all()
    if request.method == 'GET':
        return render(request, 'search.html', {'tt': art_list})
    elif request.method == 'POST':
        s_target = request.POST.get('sss')
        res = []
        for i in Artwork.objects.all():
            a = i.name
            b = i.description
            c = i.tags
            if a.__contains__(s_target) or b.__contains__(s_target) or c.__contains__(s_target):
                res.append(i)
        images = []
        for i in res:
            images.append(i.image)
        return render(request, 'global_search.html', {'tt': res, 'images': images})
    else:
        return redirect('/search.html/')
