
# Exploratory Data Analysis Notes

- [Exploratory Data Analysis Notes](#exploratory-data-analysis-notes)
  - [1. Read, Clean and Validate:](#1-read-clean-and-validate)
    - [1.1 Reading](#11-reading)
    - [1.2 Cleaning](#12-cleaning)
    - [1.3 Validating](#13-validating)
  - [2. Distributions:](#2-distributions)
    - [2.1 Histograms](#21-histograms)
    - [2.2 PMFs (Probability Mass Functions)](#22-pmfs-probability-mass-functions)
    - [2.3 CDFs (Cumulative Distribution Functions)](#23-cdfs-cumulative-distribution-functions)
    - [2.4 Box plots](#24-box-plots)
    - [2.5 PDFs (Probability Density Functions)](#25-pdfs-probability-density-functions)
  - [3. Relationships](#3-relationships)
    - [3.1 Visualization](#31-visualization)
    - [3.2 Correlation](#32-correlation)
  - [4. Multivariate thinking](#4-multivariate-thinking)

> These notes were created based on DataCamp's [Exploratory Data Analysis in Python](https://learn.datacamp.com/courses/exploratory-data-analysis-in-python) course and also with part of my previous knowledge on this topic.  

> It's worh mentioning that this is a brief resume of an EDA process, the most part of the code shown here is a generic version from the DataCamp's course. These notes were made so i can revise the content of the course in case i forgot something after completing it, and i decided to share it so others can rely on this document as well ;).

## 1. Read, Clean and Validate:

First, we need to read the data from the source. It could be a database, a csv file or other formats. After that, it's highly recommended, i would say mandatory, to clean our data, *i.e.*, remove or treat any missing, invalid, incomplete or corrupted data.  

### 1.1 Reading  

* #### Reading a csv file
  ```python
  import pandas as pd
  #Create a dataframe
  data = pd.read_csv('<file_path>')
  ```

* #### Querying from a relational database
  ```python
  import pandas as pd
  from sqlalchemy import create_engine

  conn = create_engine('<database_path>')
  data = pd.read_sql_query('<sql_query>', conn)
  ```

**PS: Always remember to constantly check the data documentation, if provided, from your data source, before treating it.** 

### 1.2 Cleaning

* #### Replacing
  We can use this technique to replace outliers, missing values, corrupted data and many more. The value to replace with could be any value we want, but there are some methods like mean, median, or, for example, replacing the outliers with the max/min non-outlier values. It's up to you infer the best approach here.  

  ```python
  #Replace all the <value_to_be_replaced> values with <value_to_replace_with>
  data['<column>'].replace(to_replace=<value_to_be_replaced>,
                          value=<value_to_replace_with>,
                          inplace=True)
  ```  

* #### Filling  
  This method is commonly used to fill all missing values (NA/NaN/NaT) of a columns from a dataframe.  
  
  ```python
  #Fill all NA/null values of <column> with <value>
  data['<column>'].fillna(<value>)
  ```  

* #### Drop missing values
  
  `Row` dropping method
  ```python
  #Drop all the rows with the NA/null values in the columns specified
  data.dropna(subset=<columns_list>, inplace=True, axis='index')
  ```  

  `Column` dropping method
  ```python
  #Drop all the columns with the NA/null values in the columns specified
  data.dropna(subset=<columns_list>, inplace=True, axis='columns')
  ```  

* #### Drop duplicates

  `Complete duplicates`  
  Here, we'll drop only the **rows** that contains **all** values as duplicates, *i.e.*, the dataset has another row(s) which is/are identical to the one(s) dropped.
  ```python
  data.drop_duplicates(inplace=True)
  ```  

  `Partial duplicates`  
  Here, we'll drop only the **rows** that contains duplicated values on the columns specified on the subset argument of the function.
  ```python
  data.drop_duplicates(subset=<columns_list>, inplace=True)
  ```

### 1.3 Validating

To validate a variable, we could use some pandas attributes and methods. The goal here is to check if the variables are, in fact, according to our expectations. Since this step may vary a lot, according to the business and data provided, we'll only mention some useful methods you can try:  

  * Filtering  
  * Plotting
  * Checking the shape of data
  * Checking the data type
  * Search for outliers
  * Check the data documentation
  
## 2. Distributions:

To analyze a variable distribution, we use some of the following techniques:  

### 2.1 Histograms
   
Histograms are the simplest way to visualize a variable distribution. They count how many times a range of values occurs in the given data.  

```python
import matplotlib.pyplot as plt
'''Remember that this method doesn't handle missing data, so it should be
treated before using it. If not, just call .dropna() method after the series
name.
'''
plt.hist(<data_series>)
```  


### 2.2 PMFs (Probability Mass Functions)
    
PMFs works similarly to Histograms, but it tells the probability, drawing a random element of the data, that this element is X, *i.e.*, the desired value.  
To work with PMFs we're going to use the [empiricaldist] python library, created by Allen Downey for DataCamp's EDA in python course.  

```python
from empiricaldist import Pmf

pmf = Pmf(<data_series>, normalize=True) #this returns a Pmf object

#we can also plot the PMF as shown below:
pmf.bar()
plt.show()
```  

### 2.3 CDFs (Cumulative Distribution Functions)

The CDF is the probability of getting a value <= X, drawing a random element of the data. In other words, the CDF is the cumulative sum of PMF.  
Here, we're also going to use the [empiricaldist] python library, mentioned above. The result of ```Cdf(X)``` is the amount, between 0 and 1, of the values that are **less** or **equal** than X.  

```python
from empiricaldist import Cdf

cdf = Cdf(<data_series>) #this returns a Cdf object

#we can also plot the CDF as shown below:
cdf.plot()
plt.show()
```   
The CDFs plots are, in general, smoother than PMFs plots because they smooth out randomness.  

We can also use the inverted version of this function to get the percentiles, *i.e.*, given a `p` percentile, `cdf.inverse(p)` returns the value corresponding to the p-th percentile.   

For example:  

```python
from empiricaldist import Cdf

cdf = Cdf(<data_series>) #this returns a Cdf object

p = 0.25
q = cdf.inverse(p) #this returns the 25th percentile
```  
In the code above, `q` corresponds to the **25th percentile** of `<data_series>`.  

> To compare distributions, you could plot PMFs or CDFs on the same plot figure. Remind that CDFs are less noisy, so it's better to visualize.

### 2.4 Box plots
   
Box plots are one of the most popular ways to visualize a variable distribution, as well as one of the most powerful.

```python
import matplotlib.pyplot as plt

plt.boxplot(<data_series>)
```  

### 2.5 PDFs (Probability Density Functions)
    
In this case, we'll use the KDE (Kernel Density Estimation) to estimate the probability density function of a random variable based on its PMF.  
The [kdeplot](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) method of seaborn library takes a series, estimate its PDF and then plot it.  

```python
import seaborn as sns

sns.kdeplot(<data_series>)
```  

**Tooltips:**  

1. Use CDFs for exploration
2. Use PMFs if there is a small number of unique values
3. Use KDE if there are a lot of values
4. Sometimes, PDFs can be too sensitive to randomness, in these cases, consider using CDFs instead.  

## 3. Relationships  

To see if `a pair` of variables are related, we analyze their relationship, *i.e.*, we compare their values directly to show any correlation, we can see if two variables grow in the same proportion, or if a variable grows, the another one decreases, for example.  

### 3.1 Visualization

- #### Scatter Plots  

  The Scatter plot is the most common way to visualize the relationship between two variables, it shows a single dot, with its correspondent x (variable 1) and y (variable 2) values, for each observation of the data specified.  

  ```python
  import matplotlib.pyplot as plt

  plt.plot(<variable1>, <variable2>)
  ```  

  Sometimes, the data may look noisy (overplotting), which can be treated changing the plot's style, or corrupted, for example: a column 'weight' (in kilograms) that were created based on another weight column, which was primarily measured in pounds. The rounding of the values after the conversion may cause a grouping on the new column, making its values be discretely separated into bins.  

  We can treat the second one using a technique named `Jittering`, which consists in adding random noise to these values, filling in the values that got corrupted, like the rounding problem shown above.  

  ```python
  import numpy as np

  data_new = data['<column>'] + np.random.normal(<mean>, <std>, size=len(data))
  ```

- #### Box Plots

  Box plots are also used to visualize variables relationship, since the relationship between them is as comparison of the distribution of the variable y for each group (bin) of the variable x. It does that by estimating the KDE for each bin. To do that, we need to drop the NA values of each variable:  

  ```python
  import pandas as pd

  plot_data = data.dropna(subset=['<variable1>', '<variable2>'])
  ```  
  And then, plot the values:

  ```python
  import seaborn as sns

  sns.boxplot(x='<variable1>', y='<variable2>', data=<data_frame>)
  ```  

  To avoid showing big disparities (skewness) of the values, we could set the y axis scale to logarithmic as follows:  

  ```python
  plt.yscale('log')
  ```  

- #### Violin Plots

  What a violin plot do is basically take the groups (bins) of a variable (tipically the x axis), and infers its PDF, for each of these groups, by using KDE, and then plot it. It's similar to the boxplot, each column is a graphical representation of the distribution of a variable in its group.

  ```python
  import seaborn as sns

  sns.violinplot(x='<variable1>', y='<variable2>', data=<data_frame>)
  ```  
  Here, we could also use axis in logarithmic scale.  

### 3.2 Correlation

- #### [Pearson's Correlation Coefficient]

  The PCC determines whether a `linear correlation` between a subset of variables is positive, negative or if there is no correlation between them.  
  We can set this subset as follows:  

  ```python
  subset = <columns_list>
  ```  

  And then, use this subset to filter the original dataframe and show its [correlation matrix]:  

  ```python
  import pandas as pd

  correlation = data[subset]
  correlation.corr()
  ```

  **PS: Remember that if a PCC between two variables is 0 (zero), that concludes that there is no `linear correlation` between them, but `doesn't` mean that there is `no correlation`, they could have a `non-linear correlation`.**  

- #### Simple Regression
  
  Be aware that even if a PCC isn't a strong value, *i.e*, close to 1 or -1, there still could be an interesting correlation between the variables. To see that, we need to look at the `slope` of the regression line fitted, as shown below:  

  **PS: Remember that there could still be a `non-linear correlation` between them. To check the relationship between them we'll need to use multiple regression, covered in the [Multivariate thinking](#4-multivariate-thinking) session.**  

  **Also, keep in mind that linear regression `is not symmetric`, so a linear regression to variable1 onto variable2 is not the same thing as a regression to variable2 onto variable1. That concludes that `linear regression` does not tell much about `causation`.**

  ```python
  from scipy.stats import linregress

  subset = data.dropna(subset=['<variable1>', '<variable2>'])
  xs = subset['<variable1>']
  ys = subset['<variable2>']
  res = linregress(xs, ys)
  ```
   This returns a `LinregressResult` object from the scipy.stats `linregress` function. Check the [documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html) to see what are the atributes of this object.   

   We can use this object to compute the line of best fit as follows:  

   ```python
   import numpy as np

   fx = np.array([xs.min(), xs.max()])
   fy = res.intercept + res.slope * fx 
   plt.plot(fx, fy, '-')
   ```  


## 4. Multivariate thinking

In this section we'll see how to fit a multiple regression onto our dataset. A way to check a relationship between two variables is by analyzing the scatter plot of our data, grouped by the variable we are going to use to predict the values, filter it selecting the variable we want to predict, then compute an aggregation, most commonly mean, and plot it:  

```python
grouped = data.groupby('<variable_used_to_predict>')
filtered = grouped['<variable_to_be_predicted>'].mean()
plt.plot(filtered, 'o')
```

After checking the relationship between them, we'll start building a simple regression model using the [statsmodels] library as follows:  

```python
import statsmodels.formula.api as smf

results = smf.ols('<variable_to_be_predicted> ~ <variable_used_to_predict>').fit()
results.params
```  
- ### Adding a quadratic term

  This the simplest way to transform a simple regression into a multiple regression, we can do that as shown below:  

  ```python
  data['<variable_used_to_predict_2>'] = data['<variable_used_to_predict>'] ** 2

  results = smf.ols('<variable_to_be_predicted> ~ <variable_used_to_predict> + <variable_used_to_predict_2>').fit())
  ```  

- ### Generating predictions

  text

- ### Visualizing predictions

  text

- ### Logistic Regression
  
  To make a logistic regression, we should start with a categorical variable

[empiricaldist]: https://pypi.org/project/empiricaldist/
[Pearson's Correlation Coefficient]: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
[correlation matrix]: https://www.displayr.com/what-is-a-correlation-matrix/#:~:text=A%20correlation%20matrix%20is%20a,a%20diagnostic%20for%20advanced%20analyses.
[statsmodels]: https://www.statsmodels.org/stable/index.html