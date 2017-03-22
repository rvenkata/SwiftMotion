from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadCSVForm
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")


def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            # bulk load csv
            return HttpResponse('Success! Uploaded {}'.format(form.cleaned_data.get('filename')))
        else:
            return HttpResponse(form.errors.as_json())


def csv_view(request):
    return render(request, 'swiftmotion_backend/upload_csv.html', {})
