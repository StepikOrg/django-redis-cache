try:
    from django.urls import path
except ImportError:
    from django.conf.urls import url as path

from .views import someview

urlpatterns = [
    path('', someview),
]
