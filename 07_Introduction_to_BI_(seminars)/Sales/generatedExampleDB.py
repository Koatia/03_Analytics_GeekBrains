import pandas as pd
import numpy as np

# Create a dummy dataset
np.random.seed(0)
dates = pd.date_range(start="2022-01-01", end=pd.Timestamp.today(), freq="ME")
divisions = ["Север", "Запад", "Восток"]
channels = ["B2C", "B2B", "Mobile Commerce"]
product_category = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Books"]
cash = ["Cash", "Non-Cash"]


data = []

# Generate planned sales with less fluctuation
base_planned_sales = {"B2C": 15000, "B2B": 20000, "Mobile Commerce": 18000}
k_divisions = {"Север": 0.2, "Запад": 0.3, "Восток": 0.5}
k_product_category = {
    "Electronics": 0.3,
    "Clothing": 0.25,
    "Home & Kitchen": 0.15,
    "Sports": 0.2,
    "Books": 0.1,
}
k_cash = {"Cash": 0.35, "Non-Cash": 0.65}

for date in dates:
    for division in divisions:
        for channel in channels:
            for product in product_category:
                k = np.random.randint(-25, 25) / 100 + 1
                for money in cash:
                    planned_sales = round(
                        base_planned_sales[channel]
                        * k_divisions[division]
                        * k_product_category[product]
                        * k_cash[money]
                    )
                    actual_sales = round(planned_sales * k)
                    if actual_sales < 0:
                        actual_sales = 0

                    data.append(
                        [
                            date,
                            division,
                            channel,
                            product,
                            money,
                            actual_sales,
                            planned_sales,
                        ]
                    )

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "Date",
        "Divisions",
        "Channels",
        "Product category",
        "Cash",
        "Actual Sales",
        "Planned Sales",
    ],
)

# Save to CSV
df.to_csv("ecommerce_sales_data.csv", index=False)

df.head()
