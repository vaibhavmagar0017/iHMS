from rest_framework import serializers
from .models import (Hospital, DoctorDepartment, Doctor, Department, NurseDepartment,
                     NurseDepartmentHospital, Nurse, DoctorDepartmentHospital, Bed, Patient, Appointments)


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DoctorDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDepartment
        fields = '__all__'


class NurseDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseDepartment
        fields = '__all__'


class DoctorDepartmentHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDepartmentHospital
        fields = '__all__'


class NurseDepartmentHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseDepartmentHospital
        fields = '__all__'


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class AppointmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointments
        fields = '__all__'
