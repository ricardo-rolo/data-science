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
  - [4. Multivariate thinking](#4-multivariate-thinking)


# Exploratory Data Analysis Notes

> These notes were created based on DataCamp's 'Exploratory Data Analysis in Python' course and also with part of my previous knowledge on this topic.  

> It's worh mentioning that this is a brief resume of an EDA process, part of the code shown here is part of the DataCamp's course. These notes were made so i can revise the content of the course in case i forgot something after completing it, and i decided to share it so others can rely on this document as well ;).

## 1. Read, Clean and Validate:

First, we need to read the data from the source. It could be a database, a csv file or other formats. After that, it's highly recommended, i would say mandatory, to clean your data, *i.e.*, remove or treat any missing, invalid, incomplete or corrupted data.  

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
  We can use this technique to replace outliers, missing values, corrupted data and many more. The value to replace with could be any value you want, but there are some methods like mean, median, or, for example, replacing the outliers with the max/min non-outlier values. It's up to you infer the best approach here.  

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

To validate a variable, you could use some pandas attributes and methods. The goal here is to check if the variables are, in fact, according to your expectations. Since this step may vary a lot, according to the business and data provided, we'll only mention some useful methods you can try:  

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

## 4. Multivariate thinking

[empiricaldist]: https://pypi.org/project/empiricaldist/