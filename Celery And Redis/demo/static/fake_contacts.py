import pandas as pd

data = []
for i in range(1, 101):
    data.append({
        "name": f"User{i}",
        "email": f"user{i}@example.com",
        "message": f"Hello, I am User{i}"
    })

df = pd.DataFrame(data)
df.to_csv("sample_contacts.csv", index=False)
