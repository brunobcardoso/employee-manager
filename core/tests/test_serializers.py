import pytest

from mixer.backend.django import mixer
from core.models import Employee
from core.serializers import EmployeeSerializer


@pytest.mark.django_db
def test_employee_serializer_contains_expected_fields():
    employee = mixer.blend(Employee)

    serializer = EmployeeSerializer(instance=employee)
    data = serializer.data

    assert set(data.keys()) == {'id', 'name', 'email', 'department'}


@pytest.mark.django_db
def test_employee_field_content():
    employee = mixer.blend(Employee)

    serializer = EmployeeSerializer(instance=employee)
    data = serializer.data

    assert data['id'] == employee.id
    assert data['name'] == employee.name
    assert data['email'] == employee.email
    assert data['department'] == employee.department.name
