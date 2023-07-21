from django.urls import path

from .views import login_page, logout_page
from .newviews import registration_form
urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', registration_form, name='register'),
]