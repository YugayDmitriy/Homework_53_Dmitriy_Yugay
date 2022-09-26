from django.contrib import messages
from django.shortcuts import render
from todolist.models import Item


def add_item(request):
    if request.method == "POST":
        name = request.POST['name']
        created_at = request.POST['created_at']
        item = Item(name=name, created_at=created_at)
        item.save()
        messages.info(request, "Задача успешно добавлена")
    else:
        pass
    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request, 'index.html', context=context)
