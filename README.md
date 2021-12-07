# Data-Mining
Data mining with python on list of films produced by Walt Disney Company.

## Contents
* [Attribute's properties](#atrributes-properties)

* [Data Skewness](#data-skewness)

* [Data Correctness & Completeness](#data-correctness-and-completeness)

* [Noise Detction](#noise-detection)

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

## Noise Detection
[UP](#contents)

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

After removing unnecessary attributes, the dissimilarity matrix have been computed. You can see and follow the computation steps [here](dissimilarity_matrix.ipynb.ipynb)

---

## Corrolation
[UP](#contents)

Corrolation between attributes of dataset have been computed after some cleaning and normalization steps. Some unnecessary attributes have been ignored and some nominal attributes have been converted to numerical values.
The procedure and the final results can be find [here](data-corrolation.ipynb)

---

## Scatter Plot
[UP](#contents)


---

## Data Cleaning
[UP](#contents)

Doing cleaning on the dataset with 35 attributes(columns), we reached a dataset with only 17 attributes(columns).

Columns containing more than 40% missing or invalid values have been dropped.

Also the remaining columns' missing values have been filled automatically using attribute's median.

You can see the procedure and the results by executing [cleaningDataset.py](cleaningDatase.py) file.

---

## Redundant Data
[UP](#contents)


---

## Dimensional Reduction
[UP](#contents)


---

## Normalization
[UP](#contents)

Data have been normalized using min-max scaling which scaled data in range [0,1]. Alongside with the normalizing the dataset, z-score standardization have been also don on the dataset. You can see and compare an attribute before and after the procedure below.

#### [Original and Normalized Data Scatter Plot](/Results/original-and-normalized.png)
![original and normalized scatter](/Results/original-and-normalized.png)


#### [Normalized Data Scatter Plot](/Results/normalized-scatter-plot.png)
![normalized scatter plot](/Results/normalized-scatter-plot.png)


The results are accessible at [min-max_normalization.py](min-max_normalization.py).

---

## numerosity Reduction
[UP](#contents)

Knowing the consepts of the records of the datasets, it's simply wrong to perform a numerosity reduction on the data.
Each record contains data about a single movie produced by Disney Pictures and records are not normally related to on another. **But**, redundancy is not accepted and duplicate data records must be removed from the dataset. This problem has been solved during data cleaning proccess.
