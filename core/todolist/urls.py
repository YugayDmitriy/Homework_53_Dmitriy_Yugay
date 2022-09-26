from django.urls import path
from .views.add import add_item
from .views.base import index
from .views.delete import delete_item
from .views.edit import edit_item
from .views.update import update_item

urlpatterns = [
    path('', index, name='index'),
    path('add_item', add_item, name='add_item'),
    path('delete_item/<int:myid>/', delete_item, name='delete_item'),
    path('edit_item/<int:myid>/', edit_item, name='edit_item'),
    path('update_item/<int:myid>/', update_item, name='update_item')
]
