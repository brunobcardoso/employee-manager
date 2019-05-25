from django.urls import path

from core import views

urlpatterns = [
    path(
        'employee/', views.EmployeeList.as_view(),
        name='employee-list'
    ),
    path(
        'employee/<int:pk>/', views.EmployeeDetail.as_view(),
        name='employee-detail'
    ),
    path(
        'department/', views.DepartmentList.as_view(),
        name='department-list'
    ),
    path(
        'department/<int:pk>/', views.DepartmentDetail.as_view(),
        name='department-detail'
    ),
]
