import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("indian_pharmaceutical_products_clean.csv")

#Top brands by product count
top_brands=df['brand_name'].value_counts().head(10)
print(top_brands)

#visualization 
plt.figure(figsize=(10,6))

top_brands.plot(kind='bar',color='pink') #plots a bar graph,color of bars is pink
plt.title("Top 10 pharma brands by products") #title of the graph
plt.xlabel('Brand Name') #label for x-axis
plt.ylabel('Number of products') #label for y-axis
plt.xticks(rotation=45) #rotates the names of brands by 45 deg
plt.tight_layout() #adjust spaces to prevent overlapping 
plt.savefig('top_brands.png',dpi=300,bbox_inches='tight')
#to save the figure
#dpi 300 is for highest resolution
#bbox_inches='tight' is for removing extra whitespaces
plt.show()

#plt.show() erases the memory of graph, so save the graph before showing


