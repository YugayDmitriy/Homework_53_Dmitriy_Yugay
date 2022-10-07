from django.contrib import messages
from django.shortcuts import redirect
from todolist.models import Item


def update_item(request, myid):
    item = Item.objects.get(id=myid)
    item.name = request.POST.get('name')
    item.status = request.POST.get('status')
    item.discription = request.POST.get('discription')
    item.created_at = request.POST.get('created_at')
    item.save()
    messages.info(request, "Задача успешно отредактирована")
    return redirect('items_list')
