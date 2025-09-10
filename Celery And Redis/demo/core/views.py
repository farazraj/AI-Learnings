from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from celery.result import AsyncResult
from .tasks import long_task

def start_long_task(request):
    # pass ?s=10 to change length
    s = int(request.GET.get("s", 5))
    result = long_task.delay(s)
    return JsonResponse({"task_id": result.id, "status": "STARTED"})

def task_status(request, task_id):
    ar = AsyncResult(task_id)
    info = ar.info if hasattr(ar, "info") else None
    return JsonResponse({
        "task_id": task_id,
        "status": ar.status,
        "result": ar.result,
        "info": info
    })


from .models import Submission, ContactMessage
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubmissionForm
import pandas as pd
from .tasks import process_submission, process_contact_message, process_bulk_contacts, process_bulk_contacts_ws

def submit_name(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.processed = False
            submission.save()
            process_submission.delay(submission.id)  # send async
            messages.success(request, "Your submission is being processed. Refresh to see status.")
            return redirect("submit-name")
    else:
        form = SubmissionForm()

    submissions = Submission.objects.all()
    return render(request, "submit_name.html", {"form": form, "submissions": submissions})



def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            contact = ContactMessage.objects.create(
                name=name, email=email, message=message, processed=False
            )
            process_contact_message.delay(contact.id)  # async task
            messages.success(request, "Your message is being processed.")
            return redirect("contact")
        else:
            messages.error(request, "All fields are required!")

    messages_list = ContactMessage.objects.all().order_by("-id")
    return render(request, "contact.html", {"messages_list": messages_list})


def bulk_upload_view(request):
    if request.method == "POST":
        csv_file = request.FILES.get("csv_file")
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "Please upload a CSV file.")
            return redirect("bulk_upload")

        # Read CSV with pandas
        df = pd.read_csv(csv_file)

        # Ensure required columns exist
        required_cols = {"name", "email", "message"}
        if not required_cols.issubset(df.columns):
            messages.error(request, "CSV must contain name, email, message columns.")
            return redirect("bulk_upload")

        # Convert to list of dicts
        contacts_data = df.to_dict(orient="records")

        #Option A : Send task to Celery | Normal async process 
        # process_bulk_contacts.delay(contacts_data)
        
        
        # Option B: async processing + real-time WebSocket updates
        process_bulk_contacts_ws.delay(contacts_data)
        
        messages.success(request, f"{len(contacts_data)} contacts are being processed.")
        return redirect("bulk_upload")

    return render(request, "bulk_upload.html")