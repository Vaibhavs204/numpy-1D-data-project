# 1.  Load the sales.csv file using NumPy and display the dataset.
import numpy as np

data = np.genfromtxt(
    "sales.csv",
    delimiter=",",
    dtype=None,
    encoding="utf-8",
    names=True
)

print(data)


#2. Find the total number of sales records.
print("total number of sales records:", data.shape[0])

#3. Display only the Product_Name and Sales_Amount columns.
print("product name with total sales:",data[['Product_Name','Sales_Amount']])
# 4. Calculate the total sales revenue.
revenue=data['Quantity']*data['Unit_Price']
print("all revenue",revenue)
print ("total sales revenue:",np.sum(revenue))
# 5. Find the average sales amount per invoice.
average_sales=(np.mean(data['Sales_Amount']))
print("average sales amount per invoice:",average_sales)


#6. Find the product with the highest sales amount.
print("product with highest sales amount:",np.max(data['Sales_Amount']))

#7. Find the product with the lowest sales amount.
print("product with lowest sales amount:",np.min(data['Sales_Amount']))
#8. Calculate the total quantity of products sold.
print("total quantity of product sold:",np.sum(data['Quantity']))

#9. Find the average profit from all sales.
print("average profit from all sales:",np.mean(data['Profit']))

#10. Display all products belonging to the Electronics category.
for x in data:
    if x['Category'] == 'Electronics':
        print(x['Product_Name'])


mask = data['Category'] == 'Electronics'
electronics_products = data['Product_Name'][mask]
print("products belonging to the electronics category:",electronics_products)


#11 .Find all transactions where Sales_Amount is greater than 10000.
print("transaction where sales amount is greater than 10000:",data[data['Sales_Amount']>10000])

#12. Display all sales made using UPI payment mode.

payment=data['Payment_Mode']=='UPI'
payment_made=data['Product_Name'][payment]
print("sales made using upi payment mode:",payment_made)

#13. Find the total sales for each month.
months = data['Month']
sales = data['Sales_Amount'].astype('i')
unique_months = np.unique(months)
for month in unique_months:
    total = sales[months == month].sum()
    print(" total sales of",month, ":", total)
    
#14. Identify the month with the highest sales.
highest_sales=data[np.argmax(data['Sales_Amount'])]
print("highest sales:",highest_sales)


#15. Sort the dataset based on Profit in descending order.
sort_profit=data[np.argsort(-data['Profit'])]
print("sales in descending order:",sort_profit)
#16. Find the top 3 most profitable products..
top3 = np.argsort(data["Profit"])[-3:][::-1]
print("top 3 profitable product:",data["Product_Name"][top3])

#17. Calculate the profit percentage for each product:
#18. Profit_Percentage = (Profit / Sales_Amount) * 100
pro = data['Profit'].astype('i')

print(pro)
sal =  data['Sales_Amount'].astype('i')
profit_percentage=(data['Profit'] / data['Sales_Amount'].astype('i')) * 100

print("profit percentage :",profit_percentage)
#19. Increase all Unit_Price values by 15% using NumPy operations.
data['Unit_Price'] = data['Unit_Price' ].astype(float) * 1.15

print("increased all unit price by 15%:",data['Unit_Price'])
#20. Find the city that generated the highest total sales.

sales = data['Sales_Amount'].astype(float)
cities = data['City']

index = np.argmax(sales)

print("City with highest generated total sales :", cities[index])
print("highest total sales of the city:", sales[index])