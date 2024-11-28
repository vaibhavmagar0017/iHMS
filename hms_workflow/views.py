from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import *
from .models import *


# Hospital GET, POST, PATCH, DELETE

class HospitalListAPIView(APIView):
    def get(self, request):
        hospitals = Hospital.objects.all()
        serializer = HospitalSerializer(hospitals, many=True)
        return Response(serializer.data)


class HospitalCreateAPIView(APIView):
    def post(self, request):
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HospitalUpdateAPIView(APIView):
    def patch(self, request, pk):
        try:
            hospital = Hospital.objects.get(pk=pk)
        except Hospital.DoesNotExist:
            return Response({"message": "Hospital not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = HospitalSerializer(hospital, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HospitalDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            hospital = Hospital.objects.get(pk=pk)
        except Hospital.DoesNotExist:
            return Response({"message": "Hospital not found"}, status=status.HTTP_404_NOT_FOUND)

        hospital.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Doctor GET, POST, PATCH, DELETE

class DoctorListAPIView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)


class DoctorCreateAPIView(APIView):
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorUpdateAPIView(APIView):
    def patch(self, request, pk):
        try:
            doctors = Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return Response({"message": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DoctorSerializer(doctors, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            doctors = Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return Response({"message": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

        doctors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Nurse GET, POST, PATCH, DELETE

class NurseListAPIView(APIView):
    def get(self, request):
        nurse = Nurse.objects.all()
        serializer = NurseSerializer(nurse, many=True)
        return Response(serializer.data)


class NurseCreateAPIView(APIView):
    def post(self, request):
        serializer = NurseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NurseUpdateAPIView(APIView):
    def patch(self, request, pk):
        try:
            nurse = Nurse.objects.get(pk=pk)
        except Nurse.DoesNotExist:
            return Response({"message": "Nurse not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NurseSerializer(nurse, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NurseDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            nurse = Nurse.objects.get(pk=pk)
        except Nurse.DoesNotExist:
            return Response({"message": "nurse not found"}, status=status.HTTP_404_NOT_FOUND)

        nurse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Department GET, POST, PATCH, DELETE

class DepartmentListAPIView(APIView):
    def get(self, request):
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data)


class DepartmentCreateAPIView(APIView):
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentUpdateAPIView(APIView):
    def patch(self, request, pk):
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Response({"message": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentSerializer(department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Response({"message": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

        department.delete()
        return Response({"message": "Department delete Successfully"}, status=status.HTTP_204_NO_CONTENT)
