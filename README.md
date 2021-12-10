# Data-Mining

Data mining on a dataset of movies produced by Walt Disney Company, using python.

---
## Contributors

| Name | email | github name |
| :-- | :---: | :---------: |
| Sara Asadi | saraasadi7899@gmail.com | [saraasadi78](https://github.com/saraasadi78) |
| Vahid Ramezani | vahid.ramezani.2014@gmail.com | [ConnorLynch2000](https://github.com/ConnorLynch2000) |


---

## Contents
* [Attribute's properties](#atrributes-properties)

* [Data Skewness](#data-skewness)

* [Data Correctness & Completeness](#data-correctness-and-completeness)

* [Outlier Detction](#outlier-detection)

* [Histogram](#histogram)

* [Dissimilarity Matrix](#dissimilarity-matrix)

* [Corrolation](#corrolation)

* [Scatter Plot](#scatter-plot)

* [Data Cleaning](#data-cleaning)

* [Redundant Data](#redundant-data)

* [Dimensional Reduction](#dimensional-reduction)

* [Normalization](#normalization)

* [Numerosity Reduction](#numerosity-reduction)

---

## Atrribute's Properties
[UP](#contents)

| Name | Type | Range | Mean | Median | Mode | Min | Max |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Title | Nominal | -- | -- | -- | -- | -- | -- |
| Production Company | Nominal | -- | -- | -- | -- | -- | -- |
| Release Date | Interval | [-,now] | -- | -- | -- | -- | -- |
| Running Time | Ratio | [40,167] | 97.8136 | 96 | 100 | 40.0 | 167 |
| Country | Nominal | -- | -- | -- | -- | -- | -- |
| Language | Nominal | -- | -- | -- | -- | -- | -- |
| Box Office | Ratio | [7.7,1.657b] | 165932061.3922 | 44900000.0 | 4000000 | 7.7 | 1657000000 |
| Budget | Ratio | [300k,410.6m] | 63877468.3098 | 30000000.0 | [5.0e+06 1.5e+08] | 300000 | 410600000.0 |
| Directed By | Nominal | -- | -- | -- | -- | -- | -- |
| Writen by | Nominal | -- | -- | -- | -- | -- | -- |
| Based on | Nominal | -- | -- | -- | -- | -- | -- |
| Produced by | Nominal | -- | -- | -- | -- | -- | -- |
| Starring | Nominal | -- | -- | -- | -- | -- | -- |
| Music by | Nominal | -- | -- | -- | -- | -- | -- |
| Distributed by | Nominal | -- | -- | -- | -- | -- | -- |
| Story by | Nominal | -- | -- | -- | -- | -- | -- |
| Narrated by | Nominal | -- | -- | -- | -- | -- | -- |
| Cinematography | Nominal | -- | -- | -- | -- | -- | -- |
| Edited by | Nominal | -- | -- | -- | -- | -- | -- |
| Screenplay by | Nominal | -- | -- | -- | -- | -- | -- |
| Production Company | Nominal | -- | -- | -- | -- | -- | -- |
| Color Proccess | Nominal | -- | -- | -- | -- | -- | -- |
| Hepburn | Nominal | -- | -- | -- | -- | -- | -- |
| Adaption by | Nominal | -- | -- | -- | -- | -- | -- |
| Animation by | Nominal | -- | -- | -- | -- | -- | -- |

---

## Data Skewness
[UP](#contents)

You can simply observe the skewness computed for diffrent attributes [here](skewness.ipynb).

Results are as follows:

#### Box Office
![Box Office Skewness](/Results/Box_Office_skew.png)

#### Budget
![Budget Skewness](/Results/Budget_skewness.png)

#### Running Time
![Running Time](/Results/Running_time_skew.png)


---

## Data Correctness and Completeness
[UP](#contents)

Using human sences and also statistical factors the correctness and completeness of data have been analysed. [Data cleaning](#data-cleaning) step have been taken based on the results of the aforementioned analysis.

You can see below the [visual results of the analysis](/Results/Incompleteness.png).

![incompleteness](/Results/Incompleteness.png)


---

## Outlier Detection
[UP](#contents)

Using **box plot** tool, the valid range of values for data has been computed and data records beyond the foresaid range have been removed.

Box plots are shown below.

#### [Box Office Box Plot](/Results/box-office-boxplot.png)
![box office box plot](/Results/box-office-boxplot.png)


#### [Budget Box Plot](/Results/budget-boxplot.png)
![budget box plot](/Results/Budget-boxplot.png)


#### [Running Time Box Plot](/Results/Running-time-boxplot.png)
![running time box plot](/Results/Running-time-boxplot.png)


---

## Histogram
[UP](#contents)

Below you can see histogram of some of the data attributes.
You can find the computation code [here](histogram.ipynb).


#### Box Office
![Box Office Histogram](/Results/Box_Office_Histogram.png)

#### Budget
![Budget Histogram](/Results/Budget_Histogram.png)

#### Running Time
![Running Histogram](/Results/Running_Time_Histogram.png)


---

## Dissimilarity Matrix
[UP](#contents)

After removing unnecessary attributes, the dissimilarity matrix have been computed. You can see and follow the computation steps [here]: (dissimilarity_matrix.ipynb)

---

## Corrolation
[UP](#contents)

Corrolation between attributes of dataset have been computed after some cleaning and normalization steps. Some unnecessary attributes have been ignored and some nominal attributes have been converted to numerical values.
The procedure and the final results can be find [here](data-corrolation.ipynb)

#### [Corrolation Heatmap](/Results/corrolation-heatmap.png)
![corrolation heatmap](/Results/corrolation-heatmap.png)

---

## Scatter Plot
[UP](#contents)

Scatter plot for [corrolated](#corrolation) attributes are shown below.

#### [Company-Director Scatter Plot](/Results/Company-Director.png)
![company-director scatter](/Results/Company-Director.png)

#### [Director-Composer Scatter Plot](/Results/Director-Composer.png)
![company-director scatter](/Results/Director-Composer.png)

#### [Language-Country Scatter Plot](/Results/Language-country.png)
![company-director scatter](/Results/Language-country.png)

#### [Budget-Box Office Scatter Plot](/Results/budget-box_office.png)
![company-director scatter](/Results/budget-box_office.png)



---

## Data Cleaning
[UP](#contents)

Doing cleaning on the dataset with 35 attributes(columns), we reached a dataset with only 17 attributes(columns).

Columns containing more than 40% missing or invalid values have been dropped.

Also the remaining columns' missing values have been imputed automatically using attribute's median.

You can see the procedure and the results by executing [cleaningDataset.py](cleaningDatase.py) file.

---

## Redundant Data
[UP](#contents)

redundant data records have been handled or removed during [data cleaning](#data-cleaning) proccess.


---

## Dimensional Reduction
[UP](#contents)


Some useful notes can be taken from regularly observing the dataset. There are some attributes with different labels but containing same data values, Outwardly and inwardly. There also are some attributes with more than 40% of missing data or invalid data.

All these cases have been addressed while doing [cleaning](#data-cleaning) on the data set. 

---

## Normalization
[UP](#contents)

Data have been normalized using min-max scaling which scaled data in range [0,1]. Alongside with the normalizing the dataset, z-score standardization have been also done on the dataset. You can see and compare an attribute before and after the procedure below.

#### [Original and Normalized Data Scatter Plot](/Results/original-and-normalized.png)
![original and normalized scatter](/Results/original-and-normalized.png)


#### [Normalized Data Scatter Plot](/Results/normalized-scatter-plot.png)
![normalized scatter plot](/Results/normalized-scatter-plot.png)


The results are accessible at [min-max_normalization.py](min-max_normalization.py).

---

## numerosity Reduction
[UP](#contents)

Knowing the consepts of the records of the datasets, it's simply wrong to perform a numerosity reduction on the data.
Each record contains data about a single movie produced by Disney Pictures and records are not normally related to on another. **But**, redundancy is not accepted and duplicate data records must be removed from the dataset. **Also** outlier records have been detected and removed. This problems have been solved during [data cleaning](#data-cleaning) and [outlier detection](#outlier-detection) proccesses.
