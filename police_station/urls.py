from django.urls import path
from . import views

urlpatterns = [
    path('view_fir_commissioner/',views.view_fir_commissioner,name="view_fir_commissioner"),
    path('add_police_station/,',views.add_police_station,name="add_police_station"),
    path('view_police_station/',views.view_police_station,name="view_police_station"),
    path('edit_police_station/<int:id>',views.edit_police_station,name="edit_police_station"),
    path('delete_police_station/<int:id>',views.delete_police_station,name="delete_police_station"),
    path('view_police/',views.view_police,name='view_police'),
    path('add_fir_commissioner/',views.add_fir_commissioner,name='add_fir_commissioner'),
    path('add_police/',views.add_police,name='add_police'),
    path('edit_police/<int:id>',views.edit_police,name='edit_police'),
    path('delete_police/<int:id>',views.delete_police,name='delete_police')
]