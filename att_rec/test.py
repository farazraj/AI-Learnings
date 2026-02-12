from zk import ZK, const

def test_device(ip="192.168.0.200", port=4370):
    zk = ZK(ip, port=port, timeout=5)
    conn = None
    try:
        conn = zk.connect()
        conn.disable_device()
        print("✅ Connected to device")

        # Fetch users
        users = conn.get_users()
        print("Total users:", len(users))

        # Fetch attendance
        attendance = conn.get_attendance()
        print("Total attendance records:", len(attendance))

        # Show first 5 attendance logs with all attributes
        for att in attendance[:5]:
            print(att.__dict__)

    except Exception as e:
        print("❌ Process failed:", e)
    finally:
        if conn:
            conn.enable_device()
            conn.disconnect()

test_device()
