from django.contrib import admin
from django.urls import path
from newRule_app.views import RuleView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RuleView.as_view(), name="add_rule"),
]