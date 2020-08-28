# Exploratory Data Analysis Notes
---

## 1. Read, Clean and Validate:

First, we need to read the data from the source. It could be a database, a csv file or other formats. After that, it's highly recommended to clean your data, *i.e.*, remove or treat any missing, invalid, incomplete or corrupted data.  

Example of reading a csv file in python:  

```python
import pandas as pd
data = pd.read_csv(<file_path>)
```

**PS: Always remember to constantly check the data documentation before treating it.**

To treat some of this data, we rely on a couple most used techniques, such as:  

1. **Replacing**  
   
    ```python
    #Replace all the <value_to_be_replaced> values with <value_to_replace_with>
    data[<column>].replace(to_replace=<value_to_be_replaced>,
                            value=<value_to_replace_with>,
                            inplace=True)
    ```
2. **Filling**  
   
    ```python
    #Fill all NA/null values of <column> with <value>
    data[<column>].fillna(<value>)
    ```
3. **Trimming**  
   
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

## 2. Distributions:  

To analyze a variable distribution, we use some of the following techniques:  

1. **Histograms**  
   
    Histograms are the simplest way to visualize a variable distribution.  

    ```python
    import matplotlib.pyplot as plt
    '''Remember that this method doesn't handle missing data, so it should be
    treated before using it. If not, just call .dropna() method after the series
    name.
    '''
    plt.hist(<data_series>)
    ```
2. **PMFs (Probability Mass Functions):**

