import pandas as pd
import matplotlib.pyplot as plt

def visualize_data():

    df = pd.read_csv("data/sales_data.csv")

    # Line Chart
    plt.figure(figsize=(8,5))
    plt.plot(df["Month"], df["Sales"], marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.show()

    # Bar Chart
    region_sales = df.groupby("Region")["Sales"].sum()

    plt.figure(figsize=(8,5))
    plt.bar(region_sales.index, region_sales.values)
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.show()

    # Pie Chart
    product_sales = df.groupby("Product")["Sales"].sum()

    plt.figure(figsize=(6,6))
    plt.pie(
        product_sales.values,
        labels=product_sales.index,
        autopct="%1.1f%%"
    )

    plt.title("Product Sales Distribution")
    plt.show()

    # Insights
    print("\n===== DATA INSIGHTS =====")
    print("Highest Sales Month:", df.loc[df["Sales"].idxmax(), "Month"])
    print("Highest Sales Region:", region_sales.idxmax())
    print("Top Product:", product_sales.idxmax())