from django.contrib.auth import login, logout
from django.db.models import Q, Sum
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dogovor, Payment, Notification
from .forms import DogovorForm, PaymentForm
from .converter import *
from datetime import datetime, timedelta
from .param import *


def main(request):
    end = datetime.now().date() + timedelta(days=EXPIRED_DAYS)
    dogovor_count = Dogovor.objects.all().count()
    dogovor_active_count = Dogovor.objects.filter(active=True).count()
    dogovor_expiring_count = Dogovor.objects.filter(Q(end_date__lte=end) & Q(active=True)).count()
    dogovor_expired_count = Dogovor.objects.filter(Q(end_date__lte=datetime.now().date()) & Q(active=True)).count()

    data = {
        'title': 'Dashboard',
        'count': dogovor_count,
        'active_count': dogovor_active_count,
        'expiring_count': dogovor_expiring_count,
        'expired_count': dogovor_expired_count,
    }
    return render(request, 'dogovor/index.html', data)


def dogovor_inactive(request):
    dogovor_data = Dogovor.objects.filter(active=False).order_by('-date')

    data = {
        'title': 'Расторгнутые договора',
        'dogovors': dogovor_data,
        'query': 'Расторгнутые',
    }
    return render(request, 'dogovor/inactive.html', data)


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
    payments = Payment.objects.filter(dogovor_id=dogovor_id).order_by('date')
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
            return redirect('dogovor', dogovor_id=dogovor.id)
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
                                              Q(tel3__contains=query)).order_by('-date')
    else:
        dogovor_data = []
        query = ''
    data = {
        'title': 'Результат поиска',
        'dogovors': dogovor_data,
        'query': query,
    }
    return render(request, 'dogovor/search.html', data)


def dogovor_search_name(request):
    if request.method == 'POST':
        name = request.POST['name'].strip()
        dogovor_data = Dogovor.objects.filter(name__contains=name).order_by('-date')[:500]
    else:
        dogovor_data = []
        name = ''

    data = {
        'title': 'Результат поиска',
        'dogovors': dogovor_data,
        'name': name,
    }
    return render(request, 'dogovor/name.html', data)


def dogovor_search_address(request):
    end = datetime.now().date() + timedelta(days=EXPIRED_DAYS)
    address_city = Dogovor.objects.values('address_city').distinct().order_by('address_city')
    address_street = Dogovor.objects.values('address_street').distinct().order_by('address_street')
    if request.method == 'POST':
        city = request.POST['address_city']
        street = request.POST['address_street']
        expiring = request.POST.get('expiring')
        error_message = ''
        if city and street:
            dogovor_data = Dogovor.objects.filter(Q(address_city=city) & Q(address_street=street) & Q(active=True))
            if expiring:
                dogovor_data = dogovor_data.filter(end_date__lte=end)
        elif city:
            dogovor_data = Dogovor.objects.filter(Q(address_city=city) & Q(active=True))
            if expiring:
                dogovor_data = dogovor_data.filter(end_date__lte=end)
        elif street:
            dogovor_data = []
            error_message = 'Выберите населенный пункт'
        else:
            dogovor_data = []
            error_message = 'Задайте параметры поиска'
    else:
        dogovor_data = []
        city = ''
        street = ''
        error_message = 'Параметры поиска'
    data = {
        'title': 'Результат поиска',
        'cities': address_city,
        'streets': address_street,
        'city': city,
        'street': street,
        'dogovors': dogovor_data,
        'message': error_message,
    }
    return render(request, 'dogovor/search_address.html', data)


def city_autocomplete(request):
    q = request.GET['term']
    qs = Dogovor.objects.values('address_city').distinct().order_by('address_city')
    data = []
    if q:
        qs = qs.filter(address_city__istartswith=q)
        for item in qs:
            data.append(item['address_city'])
    return JsonResponse(data, safe=False)


def street_autocomplete(request):
    q = request.GET['term']
    qs = Dogovor.objects.values('address_street').distinct().order_by('address_street')
    data = []
    if q:
        qs = qs.filter(address_street__istartswith=q)
        for item in qs:
            data.append(item['address_street'])
    return JsonResponse(data, safe=False)


def name_autocomplete(request):
    q = request.GET['term']
    qs = Dogovor.objects.values('name').distinct().order_by('name')
    data = []
    if q:
        qs = qs.filter(name__istartswith=q)
        for item in qs:
            data.append(item['name'])
    return JsonResponse(data, safe=False)


def dogovor_newpay(request, dogovor_id):
    qs = Dogovor.objects.get(pk=dogovor_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            Payment.objects.create(**form.cleaned_data)
            return redirect('dogovor', dogovor_id=dogovor_id)
        else:
            print('invalid form')
    else:
        form = PaymentForm()
    data = {
        'title': 'Новый платеж',
        'form': form,
        'dogovor': qs,
    }
    return render(request, 'dogovor/newpay.html', data)


def dogovor_updatepay(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    dogovor = payment.dogovor_id
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('dogovor', dogovor_id=dogovor.id)
        else:
            print('form error', form)
    form = PaymentForm(instance=payment)
    data = {
        'form': form,
        'dogovor': dogovor,
        'payment_id': payment_id,
    }
    return render(request, 'dogovor/updatepay.html', data)


def payment_delete(request, payment_id):
    instance = get_object_or_404(Payment, pk=payment_id)
    dogovor_id = instance.dogovor_id.id
    instance.delete()
    return redirect('dogovor', dogovor_id=dogovor_id)


def payments(request):
    payments_data = Payment.objects.all().order_by('-date')[:100]
    summa = payments_data.aggregate(Sum('amount'))['amount__sum']
    data = {
        'title': 'Последние платежи',
        'payments': payments_data,
        'summa': summa,
    }
    return render(request, 'dogovor/payments.html', data)


def payments_by_date(request):
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        if end_date:
            payments_data = Payment.objects.filter(date__range=(start_date, end_date)).order_by('-date')
        else:
            payments_data = Payment.objects.filter(date__gte=start_date).order_by('-date')
        summa = payments_data.aggregate(Sum('amount'))['amount__sum']
    else:
        payments_data = []
        start_date = ''
        end_date = ''
        summa = 0
    data = {
        'title': 'Результат поиска',
        'payments': payments_data,
        'start_date': start_date,
        'end_date': end_date,
        'summa': summa,
    }
    return render(request, 'dogovor/datepayments.html', data)


def payments_by_name(request):
    if request.method == 'POST':
        name = request.POST['name'].strip()
        payments_data = Payment.objects.filter(dogovor_id__name__contains=name).order_by('-date')[:500]
        summa = payments_data.aggregate(Sum('amount'))['amount__sum']
    else:
        payments_data = []
        name = ''
        summa = 0
    data = {
        'title': 'Результат поиска',
        'payments': payments_data,
        'name': name,
        'summa': summa,
    }
    return render(request, 'dogovor/namepayments.html', data)


def payments_by_number(request):
    if request.method == 'POST':
        number = request.POST['number'].strip()
        payments_data = Payment.objects.filter(dogovor_id__number__contains=number).order_by('-date')[:500]
        summa = payments_data.aggregate(Sum('amount'))['amount__sum']
    else:
        payments_data = []
        number = ''
        summa = 0
    data = {
        'title': 'Результат поиска',
        'payments': payments_data,
        'number': number,
        'summa': summa,
    }
    return render(request, 'dogovor/numpayments.html', data)


def notifications(request):
    today = datetime.today().date()
    notification_data = Notification.objects.filter(create_time__date=today).order_by('-create_time')
    data = {
        'title': 'Номера телефонов для уведомлений',
        'notifications': notification_data,
    }
    return render(request, 'dogovor/notifications.html', data)


def add_notifications(request):
    if request.method == 'POST':
        dogovors = request.POST.getlist('dogovor_id[]')
        for item in dogovors:
            dogovor = Dogovor.objects.get(id=item)
            Notification.objects.create(dogovor_id=dogovor, notify_type='Call')
    return redirect('notifications')
