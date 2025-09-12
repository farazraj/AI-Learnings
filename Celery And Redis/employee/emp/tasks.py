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


@shared_task
def delete_all_employees():
    from time import sleep
    channel_layer = get_channel_layer()

    # Notify that task has started
    async_to_sync(channel_layer.group_send)(
        "employee_status",
        {"type": "send_status", "message": "🚀 Task started: Deleting employees..."}
    )

    sleep(1)

    total = Employee.objects.count()
    async_to_sync(channel_layer.group_send)(
        "employee_status",
        {"type": "send_status", "message": f"Found {total} employees to delete."}
    )

    sleep(1)

    deleted_count = 0
    # Use iterator() to avoid prefetching the entire queryset
    for emp in Employee.objects.iterator():
        emp.delete()
        deleted_count += 1

        # Send progress update
        async_to_sync(channel_layer.group_send)(
            "employee_status",
            {"type": "send_status", "message": f"Deleted {deleted_count}/{total} employees"}
        )

        sleep(1)  # 🔹 artificial delay so you see updates happening

    async_to_sync(channel_layer.group_send)(
        "employee_status",
        {"type": "send_status", "message": f"✅ Finished deleting {deleted_count} employees!"}
    )

    return f"Deleted {deleted_count} employees"
