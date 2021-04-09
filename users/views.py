from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime
from django import forms
from django.shortcuts import redirect

# Create your views here.

def current_datetime(request):
    now = datetime.datetime.utcnow()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html, status=404)


def detail(request, poll_id):
    return render(request, 'users/detail.html', {"poll":poll_id})


def handle_uploaded_file(f):
    with open('name.'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def upload_file(request):
    print("--------------")
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print("++++++++++++++++++++", form.is_valid())
        
        if form.is_valid():
            print("-----------------------")
            handle_uploaded_file(request.FILES['file'])
            return redirect( reverse('users:detail', args=(1,)) )
    else:
        form = UploadFileForm()
    return render(request, 'users/upload.html', {'form': form})