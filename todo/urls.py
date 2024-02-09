from django.urls import path
from .api.views import *

urlpatterns = [
    path('',TodoView.as_view(),name="get_all_todos" ),
    path('del/<int:pk>',DeleteTodoView.as_view(),name="delete" ),
    path('update/<int:pk>',UpdateTodoView.as_view(),name="check" ),
]
