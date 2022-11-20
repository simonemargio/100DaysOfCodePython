# Day 92

&nbsp;

### Today's topic 🎯
Data visualisation with Matplotlib


&nbsp;

### Final result 🎉
![92-1](https://user-images.githubusercontent.com/110282927/189910549-b0a9d793-6ea3-4663-944e-ee3ef40544c2.png)
![92-2](https://user-images.githubusercontent.com/110282927/189910551-c0ca5303-ecc3-4125-85df-b3cb002de62a.png)
![92-4](https://user-images.githubusercontent.com/110282927/189910556-bab7011e-d2fc-4823-9da2-aea8b06ed6f3.png)
![92-5](https://user-images.githubusercontent.com/110282927/189910558-958c017f-240c-4570-b628-ee613fbfd941.png)


&nbsp;

### Solution ✍️

Import Statements
```
import pandas as pd
```

Challenge: Read the .csv file and store it in a Pandas dataframe
```
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
```

Challenge: Examine the first 5 rows and the last 5 rows of the of the dataframe
```
df.head()
df.tail()
```

Challenge: Check how many rows and how many columns there are. What are the dimensions of the dataframe?
```
df.shape
```

Challenge: Count the number of entries in each column of the dataframe
```
df.count
```

Challenge: Calculate the total number of post per language. Which Programming language has had the highest total number of posts of all time?
```
df.groupby('TAG').sum()
```

Challenge: How many months of data exist per language? Which language had the fewest months with an entry?
```
df.groupby('TAG').count()
```

Let's fix the date format to make it more readable. We need to use Pandas to change format from a string of "2008-07-01 00:00:00" to a datetime object with the format of "2008-07-01"
```
df['DATE'][1]
df.DATE[1]
type(df['DATE'][1])
```

Data Manipulation
```
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
```
Challenge: What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the column names and print out the first 5 rows of the dataframe.
```
reshaped_df.shape
reshaped_df.columns
reshaped_df.head()
```

Challenge: Count the number of entries per programming language. Why might the number of entries be different?
```
reshaped_df.count()
reshaped_df.head()
reshaped_df.isna().values.any()
```

Data Visualisaton with with Matplotlib
```
Challenge: Use the matplotlib documentation to plot a single programming language (e.g., java) on a chart.
import matplotlib.pyplot as plt
plt.plot(reshaped_df.index, reshaped_df['java'])
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
```