from django.contrib import admin

from med.models import Count, Patient, Disease, Doctor, Icon, PatientDoctor, Department


@admin.register(Count)
class CountAdmin(admin.ModelAdmin):
    list_display = ("doctor",)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("fullname",)


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("fullname",)


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(PatientDoctor)
class PatientDoctorAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("title",)
