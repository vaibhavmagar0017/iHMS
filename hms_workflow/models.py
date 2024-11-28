from django.db import models


# Create your models here.


class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=100)
    hospital_address = models.CharField(max_length=200)

    def __str__(self):
        return self.hospital_name


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=100)
    doctor_address = models.CharField(max_length=200)

    def __str__(self):
        return self.doctor_name


class Nurse(models.Model):
    nurse_id = models.AutoField(primary_key=True)
    nurse_name = models.CharField(max_length=100)
    nurse_address = models.CharField(max_length=200)

    def __str__(self):
        return self.nurse_name


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    department_description = models.CharField(max_length=200)

    def __str__(self):
        return self.department_name


class DoctorDepartment(models.Model):
    doctor_department_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class NurseDepartment(models.Model):
    nurse_department_id = models.AutoField(primary_key=True)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class DoctorDepartmentHospital(models.Model):
    doctor_department_hospital_id = models.AutoField(primary_key=True)
    doctor_department = models.ForeignKey(DoctorDepartment, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)


class NurseDepartmentHospital(models.Model):
    nurse_department_hospital_id = models.AutoField(primary_key=True)
    nurse_department = models.ForeignKey(NurseDepartment, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)


class Bed(models.Model):
    bed_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    is_icu_bed = models.BooleanField()


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    patient_address = models.CharField(max_length=200)
    discharged = models.BooleanField()

    def __str__(self):
        return self.patient_name


class Appointments(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    duration = models.IntegerField()
    notes = models.TextField(blank=True)
