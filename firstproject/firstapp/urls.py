from django.urls import path
from firstapp.views import index,PostCreate,detail  
app_name="firstapp"
urlpatterns = [
    path('',index,name='index'),
    path('create/',PostCreate.as_view(),name='create'),
    path('detail/<int:pk>/', detail, name='detail')
]