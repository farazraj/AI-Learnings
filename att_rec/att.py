from zk import ZK
import pandas as pd

def export_attendance_to_excel(ip: str, port: int = 4370, filename: str = "attendance.xlsx"):
    zk = ZK(ip, port=port, timeout=5)
    conn = None
    try:
        conn = zk.connect()
        conn.disable_device()
        print("✅ Connected to device")

        # Fetch attendance
        attendance = conn.get_attendance()

        if not attendance:
            print("⚠️ No attendance data found.")
            return

        # Convert all attributes of each record into dict
        records = [att.__dict__ for att in attendance]

        # Put into DataFrame
        df = pd.DataFrame(records)

        # Save to Excel
        df.to_excel(filename, index=False)
        print(f"📂 Attendance exported to {filename} with columns: {list(df.columns)}")

    except Exception as e:
        print("❌ Process failed:", e)
    finally:
        if conn:
            conn.enable_device()
            conn.disconnect()


export_attendance_to_excel("192.168.0.200", filename="logs.xlsx")
