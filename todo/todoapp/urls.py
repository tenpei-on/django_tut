from django.urls import path
from .views import TodoDetail, Todolist, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path('list/', Todolist.as_view(),name='rlist'),
    path('detail/<int:pk>', TodoDetail.as_view(),name='rdetail'),
    path('create/', TodoCreate.as_view(),name='rcreate'),
    path('delete/<int:pk>', TodoDelete.as_view(),name='rdelete'),
    path('update/<int:pk>', TodoUpdate.as_view(),name='rupdate'),
]
