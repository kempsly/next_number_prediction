from django.urls import path
from django.conf.urls.static import static
from .views import handlerView

urlpatterns = [
    path("", handlerView, name="home-page")
]