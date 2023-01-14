from django.urls import path
from .views import *


urlpatterns = [
    path('', todoForm, name='todo'),
    path('edit_todo/<int:pk>', edit_todos, name='edit_todo')
]
