import pytest
from mixer.backend.django import mixer

from core.models import Department


@pytest.fixture
def employee_payload():
    department = mixer.blend(Department)
    return {
        'name': 'Alicia',
        'email': 'test@example.com',
        'department': department.name
    }


@pytest.fixture
def department_payload():
    return {
        'name': 'Technology',
    }
