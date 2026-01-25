from django.contrib import admin
from django.urls import path
from contact.views import contact_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/contact/", contact_api),
]
