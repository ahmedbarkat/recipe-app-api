from django.urls import path
from user import views


app_name = 'user'

urlpatterns = [
    path('create/',views.CreateUserView.as_view()),
    path('token/',views.CreateUserToken.as_view()),
    path('me/',views.ManageUserView.as_view())
]

