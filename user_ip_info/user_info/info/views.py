from django.shortcuts import render


def user_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'info/user_ip.html', {'ip_address': ip})
