from django.urls import path
from . import views 

urlpatterns = [
    path("",views.index, name="index"),
    path("rauf", views.rauf, name="rauf"),
    path("ahsan",views.ahsan, name="ahsan"),
    path("<str:name>",views.greet, name="greet")

]