#!/usr/bin/env python3
import subprocess
import random
from datetime import datetime

# Connection string
CONN = "postgresql://appuser:dbuser123@localhost:5000/myapp"

# Product data with realistic pricing
products = [
    (1, "Classic Silk Blouse", 129.99),
    (2, "High-Waist Designer Jeans", 189.99),
    (3, "Italian Leather Handbag", 299.99),
    (4, "Floral Summer Dress", 89.99),
    (5, "Cashmere V-Neck Sweater", 149.99),
    (6, "Suede Ankle Boots", 179.99),
    (7, "Classic Trench Coat", 249.99),
    (8, "Designer Silk Scarf", 79.99),
    (9, "Black Cocktail Dress", 159.99),
    (10, "Premium White Sneakers", 119.99),
    (11, "Wool Blend Blazer", 199.99),
    (12, "Satin Evening Clutch", 69.99),
    (13, "Linen Wide-Leg Pants", 99.99),
    (14, "Leather Crossbody Bag", 139.99),
    (15, "Striped Cotton T-Shirt", 39.99),
    (16, "Denim Jacket", 129.99),
    (17, "Chelsea Leather Boots", 189.99),
    (18, "Cashmere Blend Scarf", 89.99),
    (19, "Slim Fit Chinos", 79.99),
    (20, "Leather Belt", 49.99)
]

print("Starting analytics data population...")
inserted_count = 0
skipped_count = 0

for product_id, product_name, price in products:
    print(f"\nProcessing Product {product_id}: {product_name} (${price})")
    
    for day in range(29, -1, -1):  # 30 days: 29 to 0
        # Generate realistic metrics based on price point
        # Higher priced items generally have fewer views but better conversion
        if price > 200:
            base_views = random.randint(80, 150)
            base_orders = random.randint(3, 8)
        elif price > 100:
            base_views = random.randint(120, 200)
            base_orders = random.randint(5, 12)
        else:
            base_views = random.randint(150, 250)
            base_orders = random.randint(8, 15)
        
        views = base_views
        orders = base_orders
        units_sold = orders
        revenue = round(orders * price, 2)
        conversion_rate = round((orders * 100.0) / views, 2)
        
        # Build SQL statement
        sql = f"""INSERT INTO product_performance_analytics 
                  (product_id, date, views, orders, revenue, units_sold, conversion_rate, created_at) 
                  VALUES ({product_id}, NOW() - INTERVAL '{day} days', {views}, {orders}, {revenue}, {units_sold}, {conversion_rate}, NOW()) 
                  ON CONFLICT (product_id, date) DO NOTHING;"""
        
        # Execute the SQL
        try:
            result = subprocess.run(
                ['psql', CONN, '-c', sql],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                if "INSERT 0 1" in result.stdout:
                    inserted_count += 1
                elif "INSERT 0 0" in result.stdout:
                    skipped_count += 1
            else:
                print(f"  Error on day {day}: {result.stderr.strip()}")
        
        except subprocess.TimeoutExpired:
            print(f"  Timeout on day {day}")
        except Exception as e:
            print(f"  Exception on day {day}: {str(e)}")
    
    print(f"  Completed product {product_id}")

print(f"\n{'='*60}")
print(f"Analytics population complete!")
print(f"Records inserted: {inserted_count}")
print(f"Records skipped (already exist): {skipped_count}")
print(f"{'='*60}")
