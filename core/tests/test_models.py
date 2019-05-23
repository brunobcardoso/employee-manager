import pytest

from mixer.backend.django import mixer
from core.models import Department, Employee

pytestmark = pytest.mark.django_db


def test_department_creation():

    department = mixer.blend(Department, name='Technology')

    assert isinstance(department, Department)
    assert department.__str__() == 'Technology'
    assert Department.objects.exists()


def test_employee_creation():

    employee = mixer.blend(Employee, name='John Smith')

    assert isinstance(employee, Employee)
    assert employee.__str__() == 'John Smith'
    assert Employee.objects.exists()
