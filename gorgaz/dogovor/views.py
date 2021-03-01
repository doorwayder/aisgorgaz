from django.contrib.auth import login, logout
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dogovor, Payment
from .forms import DogovorForm
from .converter import *


def main(request):
    dogovor_data = Dogovor.objects.filter(end_date__isnull=False).order_by('-date')[:100]

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


def dogovor_view(request, dogovor_id):
    dogovor = get_object_or_404(Dogovor, pk=dogovor_id)
    payments = Payment.objects.filter(dogovor_id=dogovor_id).order_by('-date')
    return render(request, 'dogovor/dogovor.html', {'dogovor': dogovor, 'payments': payments})


def dogovor_add(request):
    if request.method == 'POST':
        form = DogovorForm(request.POST)
        if form.is_valid():
            Dogovor.objects.create(**form.cleaned_data)
    else:
        form = DogovorForm()
    data = {
        'title': 'Новый договор',
        'form': form,
    }
    return render(request, 'dogovor/add.html', data)


def dogovor_update(request, dogovor_id):
    dogovor = Dogovor.objects.get(pk=dogovor_id)
    if request.method == 'POST':
        form = DogovorForm(request.POST, instance=dogovor)
        if form.is_valid():
            form.save()
            return redirect('main')
    form = DogovorForm(instance=dogovor)
    data = {
        'form': form,
        'dogovor_id': dogovor_id,
    }
    return render(request, 'dogovor/update.html', data)


def dogovor_search(request):
    if request.method == 'POST':
        query = request.POST['query'].strip()
        dogovor_data = Dogovor.objects.filter(Q(name__contains=query) | Q(number__contains=query) |
                                              Q(tel1__contains=query) | Q(tel2__contains=query) |
                                              Q(tel3__contains=query)).order_by('-date')[:50]
    else:
        dogovor_data = []
        query = ''
    data = {
        'title': 'Результат поиска',
        'dogovors': dogovor_data,
        'query': query,
    }

    return render(request, 'dogovor/search.html', data)
