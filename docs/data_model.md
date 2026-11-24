# CommerceFlow Source Data Model

This document defines the source-level data model for the CommerceFlow
e-commerce analytics platform.

## 1. Customers

Grain: One row per customer.

| Column | Description |
|---|---|
| customer_id | Unique customer identifier |
| first_name | Customer first name |
| last_name | Customer last name |
| email | Customer email address |
| signup_date | Date the customer registered |
| country | Customer country |
| state | Customer state or region |
| customer_segment | Customer segment |
| updated_at | Last time the customer record changed |

Primary Key: `customer_id`

---

## 2. Products

Grain: One row per product.

| Column | Description |
|---|---|
| product_id | Unique product identifier |
| product_name | Product name |
| category | Product category |
| brand | Product brand |
| unit_price | Current product price |
| is_active | Whether the product is currently active |
| created_at | Product creation timestamp |
| updated_at | Last product update timestamp |

Primary Key: `product_id`

---

## 3. Orders

Grain: One row per order.

| Column | Description |
|---|---|
| order_id | Unique order identifier |
| customer_id | Customer who placed the order |
| order_timestamp | When the order was created |
| order_status | Current order status |
| shipping_country | Shipping destination country |
| shipping_state | Shipping destination state |
| subtotal | Total before tax and shipping |
| tax_amount | Tax charged |
| shipping_amount | Shipping cost |
| order_total | Final order amount |
| updated_at | Last order update timestamp |

Primary Key: `order_id`

Foreign Key: `customer_id -> customers.customer_id`

---

## 4. Order Items

Grain: One row per product within an order.

| Column | Description |
|---|---|
| order_item_id | Unique order item identifier |
| order_id | Associated order |
| product_id | Purchased product |
| quantity | Number of units purchased |
| unit_price | Product price at purchase time |
| discount_amount | Discount applied |
| line_total | Final amount for the line item |

Primary Key: `order_item_id`

Foreign Keys:

- `order_id -> orders.order_id`
- `product_id -> products.product_id`

---

## 5. Payments

Grain: One row per payment transaction.

| Column | Description |
|---|---|
| payment_id | Unique payment identifier |
| order_id | Associated order |
| payment_timestamp | When payment was attempted |
| payment_method | Payment method |
| payment_status | Payment result |
| amount | Payment amount |

Primary Key: `payment_id`

Foreign Key: `order_id -> orders.order_id`

---

## 6. Events

Grain: One row per customer behavioral event.

| Column | Description |
|---|---|
| event_id | Unique event identifier |
| customer_id | Customer performing the action |
| session_id | Website/app session identifier |
| event_timestamp | When the event occurred |
| event_type | Type of event |
| product_id | Product associated with the event, when applicable |
| device_type | Device used |
| traffic_source | Source of the visitor |

Primary Key: `event_id`

Foreign Keys:

- `customer_id -> customers.customer_id`
- `product_id -> products.product_id`

Example event types:

- `page_view`
- `product_view`
- `add_to_cart`
- `checkout_started`
- `purchase`