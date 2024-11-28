from django.contrib import admin
from .models import Hospital, Doctor, Nurse, Department, DoctorDepartment, NurseDepartment, \
    DoctorDepartmentHospital, NurseDepartmentHospital, Bed, Patient


# Register your models here.


admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Department)
admin.site.register(DoctorDepartment)
admin.site.register(NurseDepartment)
admin.site.register(DoctorDepartmentHospital)
admin.site.register(NurseDepartmentHospital)
admin.site.register(Bed)
admin.site.register(Patient)
