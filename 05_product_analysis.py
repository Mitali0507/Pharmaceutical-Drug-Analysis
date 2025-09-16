import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("indian_pharmaceutical_products_clean.csv")

#discontinued and continued product analysis
non_active=df[df['is_discontinued']==True] #creating a dataset for desired activity
active=df[df["is_discontinued"]==False]

print(f"Total Active products: {active.value_counts().sum()}")
print(f"Total discontinued products: {non_active.value_counts().sum()}")

#price comparison between active and non-active drugs

print(f"Average price of discontinued products: {non_active["price_inr"].mean()}")
print(f"Average price of active products: {active["price_inr"].mean()}")

#creating a bar graph for two numeric datasets comparison, in this case its the average
labels=['Active','Discontinued']
averages=[active["price_inr"].mean(),non_active["price_inr"].mean()]
plt.barh(labels,averages,color=["#c90076","#6fa8dc"]) #for horizontal graph(for quick view)
plt.savefig("Horizontal_price.png",dpi=300,bbox_inches="tight")
plt.show()

#vertical bar graph
plt.figure(figsize=(8,6))
plt.bar(labels,averages,color=["#c90076","#6fa8dc"])
plt.title("Average Price: Active vs Discontinued")
plt.ylabel("Price(INR)")
plt.tight_layout()
plt.savefig("Vertical_price.png",dpi=300,bbox_inches="tight")
plt.show()

