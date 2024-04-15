from django.urls import path
from med.views import (
    HomeView,
    AboutView,
    DoctorView,
    PatientView,
    patient_create,
    doctor_view,
    Acceptance,
    LoginView,
    UserLogoutView,
    ServicesView,
    DepartmentView, Contact,
)

app_name = "med"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("about/", AboutView.as_view(), name="about"),
    path("doctor/", DoctorView.as_view(), name="doctor"),
    path("bemor/", PatientView.as_view(), name="bemor"),
    path("patient/create/", patient_create, name="create-patient"),
    path("appoint/", doctor_view, name="appoint"),
    path("acceptance/list/", Acceptance.as_view(), name="acceptance"),
    path("services/", ServicesView.as_view(), name="services"),
    path("medilab/department/", DepartmentView.as_view(), name="department"),
    path('medilab/contact/', Contact.as_view(), name="contact"),
]
