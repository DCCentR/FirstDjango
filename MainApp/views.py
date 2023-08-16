from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    text =  """ <h1>"Изучаем django"</h1>
                <strong>Автор</strong>: <i>Горюнов А.А.</i>
            """
    return HttpResponse(text)

def about(request):
    text =  """ <p>Имя: <b>Андрей</b></p>
                <p>Отчество: <b>Александрович</b></p>
                <p>Фамилия: <b>Горюнов</b></p>
                <p>Телефон: <b>8-977-777-77-77</b></p>
                <p>Email: <b>bibaboba@gmail.com</b></p>
            """
    return HttpResponse(text)

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

def item(request, item_id):
    for item in items:
        if item['id'] == int(item_id):
            return HttpResponse(f"<p>Название: {item['name']}</p><p>Количество: {item['quantity']}</p><p><a href=\"/items\">назад к списку товаров</a></p>")
    return HttpResponse(f"Товар с id={item_id} не найден")

def items_list(request):
    items_html = "<ol>"
    for index, item in enumerate(items):
        items_html += f"<li><a href=\"/item/{item['id']}\">{item['name']}</a></li>"
    items_html += "</ol>"
    return HttpResponse(items_html)