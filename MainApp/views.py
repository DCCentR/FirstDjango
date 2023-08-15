from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    text =  """ <h1>"Изучаем django"</h1>
                <strong>Автор</strong>: <i>Горюнов А.А.</i>
            """
    return HttpResponse(text)

def about(request):
    text =  """ Имя: <b>Андрей</b><br>
                Отчество: <b>Александрович</b><br>
                Фамилия: <b>Горюнов</b><br>
                телефон: <b>8-977-777-77-77</b><br>
                email: <b>bibaboba@gmail.com</b>
            """
    return HttpResponse(text)

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]