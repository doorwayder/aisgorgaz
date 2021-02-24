from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dogovor, Payment
from .forms import SearchForm, DogovorForm
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


def dogovor_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Dogovor.objects.annotate(search=SearchVector('name', 'number'),).filter(search=query)
    return render(request, 'dogovor/search.html', {'form': form, 'query': query, 'results': results})


def dogoovor_edit(request):
    if request.method == 'POST':
        form = DogovorForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = DogovorForm()
    data = {
        'title': 'Договор',
        'form': form,
    }
    return render(request, 'dogovor/dogovor.html', data)


def dogovor_view(request, dogovor_id):
    dogovor = get_object_or_404(Dogovor, pk=dogovor_id)
    payments = Payment.objects.filter(dogovor_id=dogovor_id).order_by('-date')
    return render(request, 'dogovor/dogovor.html', {'dogovor': dogovor, 'payments': payments})


# class UpdateDogovorView(LoginRequiredMixin, UpdateView):
#     model = Dogovor
#     fields = ['name', 'number', 'date', 'end_date', 'tel1', 'tel2', 'tel3', 'fiz', 'address_city', 'address_street',
#               'address_house', 'address_kv', 'equip', 'sum', 'discount', 'amount', 'comment', 'active']
