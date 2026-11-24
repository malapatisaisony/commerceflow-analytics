from pathlib import Path
import csv
import random
from datetime import datetime, timedelta

from faker import Faker


fake = Faker()
Faker.seed(42)
random.seed(42)


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"


PRODUCT_CATEGORIES = {
    "Electronics": [
        "Wireless Headphones",
        "Bluetooth Speaker",
        "Smart Watch",
        "USB-C Hub",
        "Webcam",
    ],
    "Home": [
        "Desk Lamp",
        "Coffee Maker",
        "Storage Basket",
        "Throw Pillow",
        "Water Bottle",
    ],
    "Clothing": [
        "T-Shirt",
        "Hoodie",
        "Jeans",
        "Jacket",
        "Sweater",
    ],
    "Accessories": [
        "Backpack",
        "Wallet",
        "Sunglasses",
        "Cap",
        "Phone Case",
    ],
}

CUSTOMER_SEGMENTS = [
    "new",
    "regular",
    "loyal",
]


def random_datetime(start_date: datetime, end_date: datetime) -> datetime:
    """Return a random datetime between two dates."""
    difference = end_date - start_date
    random_seconds = random.randint(0, int(difference.total_seconds()))
    return start_date + timedelta(seconds=random_seconds)


def generate_customers(count: int = 1000) -> list[dict]:
    customers = []

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2026, 11, 24)

    for customer_number in range(1, count + 1):
        signup_datetime = random_datetime(start_date, end_date)

        first_name = fake.first_name()
        last_name = fake.last_name()

        customer = {
            "customer_id": f"CUST-{customer_number:06d}",
            "first_name": first_name,
            "last_name": last_name,
            "email": fake.unique.email(),
            "signup_date": signup_datetime.date().isoformat(),
            "country": "United States",
            "state": fake.state_abbr(),
            "customer_segment": random.choice(CUSTOMER_SEGMENTS),
            "updated_at": signup_datetime.isoformat(),
        }

        customers.append(customer)

    return customers


def generate_products() -> list[dict]:
    products = []

    product_number = 1

    for category, product_names in PRODUCT_CATEGORIES.items():
        for product_name in product_names:
            created_at = random_datetime(
                datetime(2023, 1, 1),
                datetime(2025, 12, 31),
            )

            product = {
                "product_id": f"PROD-{product_number:04d}",
                "product_name": product_name,
                "category": category,
                "brand": fake.company(),
                "unit_price": round(random.uniform(10.00, 500.00), 2),
                "is_active": random.choice([True, True, True, False]),
                "created_at": created_at.isoformat(),
                "updated_at": created_at.isoformat(),
            }

            products.append(product)
            product_number += 1

    return products


def write_csv(filename: str, rows: list[dict]) -> None:
    if not rows:
        return

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    file_path = DATA_DIR / filename

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {file_path}")


def main() -> None:
    customers = generate_customers()
    products = generate_products()

    write_csv("customers.csv", customers)
    write_csv("products.csv", products)


if __name__ == "__main__":
    main()