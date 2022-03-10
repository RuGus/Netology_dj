import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def home_view(request):
    template_name = "app/home.html"
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        "Главная страница": reverse("home"),
        "Показать текущее время": reverse("time"),
        "Показать содержимое рабочей директории": reverse("workdir"),
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {"pages": pages}
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.now().time()
    msg = f"Текущее время: {current_time}"
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    files_list = "<br/>"
    for dirpath, dirnames, filenames in os.walk("."):
        # перебрать каталоги
        for dirname in dirnames:
            files_list += f"Каталог: {os.path.join(dirpath, dirname)} <br/>"
        # перебрать файлы
        for filename in filenames:
            files_list += f"Файл: {os.path.join(dirpath, filename)} <br/>"
    msg = f"В рабочей директории размещены следующие файлы и каталоги: {files_list}"
    return HttpResponse(msg)
