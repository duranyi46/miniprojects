import pandas as pd
import matplotlib.pyplot as plt


colors = pd.read_csv("C:\\Users\\deadp\\pythonProject\\lego\\colors.csv.gz", compression = 'gzip')
print(colors.head(5))

num_colors = colors['name'].nunique()
print(num_colors)

colors_summary = colors_summary = colors.groupby('is_trans').count()
print(colors_summary)

sets = pd.read_csv("C:\\Users\\deadp\\pythonProject\\lego\\sets.csv.gz", compression='gzip')
parts_by_year = sets.groupby('year')['num_parts'].sum()
print(parts_by_year)


parts_by_year.plot(kind='line')
plt.xlabel('Year')
plt.ylabel('Number of Parts')
plt.title('Number of Lego Parts by Year')
plt.grid(True)
plt.show()

themes_by_year = sets.groupby('year')[['theme_id']].nunique()
print(themes_by_year.head(5))