


from django.urls import path
from .import views

app_name = "users"

urlpatterns = [
    
    path('register/',views.register, name="reg"),
    path('mylogin/',views.mylogin, name="log"),
    path('logout/',views.logout_view, name="out"),
   
]