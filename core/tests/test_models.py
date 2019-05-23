import pytest

from core.models import Department


@pytest.mark.django_db
def test_department_creation():
    department = Department.objects.create(
        name='Technology'
    )

    assert isinstance(department, Department)
    assert department.__str__() == 'Technology'
    assert Department.objects.exists()

