import re

from django.http import HttpResponse
from django.shortcuts import render
from media.forms import FileUploadForm, ReadFileForm


def upload_file(request):
    if request.method == 'POST':
        upload_file_form = FileUploadForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=f"Название файла: {file.name}, Размер: {file.size} (байт)", status=200)
    else:
        upload_file_form = FileUploadForm()

    context = {
        'file': upload_file_form
    }
    return render(request, 'media/file_load.html', context=context)


def read_file(request):
    smoke = ['закур', 'покур', 'выкур', 'кур']
    if request.method == 'POST':
        read_file_form = ReadFileForm(request.POST, request.FILES)
        if read_file_form.is_valid():
            text_file = read_file_form.cleaned_data['file'].read()
            text_str = text_file.decode('CP1251')
            for work in smoke:
                print("\n", re.findall(fr'\b{work}', text_str.lower()), "\n")
                if re.findall(fr'\b{work}', text_str.lower(), 1):
                    return HttpResponse('Цензура не прошла')
                else:
                    return HttpResponse(content=text_str, status=200)
    else:
        read_file_form = ReadFileForm()
    context = {
        'form': read_file_form,
        'file': read_file_form
    }
    return render(request, 'media/upload.html', context=context)
