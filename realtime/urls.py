from django.conf.urls import url

from realtime.views import RegistrationView

urlpatterns = [
    url(r'^registration', RegistrationView.as_view()),

]
