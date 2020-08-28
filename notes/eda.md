- [Exploratory Data Analysis Notes](#exploratory-data-analysis-notes)
  - [1. Read, Clean and Validate:](#1-read-clean-and-validate)
    - [1.1 Reading](#11-reading)
    - [1.2 Cleaning](#12-cleaning)
    - [1.3 Validating](#13-validating)
  - [2. Distributions:](#2-distributions)
    - [2.1 Histograms](#21-histograms)
    - [2.2 PMFs (Probability Mass Functions)](#22-pmfs-probability-mass-functions)
    - [2.3 CDFs (Cumulative Distribution Functions)](#23-cdfs-cumulative-distribution-functions)


# Exploratory Data Analysis Notes

> These notes were created based on DataCamp's Exploratory Data Analysis in Python course and also part of my previous knowledge on this topic. The examples are also from the 

## 1. Read, Clean and Validate:

First, we need to read the data from the source. It could be a database, a csv file or other formats. After that, it's highly recommended to clean your data, *i.e.*, remove or treat any missing, invalid, incomplete or corrupted data.  

### 1.1 Reading  

```python
import pandas as pd
data = pd.read_csv('../data/billboard.csv')
```

**PS: Always remember to constantly check the data documentation before treating it.** 

### 1.2 Cleaning

* #### Replacing
   We can use this technique to replace outliers, missing values, corrupted data and many more. The value to replace with could be any value you want, but there are some methods like mean, median, or, for example, replacing the outliers with the max/min non-outlier values. It's up to you infer the best approach here.  

```python
#Replace all the <value_to_be_replaced> values with <value_to_replace_with>
data[<column>].replace(to_replace=<value_to_be_replaced>,
                        value=<value_to_replace_with>,
                        inplace=True)
```  

* #### Filling
   Filling is most used to 
```python
#Fill all NA/null values of <column> with <value>
data[<column>].fillna(<value>)
```  

* #### Trimming
   
`Row` dropping method
```python
#Drop all the rows with the NA/null values in the columns specified
data.dropna(subset=<columns_list>, inplace=True, axis='index')
```  

`Column` dropping method
```python
#Drop all the rows with the NA/null values in the columns specified
data.dropna(subset=<columns_list>, inplace=True, axis='columns')
```  

### 1.3 Validating

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
    
<<<<<<< HEAD
PMFs works similarly to Histograms, but it tells the probability, drawing a random element of the data, that this element is X, *i.e.*, the desired value.  
To work with PMFs we're going to use the [empiricaldist] python library, created by Allen Downey for DataCamp's EDA in python course.  
=======
    PMFs works similarly to Histograms, but it tells the probability, drawing a random element of the data, that this element is X, *i.e.*, the desired value.  
    To work with PMFs we're going to use the [empiricaldist] python library, created by **Allen Downey** for DataCamp's EDA in python course.  
>>>>>>> 89fb87f2d61c61f0b871ba1c55181769306fe510

```python
from empiricaldist import Pmf

pmf = Pmf(<data_series>, normalize=True) #this returns a Pmf object

#we can also plot the PMF as shown below:
pmf.bar()
plt.show()
```  

<<<<<<< HEAD
=======
    The CDF is the probability of getting a value <= X, drawing a random element of the data. In other words, the CDF is the cumulative sum of PMF.  
    Here, we're also going to use the [empiricaldist] python library, mentioned above. The result of ```Cdf(X)``` is the amount, between 0 and 1, of the values that are **less** or **equal** than X.
>>>>>>> 89fb87f2d61c61f0b871ba1c55181769306fe510

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
We can also use the inverted version of this function to get the percentiles, *i.e.*, given a `p` percentile, `cdf.inverse(p)` returns the value corresponding to the p-th percentile.   

For example:  

```python
from empiricaldist import Cdf

cdf = Cdf(<data_series>) #this returns a Cdf object

p = 0.25
q = cdf.inverse(p) #this returns the 25th percentile
```  
In the code above, `q` corresponds to the **25th percentile** of `<data_series>`.


<<<<<<< HEAD
=======
    p = 0.25
    q = cdf.inverse(p) #this returns the 25th percentile
    ```  
    In the code above, `q` corresponds to the **25th percentile** of `<data_series>`.
    
>>>>>>> 89fb87f2d61c61f0b871ba1c55181769306fe510
[empiricaldist]: https://pypi.org/project/empiricaldist/