from celery import shared_task
from emp.models import Employee
import time
import pandas as pd
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@shared_task
def process_bulk_employee(emp_data):
    """
    Bulk contact processing + WebSocket status updates
    """
    df = pd.DataFrame(emp_data)
    channel_layer = get_channel_layer()
    total = len(df)

    for i, row in df.iterrows():
        obj = Employee.objects.create(
            name=row["name"],
            phone=row["phone"],
        )
        time.sleep(1)
        obj.save()

        # send progress update
        progress = f"Processed {i+1}/{total} Employees"
        async_to_sync(channel_layer.group_send)(
            "bulk_upload_status",
            {"type": "send_status", "message": progress}
        )

    # final message
    async_to_sync(channel_layer.group_send)(
        "bulk_upload_status",
        {"type": "send_status", "message": f"✅ Finished processing {total} Employees!"}
    )

    return f"Processed {total} Employees"