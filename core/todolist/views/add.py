from django.contrib import messages
from django.shortcuts import render, redirect
from todolist.models import Item


def add_item(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == "POST":
        name = request.POST['name']
        discription = request.POST['discription']
        created_at = request.POST['created_at']
        item = Item(name=name, discription=discription, created_at=created_at)
        item.save()
        messages.info(request, "Задача успешно добавлена")
        return redirect('items_list')
