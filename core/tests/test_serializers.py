import pytest

from mixer.backend.django import mixer
from core.models import Employee, Department
from core.serializers import EmployeeSerializer, DepartmentSerializer

pytestmark = pytest.mark.django_db


def test_employee_serializer_contains_expected_fields():
    employee = mixer.blend(Employee)

    serializer = EmployeeSerializer(instance=employee)
    data = serializer.data

    assert set(data.keys()) == {'id', 'name', 'email', 'department'}


def test_employee_field_content():
    employee = mixer.blend(Employee)

    serializer = EmployeeSerializer(instance=employee)
    data = serializer.data

    assert data['id'] == employee.id
    assert data['name'] == employee.name
    assert data['email'] == employee.email
    assert data['department'] == employee.department.name


def test_department_serializer_contains_expected_fields():
    department = mixer.blend(Employee)

    serializer = DepartmentSerializer(instance=department)
    data = serializer.data

    assert set(data.keys()) == {'id', 'name'}


def test_department_field_content():
    department = mixer.blend(Department)

    serializer = DepartmentSerializer(instance=department)
    data = serializer.data

    assert data['id'] == department.id
    assert data['name'] == department.name