from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blogHome/', views.BlogHome, name="blogHome"),
    # path('', WomenHome.as_view(), name='home'),
]
