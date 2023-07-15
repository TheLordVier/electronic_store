from django.urls import path

from core.views import ListCreateUserView, RetrieveDestroyUserView, UserLogin, UserLogout

urlpatterns = [
    path("", ListCreateUserView.as_view()),
    path("<int:pk>", RetrieveDestroyUserView.as_view()),
    path("user_login", UserLogin.as_view()),
    path("user_logout", UserLogout.as_view()),
]
