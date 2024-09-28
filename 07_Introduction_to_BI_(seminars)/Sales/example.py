import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the generated CSV file
df = pd.read_csv('ecommerce_sales_data.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Aggregate data for plotting
monthly_sales = df.groupby(['Date', 'Segment']).agg({'Actual Sales': 'sum', 'Planned Sales': 'sum'}).reset_index()
quarterly_sales = df.groupby([pd.Grouper(key='Date', freq='Q'), 'Segment']).agg({'Actual Sales': 'sum', 'Planned Sales': 'sum'}).reset_index()
category_sales = df.groupby(['Segment', 'Product Type']).agg({'Actual Sales': 'sum', 'Planned Sales': 'sum'}).reset_index()
top_products_sales = df.groupby(['Product Type', 'Segment']).agg({'Actual Sales': 'sum', 'Planned Sales': 'sum'}).reset_index().nlargest(5, 'Actual Sales')
cumulative_sales = df.groupby(['Date', 'Segment']).agg({'Actual Sales': 'sum', 'Planned Sales': 'sum'}).groupby(level=1).cumsum().reset_index()

# Plotting
fig, axes = plt.subplots(3, 2, figsize=(14, 18))
fig.suptitle('E-Commerce Sales Dashboard', fontsize=16)

# Card 1: Total Sales
total_sales = df['Actual Sales'].sum()
axes[0, 0].text(0.5, 0.5, f"Total Sales\n{total_sales:,.0f} ₽",
                horizontalalignment='center', verticalalignment='center',
                fontsize=24, bbox=dict(facecolor='skyblue', alpha=0.5))
axes[0, 0].axis('off')

# Card 2: Total Plan
total_plan = df['Planned Sales'].sum()
axes[0, 1].text(0.5, 0.5, f"Total Plan\n{total_plan:,.0f} ₽",
                horizontalalignment='center', verticalalignment='center',
                fontsize=24, bbox=dict(facecolor='lightgreen', alpha=0.5))
axes[0, 1].axis('off')

# Adding the third card separately
achievement = (total_sales / total_plan) * 100
fig.add_subplot(3, 2, 3).text(0.5, 0.5, f"Achievement\n{achievement:.2f}%",
                              horizontalalignment='center', verticalalignment='center',
                              fontsize=24, bbox=dict(facecolor='lightcoral', alpha=0.5))
fig.add_subplot(3, 2, 3).axis('off')

# Graph 1: Monthly Sales by Segment
for segment in df['Segment'].unique():
    segment_data = monthly_sales[monthly_sales['Segment'] == segment]
    axes[1, 0].plot(segment_data['Date'], segment_data['Actual Sales'], label=f'Actual Sales {segment}', marker='o')
    axes[1, 0].plot(segment_data['Date'], segment_data['Planned Sales'], label=f'Planned Sales {segment}', linestyle='--')
axes[1, 0].set_title('Monthly Sales by Segment')
axes[1, 0].set_xlabel('Date')
axes[1, 0].set_ylabel('Sales')
axes[1, 0].legend()

# Graph 2: Quarterly Sales by Segment
for segment in df['Segment'].unique():
    segment_data = quarterly_sales[quarterly_sales['Segment'] == segment]
    axes[1, 1].bar(segment_data['Date'].astype(str), segment_data['Actual Sales'], label=f'Actual Sales {segment}', alpha=0.7)
    axes[1, 1].bar(segment_data['Date'].astype(str), segment_data['Planned Sales'], label=f'Planned Sales {segment}', alpha=0.7)
axes[1, 1].set_title('Quarterly Sales by Segment')
axes[1, 1].set_xlabel('Quarter')
axes[1, 1].set_ylabel('Sales')
axes[1, 1].legend()

# Graph 3: Sales by Category (Pie Chart)
axes[2, 0].pie(category_sales[category_sales['Segment'] == 'B2C']['Actual Sales'],
               labels=category_sales[category_sales['Segment'] == 'B2C']['Product Type'], autopct='%1.1f%%')
axes[2, 0].set_title('Sales by Category in B2C')

axes[2, 1].pie(category_sales[category_sales['Segment'] == 'B2B']['Actual Sales'],
               labels=category_sales[category_sales['Segment'] == 'B2B']['Product Type'], autopct='%1.1f%%')
axes[2, 1].set_title('Sales by Category in B2B')

# Graph 4: Top 5 Products
x = np.arange(len(top_products_sales))
width = 0.35
fig.add_subplot(3, 2, 5).bar(x - width/2, top_products_sales['Actual Sales'], width, label='Actual Sales')
fig.add_subplot(3, 2, 5).bar(x + width/2, top_products_sales['Planned Sales'], width, label='Planned Sales')
fig.add_subplot(3, 2, 5).set_title('Top 5 Products')
fig.add_subplot(3, 2, 5).set_xticks(x)
fig.add_subplot(3, 2, 5).set_xticklabels(top_products_sales['Product Type'])
fig.add_subplot(3, 2, 5).set_xlabel('Products')
fig.add_subplot(3, 2, 5).set_ylabel('Sales')
fig.add_subplot(3, 2, 5).legend()

# Graph 5: Cumulative Sales by Segment
for segment in df['Segment'].unique():
    segment_data = cumulative_sales[cumulative_sales['Segment'] == segment]
    fig.add_subplot(3, 2, 6).plot(segment_data['Date'], segment_data['Actual Sales'], label=f'Cumulative Actual Sales {segment}', marker='o')
    fig.add_subplot(3, 2, 6).plot(segment_data['Date'], segment_data['Planned Sales'], label=f'Cumulative Planned Sales {segment}', linestyle='--')
fig.add_subplot(3, 2, 6).set_title('Cumulative Sales by Segment')
fig.add_subplot(3, 2, 6).set_xlabel('Date')
fig.add_subplot(3, 2, 6).set_ylabel('Cumulative Sales')
fig.add_subplot(3, 2, 6).legend()

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()
