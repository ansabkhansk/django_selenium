from django.urls import path
from . import views

urlpatterns = [
    path("", views.state, name="state"),
    path("state/", views.state, name="state"),
    path("category/", views.category, name="category"),
    path("subcategory/", views.subcategory, name="subcategory"),
    path("jobs/", views.job, name="jobs"),
]
