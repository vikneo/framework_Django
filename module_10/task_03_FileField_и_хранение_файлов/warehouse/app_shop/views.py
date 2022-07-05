import os
from _csv import reader
from decimal import Decimal
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_shop.forms import UploadFileForm, DocumentFile
from app_shop.models import Shop


def items_list(request):
    items = Shop.objects.all()
    return render(request, 'app_shop/items_list.html', context={'items_list': items})


def upload_file(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['file'].read()
            try:
                price_str = price_file.decode('utf-8').split('\n')
            except Exception:
                price_str = price_file.decode('CP1251').split('\n')
            csv_reader = reader(price_str, delimiter=",", quotechar='"')
            count_yes = 0
            count_no = 0
            for row in csv_reader:
                if row:
                    shop = Shop.objects.filter(code=row[1])
                    try:
                        if shop:
                            shop.update(title=row[0], price=Decimal(row[2]))
                            count_yes += 1
                        else:
                            Shop.objects.create(
                                title=row[0],
                                code=row[1],
                                price=row[2]
                            )
                            count_no += 1
                    except Exception:
                        pass
            return HttpResponse(content=f'Данные успешно обновлены\n Обновлено товаров:  {count_yes} (шт)\n'
                                        f'Добавлено товаров: {count_no} (шт)', status=200)
    else:
        upload_file_form = UploadFileForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'app_shop/upload_price_file.html', context=context)


def model_form_file(request):
    date = datetime.now().strftime('%d_%m_%Y-%H-%M-%S_')
    if request.method == 'POST':
        new_file = request.FILES['file'].name
        request.FILES['file'].name = date + new_file
        form = DocumentFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = DocumentFile()
    return render(request, 'app_shop/file_form_upload.html', {'form': form})

