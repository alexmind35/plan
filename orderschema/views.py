from django.shortcuts import render, redirect
from django.views.generic.base import View

from orderschema.forms import UserForm, UsermodForm, ServicemodForm, OrdermodForm
from orderschema.models import Servicemod


class LandingView(View):
    def get(self, request):
        servicemod = Servicemod.objects.all()

        return render(request, "pages/landingpage.html",
                      {
                          "servicemod_list": servicemod,
                      })


def addOrder(request):
    error_form = ''
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_usermod = UsermodForm(request.POST)
        form_servicemod = ServicemodForm(request.POST)
        if all([form_user.is_valid(), form_usermod.is_valid(), form_servicemod.is_valid()]):
            form_usermod.save()


            return redirect('home')
        else:
            error_form = 'Форма была заполнена некоректно'

    form_add_user = UserForm()
    form_add_usermod = UsermodForm()
    form_add_servicemod = ServicemodForm()

    dataform = {
        'form_add_user': form_add_user,
        'form_add_usermod': form_add_usermod,
        'form_add_servicemod': form_add_servicemod,
        'error': error_form
    }

    return render(request, 'pages/landingpage.html', dataform)

def addForm(request):
    error_form = ''
    if request.method == 'POST':
        form_order = OrdermodForm(request.POST)
        if form_order.is_valid():
            form_order.save()

            return redirect('home')
        else:
            error_form = 'Форма была заполнена некоректно'

    form_add_order = OrdermodForm()

    dataform = {
        'form_add_order': form_add_order,
        'error': error_form
    }

    return render(request, 'pages/landingpage.html', dataform)