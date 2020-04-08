from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_all, name='all_businesses'),
    path('new_business/', views.add_new, name='new_business'),
    path('<int:business_id>', views.individual_business, name='individual_business')
]