from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from core.models import Employee
from core.serializers import EmployeeSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminUser,)


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminUser,)
