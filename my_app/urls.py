from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('hospital/<int:pk>', views.detail_page, name='detail_page'),
    path('hospital/create/', views.CreateHospital.as_view(template_name='my_app/create_hospital.html'), name='create_page'),
    path('hospital/update/<int:pk>', views.UpdateHospital.as_view(template_name='my_app/update_page.html'), name='update_page'),
    path('hospital/delete/<int:pk>', views.DeleteHospital.as_view(template_name='my_app/delete_page.html'), name='delete_page'),
]