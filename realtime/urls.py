from django.conf.urls import url

from realtime.views import RegistrationView, LoginView, LogoutView

urlpatterns = [
    url(r'^registration', RegistrationView.as_view()),
    url(r'^login', LoginView.as_view()),
    url(r'^logout', LogoutView.as_view())

]
