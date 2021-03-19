from django.urls import path

from .views import user_list, user_detail

urlpatterns = [
    path('list/', user_list),
    path('detail/<int:pk>/', user_detail),
]
