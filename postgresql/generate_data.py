# generate_data.py
import uuid
import random
import json
from datetime import datetime, timedelta
from faker import Faker

faker = Faker()

# Helper function to generate random datetime
def random_timestamp():
    return (datetime.now() - timedelta(days=random.randint(0, 1000))).isoformat()

# Generate users
users = []
for _ in range(5):
    user_id = str(uuid.uuid4())
    users.append({
        "_id": user_id,
        "password": faker.password(length=12),
        "last_login": random_timestamp(),
        "is_superuser": False,
        "email": faker.unique.email(),
        "is_staff": False,
        "is_active": True,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    })

# Generate profiles
profiles = []
for user in users:
    profiles.append({
        "_id": str(uuid.uuid4()),
        "_user_id": user["_id"],
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    })

# Generate categories
categories = []
for _ in range(5):
    categories.append({
        "_id": str(uuid.uuid4()),
        "name": faker.word(),
        "parent_id": None,
        "category_type": random.choice(["income", "expense"]),
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    })

# Generate transactions
transactions = []
for _ in range(20):
    transactions.append({
        "_id": str(uuid.uuid4()),
        "_user_id": random.choice(users)["_id"],
        "date": random_timestamp(),
        "amount": round(random.uniform(10, 1000), 2),
        "_category_id": random.choice(categories)["_id"] if random.choice([True, False]) else None,
        "description": faker.text(max_nb_chars=50),
        "tag": faker.word(),
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    })

# Generate tokens
tokens = []
for user in users:
    tokens.append({
        "_id": str(uuid.uuid4()),
        "_user_id": user["_id"],
        "is_active": True,
        "token": faker.uuid4(),
        "expired_at": (datetime.now() + timedelta(days=30)).isoformat(),
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    })

# Pack everything
data = {
    "users": users,
    "profiles": profiles,
    "categories": categories,
    "transactions": transactions,
    "tokens": tokens
}

# Save to JSON
with open('generated_data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("✅ Data generated and saved to generated_data.json")

