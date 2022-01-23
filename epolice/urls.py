from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('register/',views.register,name='register'),
    path('otp/',views.otp,name='otp'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('profile/',views.profile,name='profile'),
    path('contact/',views.contact,name='contact'),
    path('add_fir/',views.add_fir,name='add_fir'),
    path('view_fir/',views.view_fir,name='view_fir'),
    path('add_criminal/',views.add_criminal,name='add_criminal'),
    path('view_criminal/',views.view_criminal,name='view_criminal'),
    path('edit_criminal/<int:id>',views.edit_criminal,name='edit_criminal'),
    path('delete_criminal/<int:id>',views.delete_criminal,name='delete_criminal'),
    path('view_fir_police/',views.view_fir_police,name='view_fir_police'),
    path('solved_fir/<int:id>',views.solved_fir,name='solved_fir'),

]