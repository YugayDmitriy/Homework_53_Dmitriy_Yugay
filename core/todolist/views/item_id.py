from todolist.models import Item
from django.shortcuts import render, get_object_or_404


def items_id(request, myid):
    items = get_object_or_404(Item, id=myid)
    return render(request, 'items_id.html', context={
        'items': items
    })
