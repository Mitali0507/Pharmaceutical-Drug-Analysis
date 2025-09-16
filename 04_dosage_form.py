import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("indian_pharmaceutical_products_clean.csv")

#most common dosage form
dosage_form=df['dosage_form'].value_counts().head(5)
print(dosage_form)

#visualization
plt.figure(figsize=(10,6))

dosage_form.plot(kind='bar',color='#B9AEDC') #hex color codes can also be used
plt.title('Top 5 dosage forms')
plt.xlabel('Dosage Form')
plt.ylabel('Total')
plt.xticks(rotation=0) #for horizontal display

plt.tight_layout()
plt.savefig('dosage_form.png',dpi=300,bbox_inches='tight')
plt.show()

