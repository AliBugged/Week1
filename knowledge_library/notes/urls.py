from django.urls import path
from .views import note_list, note_create, note_update, note_delete

urlpatterns = [
    path('', note_list, name='note_list'),
    path('create/', note_create, name='note_create'),
    path('update/<int:note_id>/', note_update, name='note_update'),
    path('delete/<int:note_id>/', note_delete, name='note_delete'),
]