from django.urls import path
from . import views

app_name    = "users"
urlpatterns = [ 
    path('block/<uuid:pk>/', views.block, name="block"),
]


