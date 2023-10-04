import json
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Generate mock data for 10 users
users = []
for _ in range(10):
    name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    password = fake.password(length=8)  # Generate a random password
    is_superuser = random.choice([True, False])
    is_support = random.choice([True, False])
    is_manager = random.choice([True, False])
    is_commercial = random.choice([True, False])

    user_data = {
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "password": password,
        "is_superuser": is_superuser,
        "is_support": is_support,
        "is_manager": is_manager,
        "is_commercial": is_commercial,
    }
    users.append(user_data)

# Save the mock data to a JSON file
with open("mocks/mock_users.json", "w") as json_file:
    json.dump(users, json_file, indent=4)

print("Mock data has been generated and saved to mock_users.json.")