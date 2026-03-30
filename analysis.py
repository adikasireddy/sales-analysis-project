import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Load Data
file_path = r"C:\Users\ASUS\OneDrive\Desktop\data analysis\python\sales_data.csv"

try:
    data = pd.read_csv(file_path)
    print("✅ Data Loaded Successfully")
    print("Columns:", data.columns)
except Exception as e:
    print("❌ Error loading file:", e)
    raise SystemExit

# Remove unwanted columns
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

# Convert data types
data['OrderDate'] = pd.to_datetime(data['OrderDate'], errors='coerce')
data['Revenue'] = pd.to_numeric(data['Revenue'], errors='coerce')

# Drop missing values
data = data.dropna()

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# 4. Analysis & Visualization

#  Daily Revenue Trend (Professional)
daily_sales = data.groupby('OrderDate')['Revenue'].sum().sort_index()

plt.figure(figsize=(10,5))
plt.plot(daily_sales.index, daily_sales.values, marker='o')

plt.title("Daily Revenue Trend", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Revenue")

plt.grid()
plt.xticks(rotation=40)
plt.tight_layout()

plt.savefig(f"{output_folder}/daily_sales.png")
plt.show()

print("📈 Daily revenue chart saved")


#  Revenue by Product (Professional)
product_sales = data.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
bars = plt.bar(product_sales.index, product_sales.values)

plt.title("Revenue by Product", fontsize=14)
plt.xlabel("Product")
plt.ylabel("Total Revenue")

# Add values on bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval)}',
             ha='center', va='bottom')

plt.grid(axis='y')
plt.tight_layout()

plt.savefig(f"{output_folder}/product_sales.png")
plt.show()

print("📊 Product revenue chart saved")


#  Revenue by Region (Professional)
region_sales = data.groupby('Region')['Revenue'].sum()

plt.figure(figsize=(6,6))

plt.pie(
    region_sales.values,
    labels=region_sales.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Revenue Distribution by Region", fontsize=14)
plt.tight_layout()

plt.savefig(f"{output_folder}/region_sales.png")
plt.show()

print("🥧 Region revenue chart saved")


#  Top 5 Products (Advanced Chart)
top_products = product_sales.head(5)

plt.figure(figsize=(8,5))
bars = plt.bar(top_products.index, top_products.values)

plt.title("Top 5 Products by Revenue", fontsize=14)
plt.xlabel("Product")
plt.ylabel("Revenue")

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval)}',
             ha='center', va='bottom')

plt.tight_layout()
plt.show()

# 5. Business Insights
print("\n🔍 BUSINESS INSIGHTS:")

# Top product
top_product = product_sales.idxmax()
print(f"🏆 Best-selling product: {top_product}")

# Top region
top_region = region_sales.idxmax()
print(f"🌍 Best-performing region: {top_region}")

# Total revenue
total_revenue = data['Revenue'].sum()
print(f"💰 Total Revenue: ₹{total_revenue:,}")

# Average daily revenue
avg_sales = daily_sales.mean()
print(f"📅 Average Daily Revenue: ₹{avg_sales:.2f}")