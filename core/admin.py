from django.contrib import admin

from core.models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'created_at', 'updated_at')
    list_filter = ('department', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'department__name', )


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)

admin.site.site_header = 'Employee Manager Admin Panel'
admin.site.index_title = 'Services Manager'
admin.site.site_title = 'Employee Manager Admin Panel'
