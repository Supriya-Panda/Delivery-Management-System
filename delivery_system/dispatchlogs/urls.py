from django.urls import path
from .views import compliance_report

urlpatterns = [
    path("compliance-report/", compliance_report, name="compliance-report"),

]