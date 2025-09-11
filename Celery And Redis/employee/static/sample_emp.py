import pandas as pd

data = []
base_number = 9876500000  # starting mobile number

for i in range(1, 101):
    data.append({
        "name": f"User{i}",
        "phone": str(base_number + i)  # generates unique 10-digit phone numbers
    })

df = pd.DataFrame(data)
df.to_csv("sample_employees.csv", index=False)
