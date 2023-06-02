from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:id>', views.view_record, name="record"),
    path('record/delete/<int:id>', views.delete_record, name='delete'),
    path('new/', views.create_record, name="create"),
    path('record/edit/<int:id>', views.edit_record, name='update'),
]
