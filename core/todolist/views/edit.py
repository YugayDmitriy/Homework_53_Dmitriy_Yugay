from django.shortcuts import render
from todolist.models import Item


def edit_item(request, myid):
    sel_item = Item.objects.get(id=myid)
    item_list = Item.objects.all()
    choices = Item.CHOISES
    context = {
        'sel_item': sel_item,
        'item_list': item_list,
        'choices': choices
    }
    return render(request, 'create.html', context=context)
