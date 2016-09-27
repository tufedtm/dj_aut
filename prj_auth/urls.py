from django.conf.urls import url

from .views import HomeView, LoginView, LogoutView, RegistrationView

app_name = 'prj_auth'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^registration', RegistrationView.as_view(), name='registration'),
]
