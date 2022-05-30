from django.shortcuts import render


def advertisement_title(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def advertisement_detail_python_basic(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_detail_Python_basic.html', {})


def advertisement_detail_sql(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_detail_sql.html', {})


def advertisement_detail_python_pro(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_detail_python_pro.html', {})


def advertisement_detail_web(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_detail_web.html', {})


def advertisement_detail_django(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_detail_django.html', {})

