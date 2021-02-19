from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.timezone import datetime, timedelta
from .models import Dogovor
from .converter import *


def main(request):
    dogovor_data = Dogovor.objects.filter(end_date__isnull=False).order_by('-date')[:30]
    print(dogovor_data)

    data = {
        'title': 'Последние договора',
        'dogovors': dogovor_data,
    }
    return render(request, 'dogovor/index.html', data)


def convert(request):
    print('Converting...')
    result = converter()
    if result:
        i = 0
        for row in result:
            i += 1
            street = getu(row['Codg'], row['Codu'])
            city = getg(row['Codg'])
            if row['Kv'] != '':
                kv = row['Kv']
            else:
                kv = None
            #
            # Dogovor.objects.create(name=row['Fam'], number=row['Nom'], date=row['Datdog'], end_date=row['Datsrok'],
            #                        tel1=row['Tel'], fiz=row['Fl'], address_city=city, address_street=street,
            #                        id_old=row['Idold'], equip=row['Oborud'], comment=row['Coment'], sum=row['Sum0'],
            #                        discount=row['Skid'], amount=row['Sum1'], address_house=row['Dom'],
            #                        address_kv=kv)
            print(f'[{i}]')

    return render(request, 'dogovor/index.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    data = {
        'form': form,
    }
    return render(request, 'dogovor/login.html', data)


def user_logout(request):
    logout(request)
    return redirect('login')
