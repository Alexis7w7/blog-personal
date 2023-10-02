from django.urls import path
from . import views

# views
urlpatterns = [
    path('', views.posts, name='publicaciones'),
    path('<int:id>/', views.post, name='post')
]
