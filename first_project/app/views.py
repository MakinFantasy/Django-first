from dataclasses import dataclass
from time import time
from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime, timedelta
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)  

# Done
def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = (datetime.utcnow() + timedelta(hours=3)).strftime('%Y-%m-%d %H-%m')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg) 

# Done 
def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    files = os.listdir(path='.')
    files_str = str()
    for i in files:
        files_str += str(i)
    files_str = files_str.replace('.', ', ')
    return HttpResponse(files_str)
