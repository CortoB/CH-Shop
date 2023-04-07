from django.urls import path
from . import views

# UrlConfig
urlpatterns = [
    path('showtime/', views.show_time)
]
