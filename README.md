
## A Machine Learning Approach to Improve the Detection of CI Skip Commits

CSL7090 | SDE July 2022 | Term Project

**Paper:** 

R. Abdalkareem, S. Mujahid and E. Shihab, "A Machine Learning Approach to Improve the Detection of CI Skip Commits," in IEEE Transactions on Software Engineering, vol. 47, no. 12, pp. 2740-2754, 1 Dec. 2021, doi: 10.1109/TSE.2020.2967380.

Ref : https://ieeexplore.ieee.org/abstract/document/8961089

**Brief Description:**

In today's world going to market faster is extremly important and if we are not able to do so becuase of running longer and longer pipeline cycles for small & small changes in UI or some very minor bug fixes. The paper has tried to solve this problem by using Decision Tree algorithm of Machine Learning. Since this is extremly desired in today's world to make CI-CD pipleine more intelligent that they do not just follow a scheuld or they do not just follow a trigger of push & merge but they be more intelligent and to make them intelligent we have to use AI\ML but in this paper they have used Decision Tree but we think that if we use some other Model which are more efficient in processing human language then may be we can improve the solution proposed in this paper.



## Authors
- [Debonil Ghosh	[M21AIE225] ](https://www.github.com/debonil)
- [Ravi Shankar Kumar [M21AIE247]](https://www.github.com/debonil)



## Demo

https://youtu.be/5iA4ZghTVS0

https://youtu.be/MzQAmS6U23k


## Usage

    1. Data download from GitHub API & prepare feature vector with data-preparation.py

    2. Normalize feature vector, train ML models, and store results all-repo-ml-training.py



## Results

**Detailed Classifier Accuracy summary**
|Classifier         |Mean       |Median     |Max  |Min        |Standard Deviation|
|-------------------|-----------|-----------|-----|-----------|------------------|
|Ridge Classifier   |0.907612264|0.94075    |1    |0.64       |0.099287063       |
|RBF SVM            |0.906718868|0.942      |0.974|0.67       |0.089866116       |
|QDA                |0.906222013|0.943      |1    |0.67       |0.095284405       |
|Logistic Regression|0.904225472|0.94425    |1    |0.69       |0.08755999        |
|Gaussian Process   |0.902325472|0.93775    |1    |0.64       |0.09924061        |
|Random Forest      |0.895325472|0.93625    |1    |0.69       |0.089522373       |
|Naive Bayes        |0.893238679|0.93125    |1    |0.65       |0.098224384       |
|Neural Net         |0.886575157|0.936583333|0.973|0.67       |0.097637189       |
|Nearest Neighbors  |0.838960377|0.87       |0.975|0.556603774|0.136013828       |
|Linear SVM         |0.825698742|0.901833333|0.968|0.393      |0.170268225       |
|Decision Tree      |0.821083962|0.872      |0.975|0.568      |0.143949334       |
|AdaBoost           |0.784083962|0.872      |0.975|0.3        |0.210291759       |

**Detailed Classifier performance for different repositories with respect to different metrices:**

### Accuracy Summary

| Project               |   Logistic Regression |   Neural Net |   Linear SVM |   RBF SVM |   Random Forest |   Ridge Classifier |   Gaussian Process |   Nearest Neighbors |   AdaBoost |   Decision Tree |   Naive Bayes |      QDA |
|:----------------------|----------------------:|-------------:|-------------:|----------:|----------------:|-------------------:|-------------------:|--------------------:|-----------:|----------------:|--------------:|---------:|
| eBay_parallec         |              1        |     1        |     1        |  1        |        1        |           1        |           0.972973 |            0.972973 |   0.945946 |        0.945946 |      0.567568 | 0.567568 |
| dropwizard_dropwizard |              0.975155 |     0.975155 |     0.975155 |  0.975155 |        0.97205  |           0.975155 |           0.974379 |            0.972826 |   0.975155 |        0.968168 |      0.975155 | 0.975155 |
| jMotif_GI             |              0.96875  |     0.96875  |     0.9375   |  0.875    |        0.875    |           0.864583 |           0.96875  |            0.875    |   0.864583 |        0.791667 |      0.875    | 0.875    |
| jMotif_SAX            |              0.952381 |     0.952381 |     0.952381 |  0.952381 |        0.958333 |           0.952381 |           0.958333 |            0.958333 |   0.869048 |        0.958333 |      0.869048 | 0.869048 |
| steve-community_steve |              0.951276 |     0.944316 |     0.951276 |  0.951276 |        0.944316 |           0.951276 |           0.948956 |            0.944316 |   0.951276 |        0.911833 |      0.951276 | 0.951276 |
| Average               |              0.969512 |     0.96812  |     0.963262 |  0.950762 |        0.94994  |           0.948679 |           0.964678 |            0.94469  |   0.921202 |        0.915189 |      0.847609 | 0.847609 |
| Median                |              0.969131 |     0.968435 |     0.957822 |  0.951829 |        0.954137 |           0.951829 |           0.966714 |            0.951511 |   0.933574 |        0.930568 |      0.872024 | 0.872024 || 

### Recall Summary

Project                     |   Logistic Regression |   Neural Net |   Linear SVM |   RBF SVM |   Random Forest |   Ridge Classifier |   Gaussian Process |   Nearest Neighbors |   AdaBoost |   Decision Tree |   Naive Bayes |   QDA |
|:----------------------------|----------------------:|-------------:|-------------:|----------:|----------------:|-------------------:|-------------------:|--------------------:|-----------:|----------------:|--------------:|------:|
| eBay_parallec               |              1        |     1        |     1        |  1        |        1        |           1        |           0.969697 |            0.969697 |  0.941176  |        0.933333 |             0 |     0 |
| jMotif_GI                   |              0.869565 |     0.869565 |     0.769231 |  0        |        0        |           0        |           0.869565 |            0        |  0         |        0        |             0 |     0 |
| tracee_contextlogger        |              0.8      |     0.8      |     0.774194 |  0.857143 |        0.8      |           0.774194 |           0.8      |            0.857143 |  0.142857  |        0.774194 |             0 |     0 |
| jMotif_SAX                  |              0.789474 |     0.789474 |     0.789474 |  0.789474 |        0.810811 |           0.789474 |           0.810811 |            0.810811 |  0         |        0.810811 |             0 |     0 |
| ksclarke_solr-iso639-filter |              0.72     |     0.753623 |     0.732394 |  0.716418 |        0.724638 |           0.72     |           0.742857 |            0.684211 |  0         |        0.705882 |             0 |     0 |
| Average                     |              0.835808 |     0.842532 |     0.813058 |  0.672607 |        0.66709  |           0.656733 |           0.838586 |            0.664372 |  0.216807  |        0.644844 |             0 |     0 |
| Median                      |              0.817904 |     0.821266 |     0.781834 |  0.752946 |        0.762319 |           0.747097 |           0.824698 |            0.747511 |  0.0714286 |        0.740038 |             0 |     0 || 

### F1 Score Summary

Project                     |   Logistic Regression |   Neural Net |   Linear SVM |   RBF SVM |   Random Forest |   Decision Tree |   Ridge Classifier |   Gaussian Process |   Nearest Neighbors |   AdaBoost |   Naive Bayes |   QDA |
|:----------------------------|----------------------:|-------------:|-------------:|----------:|----------------:|----------------:|-------------------:|-------------------:|--------------------:|-----------:|--------------:|------:|
| eBay_parallec               |              1        |     1        |     1        |   1       |        1        |        1        |           1        |           0.941176 |            0.941176 |   0.888889 |             0 |     0 |
| ksclarke_solr-iso639-filter |              0.84375  |     1        |     0.928571 |   1       |        0.961538 |        0.96     |           0.84375  |           0.962963 |            0.787879 |   0        |             0 |     0 |
| jMotif_SAX                  |              0.9375   |     0.9375   |     0.9375   |   0.9375  |        1        |        1        |           0.9375   |           1        |            1        |   0        |             0 |     0 |
| jMotif_GI                   |              0.909091 |     0.909091 |     0.714286 |   0       |        0        |        0        |           0        |           0.909091 |            0        |   0        |             0 |     0 |
| tracee_contextlogger        |              0.705882 |     0.705882 |     0.666667 |   0.8     |        0.705882 |        0.666667 |           0.666667 |           0.705882 |            0.8      |   1        |             0 |     0 |
| Average                     |              0.879245 |     0.910495 |     0.849405 |   0.7475  |        0.733484 |        0.725333 |           0.689583 |           0.903823 |            0.705811 |   0.377778 |             0 |     0 |
| Median                      |              0.894168 |     0.923997 |     0.888988 |   0.86875 |        0.847511 |        0.842667 |           0.766667 |           0.925134 |            0.793939 |   0.188889 |             0 |     0 || 

### ROC AUC Summary

Project                     |   Gaussian Process |   Linear SVM |   Logistic Regression |   Neural Net |   Nearest Neighbors |   RBF SVM |   Random Forest |   Ridge Classifier |   AdaBoost |   Decision Tree |   Naive Bayes |   QDA |
|:----------------------------|-------------------:|-------------:|----------------------:|-------------:|--------------------:|----------:|----------------:|-------------------:|-----------:|----------------:|--------------:|------:|
| eBay_parallec               |           1        |     1        |              1        |     1        |            1        |  1        |        1        |           1        |  1         |        0.875    |             0 |     0 |
| tracee_contextlogger        |           0.923077 |     0.923077 |              0.923077 |     0.923077 |            0.923077 |  0.923077 |        0.923077 |           0.923077 |  0.0769231 |        0.923077 |             0 |     0 |
| jMotif_GI                   |           0.833333 |     0.833333 |              0.833333 |     0.833333 |            0        |  0        |        0        |           0        |  0         |        0        |             0 |     0 |
| jMotif_SAX                  |           0.681818 |     0.681818 |              0.681818 |     0.681818 |            0.681818 |  0.681818 |        0.681818 |           0.681818 |  0         |        0.681818 |             0 |     0 |
| ksclarke_solr-iso639-filter |           0.604651 |     0.604651 |              0.627907 |     0.604651 |            0.604651 |  0.55814  |        0.581395 |           0.627907 |  0         |        0.55814  |             0 |     0 |
| Average                     |           0.808576 |     0.808576 |              0.813227 |     0.808576 |            0.641909 |  0.632607 |        0.637258 |           0.64656  |  0.215385  |        0.607607 |             0 |     0 |
| Median                      |           0.820955 |     0.820955 |              0.82328  |     0.820955 |            0.661864 |  0.657213 |        0.659538 |           0.664189 |  0.0384615 |        0.644713 |             0 |     0 || 

### Precision Summary

Project                     |   Logistic Regression |   Neural Net |   Linear SVM |   RBF SVM |   Random Forest |   Ridge Classifier |   Gaussian Process |   Nearest Neighbors |   AdaBoost |   Decision Tree |   Naive Bayes |   QDA |
|:----------------------------|----------------------:|-------------:|-------------:|----------:|----------------:|-------------------:|-------------------:|--------------------:|-----------:|----------------:|--------------:|------:|
| eBay_parallec               |              1        |     1        |     1        |  1        |        1        |           1        |           0.97619  |            0.97619  |   0.952381 |        0.9375   |           0.5 |   0.5 |
| tracee_contextlogger        |              0.930288 |     0.930288 |     0.924038 |  0.942788 |        0.930288 |           0.924038 |           0.930288 |            0.942788 |   0.538462 |        0.924038 |           0.5 |   0.5 |
| jMotif_GI                   |              0.910714 |     0.910714 |     0.892857 |  0.5      |        0.5      |           0.494048 |           0.910714 |            0.5      |   0.494048 |        0.452381 |           0.5 |   0.5 |
| jMotif_SAX                  |              0.837484 |     0.837484 |     0.837484 |  0.837484 |        0.840909 |           0.837484 |           0.840909 |            0.840909 |   0.5      |        0.840909 |           0.5 |   0.5 |
| ksclarke_solr-iso639-filter |              0.774271 |     0.802326 |     0.786453 |  0.77907  |        0.782761 |           0.774271 |           0.794389 |            0.74677  |   0.468254 |        0.771133 |           0.5 |   0.5 |
| Average                     |              0.890552 |     0.896163 |     0.888167 |  0.811869 |        0.810792 |           0.805968 |           0.890498 |            0.801332 |   0.590629 |        0.785192 |           0.5 |   0.5 |
| Median                      |              0.900633 |     0.903438 |     0.890512 |  0.824676 |        0.82585  |           0.821726 |           0.900606 |            0.82112  |   0.519231 |        0.813051 |           0.5 |   0.5 |



## Conclusion

Neural Net has best accuracy among all classifiers, but Random Forest Classifier has explainability of the model with comparable performance with Neural Net