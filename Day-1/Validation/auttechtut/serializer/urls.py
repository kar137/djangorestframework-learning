from .views import StudentSerializeView
from django.urls import path

urlpatterns = [
    path('serialize2/', StudentSerializeView.as_view())
]