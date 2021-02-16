from django.shortcuts import render, redirect
from django.utils.timezone import datetime, timedelta
from .models import Dogovor


def main(request):
   return render(request, 'dogovor/index.html')
