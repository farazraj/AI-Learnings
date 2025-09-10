from celery import shared_task
from .models import Submission, ContactMessage
import time

@shared_task(bind=True)
def long_task(self, seconds=5):
    """A pretend-heavy job that reports progress."""
    total = seconds
    for i in range(total):
        time.sleep(1)                # simulate work
        self.update_state(state="PROGRESS", meta={"current": i+1, "total": total})
    return {"message": "done", "seconds": seconds}

@shared_task
def process_submission(submission_id):
    time.sleep(5)  # simulate heavy work
    submission = Submission.objects.get(id=submission_id)
    submission.processed = True
    submission.save()
    return f"Processed {submission.name}"

@shared_task
def process_contact_message(contact_id):
    time.sleep(5)  # simulate delay for sending email
    contact = ContactMessage.objects.get(id=contact_id)
    contact.processed = True
    contact.save()
    return f"Processed contact from {contact.name}"




#this is without using django channels + Websocket
import pandas as pd
@shared_task
def process_bulk_contacts(contacts_data):
    """
    contacts_data = list of dicts [{'name':..., 'email':..., 'message':...}]
    """
    df = pd.DataFrame(contacts_data)

    for _, row in df.iterrows():
        obj = ContactMessage.objects.create(
            name=row["name"],
            email=row["email"],
            message=row["message"],
            processed=False
        )
        # simulate processing (e.g., sending email)
        time.sleep(1)
        obj.processed = True
        obj.save()

    return f"Processed {len(df)} contacts"


#This is using django channels + Websocket

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def process_bulk_contacts_ws(contacts_data):
    """
    Bulk contact processing + WebSocket status updates
    """
    df = pd.DataFrame(contacts_data)
    channel_layer = get_channel_layer()
    total = len(df)

    for i, row in df.iterrows():
        obj = ContactMessage.objects.create(
            name=row["name"],
            email=row["email"],
            message=row["message"],
            processed=False
        )
        time.sleep(1)  # simulate processing
        obj.processed = True
        obj.save()

        # send progress update
        progress = f"Processed {i+1}/{total} contacts"
        async_to_sync(channel_layer.group_send)(
            "bulk_upload_status",
            {"type": "send_status", "message": progress}
        )

    # final message
    async_to_sync(channel_layer.group_send)(
        "bulk_upload_status",
        {"type": "send_status", "message": f"✅ Finished processing {total} contacts!"}
    )

    return f"Processed {total} contacts"





