from django.shortcuts import render
from todolist.models import Item


def items(request):
    item_list = Item.objects.all()
    choices = Item.CHOISES
    context = {
        'item_list': item_list,
        'choices': choices
    }
    return render(request, 'items_list.html', context=context)
