from django.urls import path
from .views import SignUpView # type: ignore
urlpatterns = [
    path("signup/",SignUpView.as_view(),name="signup"),
]