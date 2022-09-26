from django.contrib import messages
from django.shortcuts import redirect
from todolist.models import Item


def update_item(request, myid):
    item = Item.objects.get(id=myid)
    item.name = request.POST['name']
    item.status = request.POST['status']
    item.created_at = request.POST['created_at']
    item.save()
    messages.info(request, "Задача успешно отредактирована")
    return redirect('index')
