from _csv import reader
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render
from app_shop.forms import UploadFileForm
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
