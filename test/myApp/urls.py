from django.urls import path
from . import views

urlpatterns=[
    path('signup', views.add_USER1, name='add_USER1'),
    path('login', views.login_user, name='login'),
    path('display', views.displayView, name="display"),
    path('<int:book_id>/update', views.update, name="update"),
    path('add', views.add , name="add"),
    path('menu', views.menu , name="menu"),
    path('<int:book_id>/delete', views.delete , name="delete"),
    
]
    
