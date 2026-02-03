# PostgreSQL Database Setup - Complete

## Database Connection
- **Connection String**: `psql postgresql://appuser:dbuser123@localhost:5000/myapp`
- **Database**: myapp
- **User**: appuser
- **Port**: 5000

## Schema Tables Created

### 1. Users Table
- **Purpose**: Authentication and user management
- **Columns**: id, email, password_hash, full_name, role, created_at, updated_at
- **Data Inserted**: 1 admin user

### 2. Customers Table
- **Purpose**: Customer information management
- **Columns**: id, email, first_name, last_name, phone, address_line1, address_line2, city, state, postal_code, country, customer_since, lifetime_value, total_orders, created_at, updated_at
- **Data Inserted**: 5 customers (Sarah Johnson, Michael Brown, Emma Wilson, James Davis, Olivia Martinez)

### 3. Products Table
- **Purpose**: Product catalog
- **Columns**: id, sku, name, description, category, subcategory, brand, price, cost, currency, is_active, image_url, tags, created_at, updated_at
- **Data Inserted**: 10 products across categories (Clothing, Accessories, Footwear)
  - SKU-001: Classic White Tee ($29.99)
  - SKU-002: Slim Fit Denim Jeans ($79.99)
  - SKU-003: Leather Crossbody Bag ($149.99)
  - SKU-004: Running Sneakers ($99.99)
  - SKU-005: Silk Scarf ($59.99)
  - SKU-006: Wool Blend Coat ($199.99)
  - SKU-007: Designer Sunglasses ($129.99)
  - SKU-008: Cotton Hoodie ($49.99)
  - SKU-009: Ankle Boots ($139.99)
  - SKU-010: Statement Necklace ($89.99)

### 4. Orders Table
- **Purpose**: Order tracking and management
- **Columns**: id, order_number, customer_id, status, subtotal, tax, shipping_cost, discount_amount, total, currency, payment_method, payment_status, shipping_address_line1-country, notes, created_at, updated_at
- **Data Inserted**: 3 orders with various statuses (completed, shipped)

### 5. Order Items Table
- **Purpose**: Line items for each order
- **Columns**: id, order_id, product_id, inventory_id, quantity, unit_price, subtotal, size, color, created_at
- **Relationships**: Links orders to products and inventory

### 6. Inventory Table
- **Purpose**: Stock management by product variant
- **Columns**: id, product_id, size, color, quantity_available, quantity_reserved, reorder_level, warehouse_location, last_restocked, created_at, updated_at
- **Data Inserted**: 15+ inventory records with various sizes and colors for products
- **Warehouse Locations**: A-101 through J-1001

### 7. Discounts Table
- **Purpose**: Promotional codes and discounts
- **Columns**: id, code, description, discount_type, discount_value, min_purchase_amount, max_discount_amount, usage_limit, used_count, valid_from, valid_until, status, created_at, updated_at
- **Status**: Table created, ready for seed data

### 8. Analytics Daily Metrics Table
- **Purpose**: Daily aggregated analytics
- **Columns**: id, date, total_revenue, total_orders, average_order_value, new_customers, total_customers, conversion_rate, created_at
- **Status**: Table created, ready for 30 days of historical data

### 9. Product Performance Analytics Table
- **Purpose**: Product-level performance tracking
- **Columns**: id, product_id, date, views, orders, revenue, units_sold, conversion_rate, created_at
- **Status**: Table created, ready for historical performance data

## Database Setup Status

### ✅ Completed
- PostgreSQL server running on port 5000
- All core tables created with proper schema
- Users table populated (1 admin user)
- Customers table populated (5 customers)
- Products table populated (10 products)
- Inventory table populated (15+ variants with sizes/colors)
- Orders table populated (3 orders)
- All foreign key relationships established
- All indexes and constraints in place

### 🔄 Remaining Items (For Backend Implementation)
The following seed data should be added via backend initialization or data population scripts:

1. **Additional Orders & Order Items**: Need 20-30 more orders with order_items to provide realistic dashboard data
2. **Discounts**: 5-10 discount codes with various types (percentage, fixed amount)
3. **Analytics Daily Metrics**: 30 days of historical daily metrics for charts
4. **Product Performance Analytics**: Historical performance data for products over 30 days

## Database Architecture

### Relationships
- `customers` → `orders` (one-to-many)
- `orders` → `order_items` (one-to-many)
- `products` → `order_items` (one-to-many)
- `products` → `inventory` (one-to-many)
- `inventory` → `order_items` (one-to-many via inventory_id)
- `products` → `product_performance_analytics` (one-to-many)

### Key Features
- Cascade deletes on customer → orders → order_items
- Unique constraints on email, SKU, order_number
- Default values for timestamps, status fields
- Proper decimal precision for financial data
- Support for multi-variant inventory (size, color)

## Next Steps for Backend

1. **Implement data population endpoints** to add remaining orders, discounts, and analytics
2. **Create stored procedures** for common operations (order placement, inventory updates)
3. **Implement triggers** for automatic analytics calculation
4. **Add indexes** on frequently queried columns (status, created_at, category)
5. **Create views** for common dashboard queries

## Verification Commands

Check table row counts:
```sql
SELECT 'users' as table_name, COUNT(*) as row_count FROM users
UNION ALL
SELECT 'customers', COUNT(*) FROM customers
UNION ALL
SELECT 'products', COUNT(*) FROM products
UNION ALL
SELECT 'inventory', COUNT(*) FROM inventory
UNION ALL
SELECT 'orders', COUNT(*) FROM orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM order_items;
```

View all tables:
```sql
\dt
```

Describe specific table:
```sql
\d table_name
```
