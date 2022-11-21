# Day 93

&nbsp;

### Today's topic 🎯
Aggregate and merge data with Pandas: analyse the LEGO dataset

&nbsp;

### Solution ✍️
See: Lego_Analysis_for_Course_(completed).ipynb

Import Statements
```
import pandas as pd
```

Challenge: How many different colours does the LEGO company produce? Read the colors.csv file in the data folder and find the total number of unique colours. Try using the .nunique() method to accomplish this.
```
colors = pd.read_csv('data/colors.csv')

```

```
colors.head()
```

```
colors['name'].nunique()
```


Challenge: Find the number of transparent colours where is_trans == 't' versus the number of opaque colours where is_trans == 'f'. See if you can accomplish this in two different ways.
```
colors.groupby('is_trans').count() 
```

```
colors.is_trans.value_counts()
```

Challenge: Read the sets.csv data and take a look at the first and last couple of rows.
```
sets = pd.read_csv('data/sets.csv')
```

```
sets.head()
```

```
sets.tail()
```


Challenge: In which year were the first LEGO sets released and what were these sets called?
```
sets.sort_values('year').head()
```


Challenge: How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer in the year the company started?
```
sets[sets['year'] == 1949]
```


Challenge: Find the top 5 LEGO sets with the most number of parts.
```
sets.sort_values('num_parts', ascending=False).head()
```


Challenge: Use .groupby() and .count() to show the number of LEGO sets released year-on-year. How do the number of sets released in 1955 compare to the number of sets released in 2019?
```
sets_by_year = sets.groupby('year').count()
```

```
sets_by_year['set_num'].head()
```

```
sets_by_year['set_num'].tail()
```

Let's work out the number of different themes shipped by year. This means we have to count the number of unique theme_ids per calendar year.
```
themes_by_year = sets.groupby('year').agg({'theme_id' : pd.Series.nunique})
```

```
themes_by_year.rename(columns = {'theme_id' : 'nr_themes'}, inplace = True)
```

```
themes_by_year.tail()
```

Challenge: Plot the number of themes released by year on a line chart. Only include the full calendar years (i.e., exclude 2020 and 2021).
```
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
```


Database Schemas, Foreign Keys and Merging DataFrames
Challenge: Explore the themes.csv. How is it structured? Search for the name 'Star Wars'. How many ids correspond to this name in the themes.csv? Now use these ids and find the corresponding the sets in the sets.csv (Hint: you'll need to look for matches in the theme_id column)
```
themes = pd.read_csv('data/themes.csv') # has the theme names!
themes.head()
```

```
themes[themes.name == 'Star Wars']
```

```
sets[sets.theme_id == 18]
```

```
sets[sets.theme_id == 209]
```

Merging (i.e., Combining) DataFrames based on a Key
```
set_theme_count = pd.DataFrame({'id':set_theme_count.index, 
                                'set_count':set_theme_count.values})
set_theme_count.head()
```

```
merged_df = pd.merge(set_theme_count, themes, on='id')
merged_df[:3]
```

```
# Basic, but unreadable
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
```

```
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])
```

...