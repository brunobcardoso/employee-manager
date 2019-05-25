import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status

from core.models import Employee

pytestmark = pytest.mark.django_db


def test_list_employees(admin_client):
    mixer.cycle(3).blend(Employee)
    response = admin_client.get(reverse('employee-list'))
    assert response.status_code == status.HTTP_200_OK


def test_create_employee(admin_client, employee_payload):
    response = admin_client.post(reverse('employee-list'), employee_payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert Employee.objects.count() == 1


def test_delete_employee(admin_client):
    employee = mixer.blend(Employee)
    response = admin_client.delete(
        reverse('employee-detail', kwargs={'pk': employee.pk}))
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_update_employee(admin_client, employee_payload):
    employee = mixer.blend(Employee)
    response = admin_client.put(
        reverse('employee-detail', kwargs={'pk': employee.pk}),
        data=employee_payload,
        content_type='application/json'
    )
    del response.json()['id']
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == employee_payload


def test_patch_employee(admin_client):
    employee = mixer.blend(Employee)
    data = {'name': 'Alicia'}
    response = admin_client.patch(
        reverse('employee-detail', kwargs={'pk': employee.pk}), data=data,
        content_type='application/json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == data['name']
