from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('hms_workflow.urls')),
    path('admin/', admin.site.urls),
]
