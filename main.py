# Restaurant-Manager
This is a comprehensive digital solution designed to streamline daily restaurant operations, improve staff efficiency, and enhance the guest experience. This application serves as a centralized hub for managing everything from digital menu curation to automated billing and inventory tracking.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

menu_data = {
    'Item': ['Burger', 'Pizza', 'Pasta', 'Salad', 'Soda', 'Steak'],
    'Category': ['Main', 'Main', 'Main', 'Starter', 'Drink', 'Main'],
    'Price': [8, 12, 11, 7, 2.5, 22],
    'Stock': [20, 15, 10, 8, 50, 5]
}
df_menu = pd.DataFrame(menu_data)
df_menu['Sales_Count'] = np.array([15, 12, 8, 10, 45, 4])
df_menu['Revenue'] = df_menu['Price'] * df_menu['Sales_Count']

def plot_performance(df):
    plt.figure(figsize=(18, 5))
    plt.bar(df['Item'], df['Revenue'], color='blue')
    plt.title('Daily Menu Performance')
    plt.ylabel('Total Revenue')
    plt.show()

plot_performance(df_menu)
reorder_list = df_menu[df_menu['Stock'] < 10]
best_seller = df_menu.loc[df_menu['Revenue'].idxmax()]
category_revenue = df_menu.groupby('Category')['Revenue'].sum()
print(category_revenue)
