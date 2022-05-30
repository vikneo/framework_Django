from django.shortcuts import render
from django.views import View
from app_profiles.forms import UserForms


class UserFormView(View):

    def get (self, request):
        user_form = UserForms()
        return render(request, 'app_profiles/register.html', context={'user_form': user_form})

