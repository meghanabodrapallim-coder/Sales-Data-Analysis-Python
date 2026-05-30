# Interactive Sales Data Analysis System
import pandas as pd
import matplotlib.pyplot as plt

print("=== Interactive Sales Data Analysis System ===\n")

# Ask user how many products
num_products = int(input("How many products do you want to analyze? "))

# Empty lists to store data
products = []
sales = []

# Ask user to enter data
print("\nEnter product details:\n")
for i in range(num_products):
    print(f"Product {i+1}:")
    product_name = input("  Enter Product Name: ")
    product_sales = int(input("  Enter Sales Amount (₹): "))
    products.append(product_name)
    sales.append(product_sales)
    print()

# Create DataFrame
data = pd.DataFrame({
    'Product': products,
    'Sales': sales
})

# Display entered data
print("\n=== Sales Data You Entered ===")
print(data)
print()

# Calculate total sales
total_sales = data['Sales'].sum()
print(f"Total Sales: ₹{total_sales}")

# Calculate average sales
average_sales = data['Sales'].mean()
print(f"Average Sales: ₹{average_sales:.2f}")

# Find best-selling product
best_product = data.loc[data['Sales'].idxmax()]
print(f"Best-Selling Product: {best_product['Product']} (₹{best_product['Sales']})")

# Find worst-selling product
worst_product = data.loc[data['Sales'].idxmin()]
print(f"Worst-Selling Product: {worst_product['Product']} (₹{worst_product['Sales']})")

print("\nGenerating graph...")

# Create visualization
plt.figure(figsize=(10, 6))
plt.bar(data['Product'], data['Sales'], color='skyblue')
plt.xlabel('Products')
plt.ylabel('Sales (₹)')
plt.title('Interactive Sales Data Analysis')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("Graph displayed successfully!")
print("\nThank you for using Sales Data Analysis System!")