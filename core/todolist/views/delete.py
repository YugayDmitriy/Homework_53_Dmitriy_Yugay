from django.contrib import messages
from django.shortcuts import redirect
from todolist.models import Item


def delete_item(request, myid):
    item = Item.objects.get(id=myid)
    item.delete()
    messages.info(request, 'Задача успешно удалена')
    return redirect('items_list')
