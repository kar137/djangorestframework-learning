from .views import CommentSerializeView, StudentSerializeView
from django.urls import path

urlpatterns = [
    path('serialize1/', CommentSerializeView.as_view()),
    path('serialize2/', StudentSerializeView.as_view())
]