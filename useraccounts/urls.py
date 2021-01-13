from django.urls import path
from .views import Signup,Signin,signout
urlpatterns=[
    path('signup', Signup.as_view(), name="signup"),
    path('signin',Signin.as_view(), name="signin"),
    path('signout',signout, name="signout")
]