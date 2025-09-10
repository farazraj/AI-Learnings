from django.urls import path
from .views import start_long_task, task_status, submit_name, contact_view, bulk_upload_view

urlpatterns = [
   path("task/start", start_long_task),
   path("task/status/<str:task_id>", task_status),
   path("submit/", submit_name, name="submit-name"),
   path("contact/", contact_view, name="contact"),
   path("bulk-upload/", bulk_upload_view, name="bulk_upload"),
]