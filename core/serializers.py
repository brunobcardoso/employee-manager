from rest_framework import serializers

from core.models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Department.objects.all()
    )

    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'department')
