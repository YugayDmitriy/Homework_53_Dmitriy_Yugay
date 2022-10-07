from django.shortcuts import render, redirect
from todolist.models import Item


def items_list(request, *args, **kwargs):
    item_list = Item.objects.all()
    if request.method == 'GET':
        context = {
            'item_list': item_list,
        }
        return render(request, 'items_list.html', context=context)
