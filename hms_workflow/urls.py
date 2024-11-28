from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Hospital urls
    path('', views.HospitalListAPIView.as_view(), name='hospital-list-get'),
    path('hospitals/create/', views.HospitalCreateAPIView.as_view(), name='hospital-create'),
    path('hospitals/<int:pk>/update/', views.HospitalUpdateAPIView.as_view(), name='hospital-update'),
    path('hospitals/<int:pk>/delete/', views.HospitalDeleteAPIView.as_view(), name='hospital-delete'),
    # Doctor urls
    path('doctors', views.DoctorListAPIView.as_view(), name='doctor-list-get'),
    path('doctors/create/', views.DoctorCreateAPIView.as_view(), name='doctor-create'),
    path('doctors/<int:pk>/update/', views.DoctorUpdateAPIView.as_view(), name='doctor-update'),
    path('doctors/<int:pk>/delete/', views.DoctorDeleteAPIView.as_view(), name='doctor-delete'),
    # Nurse urls
    path('nurse/', views.NurseListAPIView.as_view(), name='nurse-list-get'),
    path('nurse/create/', views.NurseCreateAPIView.as_view(), name='nurse-create'),
    path('nurse/<int:pk>/update/', views.NurseUpdateAPIView.as_view(), name='nurse-update'),
    path('nurse/<int:pk>/delete/', views.NurseDeleteAPIView.as_view(), name='nurse-delete'),
    # Department urls
    path('department/', views.DepartmentListAPIView.as_view(), name='department-list-get'),
    path('department/create/', views.DepartmentCreateAPIView.as_view(), name='department-create'),
    path('department/<int:pk>/update/', views.DepartmentUpdateAPIView.as_view(), name='department-update'),
    path('department/<int:pk>/delete/', views.DepartmentDeleteAPIView.as_view(), name='department-delete'),
]
