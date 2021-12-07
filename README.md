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


---

## Redundant Data
[UP](#contents)


---

## Dimensional Reduction
[UP](#contents)


---

## Normalization
[UP](#contents)


---

## numerosity Reduction
[UP](#contents)
